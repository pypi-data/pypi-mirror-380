"""
Filters used in logging handlers
"""
from logging import Filter, StreamHandler
from tqdm import tqdm

#pylint: disable=too-few-public-methods
class NoInfoFilter(Filter):
    """Logging filter removing all INFO level log records"""
    def filter(self, record):
        return record.levelname != "INFO"

#pylint: disable=too-few-public-methods
class OnlyInfoFilter(Filter):
    """Logging filter removing all log records except INFO level records"""
    def filter(self, record):
        return record.levelname == "INFO"

class TqdmLoggingHandler(StreamHandler):
    """Logging handler when using status bar"""
    def emit(self, record):
        """Emit a log message through tqmd

        This logging handler routes log messages through
        the status bar provider tqmd so that the bar
        will stay at the bottom and log messages are
        logged above. This prevents the bar from being
        printed inbetween log messages.

        :param record: Logging record
        :type record: LogRecord
        """
        try:
            msg = self.format(record)
            tqdm.write(msg)
        except Exception:
            self.handleError(record)
