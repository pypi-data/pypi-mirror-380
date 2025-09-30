from typing import List

from bluer_options.terminal import show_usage, xtra


def help_test(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("~upload", mono=mono)

    args = [
        "[--graph 0]",
        "[--log 0]",
        "[--max_m 0.8]",
    ]

    return show_usage(
        [
            "@swallow",
            "ultrasonic",
            "test",
            f"[{options}]",
            "[-|<object-name>]",
        ]
        + args,
        "test ultrasonic sensors.",
        mono=mono,
    )


help_functions = {
    "test": help_test,
}
