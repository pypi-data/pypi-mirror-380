"""Timeout helper functions
"""
import time

class Timer():
    """Simple timeout timer
    """

    def __init__(self, timeout):
        """Class initialization

        :param timeout: Timeout in seconds
        :type timeout: float or int
        """
        self.set(timeout)

    def set(self, timeout):
        """Set a timeout

        :param timeout: Timeout in seconds
        :type timeout: float or int
        """
        self._timeout_duration = float(timeout)
        self._start_time = time.time()

    def expired(self):
        """Checks if timeout has expired

        :return: True if timeout has expired otherwise False
        :rtype: bool
        """
        return (time.time() - self._start_time) >= self._timeout_duration
