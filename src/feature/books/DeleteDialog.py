from typing import Any, Callable, Tuple
from typing import Tuple
import customtkinter as ctk
from db import Book


class DeleteDialog(ctk.CTkToplevel):
    def _delete(self) -> None:
        self._book.delete_instance()
        self.close()

    def close(self) -> None:
        if self._on_close:
            self._on_close()
        self.destroy()

    def __init__(
        self,
        *args,
        fg_color: str | Tuple[str, str] | None = None,
        #
        book: Book,
        on_close: Callable[[], Any] | None = None,
        **kwargs,
    ):
        super().__init__(*args, fg_color=fg_color, **kwargs)

        self._book = book
        self._on_close = on_close

        self.title("📚 도서 삭제")

        root_frame = ctk.CTkFrame(
            self,
            fg_color="transparent",
            width=300,
        )
        root_frame.pack(padx=10, pady=5, fill="both", expand=True)

        # --------------------------------------------------
        ctk.CTkLabel(
            root_frame,
            text="정말 삭제하시겠습니까?",
            font=("Arial", 14, "bold"),
            anchor="w",
        ).pack(side="top", fill="x", pady=5)

        # --------------------------------------------------
        action_frame = ctk.CTkFrame(root_frame)
        action_frame.pack(side="top", fill="x", pady=5)

        ctk.CTkButton(
            action_frame,
            text="취소",
            corner_radius=0,
            border_width=0,
            fg_color="transparent",
            command=self.close,
        ).pack(side="left", fill="x", expand=True)

        ctk.CTkButton(
            action_frame,
            text="삭제",
            corner_radius=0,
            border_width=0,
            command=self._delete,
        ).pack(side="left", fill="x", expand=True)
