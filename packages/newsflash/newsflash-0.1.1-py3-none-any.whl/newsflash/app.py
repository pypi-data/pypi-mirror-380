import os
from typing import Type, TypeVar
from newsflash.widgets.layout.base import Layout
from newsflash.widgets.base import Widget
from newsflash.widgets import Notifications, Columns

from django.http import HttpRequest


T = TypeVar("T")


class App:
    layout: Layout

    def __init__(self) -> None:
        self.layout = self.compose()
        self.layout.main_element = True

    def compose(self) -> Layout:
        return Columns(children=[])

    def query_one(self, id: str, type: Type[T]) -> T | None:
        notifications = Notifications()
        if id == "notifications" and isinstance(notifications, type):
            return notifications

        return self.layout.query_one(id, type)

    def query_type(self, id: str) -> Type[Widget] | None:
        return self.layout.query_type(id)

    def render(self, request: HttpRequest) -> str:
        print(type(self.layout))
        return self.layout.render(request)

    @classmethod
    def run(cls):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")
        try:
            from django.core.management import execute_from_command_line
        except ImportError as exc:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            ) from exc

        from web.app.urls import set_urlpatterns

        set_urlpatterns(cls)

        execute_from_command_line(["manage.py", "runserver"])
