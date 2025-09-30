"""File containing the controller of the logger widget."""

from datetime import datetime

from ..C import APP_NAME, DOCS_URL


class LoggerController:
    """Mainly responsible for handling the logger widget."""

    def __init__(self, views):
        """Initialize the logger controller.

        Parameters
        ----------
        view: Logger
            The view of the logger widget.
        """
        self.views = views
        self.logger_level = 1
        self.log_message(f"Welcome to {APP_NAME}!", color="green")
        self.log_message(
            "If you need help, click <b>Help</b> in the menu,"
            " enter the Help Mode (click question mark in toolbar) or visit "
            f'the <a href="{DOCS_URL}" '
            'style="color:blue;" target="_blank">documentation</a>.',
            color="green",
        )

    def log_message(self, message, color="black", loglevel=1):
        """Log a message to the logger.

        Parameters
        ----------
        message: str
            The message to log.
        color: str
            The color of the message. Default is black.
        """
        if loglevel > self.logger_level:
            return
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        full_message = (
            f"[{timestamp}]\t <span style='color: {color};'>{message}</span>"
        )
        for view in self.views:
            view.logger.append(full_message)

    def clear_log(self):
        """Clear the logger."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        clear_message = f"[{timestamp}]\t Logger cleared."
        for view in self.views:
            view.logger.clear()
            view.logger.append(clear_message)
