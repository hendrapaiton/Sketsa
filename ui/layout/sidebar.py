import flet as ft

def Sidebar(page: ft.Page):
    def handle_change(e):
        page.close(drawer)

    drawer = ft.NavigationDrawer(
        controls=[
            ft.NavigationDrawerDestination(
                label="Radiology",
                icon=ft.Icons.MEDICAL_SERVICES,
                selected_icon=ft.Icons.LOCAL_HOSPITAL,
            ),
            ft.NavigationDrawerDestination(
                label="Patient",
                icon=ft.Icons.PERSON_OUTLINED,
                selected_icon=ft.Icons.PERSON,
            ),
            ft.NavigationDrawerDestination(
                label="Management",
                icon=ft.Icons.SETTINGS_OUTLINED,
                selected_icon=ft.Icons.SETTINGS,
            ),
        ],
        on_change=handle_change,
    )

    return drawer
