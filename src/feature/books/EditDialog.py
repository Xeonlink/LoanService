from db import Book
from collections.abc import Callable
import customtkinter as ctk
import widgets
import re
import random
from utils.I18n import I18n


class EditDialog(widgets.Dialog):
    _dialog: widgets.Dialog | None = None

    @classmethod
    def show(cls, book: Book, on_destroy: Callable[[], None] | None = None) -> None:
        if cls._dialog is not None:
            cls._dialog.destroy()

        cls._dialog = cls(book, on_destroy)

    def _reset_all(self) -> None:
        self.barcode_id_field.set(str(self._book.barcode_id))
        self.title_field.set(str(self._book.title))
        self.author_field.set(str(self._book.author))
        self.publisher_field.set(str(self._book.publisher))
        self.classification_num_field.set(str(self._book.classification_num))

    def _on_update_click(self) -> None:
        self.error_textbox.configure(state="normal")
        self.error_textbox.delete(1.0, "end")

        is_fail = False
        barcode_id = self.barcode_id_field.get()
        if not barcode_id:
            text = I18n.get_text("book_dialog_barcode_required")
            self.error_textbox.insert("end", text)
            is_fail = True

        if Book.is_barcode_exist(barcode_id):
            text = I18n.get_text("book_dialog_barcode_exist")
            self.error_textbox.insert("end", text)
            is_fail = True

        title = self.title_field.get()
        if not title:
            text = I18n.get_text("book_dialog_title_required")
            self.error_textbox.insert("end", text)
            is_fail = True

        author = self.author_field.get()
        if not author:
            text = I18n.get_text("book_dialog_author_required")
            self.error_textbox.insert("end", text)
            is_fail = True

        publisher = self.publisher_field.get()
        if not publisher:
            text = I18n.get_text("book_dialog_publisher_required")
            self.error_textbox.insert("end", text)
            is_fail = True

        classification_num = self.classification_num_field.get()
        if not classification_num:
            text = I18n.get_text("book_dialog_classification_num_required")
            self.error_textbox.insert("end", text)
            is_fail = True

        elif len(classification_num.split(".")[0]) < 3:
            text = I18n.get_text("book_dialog_classification_num_length")
            self.error_textbox.insert("end", "분류번호는 3자리수 입니다.\n")
            is_fail = True

        elif re.match(r"\d{3}\.\d\d*|\d{3}", classification_num) is None:
            text = I18n.get_text("book_dialog_classification_num_numeric")
            self.error_textbox.insert("end", "분류번호는 숫자로 입력하세요.\n")
            is_fail = True

        elif float(classification_num) < 0 or float(classification_num) > 999.99:
            text = I18n.get_text("book_dialog_classification_num_range")
            self.error_textbox.insert("end", text)
            is_fail = True

        self.error_textbox.configure(state="disabled")
        if is_fail:
            return

        self._book.barcode_id = barcode_id  # type: ignore
        self._book.title = title  # type: ignore
        self._book.author = author  # type: ignore
        self._book.publisher = publisher  # type: ignore
        self._book.classification_num = classification_num  # type: ignore
        self._book.save()

        self.destroy()

    def _debug_fill(self) -> None:
        self.barcode_id_field.set(str(random.randrange(0, 123456789)))
        self.title_field.set("해리포터")
        self.author_field.set("J.K. 롤링")
        self.publisher_field.set("문학수첩")
        self.classification_num_field.set("123.45")

    def __init__(self, book: Book, on_close: Callable[[], None] | None = None):
        super().__init__(
            title_key="book_edit_dialog_title",
            resizable=(False, False),
            on_destroy=on_close,
            pad=(10, 5),
        )

        self._book = book

        # --------------------------------------------------
        ctk.CTkButton(
            self.root_frame,
            text="🔥 테스트용으로 채우기",
            border_width=0,
            command=self._debug_fill,
        ).pack(side="top", fill="x", pady=5)

        # --------------------------------------------------
        self.barcode_id_field = widgets.FormFieldH(
            self.root_frame,
            title_text_key="book_dialog_barcode_label",
            placeholder_text_key="book_dialog_barcode_placeholder",
            default_text=str(book.barcode_id),
        )
        self.barcode_id_field.pack(side="top", fill="x", pady=5)

        self.title_field = widgets.FormFieldH(
            self.root_frame,
            title_text_key="book_dialog_title_label",
            placeholder_text_key="book_dialog_title_placeholder",
            default_text=str(book.title),
        )
        self.title_field.pack(side="top", fill="x", pady=5)

        self.author_field = widgets.FormFieldH(
            self.root_frame,
            title_text_key="book_dialog_author_label",
            placeholder_text_key="book_dialog_author_placeholder",
            default_text=str(book.author),
        )
        self.author_field.pack(side="top", fill="x", pady=5)

        self.publisher_field = widgets.FormFieldH(
            self.root_frame,
            title_text_key="book_dialog_publisher_label",
            placeholder_text_key="book_dialog_publisher_placeholder",
            default_text=str(book.publisher),
        )
        self.publisher_field.pack(side="top", fill="x", pady=5)

        self.classification_num_field = widgets.FormFieldH(
            self.root_frame,
            title_text_key="book_dialog_classification_num_label",
            placeholder_text_key="book_dialog_classification_num_placeholder",
            default_text=str(book.classification_num),
        )
        self.classification_num_field.pack(side="top", fill="x", pady=5)

        # --------------------------------------------------
        self.error_textbox = ctk.CTkTextbox(
            self.root_frame,
            height=150,
            fg_color=ctk.ThemeManager.theme["CTkFrame"]["fg_color"],
            state="disabled",
        )
        self.error_textbox.pack(side="top", fill="x", pady=5, expand=True)

        # --------------------------------------------------
        action_frame = ctk.CTkFrame(self.root_frame)
        action_frame.pack(side="top", fill="x", pady=5)

        widgets.Button(
            action_frame,
            text_key="dialog_close_button",
            border_width=0,
            command=self.destroy,
            fg_color="transparent",
            width=120,
        ).pack(side="left", fill="x", expand=True)

        widgets.Button(
            action_frame,
            text_key="dialog_revert_all_button",
            border_width=0,
            command=self._reset_all,
            fg_color="transparent",
            width=120,
        ).pack(side="left", fill="x", expand=True)

        widgets.Button(
            action_frame,
            text_key="dialog_update_button",
            border_width=0,
            command=self._on_update_click,
            width=120,
        ).pack(side="left", fill="x", expand=True)

    def destroy(self) -> None:
        EditDialog._dialog = None
        return super().destroy()
