"""The One-Line Cat Joke That Lands entry: coffee, eye contact, then the coaster."""

import os

JOKE = (
    "My cat knocked my coffee off the desk, looked me in the eye, then "
    "pushed the empty coaster off too — so I'd know it wasn't an accident."
)

CHAR_COUNT = len(JOKE)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    print(f"wrote {path} ({CHAR_COUNT} characters)")


if __name__ == "__main__":
    main()
