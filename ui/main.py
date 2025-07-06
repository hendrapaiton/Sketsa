import flet as ft

class Main:
    def __call__(self, page: ft.Page):
        t = ft.Text(value="Hello, world!", color="green")
        page.controls.append(t)
        page.update()
