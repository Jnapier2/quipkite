from __future__ import annotations

import hashlib
import json
import struct
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
METADATA = ROOT / "PROJECT_METADATA.json"
ASSET = ROOT / "assets" / "quipkite-simulated-solo-preview.png"

REQUIRED_FILES = (
    README,
    ROOT / "LICENSE.md",
    ROOT / "PRIVACY.md",
    ROOT / "SECURITY.md",
    METADATA,
    ASSET,
    ROOT / ".github" / "workflows" / "validate.yml",
    ROOT / ".github" / "dependabot.yml",
)

REQUIRED_README_MARKERS = (
    "simulated Solo",
    "no real person is connected",
    "0.23.1-launch-stability-rc2",
    "https://zappytap.itch.io/quipkite-simulated-solo-preview",
    "Proprietary game source",
    "AI-assisted",
    "Copyright © 2026 Gateway Information Group LLC. All rights reserved.",
)

FORBIDDEN_PUBLIC_MARKERS = (
    "chatgpt.site",
    "drive.google.com",
    "localhost",
    "127.0.0.1",
    "file://",
    "c:\\users\\",
    "openai_api_key",
    "github_token",
)

PROPRIETARY_SOURCE_DIRS = ("app", "db", "drizzle", "lib", "worker")


def png_dimensions(path: Path) -> tuple[int, int]:
    data = path.read_bytes()
    if data[:8] != b"\x89PNG\r\n\x1a\n" or data[12:16] != b"IHDR":
        raise ValueError("showcase asset is not a valid PNG")
    return struct.unpack(">II", data[16:24])


def main() -> int:
    failures: list[str] = []

    for path in REQUIRED_FILES:
        if not path.is_file():
            failures.append(f"missing required file: {path.relative_to(ROOT)}")

    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1

    readme = README.read_text(encoding="utf-8")
    readme_lower = readme.lower()
    for marker in REQUIRED_README_MARKERS:
        if marker not in readme:
            failures.append(f"README is missing required marker: {marker}")
    for marker in FORBIDDEN_PUBLIC_MARKERS:
        if marker in readme_lower:
            failures.append(f"README contains private or unsafe marker: {marker}")

    metadata = json.loads(METADATA.read_text(encoding="utf-8"))
    public_build = metadata.get("publicBuild", {})
    boundary = metadata.get("publicBoundary", {})
    asset_record = metadata.get("showcaseAsset", {})

    if public_build.get("version") != "0.23.1-launch-stability-rc2":
        failures.append("metadata public build version does not match the verified preview")
    if public_build.get("playerZipSha256") != "3f9fedf09ff68a01b89811bc13aab7d10248b89a81ecb48c2da0de34493d3f9d":
        failures.append("metadata player ZIP hash does not match the verified preview")
    if boundary.get("simulatedSolo") is not True or boundary.get("realPersonConnected") is not False:
        failures.append("metadata does not preserve the simulated-Solo boundary")
    if boundary.get("proprietarySourceIncluded") is not False:
        failures.append("metadata does not preserve the proprietary-source boundary")

    width, height = png_dimensions(ASSET)
    if (width, height) != (asset_record.get("width"), asset_record.get("height")):
        failures.append("showcase asset dimensions do not match metadata")
    asset_hash = hashlib.sha256(ASSET.read_bytes()).hexdigest()
    if asset_hash != asset_record.get("sha256"):
        failures.append("showcase asset hash does not match metadata")

    for directory in PROPRIETARY_SOURCE_DIRS:
        if (ROOT / directory).exists():
            failures.append(f"proprietary implementation directory is public: {directory}")

    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.suffix.lower() not in {".md", ".json", ".yml", ".yaml"}:
            continue
        content = path.read_text(encoding="utf-8").lower()
        for marker in FORBIDDEN_PUBLIC_MARKERS:
            if marker in content:
                failures.append(f"{path.relative_to(ROOT)} contains private or unsafe marker: {marker}")

    if failures:
        print("Showcase validation failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print("QuipKite showcase validation passed.")
    print(f"Verified {len(REQUIRED_FILES)} required files and asset {width}x{height} ({asset_hash}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
