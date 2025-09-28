import datetime
import unicodedata
from collections.abc import Iterator
from typing import Self

from dateutil.parser import parse
from pydantic import BaseModel, ConfigDict, Field, field_validator

from .published_report import REPORT_PATTERN
from .publisher import ReportOffg, ReportPhil, ReportSCRA, get_publisher_label


def is_eq(a: str | None, b: str | None) -> bool:
    """Checks if string `a` is not None, string `b` is not None and both
    `a` and `b` are equal."""
    if a and b:
        if a.lower() == b.lower():
            return True
    return False


class Report(BaseModel):
    """The `REPORT_PATTERN` is a `re.Pattern` object that
    contains pre-defined regex group names. These group names can be mapped
    to the `Report` model's fields:

    Field | Type | Description
    --:|:--:|:--
    `publisher` | optional (str) | Type of the publisher.
    `volume` | optional (str) | Publisher volume number.
    `page` | optional (str) | Publisher volume page.
    `volpubpage` | optional (str) | Combined fields: <volume> <publisher> <page>
    `report_date` | optional (date) | Optional date associated with the report citation

    It's important that each field be **optional**. The `Report` will be joined
    to another `BaseModel` object, i.e. the `Docket`, in a third-party library.
    It must be stressed that the `Report` object is only one part of
    the eventual `DockerReportCitation` object. It can:

    1. have both a `Docket` and a `Report`,
    2. have just a `Docket`;
    3. have just a `Report`.

    If the value of the property exists, it represents whole `@volpubpage` value.

    1. `@phil`
    2. `@scra`
    3. `@offg`
    """

    model_config = ConfigDict(str_strip_whitespace=True)

    publisher: str | None = Field(default=None, max_length=5)
    volume: str | None = Field(
        default=None,
        description="Can exceptionally include letters e.g. vol 1a",
        max_length=10,
    )
    page: str | None = Field(
        default=None,
        description="Page number can have letters, e.g. 241a",
        max_length=5,
    )
    report_date: datetime.date | None = Field(
        default=None,
        description="Exceptionally, report citations reference dates.",
    )

    @field_validator("publisher")
    def publisher_limited_to_phil_scra_offg(cls, v):
        options = (ReportPhil.label, ReportSCRA.label, ReportOffg.label)
        if v and v not in options:
            raise ValueError(f"not allowed in {options=}")
        return v

    def __repr__(self) -> str:
        return f"<Report {self.volpubpage}>"

    def __str__(self) -> str:
        return self.volpubpage or ""

    def __eq__(self, other: Self) -> bool:
        """Naive equality checks will only compare direct values,
        exceptionally, when volume, publisher and page are provided,
        must compare all three values with each other.

        Examples:
            >>> a = Report(volume='10', publisher='Phil.', page='25')
            >>> b = Report(volume='10', publisher='Phil.')
            >>> a == b
            False
            >>> c = Report(volume='10', publisher='SCRA', page='25')
            >>> a == c
            False
            >>> d = Report(volume='10', publisher='Phil.', page='25')
            >>> a == d
            True

        Args:
            other (Self): The other Report instance to compare.

        Returns:
            bool: Whether values are equal
        """
        opt_1 = is_eq(self.phil, other.phil)
        opt_2 = is_eq(self.scra, other.scra)
        opt_3 = is_eq(self.offg, other.offg)
        opt_4 = all(
            [
                is_eq(self.publisher, other.publisher),
                is_eq(self.volume, other.volume),
                is_eq(self.page, other.page),
            ]
        )
        return any([opt_1, opt_2, opt_3, opt_4])

    @property
    def phil(self):
        return (
            f"{self.volume} {ReportPhil.label} {self.page}"
            if self.publisher == ReportPhil.label
            else None
        )

    @property
    def scra(self):
        return (
            f"{self.volume} {ReportSCRA.label} {self.page}"
            if self.publisher == ReportSCRA.label
            else None
        )

    @property
    def offg(self):
        return (
            f"{self.volume} {ReportOffg.label} {self.page}"
            if self.publisher == ReportOffg.label
            else None
        )

    @property
    def volpubpage(self):
        return self.phil or self.scra or self.offg

    @classmethod
    def extract_reports(cls, text: str) -> Iterator["Report"]:
        """Given sample legalese `text`, extract all Supreme Court `Report` patterns.

        Examples:
            >>> sample = "250 Phil. 271, 271-272, Jan. 1, 2019"
            >>> report = next(Report.extract_reports(sample))
            >>> type(report)
            <class 'citation_report.main.Report'>
            >>> report.volpubpage
            '250 Phil. 271'
            >>> unnormalized = "50\xa0 Off. Gaz.,\xa0 583"
            >>> report1 = next(Report.extract_reports(unnormalized))
            >>> report1.volpubpage
            '50 O.G. 583'

        Args:
            text (str): Text containing report citations.

        Yields:
            Iterator["Report"]: Iterator of `Report` instances
        """
        text = unicodedata.normalize("NFKD", text)
        for match in REPORT_PATTERN.finditer(text):
            report_date = None
            if text := match.group("report_date"):
                try:
                    report_date = parse(text).date()
                except Exception:
                    report_date = None

            publisher = get_publisher_label(match)
            volume = match.group("volume")
            page = match.group("page")

            if publisher and volume and page:
                yield Report(
                    publisher=publisher,
                    volume=volume,
                    page=page,
                    report_date=report_date,
                )

    @classmethod
    def extract_from_dict(cls, data: dict, report_type: str) -> str | None:
        """Assuming a dictionary with any of the following report_type keys
        `scra`, `phil` or `offg`, get the value of the Report property.

        Examples:
            >>> sample_data = {"scra": "14 SCRA 314"} # dict
            >>> Report.extract_from_dict(sample_data, "scra")
            '14 SCRA 314'

        Args:
            data (dict): A `dict` containing a possible report `{key: value}`
            report_type (str): Must be either "scra", "phil", or "offg"

        Returns:
            str | None: The value of the key `report_type` in the `data` dict.
        """
        if report_type.lower() in ["scra", "phil", "offg"]:
            if candidate := data.get(report_type):
                try:
                    obj = next(cls.extract_reports(candidate))
                    # will get the @property of the Report with the same name
                    if hasattr(obj, report_type):
                        return obj.__getattribute__(report_type)
                except StopIteration:
                    return None
        return None

    @classmethod
    def get_unique(cls, text: str) -> list[str]:
        """Will only get `Report` volpubpages (string) from the text. This
        is used later in `citation_utils` to prevent duplicate citations.

        Examples:
            >>> text = "(22 Phil. 303; 22 Phil. 303; 176 SCRA 240; Peñalosa v. Tuason, 22 Phil. 303, 313 (1912); Heirs of Roxas v. Galido, 108 Phil. 582 (1960)); Valmonte v. PCSO, supra; Bugnay Const. and Dev. Corp. v. Laron, 176 SCRA 240 (1989)"
            >>> len(Report.get_unique(text))
            3
            >>> set(Report.get_unique(text)) == {'22 Phil. 303', '176 SCRA 240', '108 Phil. 582'}
            True

        Args:
            text (str): Text to search for report patterns

        Returns:
            list[str]: Unique report `volpubpage` strings found in the text
        """  # noqa: E501
        return list({r.volpubpage for r in cls.extract_reports(text) if r.volpubpage})
