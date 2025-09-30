from .base import Chart, ChartContext
from .utils import Point, chart_space_to_xy, calculate_ticks
from .axes import XAxis, YAxis, format_float, order_of_magnitude
from pydantic import BaseModel
from math import floor, ceil

from django.http import HttpRequest


class SvgRect(BaseModel):
    x: float
    y: float
    width: float
    height: float
    color: str


class BarChartContext(ChartContext):
    bars: list[SvgRect]
    values: list[float]


class BarChart(Chart):
    chart_template_name: str = "chart/bar"
    labels: list[str] = []
    bars: list[float] = []
    major_x_tick: int | None = 5
    minor_x_tick: int | None = None
    major_y_tick: int | None = 10
    minor_y_tick: int | None = None

    svg_rects: list[SvgRect] = []
    x_axis: XAxis | None = None
    y_axis: YAxis | None = None

    @staticmethod
    def calculate_bar_width(
        width_in_px: float, max_width: float, ps: float, pe: float, frac: float
    ) -> float:
        chart_width_px = width_in_px - ps - pe
        width_per_bar = chart_width_px / max_width
        return width_per_bar * frac

    @staticmethod
    def calculate_bar_height(
        height_in_px: float, max_height: float, pt: float, pb: float, bar: float
    ) -> float:
        chart_height_px = height_in_px - pt - pb
        bar_height = (bar / max_height) * chart_height_px
        return bar_height

    @property
    def y_ticks(self) -> tuple[float, float]:
        major_y_tick, minor_y_tick = calculate_ticks(max(self.bars), 0)
        return major_y_tick, minor_y_tick

    @property
    def max_height(self) -> float:
        max_height = max(self.bars)
        max_height = ceil(max_height / self.y_ticks[0]) * self.y_ticks[0]
        return max_height

    @property
    def y_order_of_magnitude(self) -> int:
        return order_of_magnitude(self.y_ticks[0])

    def _build_x_axis(self) -> XAxis:
        major_x_tick, minor_x_tick = calculate_ticks(len(self.bars), 0)

        return XAxis(
            max_width=len(self.bars),
            max_height=self.max_height,
            x_points=list(range(len(self.bars))),
            x_labels=self.labels,
            width_in_px=self.width_in_px,
            height_in_px=self.height_in_px,
            padding=self.padding,
            major_grid_lines=self.x_major_grid_lines,
            minor_grid_lines=self.x_minor_grid_lines,
            major_tick=major_x_tick,
            minor_tick=minor_x_tick,
            id=self.id + "_x_axis" if self.id is not None else None,
            order_of_magnitude=1,
            align="between",
            draw_major_ticks=False,
        )

    def _build_y_axis(self) -> YAxis:
        major_y_tick, minor_y_tick = calculate_ticks(max(self.bars), 0)
        return YAxis(
            max_width=len(self.bars),
            max_height=self.max_height,
            width_in_px=self.width_in_px,
            height_in_px=self.height_in_px,
            padding=self.padding,
            major_grid_lines=self.y_major_grid_lines,
            minor_grid_lines=self.y_minor_grid_lines,
            major_tick=major_y_tick,
            minor_tick=minor_y_tick,
            id=self.id + "_y_axis" if self.id is not None else None,
            order_of_magnitude=self.y_order_of_magnitude,
        )

    def set_bars(
        self,
        labels: list[str],
        bars: list[float],
    ) -> None:
        assert self.padding is not None

        self.labels = labels
        self.bars = bars

        bar_width_frac = 0.85
        bar_width = self.calculate_bar_width(
            self.width_in_px,
            len(bars),
            self.padding.ps,
            self.padding.pe,
            bar_width_frac,
        )

        self.svg_rects = []
        for idx, bar in enumerate(bars):
            point = chart_space_to_xy(
                len(bars),
                self.max_height,
                self.padding,
                self.width_in_px,
                self.height_in_px,
                Point(x=idx, y=bar),
            )

            point.x = point.x + (1 - bar_width_frac) * bar_width / 2

            bar_height = self.calculate_bar_height(
                self.height_in_px,
                self.max_height,
                self.padding.pt,
                self.padding.pb,
                bar,
            )

            self.svg_rects.append(
                SvgRect(
                    x=point.x,
                    y=point.y,
                    width=bar_width,
                    height=bar_height,
                    color="#8839ef",
                )
            )

        major_ticks_y = [
            (t + 1) * self.y_ticks[0]
            for t in range(floor(self.max_height / self.y_ticks[0]))
        ]
        major_ticks_y = [
            format_float(t / pow(10, self.y_order_of_magnitude)) for t in major_ticks_y
        ]
        max_len = max([len(t) for t in major_ticks_y])
        self.padding.ps = 22 + 8.5 * (max_len)

    def _build_chart(
        self,
        request: HttpRequest,
        id: str,
    ) -> BarChartContext:
        x_axis = self._build_x_axis()
        y_axis = self._build_y_axis()

        x_axis = x_axis.render(request)
        y_axis = y_axis.render(request)

        return BarChartContext(
            id=id,
            width=self.width_in_px,
            height=self.height_in_px,
            width_half=self.width_in_px / 2,
            bars=self.svg_rects,
            values=self.bars,
            x_axis=x_axis,
            y_axis=y_axis,
            title=self.title,
            swap_oob=self.swap_oob,
        )

    def render_chart(self, request: HttpRequest, authenticated: bool) -> str:
        self.set_bars(
            labels=self.labels,
            bars=self.bars,
        )
        return super().render_chart(request, authenticated)
