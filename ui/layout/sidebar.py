import flet as ft
from route import route_change


def Sidebar(page: ft.Page, content: ft.Column) -> ft.NavigationDrawer:
    """Creates a sidebar with navigation options."""
    route_change(page, content, "Overview")

    def handle_change(e):
        selected_index = e.control.selected_index
        selected_label = e.control.controls[selected_index].label
        route_change(page, content, selected_label)
        page.close(drawer)

    drawer = ft.NavigationDrawer(
        controls=[
            ft.NavigationDrawerDestination(
                label="Overview",
                icon=ft.Icons.DASHBOARD,
                selected_icon=ft.Icons.SPEED,
            ),
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
