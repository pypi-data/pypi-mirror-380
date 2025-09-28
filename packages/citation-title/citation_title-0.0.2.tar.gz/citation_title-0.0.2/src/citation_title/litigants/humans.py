import re

RAW_FIRSTNAME = r"""
    [A-Z][a-z]+
    (
        (?:
            \s|-
        ) # optional second name connected by dash or space
        ["\w\.]+
    )? # optional second name with alias "Abe"
"""
RAW_MIDDLE = r"[A-Z]\."
RAW_SURNAME = r"""
    (?:
        (d|D)e
        (
            \s
            (l|L)
            (a|os)
        )? # handle "de la Cruz", "delos Santos", "de los Reyes"
        \s
        (\w+)
    )|
    (?:
        [A-Z][a-zñ]+
        (?:
            \s
            (
                ,?\sJr\.|
                ,?\sSr\.|
                III|Iii|
                IV|Iv
            )
        )?
    )
"""


ANONYMOUS = re.compile(
    r"""
    ^
    (?P<anon>
        aaa|
        bbb|
        ccc|
        xxx|
        yyy|
        zzz
    )\W*
    """,
    re.X | re.I,
)


def get_anonymous(text: str) -> str | None:
    if match := ANONYMOUS.search(text):
        if anon := match.group("anon"):
            return anon.upper()
    return None


def create_professional(title: str):
    return re.compile(
        rf"""
            ^
            {title}\s+
            (?P<first>{RAW_FIRSTNAME})\s+
            (
                (
                    (?P<middle>{RAW_MIDDLE}\s+)
                    (?P<last_with_middle>{RAW_SURNAME})
                )|
                (?P<last_only>{RAW_SURNAME})$ # must be terminal if two names (no mid initial)
            )
            """,  # noqa: E501
        re.X,
    )


ATTORNEY = create_professional(title=r"(Att(orne)?y\.?)")


def get_atty(text: str) -> str | None:
    if match := ATTORNEY.search(text):
        last = match.group("last_with_middle") or match.group("last_only")
        if last:
            return f"Atty. {last}"
    return None


ENGINEER = create_professional(title=r"(Eng(inee)?r\.?)")


def get_engr(text: str) -> str | None:
    if match := ENGINEER.search(text):
        last = match.group("last_with_middle") or match.group("last_only")
        if last:
            return f"Engr. {last}"
    return None


SPANISH_Y = re.compile(
    rf"""
    ^
    (?P<first>[A-Z][a-z]+)\s+
    (?P<paternal>{RAW_SURNAME})\s+
    (Y|y)\s+
    (?P<maternal>[A-Z][a-z]+)
    $
    """,
    re.X,
)


def get_spanish_y(text: str) -> str | None:
    """Handle the old style of names

    Examples:
        >>> get_spanish_y("Belina Bawalan Y Molina")
        'Bawalan'
        >>> get_spanish_y("Alberto De La Cruz Y Baluga")
        'De La Cruz'

    Args:
        text (str): _description_

    Returns:
        str | None: _description_
    """
    if match := SPANISH_Y.search(text):
        if surname := match.group("paternal"):
            return surname
    return None


FULL_NAME = re.compile(
    rf"""
    ^
    (Hon\.\s+)?
    (?P<first>{RAW_FIRSTNAME})\s+
    (?P<middle>{RAW_MIDDLE})\s+
    (?P<last>{RAW_SURNAME})
    $
    """,
    re.X,
)


def get_last_name(text: str) -> str | None:
    if match := FULL_NAME.search(text):
        if surname := match.group("last"):
            return surname
    return None


SPOUSES = re.compile(
    r"""
    ^
    (
        sps\.|
        spouses
    )
    \s+
    (
        (
            [a-z]{3,}
            \s+
            (and|&|&Amp;)
            \s+
            [a-z]{3,}
            \s+
            (?P<surname>[\w\s-]+)
        )|
        (
            (?P<lhs_name>[\w\s-]+)
            \s+
            (and|&|&Amp;)
            \s+
            (?P<rhs_name>[\w\s-]+)
        )
    )
    $
    """,
    re.X | re.I,
)


def get_last_name_spouses(text: str) -> str | None:
    if match := SPOUSES.search(text):
        if surname := match.group("surname"):
            return f"Sps. {surname}"
        elif lhs := match.group("lhs_name"):
            bits = lhs.split()
            match len(bits):
                case 3:
                    if len(bits[2]) >= 3:
                        return f"Sps. {bits[2]}"
                case 2:
                    if len(bits[1]) >= 2:
                        return f"Sps. {bits[1]}"
    return None


def get_canonical_human(text: str):
    if surname := get_last_name_spouses(text):
        return surname

    if surname := get_spanish_y(text):
        return surname

    if surname := get_last_name(text):
        return surname

    if anon := get_anonymous(text):
        return anon

    if atty := get_atty(text):
        return atty

    if engr := get_engr(text):
        return engr

    return text
