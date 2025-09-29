from .qt import QSplitter as QSplitter, QStackedWidget as QStackedWidget, QToolBar as QToolBar, QWidget as QWidget, Qt as Qt, Signal as Signal
from .qute import QuteMainWindow as QuteMainWindow
from .toolbutton import QToolButton as QToolButton
from _typeshed import Incomplete
from enum import Enum

class QMainWindow(QuteMainWindow):
    closed: Incomplete
    class Area(Enum):
        Left = 'left'
        Right = 'right'
        BottomLeft = 'bottom-left'
        BottomRight = 'bottom-right'
    def __init__(self) -> None: ...
    def addDockWidget(self, area: Area, name: str, widget: QWidget): ...
    def removeDockWidget(self, area: Area, index: int): ...
    def closeEvent(self, event) -> None: ...
