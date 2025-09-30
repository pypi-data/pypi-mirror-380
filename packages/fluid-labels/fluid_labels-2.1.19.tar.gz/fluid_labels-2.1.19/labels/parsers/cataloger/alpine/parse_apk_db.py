import re

from labels.model.ecosystem_data.alpine import ApkDBEntry
from labels.model.file import LocationReadCloser
from labels.model.package import Package
from labels.model.relationship import Relationship, RelationshipType
from labels.model.release import Environment
from labels.model.resolver import Resolver
from labels.parsers.cataloger.alpine.package import ParsedData, new_package

APK_DB_GLOB = "**/lib/apk/db/installed"


def _parse_list_values(value: str | None, delimiter: str | None = None) -> list[str]:
    delimiter = delimiter or " "
    if not value:
        return []
    return value.split(delimiter)


def parse_package(package: str) -> ParsedData | None:
    data: dict[str, str] = {}
    lines = package.split("\n")
    key = ""
    for line in lines:
        key = process_line(line, key, data)
    return construct_apk(data)


def process_line(line: str, key: str, data: dict[str, str]) -> str:
    if ":" in line:
        key, value = line.split(":", 1)
        data[key] = value
    elif key and key in data:
        data[key] += "\n" + line.strip()
    return key


def construct_apk(data: dict[str, str]) -> ParsedData | None:
    if not (package := data.get("P")) or not (version := data.get("V")):
        return None

    return ParsedData(
        apk_db_entry=ApkDBEntry(
            package=package,
            origin_package=data.get("o"),
            maintainer=data.get("m"),
            version=version,
            architecture=data.get("A"),
            dependencies=_parse_list_values(data.get("D")),
            provides=_parse_list_values(data.get("p")),
        ),
        license=data.get("L"),
    )


def _build_lookup_table(pkgs: list[Package]) -> dict[str, list[Package]]:
    lookup: dict[str, list[Package]] = {}

    for pkg in pkgs:
        if pkg.ecosystem_data is None:
            continue
        if not isinstance(pkg.ecosystem_data, ApkDBEntry):
            continue
        apkg = pkg.ecosystem_data
        if pkg.name not in lookup:
            lookup[pkg.name] = [pkg]
        else:
            lookup[pkg.name].append(pkg)

        for provides in apkg.provides:
            provides_k = strip_version_specifier(provides)
            if provides_k not in lookup:
                lookup[provides_k] = [pkg]
            else:
                lookup[provides_k].append(pkg)

    return lookup


def discover_package_dependencies(
    pkgs: list[Package],
) -> list[Relationship]:
    lookup: dict[str, list[Package]] = _build_lookup_table(pkgs)
    relationships: list[Relationship] = []

    for pkg in pkgs:
        if not isinstance(pkg.ecosystem_data, ApkDBEntry):
            continue

        apkg = pkg.ecosystem_data

        for dep_specifier in apkg.dependencies:
            dep = strip_version_specifier(dep_specifier)
            relationships.extend(
                Relationship(
                    from_=dep_pk.id_,
                    to_=pkg.id_,
                    type=RelationshipType.DEPENDENCY_OF_RELATIONSHIP,
                )
                for dep_pk in lookup.get(dep, [])
            )
    return relationships


def strip_version_specifier(version: str) -> str:
    splitted_version: list[str] = re.split("[<>=]", version)
    return splitted_version[0]


def parse_apk_db(
    _resolver: Resolver,
    _env: Environment | None,
    reader: LocationReadCloser,
) -> tuple[list[Package], list[Relationship]] | None:
    content = reader.read_closer.read()
    apks = [
        parsed_package
        for package in content.strip().split("\n\n")
        if package and (parsed_package := parse_package(package)) is not None
    ]

    entries = [
        entry
        for apk in apks
        if (entry := new_package(apk, _env.linux_release if _env else None, reader.location))
        is not None
    ]

    return entries, discover_package_dependencies(entries)
