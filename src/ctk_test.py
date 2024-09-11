from typing import Tuple, Union
import customtkinter as ctk
from SideMenu import SideMenu

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")
app = ctk.CTk()
app.geometry("800x600")
# app.resizable(False, False)
app.title("대출반납 관리 시스템")

side_menu = SideMenu(app)
side_menu.pack(side="left", fill="y")

page_frame = ctk.CTkFrame(app, corner_radius=0, fg_color="transparent")
page_frame.pack(
    side="left",
    fill="both",
    expand=True,
    padx=10,
    pady=10,
)

search_frame = ctk.CTkFrame(
    page_frame,
    corner_radius=0,
    fg_color="transparent",
)
search_frame.pack(side="top", fill="x")

book_add_btn = ctk.CTkButton(
    search_frame,
    text="도서 추가 ✚",
    width=100,
    height=30,
    corner_radius=0,
)
book_add_btn.pack(side="left")

search_term_frame = ctk.CTkFrame(
    search_frame,
    height=30,
    fg_color=("#979DA2", "#565B5E"),
)
search_term_frame.pack(
    side="left",
    fill="x",
    expand=True,
    padx=10,
)

search_target_combobox = ctk.CTkComboBox(
    search_term_frame,
    width=100,
    height=30,
    values=["도서명", "저자", "출판사"],
    # border_width=1,
    corner_radius=0,
    # justify="center",
)
search_target_combobox.pack(side="left", ipadx=10)

search_term_entry = ctk.CTkEntry(
    search_term_frame,
    height=30,
    corner_radius=0,
    border_width=0,
    placeholder_text="검색어를 입력하세요",
    # fg_color="transparent",
)
search_term_entry.pack(side="left", fill="x", expand=True)


def clear_entry(entry: ctk.CTkEntry):
    value = entry.get()
    entry.delete(0, len(value))


earse_btn = ctk.CTkButton(
    search_term_frame,
    text="지우기 ⌫",
    width=80,
    height=30,
    corner_radius=0,
    # border_width=2,
    fg_color=("#F9F9FA", "#343638"),
    border_color=("#979DA2", "#565B5E"),
    command=lambda: clear_entry(search_term_entry),
)
earse_btn.pack(side="left")

search_btn = ctk.CTkButton(
    search_frame,
    text="검색 🔍",
    width=100,
    height=30,
    corner_radius=0,
)
search_btn.pack(side="left")

gap_frame = ctk.CTkFrame(page_frame, height=10, fg_color="transparent")
gap_frame.pack(fill="x")

# --------------------------------------------
table_frame = ctk.CTkFrame(page_frame)
table_frame.pack(expand=True, fill="both")

thead_frame = ctk.CTkFrame(
    table_frame,
    corner_radius=0,
    fg_color=("#F9F9FA", "#343638"),
)
thead_frame.pack(side="top", fill="x")

index_label = ctk.CTkLabel(
    thead_frame,
    text="번호",
    width=20,
    height=30,
    corner_radius=0,
    fg_color="green",
)
index_label.pack(side="left")

title_label = ctk.CTkLabel(
    thead_frame,
    text="제목",
    width=100,
    height=30,
    corner_radius=0,
    fg_color=("#F9F9FA", "#343638"),
)
title_label.pack(side="left", fill="x", expand=True)

author_label = ctk.CTkLabel(
    thead_frame,
    text="저자",
    width=50,
    height=30,
    corner_radius=0,
    fg_color=("#F9F9FA", "#343638"),
)
author_label.pack(side="left")

publisher_label = ctk.CTkLabel(
    thead_frame,
    text="출판사",
    width=50,
    height=30,
    corner_radius=0,
    fg_color=("#F9F9FA", "#343638"),
)
publisher_label.pack(side="left")

book_num_label = ctk.CTkLabel(
    thead_frame,
    text="분류번호",
    width=50,
    height=30,
    corner_radius=0,
    fg_color=("#F9F9FA", "#343638"),
)
book_num_label.pack(side="left")

modifiy_label = ctk.CTkLabel(
    thead_frame,
    text="수정",
    width=50,
    height=30,
    corner_radius=0,
    fg_color=("#F9F9FA", "#343638"),
)
modifiy_label.pack(side="left")

delete_label = ctk.CTkLabel(
    thead_frame,
    text="삭제",
    width=50,
    height=30,
    corner_radius=0,
    fg_color=("#F9F9FA", "#343638"),
)
delete_label.pack(side="left")

if __name__ == "__main__":
    app.mainloop()
