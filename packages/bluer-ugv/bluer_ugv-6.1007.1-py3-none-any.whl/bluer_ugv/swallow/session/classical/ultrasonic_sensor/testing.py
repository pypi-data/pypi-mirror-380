# continues -v7

from typing import List
from RPi import GPIO
import matplotlib.pyplot as plt

from bluer_objects import file
from bluer_objects import objects
from bluer_objects.graphics.signature import justify_text

from bluer_ugv.logger import logger
from bluer_ugv.swallow.session.classical.ultrasonic_sensor.pack import (
    ClassicalUltrasonicSensorPack,
    Detection,
)
from bluer_ugv.host import signature


def test(
    object_name: str,
    max_m: float = 0.8,
    graph: bool = True,
    log: bool = True,
    line_width: int = 80,
) -> bool:
    ultrasonic_sensor_pack = ClassicalUltrasonicSensorPack(max_m=max_m)
    if not ultrasonic_sensor_pack.valid:
        return False

    list_of_detection: List[Detection] = []

    success = True
    try:
        while True:
            success, detection = ultrasonic_sensor_pack.detect(log=log)
            if not success:
                break

            if graph:
                list_of_detection.append(detection)
    except KeyboardInterrupt:
        logger.info("^C detected.")
    finally:
        GPIO.cleanup()

    if not graph:
        return success

    if not success:
        return success

    for func, name in zip(
        [
            lambda detection: int(detection.detection),
            lambda detection: int(detection.echo_detected),
            lambda detection: detection.pulse_ms,
            lambda detection: detection.distance_mm,
        ],
        [
            "detection",
            "echo detection",
            "pulse (ms)",
            "distance(mm)",
        ],
    ):
        plt.figure(figsize=(5, 5))
        plt.plot(
            [func(detection[0]) for detection in list_of_detection],
            color="green",
        )
        plt.plot(
            [func(detection[1]) for detection in list_of_detection],
            color="blue",
        )

        plt.title(
            justify_text(
                " | ".join(
                    [
                        "ultrasonic-sensor",
                    ]
                    + objects.signature(object_name=object_name)
                ),
                line_width=line_width,
                return_str=True,
            )
        )
        plt.xlabel(
            justify_text(
                " | ".join(signature()),
                line_width=line_width,
                return_str=True,
            )
        )
        plt.ylabel(name)
        plt.legend(["left", "right"])
        plt.tight_layout()
        plt.grid(True)
        if not file.save_fig(
            objects.path_of(
                object_name=object_name,
                filename="{}.png".format(
                    name.replace(" ", "-").replace("(", "-").replace(")", "-")
                ),
            ),
            log=log,
        ):
            return False

    return True
