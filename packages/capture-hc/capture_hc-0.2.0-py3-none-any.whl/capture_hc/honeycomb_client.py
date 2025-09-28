import libhoney
import time
import inspect
from functools import wraps
from typing import Any, Callable, Dict, Optional
import os
import threading
import atexit


class HoneycombClient:
    def __init__(self, writekey, dataset, debug=False, batch_size=50, flush_interval=5.0):
        """
        Initialize Honeycomb client with connection management.
        
        Args:
            writekey: Honeycomb write key
            dataset: Honeycomb dataset name
            debug: Enable debug mode
            batch_size: Number of events to batch before flushing (default: 50)
            flush_interval: Maximum seconds to wait before flushing (default: 5.0)
        """
        libhoney.init(
            writekey=writekey, 
            dataset=dataset, 
            debug=debug,
            # Configure connection pooling to prevent file descriptor exhaustion
            max_concurrent_batches=10,  # Limit concurrent connections
            block_on_send=False,  # Don't block on send
            block_on_response=False,  # Don't block on response
        )
        self._client = libhoney
        self._batch_size = batch_size
        self._flush_interval = flush_interval
        self._event_count = 0
        self._last_flush = time.time()
        self._lock = threading.Lock()
        
        # Register cleanup on exit
        atexit.register(self.close)

    def send_event(self, fields: dict):
        ev = self._client.new_event()
        for k, v in fields.items():
            ev.add_field(k, v)
        ev.send()
        self._maybe_flush()
    
    def _maybe_flush(self):
        """Flush events if batch size or time interval is reached."""
        with self._lock:
            self._event_count += 1
            current_time = time.time()
            
            # Flush if we've reached batch size or time interval
            if (self._event_count >= self._batch_size or 
                current_time - self._last_flush >= self._flush_interval):
                self._client.flush()
                self._event_count = 0
                self._last_flush = current_time
    
    def flush(self):
        """Force flush all pending events."""
        with self._lock:
            self._client.flush()
            self._event_count = 0
            self._last_flush = time.time()
    
    def close(self):
        """Close the client and flush any remaining events."""
        self.flush()
        # Note: libhoney doesn't have an explicit close method
        # The connection pool will be cleaned up by the garbage collector

    def timed(self, extra_fields=None, event_arg='event'):
        """
        Decorator to time a function and send a Honeycomb event.
        Passes a libhoney event object as a kwarg (default: 'event').
        Usage:
            @honey.timed({"alert_name": "my_func"})
            def my_func(..., event=None):
                event.add_field("key", value)
            
            @honey.timed({"alert_name": "my_func"}, event_arg='track')
            def my_func(..., track=None):
                track.add_field("key", value)
        If the wrapped function does not accept the kwarg specified by `event_arg`,
        the event object will not be injected. You can also set `event_arg=None`
        to disable injection explicitly.
        """
        extra_fields = extra_fields or {}
        def decorator(func):
            # Determine once whether the function can receive the event kwarg
            accepts_event_kwarg = False
            if event_arg:
                try:
                    signature = inspect.signature(func)
                    parameters = signature.parameters
                    accepts_event_kwarg = (
                        event_arg in parameters or
                        any(p.kind == inspect.Parameter.VAR_KEYWORD for p in parameters.values())
                    )
                except (ValueError, TypeError):
                    # If we cannot inspect, fall back to not injecting
                    accepts_event_kwarg = False
            @wraps(func)
            def wrapper(*args, **kwargs):
                start = time.time()
                ev = self._client.new_event()
                for k, v in extra_fields.items():
                    ev.add_field(k, v)
                if event_arg and accepts_event_kwarg:
                    kwargs[event_arg] = ev
                try:
                    result = func(*args, **kwargs)
                    return result
                finally:
                    duration_ms = (time.time() - start) * 1000
                    ev.add_field("duration_ms", duration_ms)
                    ev.add_field("function_name", func.__name__)
                    ev.send()
                    self._maybe_flush()
            return wrapper
        return decorator

    def run_with_timing(self, func: Callable[..., Any], *func_args: Any, extra_fields: Optional[Dict[str, Any]] = None, event_arg: str = 'event', **func_kwargs: Any) -> Any:
        """
        Instance helper that decorates and invokes `func` with timing using this client instance.
        """
        decorated = self.timed(extra_fields=extra_fields, event_arg=event_arg)(func)
        return decorated(*func_args, **func_kwargs)

    @classmethod
    def call_with_timing(
        cls,
        func: Callable[..., Any],
        *func_args: Any,
        writekey: str,
        dataset: str,
        extra_fields: Optional[Dict[str, Any]] = None,
        event_arg: str = 'event',
        debug: bool = False,
        batch_size: int = 50,
        flush_interval: float = 5.0,
        **func_kwargs: Any,
    ) -> Any:
        """
        Class helper that initializes a client and invokes `func` with timing.
        """
        client = cls(
            writekey=writekey, 
            dataset=dataset, 
            debug=debug,
            batch_size=batch_size,
            flush_interval=flush_interval
        )
        return client.run_with_timing(
            func,
            *func_args,
            extra_fields=extra_fields,
            event_arg=event_arg,
            **func_kwargs,
        )

    @staticmethod
    def lazy_timed(
        writekey: Optional[str] = None,
        dataset: Optional[str] = None,
        *,
        extra_fields: Optional[Dict[str, Any]] = None,
        event_arg: Optional[str] = 'event',
        debug: bool = False,
        batch_size: int = 50,
        flush_interval: float = 5.0,
    ) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
        """Class-level access to the lazy_timed decorator for convenience."""
        return lazy_timed(
            writekey=writekey,
            dataset=dataset,
            extra_fields=extra_fields,
            event_arg=event_arg,
            debug=debug,
            batch_size=batch_size,
            flush_interval=flush_interval,
        )


def lazy_timed(
    writekey: Optional[str] = None,
    dataset: Optional[str] = None,
    *,
    extra_fields: Optional[Dict[str, Any]] = None,
    event_arg: Optional[str] = 'event',
    debug: bool = False,
    batch_size: int = 50,
    flush_interval: float = 5.0,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Decorator factory that initializes libhoney at call-time and instruments a function.

    - Safe for environments like Airflow where module import happens in a different process
      than task execution. Initialization happens on each call; libhoney tolerates re-init.
    - If `event_arg` is None or the function does not accept the kwarg, no injection occurs.
    - Credentials can also be provided via environment variables if arguments are None:
      HONEYCOMB_WRITEKEY and HONEYCOMB_DATASET.
    """
    extra_fields = extra_fields or {}

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        # precompute signature for injection safety
        accepts_event_kwarg = False
        if event_arg:
            try:
                signature = inspect.signature(func)
                parameters = signature.parameters
                accepts_event_kwarg = (
                    event_arg in parameters or
                    any(p.kind == inspect.Parameter.VAR_KEYWORD for p in parameters.values())
                )
            except (ValueError, TypeError):
                accepts_event_kwarg = False

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Resolve credentials lazily (env fallback)
            _writekey = writekey or os.getenv('HONEYCOMB_WRITEKEY')
            _dataset = dataset or os.getenv('HONEYCOMB_DATASET')
            if not _writekey or not _dataset:
                raise ValueError(
                    'HONEYCOMB credentials missing. Provide writekey/dataset to lazy_timed or set '
                    'HONEYCOMB_WRITEKEY and HONEYCOMB_DATASET environment variables.'
                )
            # Initialize libhoney at call-time with connection management
            libhoney.init(
                writekey=_writekey, 
                dataset=_dataset, 
                debug=debug,
                max_concurrent_batches=10,
                block_on_send=False,
                block_on_response=False,
            )

            start = time.time()
            ev = libhoney.new_event()
            for k, v in extra_fields.items():
                ev.add_field(k, v)
            if event_arg and accepts_event_kwarg:
                kwargs[event_arg] = ev
            try:
                result = func(*args, **kwargs)
                return result
            finally:
                duration_ms = (time.time() - start) * 1000
                ev.add_field('duration_ms', duration_ms)
                ev.add_field('function_name', func.__name__)
                ev.send()
                # For lazy_timed, we flush immediately since it's a one-off operation
                libhoney.flush()

        return wrapper

    return decorator
