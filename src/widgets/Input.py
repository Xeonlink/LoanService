from tkinter.constants import NORMAL
from typing import Any, Tuple
import customtkinter as ctk
import widgets


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
        eraseable: bool = False,
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

        self._erasable = eraseable

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

        self._erase_button = widgets.Button(
            self,
            text="지우기 ⌫",
            text_key="widgets_input_erase_button",
            width=80,
            height=height,
            border_width=0,
            fg_color=ctk.ThemeManager.theme["CTkEntry"]["fg_color"],
            command=self.clear,
            **kwargs,
        )
        self._erase_button.pack(side="left")

    def clear(self) -> None:
        """
        Input의 내용을 없앰, 단 내용이 없어진 자리에 placeholder_text가 다시 나타나지는 않음.
        다시 나타나게 하려면, 포커스를 줬다가 뺏으면 placeholder_text가 나타남.
        """
        self._entry.delete(0, len(self._entry.get()))

    def get(self) -> str:
        """Input의 내용을 반환"""
        return self._entry.get()

    def set(self, value: str) -> None:
        """Input의 내용을 설정"""
        self._entry.delete(0, len(self._entry.get()))
        self._entry.insert(0, value)
