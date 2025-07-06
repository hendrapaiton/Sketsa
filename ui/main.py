import flet as ft


class Main:
    def __call__(self, page: ft.Page):
        page.window_width = 640
        page.window_height = 480
        page.theme_mode = ft.ThemeMode.LIGHT
        
        theme_icon = ft.IconButton(
            icon=ft.icons.DARK_MODE,
            on_click=lambda e: toggle_theme(),
            icon_size=24,
        )

        def update_theme_icon():
            """Update ikon berdasarkan tema saat ini"""
            if page.theme_mode == ft.ThemeMode.DARK:
                theme_icon.icon = ft.icons.LIGHT_MODE
                theme_icon.icon_color = "yellow"
            else:
                theme_icon.icon = ft.icons.DARK_MODE
                theme_icon.icon_color = None
            page.update()

        def toggle_theme():
            """Ganti tema dan update ikon"""
            page.theme_mode = (
                ft.ThemeMode.DARK 
                if page.theme_mode == ft.ThemeMode.LIGHT 
                else ft.ThemeMode.LIGHT
            )
            update_theme_icon()

        update_theme_icon()

        t = ft.Text(value="Hello, world!", color="green")

        page.controls.clear()
        page.controls.append(theme_icon)
        page.controls.append(t)
        page.update()
