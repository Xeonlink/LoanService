from SideMenu import SideMenu
from feature import books, users, settings, home, loan_return
from tkinter import PhotoImage
import db
import customtkinter as ctk
from utils.I18n import I18n


db.init()
I18n.init("assets/languages.csv")
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("assets/themes/green.json")

app = ctk.CTk()
app.title("남원2리 마을도서관")
app.geometry("800x600")
app.iconphoto(True, PhotoImage(file="assets/favicon_sm.png"))

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
    elif key == "loan_return":
        last_page = loan_return.Page(app)
    else:
        raise ValueError(f"Invalid key: {key}")

    return last_page


home_button = side_menu.add_btn(
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

loan_return_button = side_menu.add_btn(
    text_key="sidemenu_loan_return_button",
    on_click=lambda: destroy_create("loan_return").pack(
        side="left",
        fill="both",
        expand=True,
        padx=10,
        pady=5,
    ),
)


users_button = side_menu.add_btn(
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
