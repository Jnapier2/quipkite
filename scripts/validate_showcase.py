from __future__ import annotations

import hashlib
import json
import struct
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
METADATA = ROOT / "PROJECT_METADATA.json"
ASSET = ROOT / "assets" / "quipkite-solo-0.36.0.png"

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
    "Solo play uses fictional companions",
    "no real person is connected",
    "0.36.0",
    "privacy.1",
    "genuine screenshot",
    "awaits comparison with the final hosted artifact",
    "https://zappytap.itch.io/quipkite-simulated-solo-preview",
    "Proprietary game source",
    "Generative tools assisted",
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

    if public_build.get("version") != "0.36.0":
        failures.append("metadata version does not match the reviewed artifact")
    if public_build.get("buildId") != "quipkite-0.36.0-20261102-1":
        failures.append("metadata build ID does not match the reviewed artifact")
    if public_build.get("artifactRevision") != "privacy.1" or public_build.get("publicationStatus") != "prepared_not_promoted":
        failures.append("metadata must retain the explicit pending-publication state")
    if public_build.get("playerZipSha256") != "09843F12594DF84BC736741375F6E303CFFC19E4B7DC0F38A46496D945FFC264":
        failures.append("metadata ZIP hash does not match the reviewed artifact")
    if public_build.get("playerZipBytes") != 26669323 or public_build.get("zipEntries") != 64:
        failures.append("metadata ZIP size or entry count does not match the reviewed artifact")
    if any(key in public_build for key in ("itchProjectId", "itchUploadId", "providerBuildId")):
        failures.append("provider deployment identifiers belong in private evidence")
    verification = metadata.get("verification", {})
    if verification.get("unchangedApplicationFiles") != 60 or verification.get("archiveEntriesReviewed") != 64:
        failures.append("metadata archive coverage does not match the reviewed package")
    if verification.get("automatedRegressions") != 8 or verification.get("browserScenarios") != 4:
        failures.append("metadata local-check counts do not match the reviewed evidence")
    if verification.get("verifiedDate") != "2026-11-03":
        failures.append("metadata review date changed without evidence")
    if verification.get("hostingStatus") != "Final hosted artifact comparison pending; no new host clearance":
        failures.append("metadata must preserve the unverified final-host boundary")
    if verification.get("applicationTestsRerun") is not False:
        failures.append("metadata must not claim application tests were rerun")
    if boundary.get("simulatedSolo") is not True or boundary.get("realPersonConnected") is not False:
        failures.append("metadata does not preserve the simulated-Solo boundary")
    if boundary.get("proprietarySourceIncluded") is not False:
        failures.append("metadata does not preserve the proprietary-source boundary")
    online = boundary.get("separateOnlineExperience", {})
    if online != {"linkedFromProduct": True, "requiresAccounts": True, "twoPlayerPlayVerified": False}:
        failures.append("metadata must distinguish separate online access from reviewed Solo play")

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

    print("QuipKite showcase proposal validation passed; hosted promotion remains pending.")
    print(f"Verified {len(REQUIRED_FILES)} required files and asset {width}x{height} ({asset_hash}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
