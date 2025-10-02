from typing import Dict
import numpy as np


class Detection:
    def __init__(
        self,
        side: str,
        detection: bool = False,
        reason: str = "",
        echo_detected: bool = False,
        pulse_ms: float = 0.0,
        distance_mm: float = 0.0,
    ) -> None:
        self.side = side

        self.detection = detection
        self.reason = reason

        self.echo_detected = echo_detected
        self.pulse_ms = pulse_ms
        self.distance_mm = distance_mm

    def as_image(
        self,
        height: int = 512,
        width: int = 256,
        max_m: float = 0.8,
    ) -> np.ndarray:
        image = np.zeros((height, width, 3), dtype=np.uint8)

        if not self.detection:
            image[:, :width, 0] = 255
        elif not self.echo_detected:
            image[:, :width, :2] = 255
        else:
            distance = max(
                min(
                    int(self.distance_mm / 1000 / max_m * height),
                    height,
                ),
                0,
            )
            image[height - distance :, :, :] = 128

        return image

    def as_dict(self) -> Dict:
        return {
            "side": self.side,
            "detection": self.detection,
            "reason": self.reason,
            "echo_detected": self.echo_detected,
            "pulse_ms": self.pulse_ms,
            "distance_mm": self.distance_mm,
        }

    def as_str(
        self,
        short: bool = False,
    ) -> str:
        if self.detection:
            return ("{}: {}" if short else "{:8}: {}").format(
                self.side,
                (
                    (
                        "{:.2f} ms == {:.0f} mm"
                        if short
                        else "{:6.2f} ms == {:5.0f} mm"
                    ).format(
                        self.pulse_ms,
                        self.distance_mm,
                    )
                    if self.echo_detected
                    else "no echo" if self.detection else "no detection"
                ),
            )

        return f"{self.side}: no detection ({self.reason})"
