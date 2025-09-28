import re
from enum import Enum
from typing import NamedTuple


class Office(NamedTuple):
    canonical: str
    regex: str

    @property
    def pattern(self) -> re.Pattern:
        return re.compile(
            rf"""
            ^
            (
                the
                \s+
            )? # optional
            (
                hon
                    (
                        or
                        (\s*|\xad)?
                        able
                        \s+
                    )|
                    (
                        \s*
                        \.
                        \s+
                    )
            )? # optional
            {self.regex}
            """,
            re.X | re.I,
        )

    def search(self, text: str):
        return self.canonical if self.pattern.search(text) else None


class Entity(Enum):
    base_rp = Office(
        canonical="Republic",
        regex=r"""
            rep(ublic|\.)
            \s+
            of
            (
                \s+
                the
            )?
            \s+
            (
                philipp?ines|
                phil\xadipp?ines
            )# misspelled
        """,
    )
    base_us = Office(
        canonical="U.S.",
        regex=r"""
            united
            \s+
            states
            (
                \s+
                of
                \s+
                america
            )?
            $ # must end here, else will match 'United States Rubber Co.'
            """,
    )
    base_ca = Office(
        canonical="CA",
        regex=r"court\s+of\s+appeals",
    )
    base_iac = Office(
        canonical="IAC",
        regex=r"intermediate\s+appellate\s+court",
    )
    elect_comm = Office(
        canonical="COMELEC",
        regex=r"commission\s+on\s+elections",
    )
    audit_comm = Office(
        canonical="COA",
        regex=r"commission\s+on\s+audit",
    )
    csc_comm = Office(
        canonical="CSC",
        regex=r"civil\s+service\s+commission",
    )
    crime_sb = Office(
        canonical="Sandiganbayan",
        regex=r"sandiganbayan",
    )
    crime_ppl = Office(
        canonical="People",
        regex=r"""
            people|
            (
                people
                \s+
                of
                \s+
                the
                \s+
                philippines
            )
        """,
    )
    crime_omb = Office(
        canonical="Ombudsman",
        regex=r"(office\s+o(f|p)\s+the\s+)?(honorable\s+)?ombudsman",
    )
    crime_tb = Office(
        canonical="Tanodbayan",
        regex=r"tanodbayan",
    )
    labor_nlrc = Office(
        canonical="NLRC",
        regex=r"national\s+labor\s+relations\s+commission",
    )
    labor_cir = Office(
        canonical="Court of Industrial Relations",
        regex=r"court\s+of\s+industrial\s+relations",
    )
    labor_sss = Office(
        canonical="SSS",
        regex=r"social\s+security\s+system",
    )
    labor_gsis = Office(
        canonical="GSIS",
        regex=r"government\s+service\s+insurance\s+system",
    )
    admin_ppa = Office(
        canonical="PPA",
        regex=r"philippine\s+ports\s+authority",
    )
    admin_lrta = Office(
        canonical="LRTA",
        regex=r"light\s+rail\s+transit\s+authority",
    )
    admin_nha = Office(
        canonical="NHA",
        regex=r"national\s+housing\s+authority",
    )
    admin_miaa = Office(
        canonical="MIAA",
        regex=r"manila\s+international\s+airport\s+authority",
    )
    admin_mmda = Office(
        canonical="MMDA",
        regex=r"metropolitan\s+manila\s+development\s+authority",
    )
    admin_bcda = Office(
        canonical="BCDA",
        regex=r"bases\s+conversion\s+((?:and|&)\s+)?development\s+authority",
    )
    admin_tesda = Office(
        canonical="TESDA",
        regex=r"technical\s+education\s+(and|&)\s+skills\s+development\s+authority",
    )
    admin_nfa = Office(
        canonical="BCDA",
        regex=r"national\s+food\s+authority",
    )
    admin_tieza = Office(
        canonical="TIEZA",
        regex=(
            r"tourism\s+infrastructure\s+(and|&)\s+enterprise\s+development\s+authority"
        ),
    )
    admin_nwsa = Office(
        canonical="NWSA",
        regex=r"national\s+waterworks\s+(and|&)\s+sewerage\s+authority",
    )
    admin_mciaa = Office(
        canonical="MCIAA",
        regex=r"mactan[\s-]cebu\s+international\s+airport\s+authority",
    )
    admin_ato = Office(
        canonical="ATO",
        regex=r"airport\s+transportation\s+office",
    )
    tax_cta = Office(
        canonical="CTA",
        regex=r"court\s+o(f|p)\s+tax\s+appeals",
    )
    tax_board = Office(
        canonical="Board of Tax Appeals",
        regex=r"board\s+o(f|p)\s+tax\s+appeals",
    )
    tax_cbaa = Office(
        canonical="CBAA",
        regex=r"central\s+board\s+o(f|p)\s+assessment\s+appeals",
    )
    tax_lbaa = Office(
        canonical="LBAA",
        regex=r"local\s+board\s+o(f|p)\s+assessment\s+appeals",
    )
    tax_rev_bir = Office(
        canonical="BIR",
        regex=r"bureau\s+o(f|p)\s+internal\s+revenue",
    )
    tax_rev_coll = Office(
        canonical="Collector of Internal Revenue",
        regex=r"(insular\s+)?collector\s+o(f|p)\s+internal\s+revenue",
    )
    tax_rev_comm = Office(
        canonical="Commissioner of Internal Revenue",
        regex=r"commissioner\s+o(f|p)\s+internal\s+revenue",
    )
    tax_customs_coll = Office(
        canonical="Collector of Customs",
        regex=r"(insular\s+)?collector\s+o(f|p)\s+customs",
    )
    tax_customs_comm = Office(
        canonical="Commissioner of Customs",
        regex=r"commissioner\s+o(f|p)\s+customs",
    )

    @classmethod
    def get_canonical(cls, text: str):
        for member in cls:
            if canonical := member.value.search(text):
                return canonical
        return text
