import os
import signal
from contextlib import contextmanager

class TimeoutException(Exception): pass

@contextmanager
def time_limit(seconds):
    def signal_handler(signum, frame):
        raise TimeoutException("Prediction timed out!")

    use_signals_in_timeout = True
    if os.name == 'nt':
        """
        Windows doesnt support signals, hence
        timeout_decorators usually fall apart.
        Hence forcing them to not using signals 
        whenever using the timeout decorator.
        """
        use_signals_in_timeout = False

    if use_signals_in_timeout:
        signal.signal(signal.SIGALRM, signal_handler)
        signal.alarm(seconds)

    try:
        yield
    finally:
        if use_signals_in_timeout:
            signal.alarm(0)