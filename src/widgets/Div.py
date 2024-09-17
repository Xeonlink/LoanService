from typing import Literal
import collections.abc as c
import customtkinter as ctk


class Div:
    @classmethod
    def create(
        cls,
        master,
        width: int = 200,
        height: int = 200,
        corner_radius: int | str | None = None,
        border_width: int | str | None = None,
        bg_color: str | tuple[str, str] = "transparent",
        fg_color: str | tuple[str, str] | None = None,
        border_color: str | tuple[str, str] | None = None,
        background_corner_colors: tuple[str | tuple[str, str]] | None = None,
        overwrite_preferred_drawing_method: str | None = None,
        #
        side: Literal["top", "bottom", "left", "right"] = "top",
        fill: Literal["x", "y", "both", "none"] = "none",
        expand: bool = False,
        mx: int = 0,
        my: int = 0,
        px: int = 0,
        py: int = 0,
        **kwargs
    ):
        div = ctk.CTkFrame(
            master,
            width,
            height,
            corner_radius,
            border_width,
            bg_color,
            fg_color,
            border_color,
            background_corner_colors,
            overwrite_preferred_drawing_method,
            **kwargs
        )
        div.pack_configure(side=side, fill=fill, expand=expand, padx=mx, pady=my)

        if px < 0:
            return div
        if py < 0:
            return div

        if px == 0 and py == 0:
            return div

        frame = ctk.CTkFrame(div, fg_color="transparent")
        frame.pack_configure(fill="both", expand=True, padx=px, pady=py)
        return frame
