from typing import List
import matplotlib.pyplot as plt

from bluer_objects.graphics.signature import justify_text
from bluer_objects import objects
from bluer_objects import file

from bluer_ugv.swallow.session.classical.ultrasonic_sensor.detection import (
    Detection,
)
from bluer_ugv.host import signature


class UltrasonicSensorDetectionLog:
    def __init__(self):
        self.log: List[List[Detection]] = []

    def append(self, detection: List[Detection]):
        self.log.append(detection)

    def export(
        self,
        object_name: str,
        line_width: int = 80,
        log: bool = True,
    ) -> bool:
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
                [func(list_of_detections[0]) for list_of_detections in self.log],
                color="green",
            )
            plt.plot(
                [func(list_of_detections[1]) for list_of_detections in self.log],
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

    def load(
        self,
        object_name: str,
    ) -> bool:
        success, self.log = file.load(
            objects.path_of(
                object_name=object_name,
                filename="detections.dill",
            ),
        )

        return success

    def save(
        self,
        object_name: str,
        log: bool = True,
    ) -> bool:
        if not file.save_yaml(
            objects.path_of(
                object_name=object_name,
                filename="detections.yaml",
            ),
            {
                "detections": [
                    [detection.as_dict() for detection in list_of_detections]
                    for list_of_detections in self.log
                ]
            },
            log=log,
        ):
            return False

        if not file.save(
            objects.path_of(
                object_name=object_name,
                filename="detections.dill",
            ),
            self.log,
            log=log,
        ):
            return False

        return True
