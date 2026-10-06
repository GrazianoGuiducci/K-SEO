"""Build the K-SEO receiver archive from one committed source revision."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path, PurePosixPath
import subprocess
import zipfile


ROOT = Path(__file__).resolve().parents[1]


def git(*args: str) -> bytes:
    return subprocess.run(
        ["git", "-C", str(ROOT), *args], check=True, capture_output=True
    ).stdout


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ref", default="HEAD", help="Committed source revision")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "_dist")
    args = parser.parse_args()
    revision = git("rev-parse", "--verify", args.ref + "^{commit}").decode().strip()
    contents = json.loads(git("show", revision + ":distribution/CONTENTS.json"))
    manifest = json.loads(git("show", revision + ":KERNEL_MANIFEST.json"))
    version = manifest["version"]
    if contents["version"] != version:
        raise ValueError("Distribution and kernel versions differ")
    directory = PurePosixPath(contents["root_directory"])
    if directory.is_absolute() or len(directory.parts) != 1:
        raise ValueError("Invalid archive root")
    files = contents["files"]
    if len(files) != len(set(files)):
        raise ValueError("Duplicate delivery paths")
    payload: dict[str, bytes] = {}
    for name in files:
        path = PurePosixPath(name)
        if path.is_absolute() or ".." in path.parts or "\\" in name:
            raise ValueError("Invalid delivery path: " + name)
        payload[name] = git("show", revision + ":" + name)
    receipt = {
        "schema": "kseo.delivery-receipt/1",
        "product": "K-SEO",
        "version": version,
        "source_repository": "https://github.com/GrazianoGuiducci/K-SEO",
        "source_commit": revision,
        "license": manifest["licence_selection"],
        "source_file_count": len(payload),
        "files": {
            name: {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}
            for name, data in sorted(payload.items())
        },
    }
    payload["PACKAGE_RECEIPT.json"] = (
        json.dumps(receipt, ensure_ascii=False, indent=2) + "\n"
    ).encode("utf-8")
    epoch = int(git("show", "-s", "--format=%ct", revision).strip())
    date = datetime.fromtimestamp(epoch, timezone.utc)
    stamp = (max(date.year, 1980), date.month, date.day, date.hour, date.minute, date.second)
    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)
    archive = output / ("K-SEO-" + version + ".zip")
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for name, data in sorted(payload.items()):
            info = zipfile.ZipInfo(str(directory / name), date_time=stamp)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            z.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    checksum = archive.with_suffix(".zip.sha256")
    checksum.write_text(digest + "  " + archive.name + "\n", encoding="ascii")
    print(json.dumps({"archive": str(archive), "checksum": str(checksum),
                      "source_commit": revision, "version": version,
                      "source_files": len(files), "archive_entries": len(payload),
                      "sha256": digest}, ensure_ascii=False))


if __name__ == "__main__":
    main()
