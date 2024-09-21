from collections.abc import Callable
from utils.I18n import I18n
import customtkinter as ctk
import tkinter as tk


class Input(ctk.CTkEntry):

    def __init__(
        self,
        master,
        width: int = 140,
        height: int = 28,
        corner_radius: int | None = None,
        border_width: int = 0,
        bg_color: str | tuple[str, str] = "transparent",
        fg_color: str | tuple[str, str] | None = None,
        border_color: str | tuple[str, str] | None = None,
        text_color: str | tuple[str, str] | None = None,
        placeholder_text_color: str | tuple[str, str] | None = None,
        textvariable: ctk.Variable | None = None,
        placeholder_text: str | None = None,
        font: tuple | ctk.CTkFont | None = None,
        state: str = "normal",
        #
        placeholder_text_key: str | None = None,
        default_text: str | None = None,
        on_enter: Callable[[tk.Event], None] | None = None,
        **kwargs
    ):
        super().__init__(
            master=master,
            width=width,
            height=height,
            corner_radius=corner_radius,
            border_width=border_width,
            bg_color=bg_color,
            fg_color=fg_color,
            border_color=border_color,
            text_color=text_color,
            placeholder_text_color=placeholder_text_color,
            textvariable=textvariable,
            placeholder_text=placeholder_text,
            font=font,
            state=state,
            **kwargs
        )

        self._on_enter = on_enter
        if self._on_enter is not None:
            self.bind("<Return>", self._on_enter)

        if placeholder_text_key is not None:
            self._placeholder_text_unsubscriber = I18n.subscribe(
                key=placeholder_text_key,
                callback=lambda value: self.configure(placeholder_text=value),
            )
            self.configure(placeholder_text=I18n.get_text(placeholder_text_key))
        else:
            self._placeholder_text_unsubscriber = None

        if default_text is not None:
            self.insert(0, default_text)

    def blur(self) -> None:
        """Input의 포커스를 해제함"""
        self.winfo_toplevel().focus_set()

    def clear(self) -> None:
        """Input의 내용을 지움"""
        self.blur()
        self._entry_focus_out()
        state = self._state
        self.configure(state="normal")
        self.delete(0, "end")
        self.configure(state=state)

    def get(self) -> str:
        """Input의 내용을 가져옴"""
        return super().get()

    def set(self, value: str) -> None:
        """Input의 내용을 설정"""
        if len(value) == 0:
            state = self._state
            self.configure(state="normal")
            self.clear()
            self.configure(state=state)
            return

        state = self._state
        self.configure(state="normal")
        self.delete(0, "end")
        self.insert(0, value)
        self.configure(state=state)

    def destroy(self):
        if self._placeholder_text_unsubscriber is not None:
            self._placeholder_text_unsubscriber()
        super().destroy()
