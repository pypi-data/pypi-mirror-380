import sys

if sys.platform == "darwin":
    from .mac import QuteWindow, QuteMainWindow, QuteDialog, QuteTitleBar
else:
    from .windows import QuteWindow, QuteMainWindow, QuteDialog, QuteTitleBar
