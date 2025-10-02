#!/usr/bin/env python3
"""
The script calculates the scattering length densities of lipid groups (PO4, choline etc), averaged over a DCD trajectory

Usage:
  namd-bilayer-calculate-sld

Required inputs:
  number densities data files derived from namd-bilayer-postprocessing
"""

# This software is provided under The Modified BSD-3-Clause License (Consistent with Python 3 licenses).
# Refer to and abide by the Copyright detailed in LICENSE file found in the root directory of the library!

##################################################
#                                                #
#  Shapespyer - soft matter structure generator  #
#                                                #
#  Author: Dr Andrey Brukhno (c) 2020 - 2024     #
#          Daresbury Laboratory, SCD, STFC/UKRI  #
#  Contrib: Dr Valeria Losasso (c) 2024          #
#           BSc Saul Beck (c) 2024               #
#                                                #
##################################################

##from __future__ import absolute_import
__author__ = "Andrey Brukhno"
__version__ = "0.1.7 (Beta)"

import logging

import numpy as np

# AB: The following imports only work upon installing Shapespyer:
# pip3 install $PATH_TO_shapespyer
from shapes.basics.functions import timing
from shapes.basics.mendeleyev import Chemistry
from shapes.basics.utils import configure_logging

logger = logging.getLogger("__main__")

# Scattering lengths for each atom type
scattering_lengths = Chemistry.ecsl

# Define component composition in terms of atom types and their counts
component_composition = Chemistry.egrp

# Function to calculate SLDs from number densities
@timing
def calculate_sld(density_files):
    z_bins = None
    sld_profiles = {}

    for component, file_path in density_files.items():
        # Load data: assumes two columns, z and density
        data = np.loadtxt(file_path)
        z_bins = data[:, 0] if z_bins is None else z_bins
        number_densities = data[:, 1]

        # Calculate SLD for each bin by summing over atomic contributions
        sld = np.zeros_like(number_densities)
        for atom, count in component_composition[component].items():
            sld += number_densities * count * scattering_lengths[atom]

        # Store the SLD profile for this component
        sld_profiles[component] = sld

    return z_bins, sld_profiles
# end of calculate_sld()

def main():
    configure_logging()

    # Read .dat files for each component
    density_files = {component: f"{component.lower()}.dat" for component in component_composition.keys()}

    # Calculate SLD profiles
    z_bins, sld_profiles = calculate_sld(density_files)

    # Write SLD profiles to individual .dat files
    for component, sld in sld_profiles.items():
        output_file = f"{component.lower()}_sld.dat"
        np.savetxt(output_file, np.column_stack((z_bins, sld)))
        logger.info(f"Saved SLD profile for {component} to {output_file}")

if __name__ == "__main__":
    main()