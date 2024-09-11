import customtkinter as ctk
from typing import Callable


class SideMenuButton(ctk.CTkButton):
    _select_color: str
    _original_fg_color: str

    def __init__(self, master=None, select_color="transparent", **kw):
        super().__init__(master, **kw)
        self._select_color = select_color
        self._original_fg_color = self.cget("fg_color")
        self.configure(fg_color=self._select_color)

    def select(self):
        self.configure(fg_color=self._original_fg_color)

    def deselect(self):
        self.configure(fg_color=self._select_color)


class SideMenu(ctk.CTkFrame):
    inner_side_menu: ctk.CTkFrame
    btns: list[ctk.CTkButton]
    last_selected_btn: SideMenuButton

    def _add_btn(self, text: str = "", on_click: Callable[[], None] = lambda: None):
        btn = SideMenuButton(
            self.inner_side_menu,
            text=text,
            height=50,
            text_color=("#111111", "gray98"),  # TODO: 테마에 맞게 나중에 일괄수정 필요
            font=("Arial", 14),
            corner_radius=0,
            # fg_color="transparent",
            select_color="transparent",
        )

        def command():
            self.last_selected_btn.deselect()
            btn.select()
            self.last_selected_btn = btn
            on_click()

        btn.configure(command=command)
        btn.grid(row=len(self.btns), column=0)
        self.btns.append(btn)
        return btn

    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.btns = []

        self.inner_side_menu = ctk.CTkFrame(
            self,
            fg_color="transparent",
        )
        self.inner_side_menu.pack(side="left", fill="x")

        self._add_btn("🏠 Home")

        self._add_btn("🧔‍♂️ 회원관리")

        test = self._add_btn("📗 도서관리")
        # print(test.cget("fg_color"))
        # test.configure(fg_color=("default", "default"))

        self._add_btn("⚙️ 설정")

        self.last_selected_btn = test
        test.select()
