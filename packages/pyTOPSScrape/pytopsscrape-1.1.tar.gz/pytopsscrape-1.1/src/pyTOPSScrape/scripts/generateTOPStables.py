"""
**Author:** Emily M. Boudreaux\n
**Created:** February 2021\n
**Last Modified:** September 2025\n

Given an abundance pattern, generate opacity tables in a form that DSEP can
understand. These will be automatically queried from the Los Alamos
site, using the most recent ATOMIC opacities generated with the TOPS code.

Notes
-----
Website [1]_

Paper [2]_


[1] https://aphysics2.lanl.gov/apps/

[2] Colgan, James, et al. "A new generation of Los Alamos opacity tables." The Astrophysical Journal 817.2 (2016): 116.
"""
import argparse
# Assuming full_run is in a module that can be imported like this
from pyTOPSScrape.scripts import full_run


def main():
    """Main function to parse arguments and run the script."""
    parser = argparse.ArgumentParser(description="Generate opacity table in a"
                                     " format dsep can work with from TOPS")
    parser.add_argument("abunTable", type=str, help="Table to pull abundances"
                        " from.")
    parser.add_argument("abunMap", type=str, help="map of which classical "
                        "compositions to query the TOPS web form for. Each "
                        "classical composition will be achieved by rescaling "
                        "the base composition described in the abunTable")
    parser.add_argument("-f", "--force", help="force the generation of new"
                        " abundance tables", action="store_true")
    parser.add_argument("-d", "--outputDirectory", help="directory to save"
                        " abundance files to", default=".", type=str)
    parser.add_argument("--noopal", help="Run the code to convert TOPS table to"
                        "OPAL compatible tables", action="store_true")
    parser.add_argument("--nofetch", help="do not fetch opacity tables from"
                        " TOPS", action='store_true')
    parser.add_argument("-o", "--output", help="file to write OPAL formatted"
                        " table to", default="TOPAL.dat", type=str)
    parser.add_argument("--hardforce", action="store_true",
                        help="Override all already extant directories",
                        default=False)
    parser.add_argument("-j", "--jobs", help="Number of processes to query the "
                        "TOPS web form on", type=int, default=10)
    parser.add_argument("--rect", default=False, action="store_true", help="if "
                        "True store OPAL tables rectangularly. This is not how "
                        "DSEP uses tables; however, by way of wider "
                        "applicability --rect may be used")
    parser.add_argument("--multi", default=False, action="store_true", help="if "
                        "query the multi-group opacities instead of the planck / "
                        "grey mean opacities. Note that if --multi is used "
                        "then --noopal will be automatically turned on")

    cliArgs = parser.parse_args()
    # The vars() function converts the argparse Namespace object to a dictionary
    full_run(vars(cliArgs))


if __name__ == "__main__":
    main()
