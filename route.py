from ui.page.management import Management
from ui.page.overview import Overview
from ui.page.patient import Patient
from ui.page.radiology import Radiology


def route_change(content, route):
    content.controls.clear()
    if route == "Overview":
        content.controls.append(Overview())
    elif route == "Radiology":
        content.controls.append(Radiology())
    elif route == "Patient":
        content.controls.append(Patient())
    elif route == "Management":
        content.controls.append(Management())
    else:
        content.controls.clear()
