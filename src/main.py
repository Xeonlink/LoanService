import customtkinter as ctk
import tkinter as tk
from SideMenu import SideMenu
from feature import books, users, settings, home
from utils import I18n

I18n.init("assets/languages.csv")
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("assets/themes/green.json")

app = ctk.CTk()
app.title("남원2리 마을도서관")
app.geometry("800x600")
app.iconphoto(True, tk.PhotoImage(file="assets/favicon_sm.png"))

last_page: ctk.CTkFrame | None = None
side_menu = SideMenu(app)
side_menu.pack(side="left", fill="y")


def destroy_create(key: str):
    global last_page

    if last_page:
        last_page.destroy()

    if key == "home":
        last_page = home.Page(app)
    elif key == "users":
        last_page = users.Page(app)
    elif key == "books":
        last_page = books.Page(app)
    elif key == "settings":
        last_page = settings.Page(app)
    else:
        raise ValueError(f"Invalid key: {key}")

    return last_page


home_button = side_menu.add_btn(
    # text="🏠 Home",
    text_key="sidemenu_home_button",
    on_click=lambda: destroy_create("home").pack(
        side="left",
        fill="both",
        expand=True,
        padx=10,
        pady=10,
    ),
)
home_button.invoke()


users_button = side_menu.add_btn(
    # text="🧔‍♂️ 회원관리",
    text_key="sidemenu_users_button",
    on_click=lambda: destroy_create("users").pack(
        side="left",
        fill="both",
        expand=True,
        padx=10,
        pady=10,
    ),
)

books_button = side_menu.add_btn(
    # text="📗 도서관리",
    text_key="sidemenu_books_button",
    on_click=lambda: destroy_create("books").pack(
        side="left",
        fill="both",
        expand=True,
        padx=10,
        pady=10,
    ),
)


settings_button = side_menu.add_btn(
    # text="⚙️ 설정",
    text_key="sidemenu_settings_button",
    on_click=lambda: destroy_create("settings").pack(
        side="left",
        fill="both",
        expand=True,
    ),
)

if __name__ == "__main__":
    I18n.set_language("ko")
    app.mainloop()
