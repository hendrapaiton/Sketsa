import flet as ft
from route import route_change


def Sidebar(page: ft.Page, content: ft.Column) -> ft.NavigationDrawer:
    menu_items = [
        {
            "label": "Overview",
            "icon": ft.Icons.DASHBOARD,
            "selected_icon": ft.Icons.SPEED
        },
        {
            "label": "Radiology",
            "icon": ft.Icons.MEDICAL_SERVICES,
            "selected_icon": ft.Icons.LOCAL_HOSPITAL
        },
        {
            "label": "Patient",
            "icon": ft.Icons.PERSON_OUTLINED,
            "selected_icon": ft.Icons.PERSON
        },
        {
            "label": "Management",
            "icon": ft.Icons.SETTINGS_OUTLINED,
            "selected_icon": ft.Icons.SETTINGS
        },
    ]

    def set_active(index):
        drawer.selected_index = index
        selected_label = menu_items[index]["label"]
        route_change(content, selected_label)
        page.update()

    def handle_change(e):
        idx = e.control.selected_index
        if 0 <= idx < len(menu_items):
            set_active(idx)
            page.close(drawer)

    user_card = ft.Card(
        content=ft.Container(
            content=ft.Row(
                [
                    ft.CircleAvatar(
                        foreground_image_src="https://randomuser.me/api/portraits/men/1.jpg",
                        radius=48,
                    ),
                    ft.Column(
                        [
                            ft.Text("ADMIN", size=18, weight="bold"),
                            ft.Text("John Doe", size=12, color=ft.Colors.GREY),
                        ],
                        alignment="start",
                        spacing=0,
                    ),
                ],
                spacing=12,
                alignment="start",
            ),
            padding=18,
        ),
        margin=ft.margin.only(bottom=8, top=8),
    )

    drawer = ft.NavigationDrawer(
        controls=[
            user_card,
            *[
                ft.NavigationDrawerDestination(
                    label=item["label"],
                    icon=item["icon"],
                    selected_icon=item["selected_icon"],
                )
                for item in menu_items
            ]
        ],
        on_change=handle_change,
        tile_padding=8,
        selected_index=0,
    )

    set_active(0)

    return drawer
