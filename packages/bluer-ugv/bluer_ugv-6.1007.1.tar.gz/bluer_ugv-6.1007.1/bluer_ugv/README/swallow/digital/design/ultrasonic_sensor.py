from bluer_objects.README.items import ImageItems

from bluer_ugv.README.consts import (
    assets2,
    assets2_bluer_swallow,
)

items = [
    {
        "path": "../docs/bluer_swallow/digital/design/ultrasonic-sensor",
    },
    {
        "path": "../docs/bluer_swallow/digital/design/ultrasonic-sensor/dev.md",
    },
    {
        "path": "../docs/bluer_swallow/digital/design/ultrasonic-sensor/tester.md",
        "cols": 2,
        "items": ImageItems(
            {
                f"{assets2_bluer_swallow}/20250918_122725.jpg": "",
                f"{assets2_bluer_swallow}/20250918_194715-2.jpg": "",
                f"{assets2_bluer_swallow}/20250918_194804_1.gif": "",
                f"{assets2}/ultrasonic-sensor-tester/00.jpg": "",
            }
        ),
    },
    {
        "path": "../docs/bluer_swallow/digital/design/ultrasonic-sensor/shield.md",
        "items": ImageItems(
            {
                f"{assets2_bluer_swallow}/20250923_142200.jpg": "",
                f"{assets2_bluer_swallow}/20250923_145111.jpg": "",
            }
        ),
    },
]
