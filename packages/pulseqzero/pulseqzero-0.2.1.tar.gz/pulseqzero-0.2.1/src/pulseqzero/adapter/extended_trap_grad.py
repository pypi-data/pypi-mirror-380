import numpy as np
import torch
from ..adapter import Opts
from .grads import make_extended_trapezoid


def make_extended_trapezoid_area(
    area: float,
    channel: str,
    grad_start: float,
    grad_end: float,
    system=None,
):
    if system is None:
        system = Opts.default

    max_slew = system.max_slew * 0.99
    max_grad = system.max_grad * 0.99
    raster_time = system.grad_raster_time
    
    
    def requires_grad(x):
        return torch.as_tensor(x).requires_grad
    
    if requires_grad(area):
        raise ValueError("NOT YET DIFFERENTIABLE: make_extended_trapezoid_area() area parameter has requires_grads=True. File an issue if you need this functionality.")
    if requires_grad(grad_start):
        raise ValueError("NOT YET DIFFERENTIABLE: make_extended_trapezoid_area() grad_start parameter has requires_grads=True. File an issue if you need this functionality.")
    if requires_grad(grad_end):
        raise ValueError("NOT YET DIFFERENTIABLE: make_extended_trapezoid_area() grad_end parameter has requires_grads=True. File an issue if you need this functionality.")
    
    # Convert inputs to tensors
    area = torch.as_tensor(area, dtype=torch.float64)
    grad_start = torch.as_tensor(grad_start, dtype=torch.float64)
    grad_end = torch.as_tensor(grad_end, dtype=torch.float64)
    
    def _to_raster(time):
        return torch.ceil(time / raster_time) * raster_time

    def _calc_ramp_time(grad_1, grad_2):
        return _to_raster(torch.abs(grad_1 - grad_2) / max_slew)
    
    def _find_solution(duration: int):
        """Find extended trapezoid gradient waveform for given duration.

        The function performs a grid search over all possible ramp-up, ramp-down and flat times
        for the given duration and returns the solution with the lowest slew rate.

        Parameters
        ----------
        duration
            duration of the gradient in integer multiples of raster_time

        Returns
        -------
            Tuple of ramp-up time, flat time, ramp-down time, gradient amplitude or None if no solution was found
        """
        # Determine timings to check for possible solutions
        ramp_up_times = []
        ramp_down_times = []

        # First, consider solutions that use maximum slew rate:
        # Analytically calculate calculate the point where:
        #   grad_start + ramp_up_time * max_slew == grad_end + ramp_down_time * max_slew
        ramp_up_time = (duration * max_slew * raster_time - grad_start + grad_end) / (2 * max_slew * raster_time)
        ramp_up_time = torch.round(ramp_up_time)

        # Check if gradient amplitude exceeds max_grad, if so, adjust ramp
        # times for a trapezoidal gradient with maximum slew rate.
        if grad_start + ramp_up_time * max_slew * raster_time > max_grad:
            ramp_up_time = torch.round(_calc_ramp_time(grad_start, max_grad) / raster_time)
            ramp_down_time = torch.round(_calc_ramp_time(grad_end, max_grad) / raster_time)
        else:
            ramp_down_time = duration - ramp_up_time

        # Add possible solution if timing is valid
        if ramp_up_time > 0 and ramp_down_time > 0 and ramp_up_time + ramp_down_time <= duration:
            ramp_up_times.append(ramp_up_time)
            ramp_down_times.append(ramp_down_time)

        # Analytically calculate calculate the point where:
        #   grad_start - ramp_up_time * max_slew == grad_end - ramp_down_time * max_slew
        ramp_up_time = (duration * max_slew * raster_time + grad_start - grad_end) / (2 * max_slew * raster_time)
        ramp_up_time = torch.round(ramp_up_time)

        # Check if gradient amplitude exceeds -max_grad, if so, adjust ramp
        # times for a trapezoidal gradient with maximum slew rate.
        if grad_start - ramp_up_time * max_slew * raster_time < -max_grad:
            ramp_up_time = torch.round(_calc_ramp_time(grad_start, -max_grad) / raster_time)
            ramp_down_time = torch.round(_calc_ramp_time(grad_end, -max_grad) / raster_time)
        else:
            ramp_down_time = duration - ramp_up_time

        # Add possible solution if timing is valid
        if ramp_up_time > 0 and ramp_down_time > 0 and ramp_up_time + ramp_down_time <= duration:
            ramp_up_times.append(ramp_up_time)
            ramp_down_times.append(ramp_down_time)

        # Second, try any solution with flat_time == 0
        # This appears to be necessary for many cases, but going through all
        # timings here is probably too conservative still.
        for ramp_up_time in range(1, duration):
            ramp_up_times.append(ramp_up_time)
            ramp_down_times.append(duration - ramp_up_time)

        time_ramp_up = torch.tensor(ramp_up_times)
        time_ramp_down = torch.tensor(ramp_down_times)

        # Calculate corresponding flat times
        flat_time = duration - time_ramp_up - time_ramp_down

        # Filter search space for valid timings (flat time >= 0)
        valid_indices = flat_time >= 0
        time_ramp_up = time_ramp_up[valid_indices]
        time_ramp_down = time_ramp_down[valid_indices]
        flat_time = flat_time[valid_indices]

        # Calculate gradient strength for given timing using analytical solution
        grad_amp = -(time_ramp_up * raster_time * grad_start + time_ramp_down * raster_time * grad_end - 2 * area) / (
            (time_ramp_up + 2 * flat_time + time_ramp_down) * raster_time
        )

        # Calculate slew rates for given timings
        slew_rate1 = torch.abs(grad_start - grad_amp) / (time_ramp_up * raster_time)
        slew_rate2 = torch.abs(grad_end - grad_amp) / (time_ramp_down * raster_time)

        # Filter solutions that satisfy max_grad and max_slew constraints
        valid_indices = (
            (torch.abs(grad_amp) <= max_grad + 1e-8) & (slew_rate1 <= max_slew + 1e-8) & (slew_rate2 <= max_slew + 1e-8)
        )
        solutions = torch.nonzero(valid_indices, as_tuple=False).flatten()

        # Check if any valid solutions were found
        if solutions.shape[0] == 0:
            return None

        # Find solution with lowest slew rate and return it
        ind = torch.argmin(slew_rate1[valid_indices] + slew_rate2[valid_indices])
        ind = solutions[ind]
        return (int(time_ramp_up[ind]), int(flat_time[ind]), int(time_ramp_down[ind]), float(grad_amp[ind]))

    min_duration = torch.max(torch.tensor([torch.round(_calc_ramp_time(grad_end, grad_start) / raster_time), 2]))
    max_duration = torch.max(torch.tensor([
        torch.round(_calc_ramp_time(0, grad_start) / raster_time),
        torch.round(_calc_ramp_time(0, grad_end) / raster_time),
        min_duration])
    )

    solution = None
    for duration in range(min_duration.int(), max_duration.int() + 1):
        solution = _find_solution(duration)
        if solution:
            break
    if not solution:
        while not solution:
            max_duration *= 2
            solution = _find_solution(max_duration.int())

        def binary_search(fun, lower_limit, upper_limit):
            if lower_limit == upper_limit - 1:
                return fun(upper_limit)

            test_value = (upper_limit + lower_limit) // 2

            if fun(test_value):
                return binary_search(fun, lower_limit, test_value)
            else:
                return binary_search(fun, test_value, upper_limit)

        solution = binary_search(_find_solution, max_duration.int() // 2, max_duration.int())

    # Get timing and gradient amplitude from solution
    time_ramp_up = torch.tensor(solution[0] * raster_time)
    flat_time = torch.tensor(solution[1] * raster_time)
    time_ramp_down = torch.tensor(solution[2] * raster_time)
    grad_amp = torch.tensor(solution[3])

    # Create extended trapezoid
    def cumsum(args):
        return torch.cumsum(args, dim=0)

    if flat_time > 0:
        times = cumsum(torch.tensor([0, time_ramp_up, flat_time, time_ramp_down]))
        amplitudes = torch.tensor([grad_start, grad_amp, grad_amp, grad_end])
    else:
        times = cumsum(torch.tensor([0, time_ramp_up, time_ramp_down]))
        amplitudes = torch.tensor([grad_start, grad_amp, grad_end])

    grad = make_extended_trapezoid(
        channel=channel,
        system=system,
        times=times,
        amplitudes=amplitudes
    )


    if not torch.abs(grad.area - area) < 1e-8:
        raise ValueError(f'Could not find a solution for area={area}.')

    return grad, times, amplitudes
