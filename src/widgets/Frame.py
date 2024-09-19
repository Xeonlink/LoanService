from typing import Literal
import customtkinter as ctk


class Frame(ctk.CTkFrame):
    def __init__(
        self,
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
        **kwargs
    ):
        super().__init__(
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

    def pack(
        self,
        side: Literal["top", "bottom", "left", "right"] = "top",
        anchor: Literal[
            "n", "ne", "e", "se", "s", "sw", "w", "nw", "center"
        ] = "center",
        fill: Literal["x", "y", "both", "none"] = "none",
        expand: bool = False,
        padx: int = 0,
        pady: int = 0,
        ipadx: int = 0,
        ipady: int = 0,
    ) -> ctk.CTkFrame:
        super().pack(
            side=side,
            anchor=anchor,
            fill=fill,
            expand=expand,
            padx=padx,
            pady=pady,
        )

        if ipadx == 0 and ipady == 0:
            return self

        frame = ctk.CTkFrame(self, fg_color="transparent")
        frame.pack(side="top", fill="both", expand=True, padx=ipadx, pady=ipady)
        return frame
