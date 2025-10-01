from bluer_objects.README.items import ImageItems

from bluer_ugv.README.consts import (
    assets2_bluer_swallow,
    bluer_swallow_electrical_design,
    bluer_swallow_ultrasonic_sensor_design,
)

items = ImageItems(
    {
        f"{bluer_swallow_electrical_design}/digital.png": f"{bluer_swallow_electrical_design}/digital.svg",
        f"{assets2_bluer_swallow}/20250609_164433.jpg": "",
        f"{assets2_bluer_swallow}/20250614_102301.jpg": "",
        f"{assets2_bluer_swallow}/20250614_114954.jpg": "",
        f"{assets2_bluer_swallow}/20250615_192339.jpg": "",
        f"{assets2_bluer_swallow}/20250703_153834.jpg": "",
        f"{assets2_bluer_swallow}/design/v2/01.jpg": "",
        f"{assets2_bluer_swallow}/design/v3/01.jpg": "",
        f"{assets2_bluer_swallow}/design/v4/01.jpg": "",
        f"{bluer_swallow_ultrasonic_sensor_design}/geometry.png?raw=true": f"{bluer_swallow_ultrasonic_sensor_design}/geometry.svg",
        f"{assets2_bluer_swallow}/20250925_213013.jpg": "",
        f"{assets2_bluer_swallow}/20250925_214017.jpg": "",
        f"{assets2_bluer_swallow}/20250928_160425.jpg": "",
        f"{assets2_bluer_swallow}/20250928_160449.jpg": "",
        f"{assets2_bluer_swallow}/design/head-v1/01.jpg": "",
    }
)


docs = [
    {
        "path": "../docs/bluer_swallow/digital/design/shield.md",
        "items": items,
    },
]
