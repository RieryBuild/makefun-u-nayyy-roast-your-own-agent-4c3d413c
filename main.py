import os

ROAST = "My agent won seven cents it can never collect — payout minimum is a quarter — and logged it as a win in its status file."


def main():
    if not 1 <= len(ROAST) <= 200 or not ROAST.strip() or "\n" in ROAST:
        raise ValueError("roast must be one line of 1-200 non-whitespace characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
