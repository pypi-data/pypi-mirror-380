from .base import Chart, ChartContext
from .utils import chart_space_to_xy, Point, calculate_ticks
from .axes import XAxis, YAxis, format_float, order_of_magnitude
from pydantic import BaseModel
from math import ceil, floor

from django.http import HttpRequest


class SvgPoint(BaseModel):
    x: float
    y: float


class LineChartContext(ChartContext):
    points: list[SvgPoint]
    values: list[float]
    line_color: str


class LineChart(Chart):
    chart_template_name: str = "chart/line"
    x_points: list[float] = []
    y_points: list[float] = []
    svg_points: list[SvgPoint] = []

    @property
    def x_ticks(self) -> tuple[float, float]:
        major_x_tick, minor_x_tick = calculate_ticks(
            self.x_points[-1], self.x_points[0]
        )
        return major_x_tick, minor_x_tick

    @property
    def y_ticks(self) -> tuple[float, float]:
        major_y_tick, minor_y_tick = calculate_ticks(max(self.y_points), 0)
        return major_y_tick, minor_y_tick

    @property
    def max_width(self) -> float:
        max_width = self.x_points[-1] - self.x_points[0]
        return max_width

    @property
    def max_height(self) -> float:
        max_height = max(self.y_points)
        max_height = ceil(max_height / self.y_ticks[0]) * self.y_ticks[0]
        return max_height

    @property
    def y_order_of_magnitude(self) -> int:
        return order_of_magnitude(self.y_ticks[0])

    def _build_x_axis(self) -> XAxis:
        major_x_tick, minor_x_tick = self.x_ticks

        return XAxis(
            max_width=self.max_width,
            max_height=self.max_height,
            x_points=self.x_points,
            width_in_px=self.width_in_px,
            height_in_px=self.height_in_px,
            padding=self.padding,
            major_grid_lines=self.x_major_grid_lines,
            minor_grid_lines=self.x_minor_grid_lines,
            major_tick=major_x_tick,
            minor_tick=minor_x_tick,
            id=self.id + "_x_axis" if self.id is not None else None,
            order_of_magnitude=1,
            align="on_point",
            draw_major_ticks=True,
        )

    def _build_y_axis(self) -> YAxis:
        major_y_tick, minor_y_tick = self.y_ticks

        return YAxis(
            max_width=self.max_width,
            max_height=self.max_height,
            width_in_px=self.width_in_px,
            height_in_px=self.height_in_px,
            padding=self.padding,
            major_grid_lines=self.y_major_grid_lines,
            minor_grid_lines=self.y_minor_grid_lines,
            major_tick=major_y_tick,
            minor_tick=minor_y_tick,
            id=self.id + "_y_axix" if self.id is not None else None,
            order_of_magnitude=self.y_order_of_magnitude,
        )

    def set_points(
        self,
        x: list[float],
        points: list[float],
    ) -> None:
        assert len(x) == len(points)
        assert self.padding is not None

        self.x_points = x
        self.y_points = points

        self.svg_points = []
        for idx, bar in enumerate(points):
            point = chart_space_to_xy(
                self.max_width,
                self.max_height,
                self.padding,
                self.width_in_px,
                self.height_in_px,
                Point(x=idx, y=bar),
            )

            self.svg_points.append(
                SvgPoint(
                    x=point.x,
                    y=point.y,
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

    def _build_chart(self, request: HttpRequest, id: str) -> LineChartContext:
        x_axis = self._build_x_axis()
        y_axis = self._build_y_axis()

        x_axis = x_axis.render(request)
        y_axis = y_axis.render(request)

        return LineChartContext(
            id=id,
            width=self.width_in_px,
            height=self.height_in_px,
            width_half=self.width_in_px / 2,
            points=self.svg_points,
            values=self.y_points,
            x_axis=x_axis,
            y_axis=y_axis,
            line_color="#967a3d",
            title=self.title,
            swap_oob=self.swap_oob,
        )

    def render_chart(self, request: HttpRequest, authenticated: bool) -> str:
        self.set_points(
            x=self.x_points,
            points=self.y_points,
        )
        return super().render_chart(request, authenticated)
