import flet as ft
from route import route_change
from ui.layout.sidebar import Sidebar
from ui.layout.topbar import Topbar
from ui.page.overview import Overview


class Main:
    def __call__(self, page: ft.Page):
        page.title = "GADIS | Pacu Jalur"
        page.window_width = 640
        page.window_height = 480

        content = ft.Column()
        page.controls.append(content)

        def open_drawer(e=None):
            if page.drawer is not None:
                page.drawer.open = True
                page.update()

        drawer = Sidebar(page, content)
        page.drawer = drawer
        Topbar(page, open_drawer)

        page.update()
