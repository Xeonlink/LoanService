from typing import Callable, Any, Tuple, Generic, TypeVar
import customtkinter as ctk
from enum import Enum, auto


class Widget(Enum):
    LABEL = auto()
    BUTTON = auto()


class Anchor(Enum):
    W = "w"
    E = "e"
    CENTER = "center"


T = TypeVar("T")


class Column(Generic[T]):
    def __init__(
        self,
        widget: Widget = Widget.LABEL,
        text: str = "",
        width: int = 100,
        height: int = 30,
        anchor: Anchor = Anchor.CENTER,
        expand: bool = False,
        getter: Callable[[T], str] = lambda _: "-",
        command: Callable[[T], None] = lambda _: None,
        **kwargs,
    ):
        self.widget = widget
        self.text = text
        self.width = width
        self.height = height
        self.anchor = anchor
        self.expand = expand
        self.getter = getter
        self.command = command
        self.kwargs = kwargs


class Table(ctk.CTkFrame, Generic[T]):
    @classmethod
    def _create_label_td(cls, row_frame: ctk.CTkFrame, column: Column[T], data: T):
        td = ctk.CTkLabel(
            row_frame,
            text=column.getter(data),
            width=column.width,
            height=column.height,
            anchor=column.anchor.value,
            **column.kwargs,
        )
        if column.expand:
            td.pack(side="left", fill="x", expand=True)
        else:
            td.pack(side="left")

    @classmethod
    def _create_button_td(cls, row_frame: ctk.CTkFrame, column: Column[T], data: T):
        td = ctk.CTkButton(
            row_frame,
            text=column.getter(data),
            width=column.width,
            height=column.height,
            command=lambda: column.command(data),
            fg_color="transparent",
            **column.kwargs,
        )
        if column.expand:
            td.pack(side="left", fill="x", expand=True)
        else:
            td.pack(side="left")

    def __init__(
        self,
        master: Any,
        width: int = 200,
        height: int = 200,
        corner_radius: int | str | None = None,
        border_width: int | str | None = None,
        bg_color: str | Tuple[str, str] = "transparent",
        fg_color: str | Tuple[str, str] | None = None,
        border_color: str | Tuple[str, str] | None = None,
        background_corner_colors: Tuple[str | Tuple[str, str]] | None = None,
        overwrite_preferred_drawing_method: str | None = None,
        #
        column_def: list[Column[T]] = [],
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

        self._column_def: list[Column[T]] = column_def

        self.thead_frame = ctk.CTkFrame(
            self,
            fg_color=ctk.ThemeManager.theme["CTkEntry"]["fg_color"],
        )
        self.thead_frame.pack(side="top", fill="x")

        index_label = ctk.CTkLabel(
            self.thead_frame,
            text="번호",
            width=40,
            height=30,
        )
        index_label.pack(side="left")

        for column_info in self._column_def:
            label = ctk.CTkLabel(
                self.thead_frame,
                text=column_info.text,
                width=column_info.width,
                anchor=column_info.anchor.value,
            )
            if column_info.expand:
                label.pack(side="left", fill="x", expand=True)
            else:
                label.pack(side="left")

        scrollbar_label = ctk.CTkLabel(
            self.thead_frame,
            text="",
            width=15,
            height=30,
        )
        scrollbar_label.pack(side="left")

        self.tbody_frame = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent",
        )
        self.tbody_frame.pack(side="top", fill="both", expand=True)

    def clear(self):
        for widget in self.tbody_frame.winfo_children():
            widget.destroy()

    def append(self, index: int, data: T):
        row_frame = ctk.CTkFrame(
            self.tbody_frame,
            fg_color="transparent",
        )
        row_frame.pack(side="top", fill="x")

        index_label = ctk.CTkLabel(
            row_frame,
            text=str(index + 1),
            width=40,
            height=30,
        )
        index_label.pack(side="left")

        for column in self._column_def:
            if column.widget == Widget.LABEL:
                Table._create_label_td(row_frame, column, data)
            elif column.widget == Widget.BUTTON:
                Table._create_button_td(row_frame, column, data)
            else:
                raise ValueError("Invalid widget type")
