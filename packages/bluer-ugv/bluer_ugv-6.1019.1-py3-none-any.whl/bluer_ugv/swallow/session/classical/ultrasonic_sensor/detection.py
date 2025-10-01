from typing import Dict


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

    def as_dict(self) -> Dict:
        return {
            "side": self.side,
            "detection": self.detection,
            "reason": self.reason,
            "echo_detected": self.echo_detected,
            "pulse_ms": self.pulse_ms,
            "distance_mm": self.distance_mm,
        }

    def as_str(self) -> str:
        if self.detection:
            return "{:8}: {:16}, {:6.2f} ms == {:5.0f} mm".format(
                self.side,
                "detection" if self.echo_detected else "no detection",
                self.pulse_ms,
                self.distance_mm,
            )

        return f"{self.side}: no detection ({self.reason})"
