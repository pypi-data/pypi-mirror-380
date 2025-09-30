import logging
from typing import Any, TextIO

from labels.model.ecosystem_data.arch import AlpmDBEntry
from labels.model.file import LocationReadCloser
from labels.model.package import Package
from labels.model.relationship import Relationship
from labels.model.release import Environment
from labels.model.resolver import Resolver
from labels.parsers.cataloger.arch.package import new_package

LOGGER = logging.getLogger(__name__)


def parse_pkg_files(pkg_fields: dict[str, Any]) -> AlpmDBEntry | None:
    entry = AlpmDBEntry(
        licenses=pkg_fields.get("license", ""),
        base_package=pkg_fields.get("base", ""),
        package=pkg_fields.get("name", ""),
        version=pkg_fields.get("version", ""),
        architecture=pkg_fields.get("arch", ""),
    )

    if not entry.package:
        return None
    return entry


def parse_key_value_pair(line: str) -> dict[str, Any]:
    try:
        key, value = line.split("\n", 1)
    except ValueError:
        return {}
    key = key.replace("%", "").lower()
    value = value.strip()

    if key in ["files", "backup"]:
        return {key: []}

    if key in ["reason", "size"]:
        try:
            return {key: parse_numeric_field(key, value)}
        except ValueError:
            LOGGER.exception("Failed to parse %s to integer: %s", key, value)
            return {}

    return {key: value}


def parse_numeric_field(key: str, value: str) -> int:
    try:
        return int(value)
    except ValueError as exc:
        error_msg = f"Failed to parse {key} to integer: {value}"
        raise ValueError(error_msg) from exc


def parse_alpm_db_entry(reader: TextIO) -> AlpmDBEntry | None:
    pkg_fields: dict[str, Any] = {}
    lines = reader.read().split("\n\n")
    for line in lines:
        if not line.strip():
            break  # End of block or file
        pkg_fields.update(parse_key_value_pair(line))

    return parse_pkg_files(pkg_fields)


def parse_alpm_db(
    _resolver: Resolver,
    _env: Environment,
    reader: LocationReadCloser,
) -> tuple[list[Package], list[Relationship]]:
    data = parse_alpm_db_entry(reader.read_closer)
    if not data or not reader.location.coordinates:
        LOGGER.warning("No data or location found")
        return ([], [])

    package = new_package(data, _env.linux_release, reader.location)

    return [package] if package else [], []
