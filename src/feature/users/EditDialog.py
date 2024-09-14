from typing import Any, Callable, Tuple
import customtkinter as ctk
import components as cmp
from db import Book
import re
import random


class EditDialog(ctk.CTkToplevel):
    def reset_all(self) -> None:
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
            self.error_textbox.insert("end", "바코드를 입력하세요.\n")
            is_fail = True

        title = self.title_field.get()
        if not title:
            self.error_textbox.insert("end", "제목을 입력하세요.\n")
            is_fail = True

        author = self.author_field.get()
        if not author:
            self.error_textbox.insert("end", "저자를 입력하세요.\n")
            is_fail = True

        publisher = self.publisher_field.get()
        if not publisher:
            self.error_textbox.insert("end", "출판사를 입력하세요.\n")
            is_fail = True

        classification_num = self.classification_num_field.get()
        if not classification_num:
            self.error_textbox.insert("end", "분류번호를 입력하세요.\n")
            is_fail = True

        elif len(classification_num.split(".")[0]) < 3:
            self.error_textbox.insert("end", "분류번호는 3자리수 입니다.\n")
            is_fail = True

        elif re.match(r"\d{3}\.\d\d*|\d{3}", classification_num) is None:
            self.error_textbox.insert("end", "분류번호는 숫자로 입력하세요.\n")
            is_fail = True

        elif float(classification_num) < 0 or float(classification_num) > 999.99:
            self.error_textbox.insert(
                "end", "분류번호는 0 ~ 999.99 사이로 입력하세요.\n"
            )
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

        self.close()

    def _debug_fill(self) -> None:
        self.barcode_id_field.set(str(random.randrange(0, 123456789)))
        self.title_field.set("해리포터")
        self.author_field.set("J.K. 롤링")
        self.publisher_field.set("문학수첩")
        self.classification_num_field.set("123.45")

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

        self._on_close = on_close
        self._book = book

        self.title("📚 도서 수정")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.close)

        root_frame = ctk.CTkFrame(
            self,
            fg_color="transparent",
            width=500,
        )
        root_frame.pack(padx=10, pady=5, fill="both", expand=True)

        # --------------------------------------------------
        ctk.CTkButton(
            root_frame,
            text="🔥 테스트용으로 채우기",
            corner_radius=0,
            border_width=0,
            command=self._debug_fill,
        ).pack(side="top", fill="x", pady=5)

        # --------------------------------------------------
        self.barcode_id_field = cmp.FormFieldH(
            root_frame,
            title_text="🪪 바코드*",
            sub_text="바코드를 찍어주세요.",
            placeholder_text="ex) |l||i|ll||i|l|",
            text=str(book.barcode_id),
        )
        self.barcode_id_field.pack(side="top", fill="x", pady=5)

        self.title_field = cmp.FormFieldH(
            root_frame,
            title_text="🏷️ 제목*",
            sub_text="도서명을 입력하세요",
            placeholder_text="ex) 해리포터",
            text=str(book.title),
        )
        self.title_field.pack(side="top", fill="x", pady=5)

        self.author_field = cmp.FormFieldH(
            root_frame,
            title_text="👨‍🏫 저자*",
            sub_text="저자명을 입력하세요",
            placeholder_text="ex) J.K. 롤링",
            text=str(book.author),
        )
        self.author_field.pack(side="top", fill="x", pady=5)

        self.publisher_field = cmp.FormFieldH(
            root_frame,
            title_text="🏢 출판사*",
            sub_text="출판사명을 입력하세요",
            placeholder_text="ex) 문학수첩",
            text=str(book.publisher),
        )
        self.publisher_field.pack(side="top", fill="x", pady=5)

        self.classification_num_field = cmp.FormFieldH(
            root_frame,
            title_text="🔢 분류번호*",
            sub_text="분류번호를 입력하세요",
            placeholder_text="ex) 123.45",
            text=str(book.classification_num),
        )
        self.classification_num_field.pack(side="top", fill="x", pady=5)

        # --------------------------------------------------
        self.error_textbox = ctk.CTkTextbox(
            root_frame,
            height=150,
            corner_radius=0,
            fg_color=ctk.ThemeManager.theme["CTkFrame"]["fg_color"],
            state="disabled",
        )
        self.error_textbox.pack(side="top", fill="x", pady=5, expand=True)

        # --------------------------------------------------
        action_frame = ctk.CTkFrame(root_frame)
        action_frame.pack(side="top", fill="x", pady=5)

        close_btn = ctk.CTkButton(
            action_frame,
            text="닫기 ⛌",
            corner_radius=0,
            border_width=0,
            command=self.close,
            fg_color="transparent",
            width=120,
        )
        close_btn.pack(side="left", fill="x", expand=True)

        clear_btn = ctk.CTkButton(
            action_frame,
            text="되돌리기 ⌫",
            corner_radius=0,
            border_width=0,
            command=self.reset_all,
            fg_color="transparent",
            width=120,
        )
        clear_btn.pack(side="left", fill="x", expand=True)

        add_btn = ctk.CTkButton(
            action_frame,
            text="수정하기 📝",
            corner_radius=0,
            border_width=0,
            command=self._on_update_click,
            width=120,
        )
        add_btn.pack(side="left", fill="x", expand=True)
