from bluer_objects.README.items import ImageItems

from bluer_ugv.README.consts import (
    assets2_bluer_swallow,
    bluer_swallow_mechanical_design,
)

items = ImageItems(
    {
        "https://github.com/kamangir/bluer-ugv/raw/main/diagrams/bluer_swallow/digital.png": "https://github.com/kamangir/bluer-ugv/blob/main/diagrams/bluer_swallow/digital.svg",
        f"{assets2_bluer_swallow}/20250609_164433.jpg": "",
        f"{assets2_bluer_swallow}/20250614_102301.jpg": "",
        f"{assets2_bluer_swallow}/20250614_114954.jpg": "",
        f"{assets2_bluer_swallow}/20250615_192339.jpg": "",
        f"{assets2_bluer_swallow}/20250703_153834.jpg": "",
        f"{assets2_bluer_swallow}/design/v2/01.jpg": "",
        f"{assets2_bluer_swallow}/design/v3/01.jpg": "",
        f"{assets2_bluer_swallow}/design/v4/01.jpg": "",
        f"{bluer_swallow_mechanical_design}/ultrasonic-sensors/geometry.png?raw=true": f"{bluer_swallow_mechanical_design}/ultrasonic-sensors/geometry.svg",
    }
)


docs = [
    {
        "path": "../docs/bluer_swallow/digital/design/shield.md",
        "items": items,
    },
]
