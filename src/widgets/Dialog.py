from enum import Enum
from collections.abc import Callable
import customtkinter as ctk
from utils.I18n import I18n


class Mode(Enum):
    RECREATE = "recreate"
    FOCUS = "focus"


class Dialog(ctk.CTkToplevel):

    def __init__(
        self,
        *args,
        fg_color: str | tuple[str, str] | None = None,
        #
        title: str = "",
        title_key: str | None = None,
        resizable: tuple[bool, bool] = (False, False),
        on_destroy: Callable[[], None] | None = None,
        pad: tuple[int, int] = (0, 0),
        **kwargs,
    ):
        super().__init__(*args, fg_color=fg_color, **kwargs)

        self.title(title)
        self.resizable(*resizable)
        self.protocol("WM_DELETE_WINDOW", self.destroy)

        self._on_destroy = on_destroy

        if title_key is not None:
            self._title_text_unsubscriber = I18n.subscribe(
                key=title_key,
                callback=lambda value: self.title(value),
            )
            self.title(I18n.get_text(title_key))
        else:
            self._title_text_unsubscriber = None

        self.root_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.root_frame.pack(padx=pad[0], pady=pad[1], fill="both", expand=True)

    def destroy(self) -> None:
        if self._title_text_unsubscriber is not None:
            self._title_text_unsubscriber()
        if self._on_destroy is not None:
            self._on_destroy()
        super().destroy()
