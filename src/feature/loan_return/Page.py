from datetime import datetime, timedelta
from utils.I18n import I18n
from db import Book, Loan, User
from constants import LOAN_DAYS
import widgets.Table as table
import customtkinter as ctk
import widgets as widgets
from utils import format_loan_duration


class Page(ctk.CTkFrame):
    def _update_ui_by_user(self, user: User):
        self.username_label.configure(text=user.name)
        self.contact_label.configure(text=user.contact)

        loans: list[Loan] = []
        for loan in user.loans:  # type: ignore
            if loan.return_at is None:
                loans.append(loan)

        self._table.clear()
        for index, loan in enumerate(loans):
            self._table.append(index, loan)

    def _enter(self):
        search_text = self.loan_code_term_input.get().strip()
        # print(search_text)
        if len(search_text) == 0:
            self.username_label.configure(text="")
            self.contact_label.configure(text="")
            self._table.clear()
            return

        # search_text로 사용자를 검색
        user = User.safe_get(loan_code=search_text)
        if user is not None:
            self._user = user
            self._update_ui_by_user(user)
            return

        # search_text로 도서를 검색
        if self._user is not None:
            book = Book.safe_get(barcode_id=search_text)
            if (book is not None) and (not book.is_reading) and (not book.is_deleted):

                if self._user.has_overdue:
                    widgets.Alert(
                        message=I18n.get_text("loan_return_page_warning_has_overdue"),
                    )
                    return

                book_ids: list[int] = []
                for loan in self._user.get_loans():  # type: ignore
                    if loan.return_at is None:
                        book_ids.append(int(loan.book.id))

                # 대출
                if int(book.id) not in book_ids:
                    book.is_reading = True
                    book.save()
                    Loan.create(
                        book=book.id,
                        user=self._user.id,
                        loan_at=datetime.now(),
                        due_at=datetime.now() + timedelta(days=LOAN_DAYS),
                        return_at=None,
                    )
                    self._update_ui_by_user(self._user)
            else:
                target_loan: Loan | None = None
                for loan in self._user.get_loans():
                    if loan.book.id == book.id:  # type: ignore
                        if loan.return_at is None:
                            target_loan = loan
                            break

                # 반납
                if target_loan is not None:
                    book = target_loan.book
                    book.is_reading = False  # type: ignore
                    book.save()
                    target_loan.return_at = datetime.now()  # type: ignore
                    target_loan.save()
                    self._update_ui_by_user(self._user)  # type: ignore

    def __init__(
        self,
        master,
        width: int = 200,
        height: int = 200,
        corner_radius: int | str | None = None,
        border_width: int | str | None = None,
        bg_color: str | tuple[str, str] = "transparent",
        fg_color: str | tuple[str, str] = "transparent",
        border_color: str | tuple[str, str] | None = None,
        background_corner_colors: tuple[str | tuple[str, str]] | None = None,
        overwrite_preferred_drawing_method: str | None = None,
        **kwargs,
    ):
        super().__init__(
            master,
            width,
            height,
            corner_radius,
            border_width,
            bg_color,
            fg_color,
            border_color,
            background_corner_colors,
            overwrite_preferred_drawing_method,
            **kwargs,
        )

        self._user: User | None = None

        loan_code_frame = ctk.CTkFrame(self, fg_color="transparent")
        loan_code_frame.pack(fill="x", pady=5)

        widgets.Button(
            loan_code_frame,
            text_key="loan_return_page_loan_code_label",
            width=200,
            height=30,
        ).pack(side="left")

        loan_code_term_frame = ctk.CTkFrame(loan_code_frame, fg_color="transparent")
        loan_code_term_frame.pack(side="left", fill="x", expand=True, padx=10)

        self.loan_code_term_input = widgets.Input(
            loan_code_term_frame,
            height=30,
            placeholder_text_key="loan_return_page_loan_code_placeholder",
            on_enter=lambda _: self._enter(),
        )
        self.loan_code_term_input.pack(side="left", fill="x", expand=True)

        widgets.Button(
            loan_code_term_frame,
            width=80,
            height=30,
            text_key="erase_button",
            fg_color=ctk.ThemeManager.theme["CTkEntry"]["fg_color"],
            command=self.loan_code_term_input.clear,
        ).pack(side="left")

        widgets.Button(
            loan_code_frame,
            width=100,
            height=30,
            text_key="enter_button",
            command=self._enter,
        ).pack(side="left")

        # ----------------------------------------------------------------------
        user_frame = ctk.CTkFrame(self, fg_color="transparent")
        user_frame.pack(fill="x", pady=5)

        self.username_label = widgets.Label(
            user_frame,
            width=80,
            height=30,
            fg_color=ctk.ThemeManager.theme["CTkFrame"]["fg_color"],
            text="",
        )
        self.username_label.pack(side="left")

        self.contact_label = widgets.Label(
            user_frame,
            width=150,
            height=30,
            fg_color=ctk.ThemeManager.theme["CTkFrame"]["fg_color"],
            text="",
        )
        self.contact_label.pack(side="left")

        # ----------------------------------------------------------------------
        self._table = table.Table[Loan](
            self,
            # scrollable=False,
            column_def=[
                table.Column(
                    text="제목",
                    text_key="loan_return_page_table_column_title",
                    width=100,
                    anchor=table.Anchor.W,
                    expand=True,
                    getter=lambda loan: str(loan.book.title),
                ),
                table.Column(
                    text="저자",
                    text_key="loan_return_page_table_column_author",
                    width=120,
                    anchor=table.Anchor.W,
                    getter=lambda loan: str(loan.book.author),
                ),
                table.Column(
                    text="출판사",
                    text_key="loan_return_page_table_column_publisher",
                    width=120,
                    anchor=table.Anchor.W,
                    getter=lambda loan: str(loan.book.publisher),
                ),
                table.Column(
                    text="분류번호",
                    text_key="loan_return_page_table_column_classification_num",
                    width=80,
                    anchor=table.Anchor.W,
                    getter=lambda loan: str(loan.book.classification_num),
                ),
                table.Column(
                    text="대출기간",
                    text_key="loan_return_page_table_column_loan_date_range",
                    width=200,
                    anchor=table.Anchor.CENTER,
                    getter=lambda loan: format_loan_duration(loan.loan_at, loan.due_at),  # type: ignore
                ),
                table.Column(
                    text="",
                    text_key="loan_return_page_table_column_overdue",
                    width=50,
                    anchor=table.Anchor.CENTER,
                    getter=lambda loan: "⏺" if loan.is_overdue else "⛌",
                ),
            ],
        )
        self._table.pack(fill="both", expand=True, pady=5)
