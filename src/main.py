import customtkinter as ctk
from SideMenu import SideMenu
import components as cmp
from feature import books

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("assets/themes/green.json")
app = ctk.CTk()
app.title("대출반납 관리 시스템")
app.geometry("800x600")
# app.resizable(False, False)

side_menu = SideMenu(app)
side_btn0 = side_menu.add_btn(text="🏠 Home")
side_btn1 = side_menu.add_btn(text="🧔‍♂️ 회원관리")
side_btn2 = side_menu.add_btn(text="📗 도서관리")
side_btn3 = side_menu.add_btn(text="⚙️ 설정")
side_menu.select_initial(side_btn2)
side_menu.pack(side="left", fill="y")

page_frame = books.Page(app)
page_frame.pack(
    side="left",
    fill="both",
    expand=True,
    padx=10,
    pady=10,
)

if __name__ == "__main__":
    app.mainloop()
