from packageurl import PackageURL
from pydantic import ValidationError

from labels.model.ecosystem_data.redhat import RpmDBEntry
from labels.model.file import Location, LocationReadCloser
from labels.model.package import Language, Package, PackageType
from labels.model.relationship import Relationship
from labels.model.release import Environment, Release
from labels.model.resolver import Resolver
from labels.parsers.cataloger.redhat.rpmdb import open_db
from labels.parsers.cataloger.redhat.rpmdb.package import PackageInfo
from labels.parsers.cataloger.utils import get_enriched_location, log_malformed_package_warning


def package_url(  # noqa: PLR0913
    *,
    name: str,
    arch: str | None,
    epoch: int | None,
    source_rpm: str,
    version: str,
    release: str,
    distro: Release | None,
) -> str:
    namespace = ""
    if distro:
        namespace = distro.id_
    qualifiers: dict[str, str] = {}
    if arch:
        qualifiers["arch"] = arch
    if epoch:
        qualifiers["epoch"] = str(epoch)
    if source_rpm:
        qualifiers["upstream"] = source_rpm

    return PackageURL(
        type="rpm",
        namespace=namespace,
        name=name,
        version=f"{version}-{release}",
        qualifiers=qualifiers,
        subpath="",
    ).to_string()


def to_int(value: int | None, default: int = 0) -> int:
    return int(value) if isinstance(value, int) else default


def to_el_version(epoch: int | None, version: str, release: str) -> str:
    if epoch:
        return f"{epoch}:{version}-{release}"
    return f"{version}-{release}"


def new_redhat_package(
    *, entry: PackageInfo, location: Location, env: Environment
) -> Package | None:
    name = entry.name
    version = entry.version

    if not name or not version:
        return None

    ecosystem_data = RpmDBEntry(
        name=name,
        version=version,
        epoch=entry.epoch,
        arch=entry.arch,
        release=entry.release,
        source_rpm=entry.source_rpm,
    )

    new_location = get_enriched_location(location)

    try:
        return Package(
            name=name,
            version=to_el_version(entry.epoch, version, entry.release),
            locations=[new_location],
            language=Language.UNKNOWN_LANGUAGE,
            licenses=[entry.license],
            type=PackageType.RpmPkg,
            ecosystem_data=ecosystem_data,
            p_url=package_url(
                name=name,
                arch=entry.arch,
                epoch=entry.epoch,
                source_rpm=entry.source_rpm,
                version=version,
                release=entry.release,
                distro=env.linux_release,
            ),
        )
    except ValidationError as ex:
        log_malformed_package_warning(new_location, ex)
        return None


def parse_rpm_db(
    _: Resolver,
    env: Environment,
    reader: LocationReadCloser,
) -> tuple[list[Package], list[Relationship]]:
    packages: list[Package] = []

    if not reader.location.coordinates:
        return packages, []

    database = open_db(reader.location.coordinates.real_path)

    if not database:
        return packages, []

    for entry in database.list_packages():
        package = new_redhat_package(entry=entry, env=env, location=reader.location)
        if package is not None:
            packages.append(package)
    return packages, []
