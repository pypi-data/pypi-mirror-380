import notify2
import os
import sys
from contextlib import contextmanager


@contextmanager
def suppress_stderr():
    """Temporarily suppress C-library stderr (e.g., ALSA/JACK spam)."""
    try:
        sys.stderr.flush()
    except Exception:
        pass

    try:
        old_stderr_fd = os.dup(2)
        with open(os.devnull, 'wb') as devnull:
            os.dup2(devnull.fileno(), 2)
        try:
            yield
        finally:
            os.dup2(old_stderr_fd, 2)
            os.close(old_stderr_fd)
    except Exception:
        # If anything goes wrong, just yield without suppression
        yield


def show_notification(title, message, icon="dialog-information", urgency=notify2.URGENCY_NORMAL, timeout=notify2.EXPIRES_DEFAULT):
    """Show a desktop notification with optional icon, urgency and timeout."""
    notification = notify2.Notification(title, message, icon)
    try:
        notification.set_urgency(urgency)
        notification.set_timeout(timeout)
    except Exception:
        # Older themes/daemons may not support these
        pass
    notification.show()
