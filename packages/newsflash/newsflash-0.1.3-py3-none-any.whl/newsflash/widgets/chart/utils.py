from pydantic import BaseModel


class Padding(BaseModel):
    ps: float
    pt: float
    pe: float
    pb: float


class Point(BaseModel):
    x: float
    y: float


def chart_space_to_xy(
    max_width: float,
    max_height: float,
    padding: Padding,
    width_in_px: float,
    height_in_px: float,
    point: Point,
) -> Point:
    x_frac = point.x / max_width
    y_frac = 1 - (point.y / max_height)

    chart_width_px = width_in_px - padding.ps - padding.pe
    chart_height_px = height_in_px - padding.pt - padding.pb

    x_px = padding.ps + (x_frac * chart_width_px)
    y_px = padding.pt + (y_frac * chart_height_px)

    return Point(x=x_px, y=y_px)


def calculate_ticks(x_end: float, x_start: float) -> tuple[float, float]:
    tick = 1

    x_range = x_end - x_start
    while x_range / tick > 8:
        if x_range / tick > 50:
            tick *= 10
        elif x_range / tick > 15:
            tick *= 5
        elif x_range / tick > 8:
            tick *= 2

    return tick, tick / 5
