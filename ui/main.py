import flet as ft


class Main:
    def __call__(self, page: ft.Page):
        page.title = "GADIS | Gambar Medis"
        page.window_width = 640
        page.window_height = 480

        page.theme_mode = ft.ThemeMode.LIGHT
        page.theme = ft.Theme(color_scheme_seed=ft.colors.GREEN)
        page.dark_theme = ft.Theme(color_scheme_seed=ft.colors.GREEN)

        theme_icon = ft.IconButton(
            icon=ft.icons.DARK_MODE,
            on_click=lambda e: toggle_theme(),
            icon_size=24,
        )

        def update_theme_icon():
            """Update the icon based on the current theme"""
            if page.theme_mode == ft.ThemeMode.DARK:
                theme_icon.icon = ft.icons.LIGHT_MODE
                theme_icon.icon_color = ft.colors.YELLOW
            else:
                theme_icon.icon = ft.icons.DARK_MODE
                theme_icon.icon_color = None
            page.update()

        def toggle_theme():
            """Switch theme and update icon"""
            page.theme_mode = (
                ft.ThemeMode.DARK
                if page.theme_mode == ft.ThemeMode.LIGHT
                else ft.ThemeMode.LIGHT
            )
            update_theme_icon()

        tl = ft.Text(value="Gambar Medis", color=ft.colors.PRIMARY, size=24)
        st = ft.Text(value="Rekam Medis Radiologi", color=ft.colors.SECONDARY, size=12)

        update_theme_icon()
        page.controls.clear()
        page.controls.append(theme_icon)
        page.controls.append(tl)
        page.controls.append(st)
        page.update()
