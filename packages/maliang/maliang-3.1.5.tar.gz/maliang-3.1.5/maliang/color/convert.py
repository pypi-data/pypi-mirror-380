# Copyright (c) 2024-2025 Xiaokang2022. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for details.

"""Convert a format of color to another format.

* RGB: tuple, (Red, Green, Blue)
* HSL: tuple, (Hue, Saturation, Lightness)
* RGBA: tuple, (Red, Green, Blue, Alpha)
* HEX: hexadecimal, such as '#ABCDEF' or '#12345678'
* NAME: string, such as 'royalblue'
"""

from __future__ import annotations as _

__all__ = (
    "rgb_to_hex",
    "hex_to_rgb",
    "rgba_to_hex",
    "hex_to_rgba",
    "hsl_to_rgb",
    "rgb_to_hsl",
    "hsl_to_hex",
    "hex_to_hsl",
    "name_to_rgb",
    "rgb_to_name",
    "name_to_hex",
    "hex_to_name",
    "fix_hex_length",
    "str_to_rgb",
    # Alias
    "rgb2hex",
    "hex2rgb",
    "rgba2hex",
    "hex2rgba",
    "hsl2rgb",
    "rgb2hsl",
    "hsl2hex",
    "hex2hsl",
    "name2rgb",
    "rgb2name",
    "name2hex",
    "hex2name",
    "str2rgb",
)

import colorsys
import math

from ..core import configs
from . import colortable, rgb


def rgb_to_hex(value: tuple[int, int, int], /) -> str:
    """Convert a RGB code to a hexadecimal code.

    Args:
        value: a RGB code.

    Returns:
        A hexadecimal code.
    """
    return f"#{value[0]:02X}{value[1]:02X}{value[2]:02X}"


def hex_to_rgb(value: str, /) -> tuple[int, int, int]:
    """Convert a hexadecimal code to a RGB code.

    Args:
        value: a hexadecimal code.

    Returns:
        A RGB code.
    """
    _, b = divmod(int(value[1:], 16), 256)
    r, g = divmod(_, 256)
    return r, g, b


def rgba_to_hex(value: tuple[int, int, int, float], /) -> str:
    """Convert a RGBA code to a hexadecimal code.

    Args:
        value: a RGBA code.

    Returns:
        A hexadecimal code.
    """
    return f"#{value[0]:02X}{value[1]:02X}{value[2]:02X}{round(value[3]*255):02X}"


def hex_to_rgba(value: str, /) -> tuple[int, int, int, float]:
    """Convert a hexadecimal code to a RGBA code.

    Args:
        value: a hexadecimal code.

    Returns:
        A RGBA code.
    """
    _, a = divmod(int(value[1:], 16), 256)
    _, b = divmod(_, 256)
    r, g = divmod(_, 256)
    return r, g, b, a/255


def rgb_to_rgba(value: tuple[int, int, int], /) -> tuple[int, int, int, float]:
    """Convert a RGB code to a RGBA code.

    Args:
        value: a RGB code.

    Returns:
        A RGBA code with alpha channel ``0``.
    """
    return *value, 0.


def rgba_to_rgb(
    value: tuple[int, int, int, float],
    /,
    *,
    refer: tuple[int, int, int],
) -> tuple[int, int, int]:
    """Convert a RGBA code to a RGB code.

    Args:
        value: a RGBA code.
        refer: a RGB code as the background.

    Returns:
        A RGB code blended with the background.
    """
    return rgb.transition(value[:-1], refer, 1-value[-1])


def hsl_to_rgb(value: tuple[float, float, float], /) -> tuple[int, int, int]:
    """Convert a HSL code to a RGB code.

    Args:
        value: a HSL code.

    Returns:
        A RGB code.
    """
    c = colorsys.hls_to_rgb(value[0]/math.tau, value[1], value[2])
    return round(c[0]*255), round(c[1]*255), round(c[2]*255)


def rgb_to_hsl(value: tuple[int, int, int], /) -> tuple[float, float, float]:
    """Convert a RGB code to a HSL code.

    Args:
        value: a RGB code.

    Returns:
        A HSL code.
    """
    c = colorsys.rgb_to_hls(value[0]/255, value[1]/255, value[2]/255)
    return c[0]*math.tau, c[1], c[2]


def hsl_to_hex(value: tuple[float, float, float], /) -> str:
    """Convert a HSL code to a hexadecimal code.

    Args:
        value: a HSL code.

    Returns:
        A hexadecimal code.
    """
    return rgb_to_hex(hsl_to_rgb(value))


def hex_to_hsl(value: str, /) -> tuple[float, float, float]:
    """Convert a hexadecimal code to a HSL code.

    Args:
        value: a hexadecimal code.

    Returns:
        A HSL code.
    """
    return rgb_to_hsl(hex_to_rgb(value))


def name_to_rgb(value: str, /) -> tuple[int, int, int]:
    """Convert a color name to a RGB code.

    Args:
        value: a color name.

    Returns:
        A RGB code.
    """
    if rgb_code := colortable.MAPPING_TABLE.get(value.lower()):
        return rgb_code

    return configs.Env.root.winfo_rgb(value)


def rgb_to_name(value: tuple[int, int, int], /) -> list[str]:
    """Convert a RGB code to a color name.

    Args:
        value: a RGB code.

    Returns:
        A list of color names.
    """
    str_list: list[str] = []

    for name, rgb_code in colortable.MAPPING_TABLE.items():
        if value == rgb_code:
            str_list.append(name)

    return str_list


def name_to_hex(value: str, /) -> str:
    """Convert a color name to a hexadecimal code.

    Args:
        value: a color name.

    Returns:
        A hexadecimal code.
    """
    return rgb_to_hex(name_to_rgb(value))


def hex_to_name(value: str, /) -> list[str]:
    """Convert a hexadecimal code to a color name.

    Args:
        value: a hexadecimal code.

    Returns:
        A list of color names.
    """
    return rgb_to_name(hex_to_rgb(value))


def fix_hex_length(value: str, /) -> str:
    """Fix the length of a hexadecimal code.

    Args:
        value: a hexadecimal code.

    Returns:
        A fixed hexadecimal code.
    """
    if len(value) == 4:
        return f"#{value[1]*2}{value[2]*2}{value[3]*2}"

    if len(value) == 5:
        return f"#{value[1]*2}{value[2]*2}{value[3]*2}{value[4]*2}"

    return value


def str_to_rgb(value: str, /) -> tuple[int, int, int]:
    """Convert a color name or a hexadecimal code to a RGB code.

    Args:
        value: a color name or a hexadecimal code.

    Returns:
        A RGB code.
    """
    if value.startswith("#"):
        return hex_to_rgb(fix_hex_length(value))

    return name_to_rgb(value)


# Alias

rgb2hex = rgb_to_hex
hex2rgb = hex_to_rgb
rgba2hex = rgba_to_hex
hex2rgba = hex_to_rgba
hsl2rgb = hsl_to_rgb
rgb2hsl = rgb_to_hsl
hsl2hex = hsl_to_hex
hex2hsl = hex_to_hsl
name2rgb = name_to_rgb
rgb2name = rgb_to_name
name2hex = name_to_hex
hex2name = hex_to_name
str2rgb = str_to_rgb
