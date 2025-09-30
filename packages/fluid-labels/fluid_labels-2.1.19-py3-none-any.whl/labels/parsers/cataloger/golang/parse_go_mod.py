import re
from collections.abc import Iterator
from typing import cast

from packageurl import PackageURL

from labels.model.file import Location, LocationReadCloser
from labels.model.package import Language, Package, PackageType
from labels.model.relationship import Relationship
from labels.model.release import Environment
from labels.model.resolver import Resolver
from labels.parsers.cataloger.utils import get_enriched_location

GO_DIRECTIVE: re.Pattern[str] = re.compile(
    r"(?P<directive>require|replace) \(",
)
GO_MOD_DEP: re.Pattern[str] = re.compile(
    r"^\s+(?P<product>.+?/[\w\-\.~]+?)\sv(?P<version>\S+)",
)
GO_REPLACE: re.Pattern[str] = re.compile(
    r"^\s+(?P<old_prod>.+?/[\w\-\.~]+?)(\sv(?P<old_ver>\S+))?\s=>"
    r"\s(?P<new_prod>.+?/[\w\-\.~]+?)(\sv(?P<new_ver>\S+))?$",
)
GO_REP_DEP: re.Pattern[str] = re.compile(
    r"replace\s(?P<old_prod>.+?/[\w\-\.~]+?)(\sv(?P<old_ver>\S+))?\s=>"
    r"\s(?P<new_prod>.+?/[\w\-\.~]+?)(\sv(?P<new_ver>\S+))?$",
)
GO_REQ_MOD_DEP: re.Pattern[str] = re.compile(
    r"require\s(?P<product>.+?/[\w\-\.~]+?)\sv(?P<version>\S+)",
)
GO_VERSION: re.Pattern[str] = re.compile(
    r"\ngo (?P<major>\d)\.(?P<minor>\d+)(\.\d+)?\n",
)


def package_url(module_name: str, module_version: str) -> str:
    fields = module_name.split("/")

    if all(not f.strip() for f in fields):
        return ""

    namespace = ""
    name = ""
    subpath = ""

    if len(fields) == 1:
        name = fields[0]
    elif len(fields) == 2:
        name = fields[1]
        namespace = fields[0]
    else:
        name = fields[2]
        namespace = "/".join(fields[:2])
        subpath = "/".join(fields[3:])

    return PackageURL(  # type: ignore[misc]
        type="golang",
        namespace=namespace,
        name=name,
        version=module_version,
        qualifiers=None,
        subpath=subpath,
    ).to_string()


def add_require(
    matched: re.Match[str],
    req_dict: dict[str, Package],
    line_number: int,
    parent_location: Location,
) -> None:
    product: str = matched.group("product")
    version: str = matched.group("version")

    new_location = get_enriched_location(parent_location, line=line_number, is_transitive=False)

    req_dict[product] = Package(
        name=product,
        version=version,
        type=PackageType.GoModulePkg,
        locations=[new_location],
        p_url=package_url(product, version),
        ecosystem_data=None,
        language=Language.GO,
        licenses=[],
    )


def replace_req(
    req_dict: dict[str, Package],
    replace_list: list[tuple[re.Match[str], int]],
    parent_location: Location,
) -> Iterator[Package]:
    for matched, line_number in replace_list:
        match_dict = cast("dict[str, str]", matched.groupdict())
        old_pkg, old_version = match_dict["old_prod"], match_dict["old_ver"]
        repl_pkg, version = match_dict["new_prod"], match_dict["new_ver"]

        if old_pkg not in req_dict:
            continue

        if old_version and not version:
            version = req_dict[old_pkg].version

        if not version or (old_version and req_dict[old_pkg].version != old_version):
            continue

        new_location = get_enriched_location(parent_location, line=line_number, is_transitive=False)

        req_dict[old_pkg] = Package(
            name=repl_pkg,
            version=version,
            type=PackageType.GoModulePkg,
            locations=[new_location],
            p_url=package_url(repl_pkg, version),
            language=Language.GO,
            licenses=[],
        )

    return iter(req_dict.values())


def resolve_go_deps(
    content: str,
    location: Location,
) -> Iterator[Package]:
    go_req_directive: str = ""
    replace_list: list[tuple[re.Match[str], int]] = []
    req_dict: dict[str, Package] = {}

    for line_number, line in enumerate(content.splitlines(), 1):
        if matched := GO_REQ_MOD_DEP.search(line):
            add_require(matched, req_dict, line_number, location)
        elif replace := GO_REP_DEP.search(line):
            replace_list.append((replace, line_number))
        elif not go_req_directive:
            if directive := GO_DIRECTIVE.match(line):
                go_req_directive = directive.group("directive")
        elif go_req_directive == "replace":
            if replace := GO_REPLACE.search(line):
                replace_list.append((replace, line_number))
                continue
            go_req_directive = ""
        elif matched := GO_MOD_DEP.search(line):
            add_require(matched, req_dict, line_number, location)
        else:
            go_req_directive = ""
    return replace_req(req_dict, replace_list, location)


def parse_go_mod(
    _: Resolver | None,
    __: Environment | None,
    reader: LocationReadCloser,
) -> tuple[list[Package], list[Relationship]]:
    packages = []
    content = reader.read_closer.read()
    go_version = GO_VERSION.search(content)
    if not go_version:
        return [], []
    major = int(cast("dict[str, str]", go_version.groupdict())["major"])
    minor = int(cast("dict[str, str]", go_version.groupdict())["minor"])
    if major >= 2 or (major == 1 and minor >= 17):
        packages = list(resolve_go_deps(content, reader.location))
    return packages, []
