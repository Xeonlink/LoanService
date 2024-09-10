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

# inner_side_menu = ctk.CTkFrame(
#     side_menu,
#     fg_color="transparent",
# )
# inner_side_menu.pack(side="left", fill="x")


# home_btn = ctk.CTkButton(
#     inner_side_menu,
#     text="🏠 Home",
#     height=50,
#     font=("Arial", 14),
#     corner_radius=0,
#     fg_color="transparent",
# )
# home_btn.grid(row=0, column=0)

# users_btn = ctk.CTkButton(
#     inner_side_menu,
#     text="🧔‍♂️ 회원관리",
#     height=50,
#     corner_radius=0,
#     font=("Arial", 14),
#     fg_color="transparent",
# )
# users_btn.grid(row=1, column=0)

# books_btn = ctk.CTkButton(
#     inner_side_menu,
#     text="📗 도서관리",
#     height=50,
#     corner_radius=0,
#     font=("Arial", 14),
#     # fg_color="transparent",
# )
# books_btn.grid(row=2, column=0)

# settings_btn = ctk.CTkButton(
#     inner_side_menu,
#     text="⚙️ 설정",
#     height=50,
#     corner_radius=0,
#     font=("Arial", 14),
#     fg_color="transparent",
# )
# settings_btn.grid(row=3, column=0)

if __name__ == "__main__":
    app.mainloop()
