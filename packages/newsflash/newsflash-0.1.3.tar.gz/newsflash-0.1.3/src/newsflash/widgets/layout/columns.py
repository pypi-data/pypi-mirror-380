from .base import Layout


class Columns(Layout):
    template_name: str = "layout/columns"
    grow: bool = False
