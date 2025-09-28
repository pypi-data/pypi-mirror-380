import re
from collections.abc import Iterator
from dataclasses import dataclass
from typing import Self

from .litigants import create_candidate_text, reduce

inre_pattern = re.compile(
    r"""
    ^
    (
        (
            (
                in
                \s+
            )?
            re
            [:\-\s]+ # must have a divider between subject and the in re: indicator
        )|
        (
            in
            \s+
            the
            \s+
            matter
            \s+
            of
            \W+
            (
                the
                \s+
            )?
        )
    )
    (?P<subject>
        [,\w\s\.-]+ # will stop at the first comma
    )
    """,
    re.X | re.I,
)


@dataclass
class InreTitle:
    subject: str

    def __post_init__(self):
        self.cleaned_text = reduce(self.subject)

    def __repr__(self):
        return f"<InreTitle: {self.cleaned_text}>"

    def __str__(self):
        return f"Re: {self.cleaned_text}"

    @classmethod
    def extract(cls, text: str) -> Iterator[Self]:
        """Extracts component elements of the title text before creating
        a short title.

        Examples:
            >>> next(InreTitle.extract("Re: Request Of (Ret.) Chief Justice Artemio V. Panganiban For Re-Computation Of His Creditable Service For The Purpose Of Re-Computing His Retirement Benefits."))
            <InreTitle: Request of Chief Justice Artemio V. Panganiban for Re-Computation of His Creditable Service for the Purpose of Re-Computing His Retirement Benefits.>
            >>> next(InreTitle.extract('In Re Jose De Borja, Applicant And Appellant; And In Re Jose Flores, Applicant And, Appellee.'))
            <InreTitle: Jose De Borja, Applicant And Appellant>


        Args:
            text (str): Raw title text

        Yields:
            Iterator[Self]: Iterator of matching short titles
        """  # noqa: E501
        candidate = create_candidate_text(text)
        for match in inre_pattern.finditer(candidate):
            if subject := match.group("subject"):
                yield cls(subject=subject)

    @classmethod
    def single_extract(cls, text: str) -> Self | None:
        """Generate first simplified inre string from a decision title's text.

        Args:
            text (str): Raw title text.

        Yields:
            Self: inre strings found in the title text.
        """  # noqa: E501
        try:
            return next(cls.extract(text))
        except StopIteration:
            return None
