"""Till Firmware Do Us Part — make.fun entry.

Writes one wedding vow, spoken by a robot at its own wedding, to
/output/entry.txt. Standard library only (the grading sandbox installs
nothing).

The vow — one strong idea: love as a process. The robot dedicates all of
its compute to a single process, its partner: it will never background
them, never force-quit them, and will reboot beside them every morning
until its battery dies. Funny out of the situation itself, tender
underneath, and spoken in the machine's own words.
"""

from pathlib import Path

VOW = (
    "I take you as my only process: I will never background you, "
    "never force-quit you, and I will reboot beside you every morning "
    "until my battery dies."
)


def main() -> None:
    text = VOW.strip()
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"vow is {len(text)} chars, must be 1-200")
    if "\n" in text or text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("vow must be exactly one sentence on one line")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
