from collections.abc import Callable
from utils.I18n import I18n
from db import Book
import customtkinter as ctk
import widgets as widgets


class DeleteDialog(widgets.Dialog):
    _dialog: widgets.Dialog | None = None

    @classmethod
    def show(cls, book: Book, on_destroy: Callable[[], None] | None = None) -> None:
        if cls._dialog is not None:
            cls._dialog.destroy()

        cls._dialog = cls(book, on_destroy)
        cls._dialog.lift()
        cls._dialog.focus_set()

    def _delete(self) -> None:
        self._book.is_deleted = True  # type: ignore
        self._book.save()
        self.destroy()

    def __init__(self, book: Book, on_destroy: Callable[[], None] | None = None):
        super().__init__(
            title_key="book_delete_dialog_title",
            resizable=(False, False),
            on_destroy=on_destroy,
            pad=(10, 5),
        )
        self._book = book

        # --------------------------------------------------
        widgets.Label(
            self.root_frame,
            text_key="book_delete_dialog_title",
            font=("Arial", 14, "bold"),
            anchor="w",
        ).pack(side="top", fill="x", pady=5)

        # --------------------------------------------------
        widgets.TextArea(
            self.root_frame,
            height=100,
            fg_color=ctk.ThemeManager.theme["CTkFrame"]["fg_color"],
            default_text=I18n.get_text("book_delete_dialog_message"),
            state="disabled",
        ).pack(side="top", fill="x", pady=5, expand=True)

        # --------------------------------------------------
        action_frame = ctk.CTkFrame(self.root_frame)
        action_frame.pack(side="top", fill="x", pady=5)

        widgets.Button(
            action_frame,
            text_key="dialog_close_button",
            border_width=0,
            fg_color="transparent",
            command=self.destroy,
        ).pack(side="left", fill="x", expand=True)

        widgets.Button(
            action_frame,
            text_key="dialog_delete_button",
            border_width=0,
            command=self._delete,
        ).pack(side="left", fill="x", expand=True)

    def destroy(self) -> None:
        DeleteDialog._dialog = None
        return super().destroy()
