from utils import LangManager
import collections.abc as c
import customtkinter as ctk


class Button(ctk.CTkButton):
    """
    CTkButton을 상속받아 여러속성을 추가한 컴포넌트.

    :param text_key: 텍스트를 설정할 때 사용할 키값. 해당 키값에 따라서 text가 번역된다.
    :param text: text_key가 설정되어 있지 않다면, 이 값을 텍스트로 사용한다. 그렇지 않다면 해당 키값에 따라서 text가 설정된다.
    """

    def __init__(
        self,
        master,
        width: int = 140,
        height: int = 28,
        corner_radius: int | None = None,
        border_width: int | None = None,
        border_spacing: int = 2,
        bg_color: str | tuple[str, str] = "transparent",
        fg_color: str | tuple[str, str] | None = None,
        hover_color: str | tuple[str, str] | None = None,
        border_color: str | tuple[str, str] | None = None,
        text_color: str | tuple[str, str] | None = None,
        text_color_disabled: str | tuple[str, str] | None = None,
        background_corner_colors: tuple[str | tuple[str, str]] | None = None,
        round_width_to_even_numbers: bool = True,
        round_height_to_even_numbers: bool = True,
        text: str = "CTkButton",
        font: tuple | ctk.CTkFont | None = None,
        textvariable: ctk.Variable | None = None,
        image: ctk.CTkImage | None = None,
        state: str = "normal",
        hover: bool = True,
        command: c.Callable[[], None] | None = None,
        compound: str = "left",
        anchor: str = "center",
        #
        text_key: str | None = None,
        **kwargs
    ):
        super().__init__(
            master=master,
            width=width,
            height=height,
            corner_radius=corner_radius,
            border_width=border_width,
            border_spacing=border_spacing,
            bg_color=bg_color,
            fg_color=fg_color,
            hover_color=hover_color,
            border_color=border_color,
            text_color=text_color,
            text_color_disabled=text_color_disabled,
            background_corner_colors=background_corner_colors,
            round_width_to_even_numbers=round_width_to_even_numbers,
            round_height_to_even_numbers=round_height_to_even_numbers,
            text=LangManager.get_text(text_key) if text_key is not None else text,
            font=font,
            textvariable=textvariable,
            image=image,
            state=state,
            hover=hover,
            command=command,
            compound=compound,
            anchor=anchor,
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
