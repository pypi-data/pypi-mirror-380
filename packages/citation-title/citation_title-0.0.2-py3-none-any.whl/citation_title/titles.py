from .adverse import AdverseTitle
from .inre import InreTitle


def cite_title(text: str) -> str | None:
    """Revise value of an _already segmented_ title string
    to a shorter, readable variant for purposes of including
    text as a citation. Can be used in tandem with `citation_utils`.

    Some rules adopted:

    1. Get first mentioned title, if there are many: e.g. `x v. y`, `a v. b`, `1 v. 2`, only retrieves `x v. y`
    2. If an adversarial case title (`x v. y`) is detected, clean `x` and `y` independently.
    3. If an inre case title (`inre: subject`) is detected, clean the `subject`.
    4. Cleaning removes all content surrounded by parenthesis `()` and brackets `[]`, e.g. `(<extraneous>)` and `[<extraneous>]`
    5. Some words are abbreviated, e.g. `People of the Philippines` results in `People`

    Examples:
        >>> cite_title('League Of Cities Of The Philippines (Lcp), Represented By Lcp National President Jerry P. Treñas; City Of Calbayog, Represented By Mayor Mel Senen S. Sarmiento; And Jerry P. Treñas, In His Personal Capacity As Taxpayer,  Petitioners, Vs. Commission On Elections; Municipality Of Baybay, Province Of Leyte; Municipality Of Bogo, Province Of Cebu; Municipality Of Catbalogan, Province Of Western Samar; Municipality Of Tandag, Province Of Surigao Del Sur; Municipality Of Borongan, Province Of Eastern Samar; And Municipality Of Tayabas, Province Of Quezon,  Respondents.  [G.R. No. 177499]   League Of Cities Of The Philippines (Lcp), Represented By Lcp National President Jerry P. Treñas; City Of Calbayog, Represented By Mayor Mel Senen S. Sarmiento; And Jerry P. Treñas, In His Personal Capacity As Taxpayer,  Petitioners, Vs. Commission On Elections; Municipality Of Lamitan, Province Of Basilan; Municipality Of Tabuk, Province Of Kalinga; Municipality Of Bayugan, Province Of Agusan Del Sur; Municipality Of Batac, Province Of Ilocos Norte; Municipality Of Mati, Province Of Davao Oriental; And Municipality Of Guihulngan, Province Of Negros Oriental,  Respondents.   [G.R. No. 178056]   League Of Cities Of The Philippines (Lcp), Represented By Lcp National President Jerry P. Treñas; City Of Calbayog, Represented By Mayor Mel Senen S. Sarmiento; And Jerry P. Treñas, In His Personal Capacity As Taxpayer,  Petitioners, Vs. Commission On Elections; Municipality Of Cabadbaran, Province Of Agusan Del Norte; Municipality Of Carcar, Province Of Cebu; Municipality Of El Salvador, Province Of Misamis Oriental; Municipality Of Naga, Cebu; And Department Of Budget And Management, Respondents.')
        'League of Cities of the Phil. v. COMELEC'

    Args:
        text (str): Already segmented title string

    Returns:
        str | None: If the text is shortened, the output; else None.
    """  # noqa: E501
    if vs := AdverseTitle.single_extract(text):
        return str(vs)
    elif inre := InreTitle.single_extract(text):
        return str(inre)
    return None
