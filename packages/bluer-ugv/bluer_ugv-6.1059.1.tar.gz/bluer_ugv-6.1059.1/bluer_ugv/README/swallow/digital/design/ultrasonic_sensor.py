from bluer_objects.README.items import ImageItems

from bluer_ugv.README.consts import (
    assets2,
    assets2_bluer_swallow,
    bluer_swallow_ultrasonic_sensor_design,
)

items = [
    {
        "path": "../docs/bluer_swallow/digital/design/ultrasonic-sensor",
        "items": ImageItems(
            {
                f"{bluer_swallow_ultrasonic_sensor_design}/geometry.png?raw=true": f"{bluer_swallow_ultrasonic_sensor_design}/geometry.svg",
            }
        ),
    },
    {
        "path": "../docs/bluer_swallow/digital/design/ultrasonic-sensor/dev.md",
        "cols": 1,
        "items": ImageItems(
            {
                f"{assets2_bluer_swallow}/20251001_203056_1.gif": "",
                f"{assets2_bluer_swallow}/20251001_185852.jpg": "",
            }
        ),
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
