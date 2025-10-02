"""
.. module:: input
   :platform: Linux - tested, Windows (WSL Ubuntu) - tested
   :synopsis: abstraction class for reading in input options and arguments in YAML
   format (for shape)

.. moduleauthor:: MSc Mariam Demir <mariam.demir[@]stfc.ac.uk>

The module contains class InputParser(object)
"""

# This software is provided under The Modified BSD-3-Clause License
# (Consistent with Python 3 licenses).
# Refer to and abide by the Copyright detailed in LICENSE file found in the root
# directory of the library!

##################################################
#                                                #
#  Shapespyer - soft matter structure generator  #
#                                                #
#  Author: Dr Andrey Brukhno (c) 2020 - 2025     #
#          Daresbury Laboratory, SCD, STFC/UKRI  #
#                                                #
#  Contrib: MSc Mariam Demir (c) Oct - Dec 2023  #
#          Daresbury Laboratory, SCD, STFC/UKRI  #
#                                                #
##################################################

__author__ = "Andrey Brukhno"

# TODO: unify the coding style:
# TODO: CamelNames for Classes, camelNames for functions/methods & variables
# (where meaningful)
# TODO: hint on method/function return data type(s), same for the interface arguments
# TODO: one empty line between functions/methods & groups of interrelated imports
# TODO: two empty lines between Classes & after all the imports done
# TODO: classes and (lengthy) methods/functions must finish with a closing comment:
# '# end of <its name>'
# TODO: meaningful DocStrings right after the definition (def) of
# Class/method/function/module
# TODO: comments must be meaningful and start with '# ' (hash symbol followed by a space)
# TODO: insightful, especially lengthy, comments must be prefixed by developer's
# initials as follows:
# AB: TODO - reading the box/cell specs from a separate file?

import argparse
import logging
import os
import re

from shapes.basics.defaults import (
    CONFIG_BASE,
    OUTPUT_EXTENSIONS,
    SDLM,
    SDLP,
    Defaults,
    Fill,
    ShapeOrigin,
)
from shapes.basics.help import beauty, help
from shapes.basics.options import Options, OptionsSerDes, ShapeType

logger = logging.getLogger("__main__")


class InputParser(object):
    """
    Class **InputParser()** - parses and stores the input (arguments and flags)
    from CLI or Yaml file.
    """

    ARGUMENTS: dict[tuple[str, ...], dict[str, any]] = {
        ("-y", "--yaml"): {"help": help.YAML},
        ("-v", "--verbose"): {"action": "store_true", "help": help.VERBOSE,},
        ("-d", "--dio"): {"metavar": "IODIR", "help": help.DIRIO,},
        ("-b", "--box"): {"metavar": "IBOX", "help": help.BOXINP,},
        ("-i", "--inp"): {"metavar": "IFILE", "help": help.FINAME,},
        ("-o", "--out"): {"metavar": "ONAME", "help": help.FONAME,},
        ("-x", "--xout"): {"metavar": "OEXT", "help": help.FOEXT,},
        ("--shape",): {"help": help.SHAPE},
        ("-s", "--stype"): {"help": help.STYPE},
        ("-f", "--fill"): {"help": help.FILL},
        ("-l", "--lring"): {"help": help.LRING},
        ("-t", "--turns"): {"help": help.TURNS},
        ("-n", "--nmols"): {"help": help.NMOLS},
        ("--layers",): {"help": help.LAYERS},
        ("--nside",): {"help": help.NSIDE},
        ("--zsep",): {"help": help.ZSEP},
        ("-m", "--molids"): {"help": help.MOLIDS},
        ("--rnames",): {"help": help.RNAMES},
        ("-r", "--resnames"): {"help": help.RESNAMES},
        ("-c", "--cavr"): {"help": help.CAVR},
        ("--rmin",): {"help": help.RMIN},
        ("--dmin",): {"help": help.DMIN},
        ("--ldpd",): {"help": help.LDPD},
        ("--origin",): {"help": help.ORIGIN},
        ("--offset",): {"help": help.OFFSET},
        ("--alpha",): {"help": help.ALPHA},
        ("--theta",): {"help": help.THETA},
        ("--sbuff",): {"help": help.SBUFF},
        ("--fxz",): {"action": "store_true", "help": help.FLATTEN,},
        ("--rev",): {"action": "store_true", "help": help.REVERSE,},
        ("--frc",): {"help": help.FRC},
        ("--fracs",): {"help": help.FRACS},
        ("--mint",): {"help": help.MINT},
        ("--mext",): {"help": help.MEXT},
        ("--nl",): {"help": help.NL},
        ("--nx",): {"help": help.NX},
        ("--ny",): {"help": help.NY},
        ("--nz",): {"help": help.NZ},
        ("--dbkinks",): {"help": help.DBKINKS},
        ("--cis",): {"help": help.CIS},
        ("--alignz",): {"action": "store_true", "help": help.ALIGNZ},
        ("--dnames",): {"help": help.DNAMES},
    }
    SHAPE_ARGS = [
        "--yaml", "--verbose", "--dio", "--box", "--inp", "--out", "--xout", "--shape",
        "--stype", "--fill", "--lring", "--turns", "--nmols", "--layers", "--nside",
        "--zsep", "--molids", "--rnames", "--resnames", "--cavr", "--rmin", "--dmin",
        "--ldpd", "--origin", "--offset", "--alpha", "--theta", "--sbuff", "--fxz",
        "--rev", "--frc", "--fracs", "--mint", "--mext", "--nl", "--nx", "--ny", "--nz",
    ] # fmt: skip
    SMILES_ARGS = [
        "--yaml", "--verbose", "--dio", "--inp", "--out", "--xout", "--molids", 
        "--rnames", "--resnames", "--dbkinks", "--cis", "--origin", "--alignz",
    ] # fmt: skip
    DENSITIES_ARGS = [
        "--yaml", "--verbose", "--dio", "--inp", "--out", "--xout", "--molids", 
        "--rnames", "--resnames", "--dnames", "--cavr", "--rmin", "--origin",
    ] # fmt: skip

    @staticmethod
    def list_of_strings(arg: str) -> list[str]:
        split = re.sub(r"[\[\]\(\)]", "", arg.strip()).split(",")
        value = None
        if len(split) > 0:
            value = [var.strip() for var in split]
        elif isinstance(arg, str):
            value = [arg]
        return value

    @classmethod
    def list_of_ints(cls, arg: str) -> list[int]:
        return [int(x) for x in cls.list_of_strings(arg)]

    @classmethod
    def list_of_abs_ints(cls, arg: str) -> list[int]:
        return [abs(int(x)) for x in cls.list_of_strings(arg)]

    @classmethod
    def list_of_floats(cls, arg: str) -> list[float]:
        return [float(x) for x in cls.list_of_strings(arg)]

    @classmethod
    def list_of_list_of_floats(cls, arg: str) -> list[list[float]]:
        arg = arg.strip()
        if ":" in arg:
            flist = arg.split(":")
        elif "][" in arg:
            flist = arg.split("][")
        elif "],[" in arg:
            flist = arg.split("],[")
        else:
            flist = [arg]

        top_list: list[list[float]] = [cls.list_of_floats(inner) for inner in flist]

        return top_list

    def _make_parser(self, argv: list[str]) -> argparse.ArgumentParser:
        sname = os.path.basename(argv[0])

        if len(argv) - 1 < 1:
            # AB: print help page if no arguments are given
            argv.append("-h")
        #     raise ValueError("At least one option is expected!\n")

        hlp = help()
        tb = beauty()

        if argv[1] in ("-h", "--help"):
            hlp.header()

        parser = argparse.ArgumentParser(
            prog=sname,
            usage=tb.BOLD + sname + " -i <INP> -o <OUT> -s <SHAPE> [options]" + tb.END,
            description=None,
            epilog="End of help (nothing done)",
        )

        parser.add_argument("sname")

        selected_args = {}
        if sname == "shape_structure.py" or sname == "shape":
            selected_args = self.SHAPE_ARGS
        elif sname == "smiles.py" or sname == "smiles":
            selected_args = self.SMILES_ARGS
        elif sname == "densities.py" or sname == "densities":
            selected_args = self.DENSITIES_ARGS

        for arg in selected_args:
            for name_or_flags, kwargs in self.ARGUMENTS.items():
                if arg in name_or_flags:
                    parser.add_argument(*name_or_flags, **kwargs)
                    continue

        return parser

    def parseCLI(self, argv: list[str], options: Options | None = None) -> Options:
        """
        Takes a set of command-line arguments, and updates the options dictionary
        with parameters accordingly (see ``self._options``).

        :param argv: a list of user-specified command-line arguments
        (ref ``shape --help``)
        :return: None
        """
        parser = self._make_parser(argv)
        args = parser.parse_args(argv)
        # AK: args may contain different sets of attributes depending on the script that
        # was called, so we have to check args via getattr(obj, attr_name, default)
        # instead of the usual obj.attr_name to ensure parseCLI working if the attribute
        # was not created. Use obj.attr_name if option is required for all scripts.

        if args.verbose:
            logger.setLevel(logging.DEBUG)
            logger.info("Verbose mode is ON")
        else:
            logger.setLevel(logging.WARNING)
            logger.info("Verbose mode is OFF")

        if args.yaml:
            return OptionsSerDes.read_validated_yaml(args.yaml.strip())

        if options is None:
            options = Options()

        if args.dio:
            if args.dio.count(",") > 1:
                logger.warning(
                    "More than two IO directory names given - only two are"
                    " taken, the rest is ignored!"
                )

            dio = self.list_of_strings(args.dio)[:2]
            if not dio:
                raise ValueError("No valid values in IO directory names")

            options.input.path = dio[0]
            options.output.path = options.input.path
            if len(dio) > 1:
                options.output.path = dio[1]

            logger.debug(
                f"Got inp_path = '{options.input.path}';"
                f" out_path = '{options.output.path}'"
            )

        if args.inp:
            options.input.file = args.inp.strip()

        if args.out:
            fout = args.out.strip()
            if fout[:6] == CONFIG_BASE:
                # MS: user provided CONFIG as (full) file name for DL_POLY/DL_MESO
                logger.info(
                    f"User-provided output file name '{fout}' => DL_POLY/DL_MESO format"
                )

                if fout[-4:] == SDLP or fout[-4:] == SDLM:
                    options.output.file = fout
                else:
                    options.output.base = fout
                options.output.must_add_suffixes = False

            elif len(fout) > 4 and fout[-4:] in OUTPUT_EXTENSIONS:
                # # AB: user provided the full file name

                options.output.file = fout
                options.output.must_add_suffixes = False
            else:
                # AB: user provided the file name base
                # (make sure the '-x/--xout' is not used)
                options.output.base = fout  # OutBase + OutExt = OutFile
                options.output.must_add_suffixes = True
                logger.debug(
                    f"User-provided output file name base '{fout}' (given separately)"
                )

        if args.xout:
            options.output.ext = args.xout.strip().lower()
            options.output.must_add_suffixes = True

        if getattr(args, "box", False):
            raise NotImplementedError(
                "Box attribute of InputOptions is not used anywhere"
            )
            options.input.box = args.box.strip()

        if getattr(args, "shape", False):
            options.shape.stype = ShapeType[args.shape.rstrip().upper()]

        if getattr(args, "stype", False):
            options.shape.stype = ShapeType[args.stype.strip().upper()]

        if getattr(args, "fill", False):
            try:
                options.shape.fill = Fill[args.fill.rstrip().upper()]
            except KeyError:
                logger.warning(
                    "Unknown input value for '-f/--fill' "
                    "(shape filling algo) - using default"
                )

        if getattr(args, "turns", False):
            options.shape.turns = int(args.turns.strip())

        if getattr(args, "molids", False):
            options.molecule.molids = self.list_of_abs_ints(args.molids)

        if getattr(args, "rnames", False):
            options.molecule.resnames = self.list_of_strings(args.rnames)

        if getattr(args, "resnames", False):
            options.molecule.resnames = self.list_of_strings(args.resnames)

        if getattr(args, "dmin", False):
            options.shape.dmin = self.list_of_floats(args.dmin)

        if getattr(args, "cavr", False):
            options.shape.rmin = self.list_of_floats(args.cavr)

        if getattr(args, "rmin", False):
            options.shape.rmin = self.list_of_floats(args.rmin)

        if getattr(args, "layers", False):
            options.shape.layers = self.list_of_floats(args.layers)

        if getattr(args, "lring", False):
            options.shape.lring = int(args.lring.strip())

        if getattr(args, "nmols", False):
            options.shape.nmols = int(args.nmols.strip())

        if getattr(args, "nside", False):
            options.membrane.nside = abs(int(args.nside))

        if getattr(args, "zsep", False):
            options.membrane.zsep = abs(float(args.zsep))

        if getattr(args, "ldpd", False):
            options.base.ldpd = float(args.ldpd)

        if getattr(args, "origin", False):
            value = args.origin.strip()

            try:
                options.shape.origin = ShapeOrigin[value.upper()]
            except KeyError:
                logger.warning(
                    f"Unknown input value ('{value}') for '--origin' (algo for the "
                    f"structure origin) - using default: '{Defaults.Base.ORIGIN}' ..."
                )

        if getattr(args, "offset", False):
            options.shape.offset = self.list_of_floats(args.offset)
            logger.debug(f"Read-in offset = {args.offset} ({options.shape.offset})")

        if getattr(args, "alpha", False):
            options.angle.alpha = float(args.alpha.strip())

        if getattr(args, "theta", False):
            options.angle.theta = float(args.theta.strip())

        if getattr(args, "sbuff", False):
            options.shape.sbuff = float(args.sbuff.strip())

        if getattr(args, "fxz", False):
            options.flags.fxz = args.fxz

        if getattr(args, "rev", False):
            options.flags.rev = args.rev

        if getattr(args, "frc", False):
            options.molecule.fracs = self.list_of_list_of_floats(args.frc)
            logger.warning("DEPRECATED flag 'frc' used.")
            logger.info(f"Species' fractions = {options.molecule.fracs}")

        if getattr(args, "fracs", False):
            options.molecule.fracs = self.list_of_list_of_floats(args.fracs)
            logger.info(f"Species' fractions = {options.molecule.fracs}")

        if getattr(args, "mint", False):
            options.molecule.mint = self.list_of_abs_ints(args.mint)

        if getattr(args, "mext", False):
            options.molecule.mext = self.list_of_abs_ints(args.mext)

        if getattr(args, "nl", False):
            options.lattice.nlatt = self.list_of_abs_ints(args.nl)
            logger.warning(f"Nlatt ('{args.nl}') overrides options nx, ny, nz")

        if getattr(args, "dnames", False):
            options.density.names = self.list_of_strings(args.dnames)

        if getattr(args, "alignz", False):
            options.flags.alignz = bool(args.alignz)

        if getattr(args, "dbkinks", False):
            options.base.cis = self.list_of_strings(args.dbkinks)

        if getattr(args, "cis", False):
            options.base.cis = self.list_of_strings(args.cis)

        logger.debug(f"(parse_args):\n{args}\n")

        return options
