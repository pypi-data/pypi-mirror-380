import copy
import logging
import sys

from rich.console import Console


class ConsoleHandler(logging.Handler):
    def __init__(self, color: bool, show_traceback: bool = False) -> None:
        super().__init__()
        self.console = Console(
            file=sys.stderr,
            color_system="auto" if color else None,
            markup=False,
            emoji=False,
            highlight=False,
            log_path=False,
            width=2048,
        )
        self._show_traceback = show_traceback

    def handle(self, record: logging.LogRecord) -> bool:
        if not self._show_traceback:
            record = copy.copy(record)
            record.exc_info = None
        return super().handle(record)

    def emit(self, record: logging.LogRecord) -> None:
        try:
            self.acquire()
            try:
                if self.console.file.closed:
                    return
                self.console.print(self.get_level_message(record), end="", markup=True)
                self.console.print(self.format(record))
            finally:
                self.release()
        except RecursionError:  # pragma: no cover
            raise
        except Exception:  # pragma: no cover
            self.handleError(record)

    def setConsole(self, console: Console) -> None:
        if console is not self.console:
            self.acquire()
            try:
                self.console = console
            finally:
                self.release()

    def get_level_message(self, record: logging.LogRecord) -> str:
        if record.levelno >= logging.ERROR:
            return f"[bold red]{record.levelname}[/bold red]: "
        elif record.levelno >= logging.WARNING:
            return f"[bold yellow]{record.levelname}[/bold yellow]: "

        return ""
