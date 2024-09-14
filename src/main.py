import customtkinter as ctk
from SideMenu import SideMenu
import components as cmp
from feature import books, users, settings, home

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("assets/themes/green.json")
app = ctk.CTk()
app.title("대출반납 관리 시스템")
app.geometry("800x600")
# app.resizable(False, False)

page_frame = None

side_menu = SideMenu(app)


def on_home_btn_click():
    global page_frame

    if page_frame is not None:
        page_frame.destroy()

    page_frame = home.Page(app)
    page_frame.pack(
        side="left",
        fill="both",
        expand=True,
        padx=10,
        pady=10,
    )


side_btn0 = side_menu.add_btn(
    text="🏠 Home",
    on_click=on_home_btn_click,
)


# --------------------------------------------
def on_users_btn_click():
    global page_frame

    if page_frame is not None:
        page_frame.destroy()

    page_frame = users.Page(app)
    page_frame.pack(
        side="left",
        fill="both",
        expand=True,
        padx=10,
        pady=10,
    )


side_btn1 = side_menu.add_btn(
    text="🧔‍♂️ 회원관리",
    on_click=on_users_btn_click,
)


# --------------------------------------------
def on_books_btn_click():
    global page_frame

    if page_frame is not None:
        page_frame.destroy()

    page_frame = books.Page(app)
    page_frame.pack(
        side="left",
        fill="both",
        expand=True,
        padx=10,
        pady=10,
    )


side_btn2 = side_menu.add_btn(
    text="📗 도서관리",
    on_click=on_books_btn_click,
)


# --------------------------------------------
def on_settings_btn_click():
    global page_frame

    if page_frame is not None:
        page_frame.destroy()

    page_frame = settings.Page(app)
    page_frame.pack(
        side="left",
        fill="both",
        expand=True,
        padx=180,
        pady=10,
    )


side_btn3 = side_menu.add_btn(
    text="⚙️ 설정",
    on_click=on_settings_btn_click,
)

# --------------------------------------------
side_menu.select_initial(side_btn2)
side_menu.pack(side="left", fill="y")
on_books_btn_click()

if __name__ == "__main__":
    app.mainloop()
