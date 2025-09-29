import functools
import inspect
import time
from typing import Optional

# ----------------------
# Aggregated storage
# ----------------------
_AGGREGATED_RESULTS = {}  # func_name -> {"count": int, "total_ns": int, "unit": str, "decimals": int}

# Global toggle
ENABLED = True


def set_enabled(value: bool = True):
    """
    Globally enable or disable all @timeit() decorators.

    When disabled, @timeit() will not measure or print execution times,
    and functions will execute normally with minimal overhead.
    """
    global ENABLED
    ENABLED = value


def dump(file: Optional[str] = None):
    """
    Print or write aggregated results for all decorated functions.

    Args:
        file (str, optional): If provided, results are written to this file.
    """
    lines = []
    for func, stats in _AGGREGATED_RESULTS.items():
        count = stats["count"]
        total_ns = stats["total_ns"]
        decimals = stats["decimals"]
        unit = stats["unit"]

        # Average and total formatting
        avg_ns = total_ns / count

        formatted_total, formatted_unit_total = _format_time(total_ns, decimals, unit)
        formatted_avg, formatted_unit_avg = _format_time(avg_ns, decimals, unit)

        lines.append(
            f"[{func}] calls={count}, avg={formatted_avg} {formatted_unit_avg}, total={formatted_total} {formatted_unit_total}"
        )

    output = "\n".join(lines) if lines else "No results recorded."

    if file:
        with open(file, "w", encoding="utf-8") as f:
            f.write(output + "\n")
    else:
        print(output)


def _format_time(elapsed_ns: float, decimals: int, unit: str):
    """Format nanoseconds into the requested unit, or auto-select best unit."""
    conversions = {
        "ns": 1,
        "µs": 1_000,
        "us": 1_000,
        "ms": 1_000_000,
        "s": 1_000_000_000,
        "m": 60_000_000_000,
    }

    if unit == "auto":
        if elapsed_ns < conversions["µs"]:
            unit = "ns"
        elif elapsed_ns < conversions["ms"]:
            unit = "µs"
        elif elapsed_ns < conversions["s"]:
            unit = "ms"
        elif elapsed_ns < conversions["m"]:
            unit = "s"
        else:
            unit = "m"

    value = elapsed_ns / conversions[unit]
    formatted = f"{value:.{decimals}f}"
    return formatted, "µs" if unit == "us" else unit


class TimeIt:
    _VALID_UNITS = {"ns", "us", "µs", "ms", "s", "m", "auto"}

    def __init__(self, decimals: int = 3, unit: str = "auto", verbose: bool = True):
        self.decimals = decimals
        self.unit = unit
        self.verbose = verbose
        self._validate_unit(unit)

    def __call__(self, func):
        if inspect.iscoroutinefunction(func):
            @functools.wraps(func)
            async def async_wrapper(*args, **kwargs):
                return await self._measure_async(func, *args, **kwargs)
            return async_wrapper
        else:
            @functools.wraps(func)
            def sync_wrapper(*args, **kwargs):
                return self._measure_sync(func, *args, **kwargs)
            return sync_wrapper

    def _measure_sync(self, func, *args, **kwargs):
        if not ENABLED:
            return func(*args, **kwargs)
        start = time.perf_counter_ns()
        try:
            return func(*args, **kwargs)
        finally:
            end = time.perf_counter_ns()
            if self.verbose:
                display_time, display_unit = _format_time(end - start, self.decimals, self.unit)
                print(f"[{func.__name__}] Execution time: {display_time} {display_unit}")
            self._record(func.__name__, start, end)

    async def _measure_async(self, func, *args, **kwargs):
        if not ENABLED:
            return await func(*args, **kwargs)
        start = time.perf_counter_ns()
        try:
            return await func(*args, **kwargs)
        finally:
            end = time.perf_counter_ns()
            if self.verbose:
                display_time, display_unit = _format_time(end - start, self.decimals, self.unit)
                print(f"[{func.__name__}] Execution time: {display_time} {display_unit}")
            self._record(func.__name__, start, end)

    def _record(self, name, start_ns, end_ns):
        elapsed_ns = end_ns - start_ns
        stats = _AGGREGATED_RESULTS.setdefault(
            name, {"count": 0, "total_ns": 0, "unit": self.unit, "decimals": self.decimals}
        )
        stats["count"] += 1
        stats["total_ns"] += elapsed_ns

    def _validate_unit(self, unit):
        if unit not in self._VALID_UNITS:
            raise ValueError(f"Invalid unit '{unit}'. Choose from {self._VALID_UNITS}.")


# Public API
def timeit(decimals: int = 3, unit: str = "auto", verbose: bool = True):
    """
    Decorator to measure execution time of a function. Works with sync and async, robust to exceptions.

    Args:
        decimals (int): Number of decimal places (default=3).
        unit (str): Unit for display. "ns", "us", "µs", "ms", "s", "m", "auto" (default).
        verbose (bool): If True, prints the time after each call. Otherwise, only aggregates for dump().

    Example:
        >>> from time_my_func import timeit, dump
        >>> @timeit(verbose=True)
        ... def foo(): sum(range(1000))
        >>> foo()
        [foo] Execution time: 0.012 ms
        >>> dump()  # prints aggregated stats for all functions
    """
    return TimeIt(decimals=decimals, unit=unit, verbose=verbose)
