from feature import books, users, settings, home, loan_return
from tkinter import PhotoImage
from utils.I18n import I18n
from constants import LANGUAGE_FILE_PATH, GREEN_THEME_PATH, ICON_PATH
import topmenu
import customtkinter as ctk
import db


db.init()
I18n.init(LANGUAGE_FILE_PATH)
I18n.lang = "ko"
ctk.set_appearance_mode("system")
ctk.set_default_color_theme(GREEN_THEME_PATH)


class App(ctk.CTk):

    def _destroy_create(self, key: str):

        if self._last_page is not None:
            self._last_page.destroy()

        if key == "home":
            self._last_page = home.Page(self)
        elif key == "users":
            self._last_page = users.Page(self)
        elif key == "books":
            self._last_page = books.Page(self)
        elif key == "settings":
            self._last_page = settings.Page(self)
        elif key == "loan_return":
            self._last_page = loan_return.Page(self)
        else:
            raise ValueError(f"Invalid key: {key}")

        return self._last_page

    def __init__(self):
        super().__init__()
        self.title("남원2리 마을도서관")
        self.geometry("800x600")
        self.iconphoto(True, PhotoImage(file=ICON_PATH))
        # self.attributes("-fullscreen", True)

        self._last_page: ctk.CTkFrame | None = None
        side_menu = topmenu.TopMenu(
            self,
            button_defs=[
                topmenu.ButtonDef(
                    text_key="sidemenu_loan_return_button",
                    on_click=lambda: self._destroy_create("loan_return").pack(
                        side="left", fill="both", expand=True, padx=10, pady=5
                    ),
                ),
                topmenu.ButtonDef(
                    text_key="sidemenu_users_button",
                    on_click=lambda: self._destroy_create("users").pack(
                        side="left", fill="both", expand=True, padx=10, pady=10
                    ),
                ),
                topmenu.ButtonDef(
                    text_key="sidemenu_books_button",
                    on_click=lambda: self._destroy_create("books").pack(
                        side="left", fill="both", expand=True, padx=10, pady=10
                    ),
                ),
                topmenu.ButtonDef(
                    text_key="sidemenu_settings_button",
                    on_click=lambda: self._destroy_create("settings").pack(
                        side="left", fill="both", expand=True
                    ),
                ),
            ],
        )
        side_menu.pack(side="top", fill="x")
        side_menu.buttons[0].invoke()


if __name__ == "__main__":
    App().mainloop()
