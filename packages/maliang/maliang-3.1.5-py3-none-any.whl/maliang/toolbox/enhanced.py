# Copyright (c) 2024-2025 Xiaokang2022. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for details.

"""Enhanced versions of some ``tkinter`` classes and functions."""

from __future__ import annotations as _

__all__ = (
    "PhotoImage",
)

import functools
import tkinter

try:
    from PIL import ImageTk
except ImportError:
    ImageTk = None


if ImageTk is None:

    class PhotoImage(tkinter.PhotoImage):
        """Enhanced version of ``tkinter.PhotoImage``."""

        @functools.cached_property
        def _data(self) -> list[list[str]]:
            """Image data in the form of a string."""
            return [line.split() for line in self.tk.call(self, "data")]

        @functools.cached_property
        def _transparency_data(self) -> list[list[bool]]:
            """Transparency data of the image."""
            return [[self.transparency_get(x, y)
                    for x in range(self.width())]
                    for y in range(self.height())]

        def scale(self, x: float, y: float) -> PhotoImage:
            """Scale the PhotoImage.

            Args:
                x: The x-axis scale factor.
                y: The y-axis scale factor.

            Returns:
                A new scaled PhotoImage.
            """
            return self.resize(round(x*self.width()), round(y*self.height()))

        def resize(self, width: int, height: int) -> PhotoImage:
            """Resize the PhotoImage.

            Args:
                width: The new width of the image.
                height: The new height of the image.

            Returns:
                A new resized PhotoImage.
            """
            x, y = width/self.width(), height/self.height()
            new_image = PhotoImage(width=width, height=height)
            new_image.put([[self._data[int(j/y)][int(i/x)]
                            for i in range(width)] for j in range(height)])

            for i in range(width):
                for j in range(height):
                    if self._transparency_data[int(j/y)][int(i/x)]:
                        new_image.transparency_set(i, j, True)

            return new_image

else:

    class PhotoImage(ImageTk.PhotoImage, tkinter.PhotoImage):
        """Pillow version of ``tkinter.PhotoImage``."""

        def scale(self, x: float, y: float) -> PhotoImage:
            """Scale the PhotoImage.

            Args:
                x: The x-axis scale factor.
                y: The y-axis scale factor.

            Returns:
                A new scaled PhotoImage.
            """
            return self.resize(round(x*self.width()), round(y*self.height()))

        def resize(self, width: int, height: int) -> PhotoImage:
            """Resize the PhotoImage.

            Args:
                width: The new width of the image.
                height: The new height of the image.

            Returns:
                A new resized PhotoImage.
            """
            return PhotoImage(ImageTk.getimage(self).resize((width, height)))
