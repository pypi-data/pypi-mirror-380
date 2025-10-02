#!/usr/bin/env python3

# This software is provided under The Modified BSD-3-Clause License (Consistent with 
# Python 3 licenses).
# Refer to and abide by the Copyright detailed in LICENSE file found in the root 
# directory of the library!

##################################################
#                                                #
#  Shapespyer - soft matter structure generator  #
#               ver. 0.1.7 (beta)                #
#                                                #
#  Author: Dr Andrey Brukhno (c) 2020 - 2024     #
#          Daresbury Laboratory, SCD, STFC/UKRI  #
#                                                #
#  Contrib: MSc Mariam Demir (c) Oct - Dec 2023  #
#          Daresbury Laboratory, SCD, STFC/UKRI  #
#      (YAML IO, InputParser, topology analyses) #
#                                                #
#  Contrib: Dr Michael Seaton (c) 2024           #
#          Daresbury Laboratory, SCD, STFC/UKRI  #
#          (DL_POLY/DL_MESO DPD w-flows, tests)  #
#                                                #
#  Contrib: Dr Valeria Losasso (c) 2024          #
#          Daresbury Laboratory, SCD, STFC/UKRI  #
#        (PDB IO, Bilayer, NAMD w-flows, tests)  #
#                                                #
##################################################

##from __future__ import absolute_import
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

import os
import sys

from shapes.basics.defaults import Fill
from shapes.basics.globals import HUGE, TINY, Pi, TwoPi
from shapes.basics.input import InputParser
from shapes.basics.options import Options, OptionsSerDes
from shapes.basics.utils import Generator, LogListener, configure_logging

print("\n##################################################")
print("#                                                #")
print("#  Shapespyer - soft matter structure generator  #")
print("#               ver. 0.2.0 (beta)                #")
print("#                                                #")
print("#  Author: Dr Andrey Brukhno (c) 2020 - 2024     #")
print("#          Daresbury Laboratory, SCD, STFC/UKRI  #")
print("#                                                #")
print("##################################################\n")

### MAIN ###
def main(argv: list[str] = sys.argv):
    logger = configure_logging()

    ##### - COMMAND-LINE / YAML INPUT / HELP - START

    options = Options()
    inpPars = InputParser()
    listener = LogListener()
    options.shape.add_listener(listener)
    options.molecule.add_listener(listener)

    logger.info("Parsing input parameters (from CLI or YAML) ...")
    try:
        options = inpPars.parseCLI(argv, options)
    except Exception as e:
        logger.exception(e)
        logger.error("FULL STOP!!!")
        logger.error(f"Try '{os.path.basename(argv[0])} --help'\n")
        sys.exit(1)
    logger.info("Parsing input parameters - DONE")
    ##### - COMMAND-LINE / YAML INPUT / HELP - END

    ##### - ARGUMENTS ANALYSIS - START
    # AB: retain the sign only in options.shape.slv_buff
    # options.shape.abs_slv_buff = abs(options.shape.slv_buff) 
    # nm - rescale for Angstroems!

    if (
        options.shape.stype.is_ball
        and options.shape.fill is not Fill.RINGS0
    ):
        if options.shape.fill is Fill.RINGS:
            logger.debug(
                f"Will generate 'ball' with {options.shape.lring} "
                "molecules projected on 'equator' ring - "
                f"option '--fill=rings' (second variant) ..."
            )
        else:
            logger.debug(
                f"Will generate 'ball' of {options.shape.nmols} molecules "
                "covering its surface uniformly - option '--fill=fibo' "
                "(Fibonacci spiral) ..."
            )
        if options.shape.rmin < 0.5:
            logger.debug(
                f"Generating a 'ball' of radius Rmin = {options.shape.rmin} "
                f" < 0.5 nm ..."
            )
    logger.info(
        f"Check globals & defaults:\n"
        f"Pi = {Pi}, 2*pi = {TwoPi}, TINY = {TINY}, HUGE = {HUGE}\n"
        f"BUFF = {options.shape.abs_slv_buff}, DMIN = {options.shape.dmin}, "
        f"RMIN = {options.shape.rmin},\n"
    )
    logger.info(
        f"Requested molecule names and ids: { options.molecule.resnames} -> "
        f"{options.molecule.resnm} & {options.molecule.molids} -> "
        f"{options.molecule.molid}\n"
    )
    logger.info(
        f"Requested shape 'bone' indices: {options.molecule.mint} ... "
        f"{options.molecule.mext}\n"
    )
    logger.info(
        f"Using Nmol = {max(options.shape.lring, options.shape.nmols)}"
    )
    logger.info(f"Using Nlay = {options.shape.layers.quantity}")
    if options.shape.layers.quantity > 1:
        logger.info(f"Dmin scale = {options.shape.layers.dmin_scaling}")
        logger.info(f"Rcav scale = {options.shape.layers.cavr_scaling}")
    logger.info(f"Using Nlay = {options.shape.layers.quantity}")
    logger.info(
        f"Using Dmin = {options.shape.dmin} for min separation between heavy atoms"
    )
    logger.info(
        f"Using Rmin = {options.shape.rmin} for target internal radius (if applicable)"
    )
    logger.info(
        f"Using Rbuf = {options.shape.sbuff} for solvation buffer\n"
    )
    logger.info(
        f"Doing: input '{options.input.file}' => output '{options.output.file}'\n"
    )

    # AB: dump the input for reference
    OptionsSerDes.dump_validated_yaml(options)

    ##### - ARGUMENTS ANALYSIS - DONE

    try:
        gen = Generator(options)
        gen.read_input()
        gen.generate_shape()
        gen.dump_file()

    except Exception as e:
        logger.exception(e)
        sys.exit(2)
# end of main(argv)


if __name__ == "__main__":
    main()
    sys.exit(0)

### END OF SCRIPT ###
