import re


def get_first_mentioned(text: str) -> str:
    """Reduce long list of names into the first one found.

    Examples:
        >>> get_first_mentioned("The Province Of North Cotabato, Duly Represented By Governor Jesus Sacdalan And/Or Vice-Governor Emmanuel Piñol, For And In His Own Behalf")
        'The Province Of North Cotabato'
        >>> get_first_mentioned("The Government Of The Republic Of The Philippines Peace Panel On Ancestral Domain , Represented By Sec. Rodolfo Garcia, Atty. Leah Armamento, Atty. Sedfrey Candelaria, Mark Ryan Sullivan And/Or Gen. Hermogenes Esperon, Jr., The Latter In His Capacity As The Present And Duly-Appointed Presidential Adviser On The Peace Process  Or The So-Called Office Of The Presidential Adviser On The Peace Process")
        'The Government Of The Republic Of The Philippines Peace Panel On Ancestral Domain'

    Args:
        text (str): An 'lhs' / 'rhs' group value from `get_titles()`

    Returns:
        str: First named entity
    """  # noqa: #E501
    if texts := text.split(";"):
        bit = texts[0].strip()
        if bits := bit.split(","):
            return bits[0].strip()
    return text.strip()


_and = re.compile(
    r""",?
            \s
            (
              And|
              and|
              &
            )
            \s""",
    re.X,
)

covered = re.compile(
    r"""
    (
      \(.*?\)
    )|
    (
      \[.*?\]
    )
  """,
    re.X,
)

more_than_two_spaces = re.compile(
    r"""
    \s{2,}
    """,
    re.X,
)

extraneous_suffix = re.compile(
    r"""
    (
        et\s+al\.?|
        etc\.?
    )
    $
    """,
    re.X | re.I,
)

double_quotes = re.compile(
    r"""
    [“”‶″]
    """,
    re.X,
)


def fix_name_suffixes(text: str):
    text = text.replace("Iii", "III")
    text = text.replace(" Iv ", " IV ")
    text = text.replace(" Iv,", " IV,")
    if text.endswith(" Iv"):
        text = text.replace(" Iv", " IV")
    return text


def lowercase_connectors(text: str):
    text = text.replace("From The", "from the")
    text = text.replace("For The", "for the")
    text = text.replace("Of The", "of the")
    text = text.replace(" From ", " from ")
    text = text.replace(" For ", " for ")
    text = text.replace(" Of ", " of ")
    return text


def create_shorthand_suffix(text: str):
    if text.endswith(" Corporation"):
        text = text.replace(" Corporation", " Corp.")
    elif text.endswith(" Company"):
        text = text.replace(" Company", " Co.")
    elif text.endswith("  Incorporated"):
        text = text.replace(" Incorporated", " Inc.")
    elif text.endswith(" Philippines"):
        text = text.replace(" Philippines", " Phil.")
    return text


def reduce(text: str) -> str:
    text = text.replace("*", "")
    text = more_than_two_spaces.sub(" ", text)
    text = extraneous_suffix.sub("", text)
    text = text.removeprefix("The")
    text = create_shorthand_suffix(text)
    text = text.replace("'S ", "'s ")
    text = lowercase_connectors(text)
    text = fix_name_suffixes(text)
    return text.strip()


def create_candidate_text(text: str) -> str:
    """Remove extraneous text for forming a title and ensure continuous line exists.
    Sometimes a line break is found between text which prevents regex operations
    from functioning since these are intentionally not multiline strings.

    Examples:
        >>> raw = "Some Random Entity (the Acronym of such entity), Vs. Juan\\r\\n de la Cruz [A Docket Number]"
        >>> create_candidate_text(raw)
        'Some Random Entity , Vs. Juan  de la Cruz'
        >>> create_candidate_text("Juan Doe,[1] Complainant, V. Atty. Juan de la Cruz, Respondent.")
        'Juan Doe, Complainant, V. Atty. Juan de la Cruz, Respondent.'
        >>> create_candidate_text("In re: Abraham “Abe” Lincoln")
        'In re: Abraham "Abe" Lincoln'

    Args:
        text (str): Raw title from the database

    Returns:
        str: Candidate value to later parse for `lhs` and `rhs`
    """  # noqa: # E501
    candidate = " ".join(text.splitlines())
    text = covered.sub("", candidate.strip()).strip()
    text = double_quotes.sub('"', text)
    return text


def create_named_group(name: str, bases: tuple) -> str:
    """A partial regex string combining the bases

    Examples:
        >>> regex = create_named_group(name="lhs", bases=(r"petitioner", "plaintiff"))
        >>> match0 = re.search(regex, "mr. x, petitioners-appelees") # intentional wrong spelling
        >>> match0.groupdict()
        {'lhs_party': 'mr. x', 'lhs_label': 'petitioners-appelees'}
        >>> match1 = re.search(regex, "mr. y, plaintiff and appellants")
        >>> match1.groupdict()
        {'lhs_party': 'mr. y', 'lhs_label': 'plaintiff and appellants'}

    Args:
        name (str): The name of the regex group
        bases (tuple): A tuple of values that will be connected to each other

    Returns:
        str: A regex string of format: (<?P`name`>`patterns`)
    """  # noqa: E501
    bits = []
    connectors = (r"-", r"\s+and\s+")
    suffixes = (r"appell?ee", r"appell?ant", r"intervenor")

    def add_s(x: str):
        """Add an optional `s` to the text pattern and an optional comma `,`"""
        return f"{x}s?,?"

    for base in bases:
        for suffix in suffixes:
            for connect in connectors:
                bits.append(rf"{add_s(base)}{connect}{add_s(suffix)}")

    for suffix in suffixes:
        bits.append(rf"{add_s(suffix)}")

    for base in bases:
        bits.append(rf"{add_s(base)}")

    party_name = f"{name}_party"
    party = rf"(?P<{party_name}>.*?)"

    label_name = f"{name}_label"
    label = rf"(?P<{label_name}>{'|'.join(bits)})"

    return rf"\s*{party}[,\.\s]*{label}[,\.\s]*"
