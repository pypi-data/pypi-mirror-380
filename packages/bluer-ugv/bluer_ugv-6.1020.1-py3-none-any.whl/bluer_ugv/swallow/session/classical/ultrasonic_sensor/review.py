from blueness import module

from bluer_ugv import NAME
from bluer_ugv.swallow.session.classical.ultrasonic_sensor.log import (
    UltrasonicSensorDetectionLog,
)
from bluer_ugv.logger import logger


NAME = module.name(__file__, NAME)


def review(
    object_name: str,
    export_gif: bool = False,
    log: bool = True,
) -> bool:
    logger.info("{}.review({})".format(NAME, object_name))

    detection_log = UltrasonicSensorDetectionLog()

    if not detection_log.load(
        object_name=object_name,
    ):
        return False

    if not detection_log.export(
        object_name=object_name,
        line_width=80,
        export_gif=export_gif,
        log=log,
    ):
        return False

    return True
