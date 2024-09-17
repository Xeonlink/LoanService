from utils import LangManager
import collections.abc as c
import customtkinter as ctk


class Dialog(ctk.CTkToplevel):
    def __init__(
        self,
        *args,
        fg_color: str | tuple[str, str] | None = None,
        #
        title: str = "",
        title_key: str | None = None,
        resizable: tuple[bool, bool] = (False, False),
        on_destroy: c.Callable[[], None] | None = None,
        **kwargs,
    ):
        super().__init__(*args, fg_color=fg_color, **kwargs)
        self.title(title)
        self.resizable(*resizable)
        self.protocol("WM_DELETE_WINDOW", self.destroy)

        self._on_destroy = on_destroy

        if title_key is not None:
            self._title_text_unsubscriber = LangManager.subscribe(
                key=title_key,
                callback=lambda value: self.title(value),
            )
        else:
            self._title_text_unsubscriber = None

    def destroy(self) -> None:
        if self._title_text_unsubscriber is not None:
            self._title_text_unsubscriber()
        if self._on_destroy is not None:
            self._on_destroy()
        super().destroy()
