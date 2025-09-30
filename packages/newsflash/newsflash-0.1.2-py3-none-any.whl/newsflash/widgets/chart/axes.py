from typing import Literal

from django.http import HttpRequest
from pydantic import BaseModel

from math import floor, log10
from ..base import Widget
from .base import Padding
from .utils import Point, chart_space_to_xy


def format_float(x: float) -> str:
    return str(int(x)) if x.is_integer() else str(x)


def order_of_magnitude(x: float):
    if x == 0:
        return 0
    return floor(log10(abs(x)))


class AxisContext(BaseModel):
    graph_width_px: float
    graph_height_px: float
    padding: Padding
    major_ticks: list[tuple[Point, str]]
    minor_ticks: list[tuple[Point, str]] | None
    draw_major_ticks: bool = True
    major_grid_lines: bool
    minor_grid_lines: bool


class Axis(Widget):
    max_width: float
    max_height: float
    padding: Padding
    major_tick: float
    minor_tick: float | None
    major_grid_lines: bool
    minor_grid_lines: bool
    draw_major_ticks: bool = True
    order_of_magnitude: int


class YAxisContext(AxisContext):
    multiplier: int


class YAxis(Axis):
    template_name: str = "chart/y_axis"

    def _build_ticks(self, tick: float) -> list[tuple[Point, str]]:
        major_ticks_y = [t * tick for t in range(floor(self.max_height / tick) + 1)]
        major_ticks_points = [
            chart_space_to_xy(
                self.max_width,
                self.max_height,
                self.padding,
                self.width_in_px,
                self.height_in_px,
                Point(x=0, y=y),
            )
            for y in major_ticks_y
        ]
        major_ticks_y = [
            format_float(t / pow(10, self.order_of_magnitude)) for t in major_ticks_y
        ]
        return list(zip(major_ticks_points, major_ticks_y))

    def _build(self, request: HttpRequest) -> YAxisContext:
        if self.minor_tick is not None:
            minor_ticks = self._build_ticks(self.minor_tick)
        else:
            minor_ticks = None
        minor_ticks = None

        return YAxisContext(
            graph_width_px=self.width_in_px - self.padding.ps - self.padding.pe,
            graph_height_px=self.height_in_px - self.padding.pt - self.padding.pb,
            padding=self.padding,
            major_ticks=self._build_ticks(self.major_tick),
            minor_ticks=minor_ticks,
            major_grid_lines=self.major_grid_lines,
            minor_grid_lines=self.minor_grid_lines,
            multiplier=pow(10, self.order_of_magnitude),
        )


class XAxis(Axis):
    template_name: str = "chart/x_axis"

    x_points: list[float]
    x_labels: list[str] | None = None
    align: Literal["on_point"] | Literal["between"]

    def _build_ticks(self, tick: float) -> list[tuple[Point, str]]:
        major_ticks_x = [x for x in self.x_points if (x % tick == 0)]
        major_ticks_points = [
            chart_space_to_xy(
                self.max_width,
                self.max_height,
                self.padding,
                self.width_in_px,
                self.height_in_px,
                Point(x=x - self.x_points[0], y=0),
            )
            for x in major_ticks_x
        ]
        if self.x_labels:
            major_ticks_x = self.x_labels
        else:
            major_ticks_x = [format_float(t) for t in major_ticks_x]

        if self.align == "between":
            shift = (major_ticks_points[1].x - major_ticks_points[0].x) / 2
            major_ticks_points = [
                Point(x=p.x + shift, y=p.y) for p in major_ticks_points
            ]

        return list(zip(major_ticks_points, major_ticks_x))

    def _build(self, request: HttpRequest) -> AxisContext:
        self.minor_tick = None
        if self.minor_tick is not None:
            minor_ticks = self._build_ticks(self.minor_tick)
        else:
            minor_ticks = None

        return AxisContext(
            graph_width_px=self.width_in_px - self.padding.ps - self.padding.pe,
            graph_height_px=self.height_in_px - self.padding.pt - self.padding.pb,
            padding=self.padding,
            major_ticks=self._build_ticks(self.major_tick),
            minor_ticks=minor_ticks,
            draw_major_ticks=self.draw_major_ticks,
            major_grid_lines=self.major_grid_lines,
            minor_grid_lines=self.minor_grid_lines,
        )
