# continues -v7

from typing import List

from bluer_objects import file
from bluer_objects import objects

from bluer_ugv.logger import logger
from bluer_ugv.swallow.session.classical.ultrasonic_sensor.detection import (
    Detection,
)
from bluer_ugv.swallow.session.classical.ultrasonic_sensor.log import (
    UltrasonicSensorDetectionLog,
)


def test(
    object_name: str,
    max_m: float = 0.8,
    export: bool = True,
    log: bool = True,
    line_width: int = 80,
) -> bool:
    from RPi import GPIO

    from bluer_ugv.swallow.session.classical.ultrasonic_sensor.pack import (
        UltrasonicSensorPack,
    )

    ultrasonic_sensor_pack = UltrasonicSensorPack(max_m=max_m)
    if not ultrasonic_sensor_pack.valid:
        return False

    detection_log = UltrasonicSensorDetectionLog()

    success = True
    try:
        while True:
            success, detection = ultrasonic_sensor_pack.detect(log=log)
            if not success:
                break

            if export:
                detection_log.append(detection)
    except KeyboardInterrupt:
        logger.info("^C detected.")
    finally:
        GPIO.cleanup()

    if not export:
        return success

    if not success:
        return success

    if not detection_log.export(
        object_name=object_name,
        line_width=line_width,
        log=log,
    ):
        return False

    return detection_log.save(object_name=object_name)
