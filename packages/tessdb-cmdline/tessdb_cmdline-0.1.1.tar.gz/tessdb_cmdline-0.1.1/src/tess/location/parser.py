# ----------------------------------------------------------------------
# Copyright (c) 2024 Rafael Gonzalez.
#
# See the LICENSE file for details
# ----------------------------------------------------------------------

# --------------------
# System wide imports
# -------------------

from argparse import ArgumentParser

# ---------------------------
# Third-party library imports
# ----------------------------

from lica.validators import vfile

def dry() -> ArgumentParser:
    parser = ArgumentParser(add_help=False)
    parser.add_argument(
        "-dr",
        "--dry-run",
        default=False,
        action="store_true",
        help="Dry run, do not update database",
    )
    return parser


def place() -> ArgumentParser:
    parser = ArgumentParser(add_help=False)
    parser.add_argument(
        "-pl",
        "--place",
        type=str,
        required=True,
        help="Place name",
    )
    return parser


def nominatim() -> ArgumentParser:
    parser = ArgumentParser(add_help=False)
    parser.add_argument(
        "-to",
        "--town",
        type=str,
        default=None,
        help="Population Center",
    )
    parser.add_argument(
        "-su",
        "--sub-region",
        type=str,
        default=None,
        help="Province, county, etcr",
    )
    parser.add_argument(
        "-re",
        "--region",
        type=str,
        default=None,
        help="Federal state, comunidad autonoma",
    )
    parser.add_argument(
        "-co",
        "--country",
        type=str,
        default=None,
        help="Country",
    )
    parser.add_argument(
        "-tz",
        "--timezone",
        type=str,
        default=None,
        help="Timezone",
    )
    return parser


def coords() -> ArgumentParser:
    parser = ArgumentParser(add_help=False)
    parser.add_argument(
        "-lo",
        "--longitude",
        type=float,
        required=True,
        help="Longitude (decimal degrees)",
    )
    parser.add_argument(
        "-la",
        "--latitude",
        type=float,
        required=True,
        help="Latitude (decimal degrees)",
    )
    parser.add_argument(
        "-he",
        "--height",
        type=float,
        default=None,
        help="Meters above sea level",
    )
    return parser

def raw() -> ArgumentParser:
    parser = ArgumentParser(add_help=False)
    parser.add_argument(
        "-ra",
        "--raw",
        default=False,
        action="store_true",
        help="Raw Nominatim metadata",
    )
    return parser


def ifile() -> ArgumentParser:
    parser = ArgumentParser(add_help=False)
    parser.add_argument(
        "-ic",
        "--input-csv",
        type=vfile,
        required=True,
        help="Input CSV file",
    )
    return parser

def ofile() -> ArgumentParser:
    parser = ArgumentParser(add_help=False)
    parser.add_argument(
        "-os",
        "--output-script",
        type=str,
        required=True,
        help="Output shell script",
    )
    return parser

def nearby() -> ArgumentParser:
    parser = ArgumentParser(add_help=False)
    parser.add_argument(
        "-ne",
        "--nearby",
        type=float,
        default=None,
        help="Nearby distance to check first (defaults to %(default)s )",
    )
    return parser