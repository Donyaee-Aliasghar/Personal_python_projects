"""Module for Defining regulatory element patterns."""

import re

from .iupac_to_regex import itr

motif_patterns = {
    "TATA Box": re.compile(itr("TATAAA|TATAAT")),
    "CAAT Box": re.compile(itr("CAAT")),
    "GC Box": re.compile(itr("GGGCGG|GCGGGG")),
    "CpG Island": re.compile("CG"),
    "Inr (Initiator)": re.compile(itr("YYANWYY")),
    "BRE": re.compile(itr("SSRCGCC")),
}
