from typing import Any, Tuple
import customtkinter as ctk


class Input(ctk.CTkFrame):
    def __init__(
        self,
        master: Any,
        width: int = 200,
        height: int = 200,
        corner_radius: int | str | None = None,
        border_width: int | str | None = None,
        bg_color: str | Tuple[str, str] = "transparent",
        fg_color: str | Tuple[str, str] | None = None,
        border_color: str | Tuple[str, str] | None = None,
        background_corner_colors: Tuple[str | Tuple[str, str]] | None = None,
        overwrite_preferred_drawing_method: str | None = None,
        #
        placeholder_text: str | None = None,
        text: str | None = None,
        **kwargs,
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
            **kwargs,
        )

        self._entry = ctk.CTkEntry(
            self,
            height=height,
            # fg_color="transparent",
            border_width=0,
            placeholder_text=placeholder_text,
            **kwargs,
        )
        self._entry.pack(side="left", fill="x", expand=True)
        if text:
            self._entry.insert(0, text)

        self._erase_button = ctk.CTkButton(
            self,
            text="지우기 ⌫",
            width=80,
            height=height,
            border_width=0,
            fg_color=ctk.ThemeManager.theme["CTkEntry"]["fg_color"],
            command=self.clear,
            **kwargs,
        )
        self._erase_button.pack(side="left")

    def clear(self) -> None:
        self._entry.delete(0, len(self._entry.get()))

    def get(self) -> str:
        return self._entry.get()

    def set(self, value: str) -> None:
        self._entry.delete(0, len(self._entry.get()))
        self._entry.insert(0, value)
