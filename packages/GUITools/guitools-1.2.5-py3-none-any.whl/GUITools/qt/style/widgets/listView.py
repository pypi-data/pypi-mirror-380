from .base import BaseWidgetStyleSheet, BaseStyleSheet, BaseColor, BaseProperty
from .checkBox import indicatorStyleCheet
from .scrollBar import ScrollBarStyleSheet
from ..utils import Global

class ListViewStyleCheet(BaseWidgetStyleSheet):
    def __init__(self, prefix=""):
        super().__init__(f"{prefix} QListView")
        self.listView = self.ListView(prefix)
        self.item = self.Item(prefix)
        self.itemHover = self.ItemHover()
        self.itemSelected = self.ItemSelected(prefix)
        self.itemSelectedHover = self.ItemSelectedHover()
        self.indicator = self.Indicator(prefix)
        self.scrollBar = self.ScrollBar(prefix)
        self.scrollBarHorizontal = self.ScrollBarHorizontal(prefix)
        self.scrollBarVertical = self.ScrollBarVertical(prefix)

    class ScrollBar(BaseStyleSheet):
        def __init__(self, prefix=""):
            super().__init__('QListView QScrollBar', prefix)
            self.background_color = BaseProperty.BackgroundColor(BaseColor.table)

    class ScrollBarHorizontal(ScrollBarStyleSheet.Horizontal):
        def __init__(self, prefix=""):
            super().__init__(f'{prefix} QListView')
            self.background_color = BaseProperty.BackgroundColor(BaseColor.table)
            self.border.radius = 0

    class ScrollBarVertical(ScrollBarStyleSheet.Vertical):
        def __init__(self, prefix=""):
            super().__init__(f'{prefix} QListView')
            self.background_color = BaseProperty.BackgroundColor(BaseColor.table)
            self.border.radius = 0

    class ListView(BaseStyleSheet):
        def __init__(self, prefix=""):
            super().__init__('QListView', prefix)
            self.background_color = BaseProperty.BackgroundColor(BaseColor.table)
            self.padding = BaseProperty.Padding(value=2)

    class Item(BaseStyleSheet):
        def __init__(self, prefix=""):
            super().__init__('QListView::item', prefix)
            self.height = BaseProperty.Height(value=30)
            self.padding = BaseProperty.Padding(value=0)
            self.border = BaseProperty.Border(width=0)

    class ItemHover(BaseStyleSheet):
        def __init__(self, prefix=""):
            super().__init__('QListView::item:hover', prefix)
            self.border = BaseProperty.Border(width=0)
            self.background_color = BaseProperty.BackgroundColor(BaseColor.secondary.fromRgba(120))

    class ItemSelected(BaseStyleSheet):
        def __init__(self, prefix=""):
            super().__init__('QListView::item:selected', prefix)
            self.border = BaseProperty.Border(width=0)
            self.color = BaseProperty.Color(Global.app_color)
            self.background_color = BaseProperty.BackgroundColor(BaseColor.secondary)

    class ItemSelectedHover(BaseStyleSheet):
        def __init__(self, prefix=""):
            super().__init__('QListView::item:selected:hover', prefix)
            self.border = BaseProperty.Border(width=0)
            self.color = BaseProperty.Color(Global.app_color)
            self.background_color = BaseProperty.BackgroundColor(BaseColor.secondary)

    class Indicator(indicatorStyleCheet):
        def __init__(self, prefix=""):
            super().__init__("QListView", prefix)







