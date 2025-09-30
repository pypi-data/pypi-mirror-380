from labels.model.ecosystem_data.base import EcosystemDataModel


class ApkDBEntry(EcosystemDataModel):
    package: str
    version: str
    provides: list[str]
    dependencies: list[str]
    origin_package: str | None = None
    maintainer: str | None = None
    architecture: str | None = None
