from typing import Any, Tuple
import customtkinter as ctk
from utils import LangManager


class Label(ctk.CTkLabel):
    """
    CTKLabel을 상속받아 여러속성을 추가한 컴포넌트.

    :param text_key: 텍스트를 설정할 때 사용할 키값. 해당 키값에 따라서 text가 번역된다.
    :param text: text_key가 설정되어 있지 않다면, 이 값을 텍스트로 사용한다. 그렇지 않다면 해당 키값에 따라서 text가 설정된다.
    """

    def __init__(
        self,
        master: Any,
        width: int = 0,
        height: int = 28,
        corner_radius: int | None = None,
        bg_color: str | Tuple[str, str] = "transparent",
        fg_color: str | Tuple[str, str] | None = None,
        text_color: str | Tuple[str, str] | None = None,
        text_color_disabled: str | Tuple[str, str] | None = None,
        text: str = "CTkLabel",
        font: tuple | ctk.CTkFont | None = None,
        image: ctk.CTkImage | None = None,
        compound: str = "center",
        anchor: str = "center",
        wraplength: int = 0,
        #
        text_key: str | None = None,
        **kwargs
    ):
        super().__init__(
            master=master,
            width=width,
            height=height,
            corner_radius=corner_radius,
            bg_color=bg_color,
            fg_color=fg_color,
            text_color=text_color,
            text_color_disabled=text_color_disabled,
            text=LangManager.get_text(text_key) if text_key is not None else text,
            font=font,
            image=image,
            compound=compound,
            anchor=anchor,
            wraplength=wraplength,
            **kwargs
        )

        if text_key is not None:
            self._text_unsubscriber = LangManager.subscribe(
                key=text_key,
                callback=lambda text: self.configure(text=text),
            )
        else:
            self._text_unsubscriber = None

    def destroy(self):
        if self._text_unsubscriber is not None:
            self._text_unsubscriber()
        return super().destroy()
