
"""Decorators and job tracking utilities for Lanscape."""

from time import time
from dataclasses import dataclass, field
from typing import DefaultDict
from collections import defaultdict
import inspect
import functools
import concurrent.futures
import logging
from tabulate import tabulate


log = logging.getLogger(__name__)


def run_once(func):
    """Ensure a function executes only once and cache the result."""

    cache_attr = "_run_once_cache"
    ran_attr = "_run_once_ran"

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if getattr(wrapper, ran_attr, False):
            return getattr(wrapper, cache_attr)

        start = time()
        result = func(*args, **kwargs)
        elapsed = time() - start

        setattr(wrapper, cache_attr, result)
        setattr(wrapper, ran_attr, True)

        log.debug("run_once executed %s in %.4fs", func.__qualname__, elapsed)
        return result

    return wrapper


@dataclass
class JobStats:
    """
    Tracks statistics for job execution, including running, finished, and timing data.
    """
    running: DefaultDict[str, int] = field(
        default_factory=lambda: defaultdict(int))
    finished: DefaultDict[str, int] = field(
        default_factory=lambda: defaultdict(int))
    timing: DefaultDict[str, float] = field(
        default_factory=lambda: defaultdict(float))

    _instance = None

    def __init__(self):
        # Only initialize once
        if not hasattr(self, "running"):
            self.running = defaultdict(int)
            self.finished = defaultdict(int)
            self.timing = defaultdict(float)

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(JobStats, cls).__new__(cls)
        return cls._instance

    def __str__(self):
        """Return a formatted string representation of the job statistics."""
        data = [
            [
                name,
                self.running.get(name, 0),
                self.finished.get(name, 0),
                self.timing.get(name, 0.0)
            ]
            for name in set(self.running) | set(self.finished)
        ]
        headers = ["Function", "Running", "Finished", "Avg Time (s)"]
        return tabulate(
            data,
            headers=headers,
            tablefmt="grid"
        )


class JobStatsMixin:  # pylint: disable=too-few-public-methods
    """
    Singleton mixin that provides shared job_stats property across all instances.
    """
    _job_stats = None

    @property
    def job_stats(self):
        """Return the shared JobStats instance."""
        return JobStats()


def job_tracker(func):
    """
    Decorator to track job statistics for a method,
    including running count, finished count, and average timing.
    """
    def get_fxn_src_name(func, first_arg) -> str:
        """
        Return the function name with the class name prepended if available.
        """
        qual_parts = func.__qualname__.split(".")
        cls_name = qual_parts[-2] if len(qual_parts) > 1 else None
        cls_obj = None  # resolved lazily
        if cls_obj is None and cls_name:
            mod = inspect.getmodule(func)
            cls_obj = getattr(mod, cls_name, None)
        if cls_obj and first_arg is not None:
            if (first_arg is cls_obj or isinstance(first_arg, cls_obj)):
                return f"{cls_name}.{func.__name__}"
        return func.__name__

    def wrapper(*args, **kwargs):
        """Wrap the function to update job statistics before and after execution."""
        class_instance = args[0]
        job_stats = JobStats()
        fxn = get_fxn_src_name(
            func,
            class_instance
        )

        # Increment running counter and track execution time
        job_stats.running[fxn] += 1
        start = time()

        result = func(*args, **kwargs)  # Execute the wrapped function

        # Update statistics after function execution
        elapsed = time() - start
        job_stats.running[fxn] -= 1
        job_stats.finished[fxn] += 1

        # Calculate the new average timing for the function
        job_stats.timing[fxn] = round(
            ((job_stats.finished[fxn] - 1) * job_stats.timing[fxn] + elapsed)
            / job_stats.finished[fxn],
            4
        )

        # Clean up if no more running instances of this function
        if job_stats.running[fxn] == 0:
            job_stats.running.pop(fxn)

        return result

    return wrapper


def terminator(func):
    """
    Decorator designed specifically for the SubnetScanner class,
    helps facilitate termination of a job.
    """
    def wrapper(*args, **kwargs):
        """Wrap the function to check if the scan is running before execution."""
        scan = args[0]  # aka self
        if not scan.running:
            return None
        return func(*args, **kwargs)

    return wrapper


def timeout_enforcer(timeout: int, raise_on_timeout: bool = True):
    """
    Decorator to enforce a timeout on a function.

    Args:
        timeout (int): Timeout length in seconds.
        raise_on_timeout (bool): Whether to raise an exception if the timeout is exceeded.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """Wrap the function to enforce a timeout on its execution."""
            with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
                future = executor.submit(func, *args, **kwargs)
                try:
                    return future.result(
                        timeout=timeout
                    )
                except concurrent.futures.TimeoutError as exc:
                    if raise_on_timeout:
                        raise TimeoutError(
                            f"Function '{func.__name__}' exceeded timeout of "
                            f"{timeout} seconds."
                        ) from exc
                    return None  # Return None if not raising an exception
        return wrapper
    return decorator
