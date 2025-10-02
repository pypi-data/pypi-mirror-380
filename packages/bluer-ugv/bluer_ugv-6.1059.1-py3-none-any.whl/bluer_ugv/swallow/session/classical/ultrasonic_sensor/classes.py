from bluer_objects.env import abcli_object_name

from bluer_ugv import env
from bluer_ugv.swallow.session.classical.ultrasonic_sensor.pack import (
    UltrasonicSensorPack,
)
from bluer_ugv.swallow.session.classical.ultrasonic_sensor.detection import (
    DetectionState,
)
from bluer_ugv.swallow.session.classical.ultrasonic_sensor.log import (
    UltrasonicSensorDetectionLog,
)
from bluer_ugv.swallow.session.classical.keyboard import ClassicalKeyboard
from bluer_ugv.swallow.session.classical.setpoint.classes import ClassicalSetPoint
from bluer_ugv.logger import logger


class ClassicalUltrasonicSensor:
    def __init__(
        self,
        setpoint: ClassicalSetPoint,
        keyboard: ClassicalKeyboard,
    ):
        self.enabled = env.BLUER_UGV_ULTRASONIC_SENSOR_ENABLED == 1
        logger.info(
            "{}: {}".format(
                self.__class__.__name__,
                (
                    "enabled: warning<{:.2f} mm, danger<{:.2f} mm".format(
                        env.BLUER_UGV_ULTRASONIC_SENSOR_WARNING_THRESHOLD,
                        env.BLUER_UGV_ULTRASONIC_SENSOR_DANGER_THRESHOLD,
                    )
                    if self.enabled
                    else "disabled"
                ),
            )
        )

        self.setpoint = setpoint
        self.keyboard = keyboard

        self.pack = None

        self.log = (
            UltrasonicSensorDetectionLog()
            if env.BLUER_UGV_ULTRASONIC_SENSOR_KEEP_LOG == 1
            else None
        )

    def cleanup(self):
        if self.log is not None:
            self.log.save(object_name=abcli_object_name)
            self.log.export(object_name=abcli_object_name)

    def initialize(self) -> bool:
        if not self.enabled:
            return True

        self.pack = UltrasonicSensorPack(
            setmode=False,
            max_m=env.BLUER_UGV_ULTRASONIC_SENSOR_MAX_M,
        )

        return self.pack.valid

    def update(self) -> bool:
        if not self.enabled:
            return True

        if not self.keyboard.ultrasound_enabled:
            return True

        success, detections = self.pack.detect(
            log=env.BLUER_UGV_ULTRASONIC_SENSOR_LOG == 1
        )
        if not success:
            return success

        if self.log is not None:
            self.log.append(detections)

        log_detections: bool = False
        speed = self.setpoint.get(what="speed")
        if any(detection.state == DetectionState.DANGER for detection in detections):
            self.setpoint.stop()
            log_detections = True
            logger.info("⛔️ danger detected, stopping.")
        elif (
            any(detection.state == DetectionState.WARNING for detection in detections)
            and speed > 0
        ):
            self.setpoint.put(
                what="speed",
                value=speed // 2,
            )
            log_detections = True
            logger.info("⚠️ warning detected, lowering speed.")

        if env.BLUER_UGV_ULTRASONIC_SENSOR_LOG == 1:
            log_detections = False

        if log_detections:
            logger.info(
                "{}: {}".format(
                    self.__class__.__name__,
                    ", ".join(
                        [detection.as_str(short=True) for detection in detections]
                    ),
                )
            )

        return True
