import re
from collections.abc import Iterator
from dataclasses import dataclass
from typing import Callable, Self

from .litigants import (
    Entity,
    create_candidate_text,
    create_named_group,
    get_canonical_human,
    get_first_mentioned,
    reduce,
)

vs = r"(?P<v>v\.|vs\.?|v\.s\.)"

lhs = create_named_group(
    name="lhs",
    bases=(
        "petitioner",
        "plaintiff",
        "accused",
        "complainant",
    ),
)
lhs_inre = r"(?P<lhs_inre>(in\s+)?re:.*?)"


rhs = create_named_group(
    name="rhs",
    bases=(
        "respondent",
        "oppositor",
        "objector",
        "intervenor",
        "accused",
        "defendant",
    ),
)


adverse_complex = re.compile(
    rf"""
    ({lhs}|{lhs_inre})
    {vs}
    {rhs}
    """,
    re.X | re.I,
)

adverse_simple = re.compile(
    rf"""
    (?P<lhs>.*?)\s+ # non-greedy
    {vs}\s+
    (?P<rhs>.*) # greedy
    """,
    re.X | re.I,
)


@dataclass
class AdverseTitle:
    """Consists of two sides: a left-hand side (`lhs`) and a right-hand side (`rhs`)
    combined by the classic `v.`. The `v` indicates a party on the left-hand side
    is in opposition to a party on the right-hand side."""

    lhs: str
    rhs: str

    def __post_init__(self):
        self.x = self.clean(self.lhs)
        self.y = self.clean(self.rhs)
        self.title = f"{self.x} v. {self.y}"

    def __repr__(self) -> str:
        return f"<AdverseTitle: {str(self)}>"

    def __str__(self) -> str:
        return self.title

    @classmethod
    def clean(cls, party: str):
        """Each of the parties will be processed through a pipeline. It's necessary
        that the pipeline use `get_first_mentioned()` since this culls the original
        text into a smaller text area."""
        ordered_pipeline: list[Callable] = [
            get_first_mentioned,
            get_canonical_human,
            Entity.get_canonical,
            reduce,
        ]
        for process in ordered_pipeline:
            party = process(party)
        return party

    @classmethod
    def from_simple(cls, text: str) -> Self | None:
        """Handle title conventions _without_ labels like petitioner, respondent, etc.

        The limitation in character count is intentional, this can only cover simple cases
        that have already been pre-processed. Otherwise, a case like "Atty. Luis V. SomeLastName, Jr. v.
        Atty. Euge" will not work since the `adverse_simple` pattern will assume two parties:
        `Atty. Luis` and `SomeLastName`

        Examples:
            >>> AdverseTitle.from_simple("People of the Philippines Vs. Goliath")
            <AdverseTitle: People v. Goliath>
            >>> None is AdverseTitle.from_simple("Juan Doe, Complainant, V. Atty. Juan de la Cruz, Respondent.")
            True

        Args:
            text (str): Previously simplified text

        Returns:
            str | None: A matching short title, if found
        """  # noqa: E501
        if len(text) < 60:  #
            candidate = create_candidate_text(text)
            if match := adverse_simple.search(candidate):
                lhs, rhs = match.group("lhs"), match.group("rhs")
                if lhs and rhs:
                    return cls(lhs=lhs, rhs=rhs)
        return None

    @classmethod
    def extract_from_complex(cls, text: str) -> Iterator[Self]:
        """Extracts component elements of the title text before creating
        a short title.

        Examples:
            >>> next(AdverseTitle.extract_from_complex('Juan Doe, Complainant, V. Atty. Juan de la Cruz, Respondent.'))
            <AdverseTitle: Juan Doe v. Atty. de la Cruz>

        Args:
            text (str): Raw title text

        Yields:
            Iterator[Self]: Iterator of matching short titles
        """  # noqa: E501
        candidate = create_candidate_text(text)
        for match in adverse_complex.finditer(candidate):
            if obj := cls.evaluate(match):
                yield obj

    @classmethod
    def evaluate(cls, match: re.Match) -> Self | None:
        """Creates a versus object based on a complex match.

        Args:
            match (re.Match): sourced from `adverse_complex` object.

        Returns:
            Self | None: _description_
        """
        data = match.groupdict()
        lhs, rhs = data.get("lhs_party"), data.get("rhs_party")
        if lhs and rhs:
            return cls(lhs=lhs, rhs=rhs)

        lhs_inre = data.get("lhs_inre")
        if lhs_inre and rhs:
            return cls(lhs=lhs_inre, rhs=rhs)
        return None

    @classmethod
    def single_extract(cls, text: str) -> Self | None:
        """Generate first simplified versus string from a decision title's text.

        Examples:
            >>> AdverseTitle.single_extract("People of the Philippines Vs. Goliath") # uses simple pattern
            <AdverseTitle: People v. Goliath>
            >>> AdverseTitle.single_extract("Juan Doe,[1] Complainant, V. Atty. Juan de la Cruz, Respondent.")
            <AdverseTitle: Juan Doe v. Atty. de la Cruz>
            >>> AdverseTitle.single_extract("In re: Shoop") is None
            True

        Args:
            text (str): Raw title text.

        Yields:
            Self: vs strings found in the title text.
        """  # noqa: E501
        if match := cls.from_simple(text):
            return match

        try:
            return next(cls.extract_from_complex(text))
        except StopIteration:
            return None
