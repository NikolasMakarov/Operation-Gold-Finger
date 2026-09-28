"""Copy the four master directions to each vanilla humanlike body type.

Run with: python Tools/rebuild_worn_variants.py
Edit the unsuffixed direction PNGs and masks first; this script overwrites the
generated body-type copies.
"""

from pathlib import Path
from shutil import copyfile


ROOT = Path(__file__).resolve().parents[1]
APPAREL = ROOT / "Textures/Things/Pawn/Humanlike/Apparel"
NAMES = ("AmethystRing", "EmeraldRing", "AmethystPendant", "EmeraldPendant")
BODY_TYPES = ("Male", "Female", "Thin", "Fat", "Hulk", "Child", "Baby")
DIRECTIONS = ("north", "east", "south", "west")


def main() -> None:
    count = 0
    for name in NAMES:
        directory = APPAREL / name
        for direction in DIRECTIONS:
            for suffix in ("", "m"):
                source = directory / f"{name}_{direction}{suffix}.png"
                if not source.is_file():
                    raise FileNotFoundError(source)
                for body_type in BODY_TYPES:
                    destination = directory / f"{name}_{body_type}_{direction}{suffix}.png"
                    copyfile(source, destination)
                    count += 1
    print(f"Updated {count} worn graphic and mask files.")


if __name__ == "__main__":
    main()
