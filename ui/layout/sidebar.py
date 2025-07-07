import flet as ft

def Sidebar(page: ft.Page):
    def handle_change(e):
        page.close(drawer)

    drawer = ft.NavigationDrawer(
        controls=[
            ft.NavigationDrawerDestination(
                label="Item 1",
                icon=ft.Icons.DOOR_BACK_DOOR_OUTLINED,
                selected_icon=ft.Icons.DOOR_BACK_DOOR,
            ),
            ft.NavigationDrawerDestination(
                icon=ft.Icons.MAIL_OUTLINED,
                label="Item 2",
                selected_icon=ft.Icons.MAIL,
            ),
            ft.NavigationDrawerDestination(
                icon=ft.Icons.PHONE_OUTLINED,
                label="Item 3",
                selected_icon=ft.Icons.PHONE,
            ),
        ],
        on_change=handle_change,
    )

    return drawer
