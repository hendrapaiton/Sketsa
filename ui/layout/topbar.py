import flet as ft


def Topbar(page: ft.Page, open_drawer):
    page.theme_mode = ft.ThemeMode.DARK
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.GREEN)
    page.dark_theme = ft.Theme(color_scheme_seed=ft.Colors.GREEN)

    def update_theme_icon():
        if page.theme_mode == ft.ThemeMode.DARK:
            theme_icon.icon = ft.Icons.LIGHT_MODE
            theme_icon.icon_color = ft.Colors.YELLOW
        else:
            theme_icon.icon = ft.Icons.DARK_MODE
            theme_icon.icon_color = None

    def toggle_theme():
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        update_theme_icon()

    theme_icon = ft.IconButton(
        icon=ft.Icons.DARK_MODE,
        on_click=lambda e: toggle_theme(),
        icon_size=18,
    )

    page.appbar = ft.AppBar(
        leading=ft.IconButton(
            icon=ft.Icons.MENU,
            on_click=open_drawer,
            icon_size=18,
        ),
        toolbar_height=36,
        title=ft.Text(
            value="Gambar Medis".upper(),
            color=ft.Colors.PRIMARY,
            size=18,
            weight="bold"),
        actions=[
            theme_icon,
        ],
    )

    update_theme_icon()
