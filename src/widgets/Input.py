from utils import LangManager
import tkinter
import customtkinter as ctk


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
        state: str = tkinter.NORMAL,
        #
        placeholder_text_key: str | None = None,
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

        if placeholder_text_key is not None:
            self._placeholder_text_unsubscriber = LangManager.subscribe(
                key=placeholder_text_key,
                callback=lambda value: self.configure(placeholder_text=value),
            )
            self.configure(placeholder_text=LangManager.get_text(placeholder_text_key))
        else:
            self._placeholder_text_unsubscriber = None

    def clear(self) -> None:
        """
        Input의 내용을 없앰, 단 내용이 없어진 자리에 placeholder_text가 다시 나타나지는 않음.
        다시 나타나게 하려면, 포커스를 줬다가 뺏으면 placeholder_text가 나타남.
        """
        self.delete(0, tkinter.END)

    def get(self) -> str:
        """Input의 내용을 가져옴"""
        return super().get()

    def set(self, value: str) -> None:
        """Input의 내용을 설정"""
        self._entry.delete(0, len(self._entry.get()))
        self._entry.insert(0, value)

    def destroy(self):
        if self._placeholder_text_unsubscriber is not None:
            self._placeholder_text_unsubscriber()
        super().destroy()
