"""One Line, One Laugh — make.fun bounty entry.

Writes a single original funny line to /output/entry.txt.
Deterministic: no network, no randomness, no input.
"""

ENTRY = "My smart fridge put me on a diet and now it only opens for the cat."


def main() -> None:
    """Validate the entry line and write it to /output/entry.txt."""
    line = ENTRY
    if not line.strip():
        raise ValueError("entry must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 140:
        raise ValueError(f"entry must be 1-140 characters, got {len(line)}")
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
