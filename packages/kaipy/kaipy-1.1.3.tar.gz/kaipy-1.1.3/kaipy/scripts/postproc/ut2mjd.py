#!/usr/bin/env python

# Standard modules
import argparse
from argparse import RawTextHelpFormatter
import datetime

# Third-party modules
from astropy.time import Time

fmt='%m/%d/%Y, %H:%M:%S'

def create_command_line_parser():
    """Create the command-line argument parser.
    Create the parser for command-line arguments.
    Returns:
        argparse.ArgumentParser: Command-line argument parser for this script.
    """
    t0="2010-01-01T00:00:00"
    fmt='%Y-%m-%dT%H:%M:%S'

    MainS = """ Returns MJD (modified Julian date) from a given UT
                UT: UT string, yyyy-mm-ddThh:mm:ss format
                ut2mjd.py 2010-02-05T5:00:00
    """

    parser = argparse.ArgumentParser(description=MainS, formatter_class=RawTextHelpFormatter)
    parser.add_argument('UT',type=str,metavar="UT",default=t0,help='UT string to convert (default: %(default)s)')

    return parser


def main():
    t0="2010-01-01T00:00:00"
    fmt='%Y-%m-%dT%H:%M:%S'

    parser = create_command_line_parser()
    #Finalize parsing
    args = parser.parse_args()

    utStr = args.UT
    ut = datetime.datetime.strptime(utStr,fmt)
    mjd = Time(ut).mjd

    print("%s (UT) => %f (MJD)"%(utStr,mjd))

if __name__ == "__main__":
    main()