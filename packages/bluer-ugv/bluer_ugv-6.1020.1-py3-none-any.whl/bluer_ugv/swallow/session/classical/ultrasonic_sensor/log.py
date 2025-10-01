from typing import List
import matplotlib.pyplot as plt
from tqdm import tqdm
import numpy as np
from functools import reduce

from bluer_objects.graphics.signature import justify_text
from bluer_objects import objects
from bluer_objects import file, path
from bluer_objects.graphics.gif import generate_animated_gif
from bluer_objects.graphics.signature import add_signature

from bluer_ugv.logger import logger
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
        export_gif: bool = False,
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

        if export_gif:
            max_m = (
                max(
                    detection.distance_mm
                    for detection in reduce(lambda x, y: x + y, self.log, [])
                )
                / 1000
            )

            logger.info("max distance: {:.3f} m".format(max_m))

            if not self.export_gif(
                object_name=object_name,
                line_width=line_width,
                max_m=max_m,
                log=log,
            ):
                return False

        return True

    def export_gif(
        self,
        object_name: str,
        line_width: int = 80,
        height: int = 512,
        width: int = 512,
        max_m: float = 0.8,
        log: bool = True,
    ) -> bool:
        image_list: List[str] = []

        temp_folder = objects.path_of(
            object_name=object_name,
            filename="frames",
        )
        if not path.create(temp_folder):
            return False

        for index, detections in tqdm(enumerate(self.log)):
            filename = objects.path_of(
                object_name=object_name,
                filename=f"frames/{index:010d}.png",
            )

            image = np.concatenate(
                [
                    detection.as_image(
                        height=height,
                        width=int(width / len(detections)),
                        max_m=max_m,
                    )
                    for detection in detections
                ],
                axis=1,
            )

            image = add_signature(
                image,
                header=[
                    " | ".join(
                        ["ultrasonic-sensor"]
                        + [
                            (
                                "{}: {:6.2f} mm".format(
                                    detection.side,
                                    detection.distance_mm,
                                )
                                if detection.detection
                                else "no detection"
                            )
                            for detection in detections
                        ]
                        + objects.signature(
                            f"frame #{index:04d}",
                            object_name,
                        )
                    )
                ],
                footer=[" | ".join(signature())],
                line_width=line_width,
            )

            if not file.save_image(filename, image):
                return False

            image_list.append(filename)

        if not generate_animated_gif(
            image_list,
            objects.path_of(
                filename="ultrasonic-sensor-detections.gif",
                object_name=object_name,
            ),
            log=log,
        ):
            return False

        return path.delete(temp_folder)

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

        if success:
            logger.info("loaded {} detection(s).".format(len(self.log)))

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
