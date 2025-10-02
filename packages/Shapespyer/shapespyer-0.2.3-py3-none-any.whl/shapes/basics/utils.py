import logging
import os
import random
import sys
from typing import Optional

import numpy as np

from shapes.basics.defaults import (
    FWAV,
    SPDB,
    Defaults,
    Fill,
    ShapeOrigin,
)
from shapes.basics.functions import sfx_rval
from shapes.basics.globals import HUGE, TINY
from shapes.basics.options import InputOptions, Listener, Options
from shapes.designs.protolattice import Lattice
from shapes.designs.protolayer import Layer
from shapes.designs.protoshape import Ball, Ring, Rod
from shapes.designs.smiles import Smiles, smlFile
from shapes.ioports import ioconfig, iofield, iogro, iopdb
from shapes.ioports.ioframe import CellParameters  # , DCDFrame
from shapes.ioports.ioxyz import read_mol_xyz
from shapes.stage.protoatom import Atom
from shapes.stage.protomolecularsystem import MolecularSystem
from shapes.stage.protomolecule import Molecule
from shapes.stage.protomoleculeset import MoleculeSet
from shapes.stage.protovector import Vec3

logger = logging.getLogger("__main__")
np.set_printoptions(legacy="1.21")


class LogListener(Listener):
    """Dumps update messages to logger"""

    def update(self, o: object, name: str, error: Exception | None = None) -> None:
        """Log a message if an attribute validation in
        :class:`shapes.basics.options.ValidatedAttrs` updates or fails.
        """
        if error is None:
            logger.warning(
                f"Attribute {name} was auto-updated to {getattr(o, name)}"
                " due to the changes in one of it's prime attributes"
            )
        else:
            logger.error(f"While validating {name} an error has occured: {error}")


class WriterHandler:
    def __init__(self, options: Options) -> None:
        self.options = options

        logger.info(f"Initial user-provided output name = {options.output.file}")

        if options.output.must_add_suffixes:
            shape_sfx = []
            mol_sfx = []
            if options.output.must_add_shape_sfx:
                shape_sfx = self._construct_shape_suffixes()
            if options.output.must_add_mol_sfx:
                mol_sfx = self._construct_mol_suffixes()
            suffixes = "_".join(mol_sfx + shape_sfx)
            file = f"{options.output.base}_{suffixes}{options.output.ext}"
            self.dfout = os.path.join(options.output.path, file)
        else:
            self.dfout = options.output.full_path

        logger.info(f"input-based output file name = '{self.dfout}'")

        self.writer = None

    def _construct_mol_suffixes(self) -> list[str]:
        suffixes: list[str] = []
        m_opts = self.options.molecule

        # AB: add unique solute (residue) names as a suffix to the output file name
        setname = "-".join(m_opts.resnames)
        logger.info(
            f"res-names suffix = '{setname}'  based on unique names "
            f"'{m_opts.resnames}' ..."
        )
        suffixes.append(setname)

        if m_opts.mint:
            smint = "-".join(map(str, m_opts.mint))
            suffixes.append(f"mi{smint}")

        if m_opts.mext:
            smext = "-".join(map(str, m_opts.mext))
            suffixes.append(f"mx{smext}")

        if m_opts.fracs:
            fracs_pct = []
            # AB: for 'frc' suffix use fractions in percent
            for layer_fracs in m_opts.norm_fracs:
                layer_fracs_pct = list(map(lambda x: int(100.0 * x), layer_fracs))
                fracs_pct.append(layer_fracs_pct)
            frac_strs: list[str] = ["x".join(map(str, f)) for f in fracs_pct]
            frac_str: str = "-".join(frac_strs)
            suffixes.append(f"frc{frac_str}")
        return suffixes

    def _construct_shape_suffixes(self) -> list[str]:
        suffixes: list[str] = []
        s_opts = self.options.shape

        if s_opts.stype.is_smiles:
            # if (s_opts.lring + s_opts.nmols <
            #       s_opts.MINIMUM_NMOLS + s_opts.MINIMUM_LRING
            #    ):
            suffixes = ["smiles"]  # suffixes.append(str(s_opts.type))
        else:
            # AB: add shape type as a suffix to the output file name
            suffixes.append(str(s_opts.stype))

            # AB: shifting everything below by 4 scapes
            if s_opts.stype.is_waves:
                pass
            elif s_opts.stype.is_bilayer or s_opts.stype.is_monolayer:
                suffixes.append(f"ns{self.options.membrane.nside}")
                sfx_zsep = str(f"{sfx_rval(self.options.membrane.zsep * 10)}A")
                if (
                    abs(self.options.membrane.zsep - int(self.options.membrane.zsep))
                    < TINY
                ):
                    sfx_zsep = str(f"{int(self.options.membrane.zsep) * 10}A")
                suffixes.append("zsep" + sfx_zsep)

                # non-default s_opts.dmin
                # if len(s_opts.dmin_list) > 1:
                #     sdmins = ''
                #     for dmin in s_opts.dmin_list:
                #         sdmins += str(f"-{sfx_rval(dmin * 10.0)}")
                #     suffixes.append(f"dm{sdmins[1:]}A")
                # elif abs(s_opts.dmin - Defaults.Other.MIN_DIST) > TINY:
                if abs(s_opts.dmin - Defaults.Shape.DMIN) > TINY:
                    suffixes.append(f"dm{sfx_rval(s_opts.dmin * 10.0)}A")

                # if self.options.flag.rev:
                #     suffixes.append("rev")

            elif s_opts.stype.is_lattice:
                suffixes.append(
                    f"lat{self.options.lattice.nlatx}"
                    f"x{self.options.lattice.nlaty}"
                    f"x{self.options.lattice.nlatz}"
                )

            # elif(s_opts.lring + s_opts.nmols >=
            #       s_opts.MINIMUM_NMOLS + s_opts.MINIMUM_LRING
            #     ):
            #     suffixes = ['smiles']
            else:
                # AB: no need to use extra suffix for the fill method
                # AB: since it's encoded in nmr/nmx/nmf suffix

                sscales = ""
                if (
                    abs(abs(s_opts.layers.dmin_scaling) - 1.0) > TINY
                    or abs(abs(s_opts.layers.cavr_scaling) - 1.0) > TINY
                ):
                    sscales = str(
                        f"x{abs(s_opts.layers.dmin_scaling)}"
                        f"x{abs(s_opts.layers.cavr_scaling)}"
                    )

                if sscales or s_opts.layers.quantity > 2:
                    suffixes.append(f"ml{s_opts.layers.quantity}{sscales}")
                elif not s_opts.stype.is_vesicle and s_opts.layers.quantity > 1:
                    suffixes.append(f"ml{s_opts.layers.quantity}{sscales}")

                elif s_opts.lring >= s_opts.MINIMUM_LRING:
                    # if (s_opts.lring + s_opts.nmols > s_opts.MINIMUM_LRING + s_opts.nmols >
                    #     s_opts.MINIMUM_NMOLS + s_opts.MINIMUM_LRING
                    # ):
                    suffixes.append(f"lr{s_opts.lring}")

                if s_opts.rmin:  # non-default s_opts.rmin
                    # if abs(s_opts.rmin - Defaults.shape.rmin) > TINY:  # non-default s_opts.rmin
                    if len(s_opts.rmin_list) > 1:
                        scavrs = ""
                        for cavr in s_opts.rmin_list:
                            scavrs += str(f"-{sfx_rval(cavr * 10.0)}")
                        suffixes.append(f"cr{scavrs[1:]}A")
                    else:
                        suffixes.append(f"cr{sfx_rval(s_opts.rmin * 10.0)}A")

                # non-default s_opts.dmin
                if len(s_opts.dmin_list) > 1:
                    sdmins = ""
                    for dmin in s_opts.dmin_list:
                        sdmins += str(f"-{sfx_rval(dmin * 10.0)}")
                    suffixes.append(f"dm{sdmins[1:]}A")
                elif abs(s_opts.dmin - Defaults.Shape.DMIN) > TINY:
                    suffixes.append(f"dm{sfx_rval(s_opts.dmin * 10.0)}A")

                # AB: shifting everything below by 4 scapes
                if s_opts.turns > 1:  # non-default TURNS (for a 'rod')
                    suffixes.append(f"nt{s_opts.turns}")

                if self.options.angle.alpha > 0.0:  # non-default LEFT
                    suffixes.append(f"azml{self.options.angle.alpha}")
                elif self.options.angle.alpha < 0.0:  # non-default RIGHT
                    suffixes.append(f"azmr{abs(self.options.angle.alpha)}")

                if self.options.angle.theta > 0.0:  # non-default UP
                    suffixes.append(f"altu{self.options.angle.theta}")
                elif self.options.angle.theta < 0.0:  # non-default DOWN
                    suffixes.append(f"altd{abs(self.options.angle.theta)}")

        # AB: NOT shifting anything below by 4 scapes

        if self.options.flags.fxz:
            suffixes.append("fxz")
        if self.options.flags.rev:
            suffixes.append("rev")
        if s_opts.stype.is_pinned:
            suffixes.append("pin")

        # AB: NOT shifting anything below by 4 scapes

        if self.options.flags.alignz:  # aligning along OZ
            suffixes.append("az")

        if self.options.base.origin is not ShapeOrigin.COG:  # non-default origin
            suffixes.append(str(self.options.base.origin))

        if len(s_opts.offset) > 1:
            logger.info(f"Required origin offset = {s_opts.offset}\n")

            # soff = "-".join([f"{ofs:.4g}" for ofs in s_opts.offset])
            soff = "-".join([f"{sfx_rval(ofs, 3)}" for ofs in s_opts.offset])
            suffixes.append(f"off{soff}")

        # non-default s_opts.abs_slv_buff
        if abs(s_opts.abs_slv_buff - Defaults.Shape.SBUFF) > TINY:
            suffixes.append(f"sb{sfx_rval(s_opts.abs_slv_buff * 10)}A")

        return suffixes

    def update_nmr_suffix(self, mols: int):
        # AB: no need to use extra suffix for the fill method
        # AB: since it's encoded in nmr/nmx/nmf suffix
        # if self.options.shape.fill is Fill.RINGS0:
        sfx = "nmr"  # filling with latitudinal rings - symmetric w.r.t. XY plane
        if self.options.shape.fill is Fill.RINGS:
            sfx = (
                "nmx"  # filling with latitudinal rings - possibly asymmetric and denser
            )
        elif self.options.shape.fill is Fill.FIBO:
            sfx = "nmf"

        sub: str = "_" + str(self.options.shape.stype)  # +'_'
        sfx += str(mols)
        self.dfout = self.dfout.replace(sub, sub + "_" + sfx)  # )

        logger.info(
            f"\nReplacing '{sub}' -> '{sub + '_' + sfx}' in the output file name ..."
        )

    def update_cavr_suffix(self, new_rmin: float, rmin0: float):
        if (
            abs(new_rmin - rmin0) > TINY
            and self.options.shape.lring < self.options.shape.MINIMUM_LRING
        ):
            # AB: in case '--cavr' option was provided and rmin changed
            subr = "_" + str(self.options.shape.stype) + "_cr"
            if subr in self.dfout:
                srm = sfx_rval(new_rmin * 10.0)
                if srm[-1:] == ".":
                    srm = srm[:-1]

                idx0 = self.dfout.index(subr)
                idx1 = self.dfout[idx0 + 1 :].index("_") + idx0 + 1
                idx2 = self.dfout[idx1 + 1 :].find("A") + idx1 + 2
                if idx2 > len(self.dfout):
                    idx2 = -1
                elif idx2 < 0:
                    idx2 = self.dfout[idx1 + 1 :].rfind(".") + idx1 + 1
                subr = self.dfout[idx1:idx2]
                subn = "_cr" + srm + "A"
                logger.info(
                    f"\nReplacing '{subr}' -> '{subn}' in the output file name ..."
                )
                self.dfout = self.dfout.replace(subr, subn)

    def _set_writer(self):
        pre_rem = ""

        if self.options.output.is_gro:
            pre_rem = "GRO"
            self.writer = iogro.groFile(self.dfout, "w")

        elif self.options.output.is_xyz:
            pre_rem = "XYZ"
            logger.info(
                f"GRO input '{self.options.input.file}' => XYZ output "
                f"'{self.options.output.file}'\n"
            )
            raise NotImplementedError

        elif self.options.output.is_pdb:
            pre_rem = "PDB"
            self.writer = iopdb.pdbFile(self.dfout, "w")

        elif self.options.output.has_config_prefix:
            pre_rem = "CONFIG"
            self.writer = ioconfig.CONFIGFile(self.dfout, "w")

        else:
            raise RuntimeError(
                f"Unrecognised output format: '{self.options.output.file}' "
                "[no extension => DL_POLY/DL_MESO CONFIG]\n"
            )

        # Remark / comment lines from the input file if any
        mol_setname = "-".join(self.options.molecule.resnames)
        self.rem = f"{pre_rem} coords for molecule set {mol_setname}"
        if self.options.input.is_smiles:
            self.rem += " from SMILES"

    def write_output(
        self,
        mols_out: list[MoleculeSet] = None,
        cell: CellParameters = None,
        lenscale: float = 1.0,
    ) -> None:
        self._set_writer()

        self.output_data = {
            "header": self.rem,
            "simcell": cell,
            "molsout": mols_out,
            "lscale": lenscale,
        }

        # AB: it seems lenscale has not been used for output here
        # reconsider: it is more natural to rescale coordinates and box dimensions
        # at writing time (i.e. at a single place in the code).
        if self.writer is not None:
            # self.writer.writeOutMols(self.rem, box.dims_nda(), mols_out)
            self.writer.writeOutMols(self.output_data)
            self.writer.close()


class ReaderHandler:
    def __init__(self):
        self.mols_in: list[MoleculeSet] = []
        logger.debug(f"Created {self.mols_in} - empty input list of species")
        self.input_data = {
            "header": [],
            "simcell": CellParameters(),
            "molsinp": self.mols_in,
            "resnames": (),
            "resids": (),
            "lscale": 1.0,
        }

    def _read_sxyz(self, dfinp: str):
        # TODO: REFACTOR in new style:
        # TODO: object lists to replace arrays
        # TODO: reading template molecules for each species from separate files

        # atms_inp = []
        # atms_inp.append([])
        # axyz_inp = []
        # axyz_inp.append([] * 3)
        # atms_out = []
        # atms_out.append([])
        # axyz_out = []
        # axyz_out.append([] * 3)

        atms_inp = []
        atms_inp.append([])
        axyz_inp = []
        axyz_inp.append([] * 3)
        logger.info(
            f"Created atms_inp of {len(atms_inp)} item(s) & axyz_inp of "
            "{len(axyz_inp)} item(s) x {axyz_inp[len(axyz_inp) - 1]}\n"
        )
        read_mol_xyz(dfinp, atms_inp, axyz_inp)

    def _read_sgro(
        self,
        dfinp: str,
        mol_names: tuple[str, ...],
        mol_ids: tuple[int, ...],
    ) -> None:
        fgro = iogro.groFile(dfinp)
        self.input_data["molsinp"] = self.mols_in
        self.input_data["resnames"] = mol_names
        self.input_data["resids"] = mol_ids
        # self.input_data["lscale"]   = 1.0  # lenscale

        fgro.readInMols(self.input_data)
        # print(f"NOTE: The data read in:\n{self.input_data}\n")
        logger.debug(f"Read-in GRO box:{self.input_data['simcell']}\n")

    def _read_spdb(
        self,
        dfinp: str,
        mol_names: tuple[str, ...],
        mol_ids: tuple[int, ...],
        lenscale=0.1,
    ) -> None:
        fpdb = iopdb.pdbFile(dfinp)
        self.input_data["molsinp"] = self.mols_in
        self.input_data["resnames"] = mol_names
        self.input_data["resids"] = mol_ids
        self.input_data["lscale"] = lenscale

        fpdb.readInMols(self.input_data)
        # print(f"NOTE: The data read in:\n{self.input_data}\n")
        logger.debug(f"Read-in PDB box:{self.input_data['simcell']}\n")

    def _read_config(
        self, dfinp: str, mol_names: tuple[str, ...], lenscale: float
    ) -> None:
        # MS: currently assumes entire CONFIG file contains a single template molecule
        # MS: molecule name either taken from user input (if provided) or given default name
        # TODO: REFACTOR to use after reading in FIELD file to separate out and name individual molecules

        fconf = ioconfig.CONFIGFile(dfinp)
        mol_name = mol_names if len(mol_names) > 0 else ("MOLECULE")

        # rescale positions to nm according to user input (default 0.1 for angstroms in DL_POLY, user selects for DL_MESO/DPD)
        self.input_data["molsinp"] = self.mols_in
        self.input_data["resnames"] = (
            mol_name  # why singular (only reading a single molecule)?
        )
        # self.input_data["resids"]   = mol_ids  # not supported?
        self.input_data["lscale"] = lenscale

        fconf.readInMols(self.input_data)
        # print(f"NOTE: The data read in:\n{self.input_data}\n")
        logger.debug(f"Read-in CONFIG box:{self.input_data['simcell']}\n")

    def _read_field(
        self, dfinp: str, mol_names: tuple[str, ...], lenscale: float
    ) -> None:
        # MS: reads DL_MESO FIELD file to find template molecule
        # MS: currently rejects DL_POLY FIELD files as these can only be used with a CONFIG file
        # TODO: REFACTOR to use contents of either type of FIELD file with a CONFIG file (see above)

        ffld = iofield.FIELDFile(dfinp)

        # rescale positions to nm according to user input (default 0.1 for angstroms in DL_POLY, user selects for DL_MESO/DPD)
        self.input_data["molsinp"] = self.mols_in
        self.input_data["resnames"] = mol_names
        # self.input_data["resids"]   = mol_ids  # not supported?
        self.input_data["lscale"] = lenscale

        ffld.readInMols(self.input_data)
        # print(f"NOTE: The data read in:\n{self.input_data}\n")
        logger.debug(f"Read-in FIELD box:{self.input_data['simcell']}\n")

    def read_input(
        self,
        cell: CellParameters,
        input_options: InputOptions,
        mol_names: tuple[str, ...],
        mol_ids: tuple[int, ...],
        lenscale: float,
    ) -> list[MoleculeSet]:
        if not os.path.isfile(input_options.full_path):
            raise FileNotFoundError(f"input file not found: '{input_options.full_path}'")

        self.cell = cell

        if input_options.is_gro:
            self._read_sgro(input_options.full_path, mol_names, mol_ids)
        elif input_options.is_xyz:
            self._read_sxyz(input_options.full_path)
        elif input_options.is_config or input_options.is_dlp or input_options.is_dlm:
            self._read_config(input_options.full_path, mol_names, lenscale)
        elif input_options.is_field:
            self._read_field(input_options.full_path, mol_names, lenscale)
        elif input_options.is_pdb:
            self._read_spdb(input_options.full_path, mol_names, mol_ids)
        else:
            logger.error(
                f"Unrecongnised input format: '{input_options.file}"
                f"' [no extension => DL_POLY/DL_MESO CONFIG]\n"
            )
            raise RuntimeError

        return self.mols_in


class StructurePlacer:
    def __init__(
        self,
        mols_out: list[MoleculeSet],
        cell: CellParameters,
        options: Options,
        rlen: float = 1.0,
        sname: str = "mols_out",
        stype: str = "output",
    ):
        self.rlen = rlen
        self.options = options
        self.cell = cell

        molsys = MolecularSystem(
            sname=sname, stype=stype, molsets=mols_out, vbox=self.cell.dims_vec
        )

        mtot = molsys.getMass()
        isElemMass = molsys.setMassElems()
        if not isElemMass:
            logger.warning(
                f"\nMolSys failed to reset mass (a.u.) of all "
                f"{int(mtot)} atoms -> {molsys.getMass()} "
                f"(isMassElems = {molsys.isMassElems})"
            )
        else:
            logger.info(
                f"MolSys resetting mass (a.u.) of all "
                f"{int(mtot)} atoms -> {molsys.getMass()} "
                f"(isMassElems = {molsys.isMassElems})"
            )

        self.molsys = molsys

    def place(self) -> None:
        # AB: Rescale to nm and get Rcom & Rcog for the entire molecular system
        if self.options.input.is_smiles:
            # MS: convert angstroms used for SMILES creation to appropriate lengthscale for
            #     required output file - nm for GRO files, DPD lengthscales for DL_MESO CONFIG
            #     (lenscale will retain angstroms for xyz, PDB and DL_POLY CONFIG)
            if self.options.output.is_gro:
                rcom, rcog = self.molsys.getRvecsScaled(rscale=0.1, isupdate=True)
            else:
                lenscale = self.options.base.ldpd  # defaults to 0.1 (nm)
                self.rlen = 1.0 / lenscale
                rcom, rcog = self.molsys.getRvecsScaled(
                    rscale=0.1 * self.rlen, isupdate=True
                )
        elif not self.options.output.is_gro:
            # MS: if not using GRO file as output, convert nm to angstroms
            #     (xyz, PDB, DL_POLY CONFIG) or DPD lengthscales (DL_MESO CONFIG)
            lenscale = self.options.base.ldpd
            self.rlen = 1.0 / lenscale
            rcom, rcog = self.molsys.getRvecsScaled(rscale=self.rlen, isupdate=True)
        else:
            # MS: if using GRO file as output, retain nm as lengthscale
            #     but still calculate Rcom and Rcog for entire system
            # rcom = molsys.items[0].getRcom(isupdate=True)
            # rcog = molsys.items[0].getRcog(isupdate=True)
            # logger.info(f"\n{sname}::main(): MolSys initial Rcom[0] = {rcom}")
            # logger.info(f"{sname}::main(): MolSys initial Rcog[0] = {rcog}")
            # if len(molsys) > 1:
            #     rcom = molsys.items[1].getRcom(isupdate=True)
            #     rcog = molsys.items[1].getRcog(isupdate=True)
            #     logger.info(f"\n{sname}::main(): MolSys initial Rcom[1] = {rcom}")
            #     logger.info(f"{sname}::main(): MolSys initial Rcog[1] = {rcog}")
            rcom, rcog = self.molsys.getRvecs(isupdate=True)

        # MS: all distances and box sizes from this point onwards using and reporting
        # in correct units for output file
        logger.info(f"\nMolSys initial Rcom = {rcom}")
        logger.info(f"MolSys initial Rcog = {rcog}")

        self._move_structure(rcom, rcog)

    def _move_structure(self, rcom, rcog) -> None:
        # AB: center the system at the origin and apply solvation buffer
        bmin, bmax = self.molsys.getDims()

        cbox: np.ndarray = np.array(bmax) - np.array(bmin)

        logger.debug(f"MolSys cbox before solvbuffer = {cbox}\n")

        borg = (np.array(bmax) + np.array(bmin)) * 0.5
        rcob = Vec3(*list(borg))

        # AB: allow for shape_options.abs_slv_buff=0.0 (exactly)
        sbuf = self.options.shape.abs_slv_buff  # abs(shape_options.slv_buff)
        if sbuf > 0.00001:
            if (
                self.options.shape.stype.is_bilayer
                or self.options.shape.stype.is_monolayer
            ):
                cbox_xy = (
                    self.options.shape.dmin
                    * float(self.options.membrane.nside)
                    * self.rlen
                )
                cbox[0] = cbox_xy
                cbox[1] = cbox_xy
                cbox[2] += sbuf * self.rlen
            else:
                cbox += np.array([sbuf, sbuf, sbuf]) * self.rlen

            if self.options.shape.sbuff < -TINY:
                # AB: set box size(s) to max (only if max differs < 1%)
                maxb = max(cbox)
                maxr = 1.01
                if maxb / cbox[0] < maxr:
                    cbox[0] = maxb
                if maxb / cbox[1] < maxr:
                    cbox[1] = maxb
                if maxb / cbox[2] < maxr:
                    cbox[2] = maxb
        logger.debug(f"MolSys cbox after solvbuffer = {cbox}\n")

        hbox = cbox * 0.5
        obox = hbox  # set to [0.,0.,0.] in non-Gromacs cases
        if self.rlen > 1.0:
            obox = np.array([0.0, 0.0, 0.0])

        if len(self.options.shape.offset) == 3:
            rvoff = self.options.shape.offset
            if abs(rvoff[0]) + abs(rvoff[1]) + abs(rvoff[2]) < TINY:
                shift = -Vec3(*list(obox))
            else:
                shift = Vec3(*rvoff)
            # logger.info(f"\n{sname}::main(): MolSys will move structure "
            #       f"by offset {np.array(shift)} ...")
        else:
            shift = Vec3()

        logger.debug(
            f"MolSys rcob = {list(rcob)}\n"
            f"MolSys hbox = {hbox}\n"
            f"MolSys orig = {obox} + {list(shift)}"
        )

        if not self.options.input.is_smiles:
            # AB: just a test
            rcom_pbc, rcog_pbc = self.molsys.getRvecs(
                isupdate=True, box=cbox, isMolPBC=True
            )
            logger.info(f"\nMolSys *PBC* Rcom = {rcom_pbc}")
            logger.info(f"MolSys *PBC* Rcog = {rcog_pbc}")
        else:
            rcom, rcog = self.molsys.getRvecs(isupdate=True)

        if self.options.base.origin is ShapeOrigin.COB:
            self.molsys.moveBy(shift - rcob)
            logger.info(f"MolSys placing bounding box at {np.array(shift + obox)} ...")
            rcom += shift - rcob
            rcog += shift - rcob
        elif self.options.base.origin is ShapeOrigin.COG:
            self.molsys.moveBy(shift - rcog)
            logger.info(f"MolSys placing structure COG at {np.array(shift + obox)} ...")
            rcob += shift - rcog
            rcom += shift - rcog
        elif self.options.base.origin is ShapeOrigin.COM:
            self.molsys.moveBy(shift - rcom)
            logger.info(f"MolSys placing structure COM at {np.array(shift + obox)} ...")
            rcob += shift - rcom
            rcog += shift - rcom

        if not self.options.input.is_smiles:
            rcom, rcog = self.molsys.getRvecs(isupdate=True, box=cbox, isMolPBC=True)
        else:
            rcom, rcog = self.molsys.getRvecs(isupdate=True)

        # AB: just a test
        logger.debug(f"MolSys *PBC* Rcom = {self.molsys.getRcomPBC(cbox)}")
        logger.debug(f"MolSys *PBC* Rcog = {self.molsys.getRcogPBC(cbox)}")

        logger.debug(f"MolSys final Rcob = {rcob + obox}")
        logger.debug(f"MolSys final Rcom = {rcom + obox}")
        logger.debug(f"MolSys final Rcog = {rcog + obox}\n")

        # self.cell.cbox = cbox
        self.cell.dims_from_vec(Vec3(*list(cbox)))
        logger.debug(f"MolSys cell after solvbuffer = {self.cell}\n")


class Generator:
    def __init__(self, options: Options):
        if not options.attributes_are_valid:
            raise ValueError(
                "Cannot use options with invalid attributes to instantiate a Generator"
            )
        self.writer_handler = WriterHandler(options)
        self.reader_handler = ReaderHandler()
        self.cell = CellParameters()
        self.options = options
        self.mols_out: list[MoleculeSet] = []
        self.mols_in: list[MoleculeSet] = []
        logger.info(f"Created {self.mols_out} - empty (output) list of species\n")

    def _guess_bonds(self) -> None:
        raise NotImplementedError
        ##### - Figuring out bonding connections within molecule(s) - experimental!
        # logger.info(
        #     "\n*** Topology guessing based on .gro file (experimental) - START ***"
        # )
        #
        self.mols_in[0][0].assignBonds()
        self.mols_in[0][0].guessBondsFromDistances()
        self.mols_in[0][0].guessBondsFromAtomNames()
        #
        logger.info(
            "\n*** Topology guessing based on .gro file (experimental) - END ***\n"
        )
        ##### - Figuring out bonding connections within molecule(s) - DONE

    def order_species(self):
        ##### - Ordering species - START
        # AB: making sure the order of species is as specified in the input
        if len(self.options.molecule.resnames) < 1:
            raise RuntimeError(
                f"\n Number of requested molecules {self.options.molecule.resnames} "
                f"= {len(self.options.molecule.resnames)} (should be > 0)"
            )
        if len(self.mols_in) < 1:
            mnames = [mol.name for mol in self.mols_in]
            raise RuntimeError(
                f"\n Number of read-in molecules {mnames} = {len(self.mols_in)} "
                f" (should be > 0)"
            )

        slen = -1
        if self.options.output.ext == SPDB:
            slen = 4

        mols_inp = []
        names_upd = []
        names_inp = [mol.name for mol in self.mols_in]
        for j in range(len(self.mols_in)):
            for i in range(len(self.options.molecule.resnames)):
                is_name_new = self.options.molecule.resnames[i] not in names_inp

                l = i
                if is_name_new:
                    l = j
                    names_upd.append(self.mols_in[j][0].getName())
                if slen == 4:
                    if (
                        is_name_new
                        or self.options.molecule.resnames[i][:slen]
                        == self.mols_in[j][0].getName()[:slen]
                    ):
                        mols_inp.append(self.mols_in[l])
                        mols_inp[-1].indx = j
                        break
                elif (
                    is_name_new
                    or self.options.molecule.resnames[i] == self.mols_in[j][0].getName()
                ):
                    mols_inp.append(self.mols_in[l])
                    mols_inp[-1].indx = j
                    break

        if len(names_upd) > 0:
            # AB: reset output file name (to update rnames suffix)
            self.options.molecule.resnames = names_upd
            if self.options.output.must_add_suffixes:
                self.writer_handler = WriterHandler(self.options)

            # AB: repopulate mols_out with the number of molecules found in input
            self.mols_out = []
            for idx, name in enumerate(self.options.molecule.resnames):
                new_set = MoleculeSet(
                    idx,
                    0,
                    sname=name,
                    stype="output",
                )
                self.mols_out.append(new_set)
                logger.info(f"Added {new_set} to the output list of species\n")

        if len(self.mols_in) != len(mols_inp):
            names_inp = [mol.name for mol in self.mols_in]
            raise RuntimeError(
                f"\n Numbers of read-in {names_inp} and expected distinct molecules "
                f"{self.options.molecule.resnames} differ: {len(self.mols_in)} "
                f"=/= {len(mols_inp)}"
            )

        logger.debug(f"Read-in {self.mols_in}")

        self.mols_in = mols_inp
        ##### - Ordering species - DONE

        logger.debug(f"Ordered {mols_inp}")

        if len(self.mols_in) > 0:
            logger.info(
                f"Read-in M_mols = {len(self.mols_in)}, "
                f"Mol_Names = {[mol.name for mol in self.mols_in[:]]}, "
                f"N_mols = {[len(molset) for molset in self.mols_in]}, "
                f"N_atms = {[len(molset[0]) for molset in self.mols_in]}, "
                f"M_atms = {sum(len(mols) for molset in self.mols_in for mols in molset)}\n"
            )

    def _calc_mols_num(self):
        self.mols_distr = [len(mols) for mols in self.mols_out]
        self.mols_total = sum(self.mols_distr)
        logger.info(f"\nTotal number of molecules = {self.mols_total}")
        logger.info(f"Molecule distribution = {self.mols_distr}")

    def _gen_waves(self) -> None:
        # surface placement
        # TODO: rework to use any input file (not just .xyz) for atom coordinates
        # (and put into shapes.designs/protoshapes.py as a class)
        # TODO: coordinate with reworking of shapes.ioports/ioxyz.py into similar
        # form as other input files

        atms_inp = []
        axyz_inp = []
        logger.info(
            f"Created atms_inp of {len(atms_inp)} item(s) & axyz_inp of "
            f"{len(axyz_inp)} item(s) x 3\n"
        )

        dfinp = f"{self.options.input.path}/{FWAV}"
        read_mol_xyz(dfinp, atms_inp, axyz_inp)

        matms = len(atms_inp)
        natms = len(axyz_inp)

        logger.info(f"Total number of mesh atoms  = {matms} read-in from '{dfinp}'")
        logger.info(f"Total number of mesh points = {natms} read-in from '{dfinp}'")

        # dimin = 7.0  # angstrom
        # DMIN2 = dimin*dimin
        # DMIN4 = 0.25 # nm

        # MS: all distances now in nm (including coordinates read in from xyz file)

        DMIN4 = 0.25  # nm
        atms_inc = []
        axyz_inc = []
        mmols = len(self.mols_in)
        logger.info(
            f"\nTotal # mols = {mmols}  with # atoms = {len(self.mols_in[0][0].items)} "
            f"read-in from input"
        )

        xmin = HUGE
        ymin = HUGE
        zmin = HUGE
        xmax = -HUGE
        ymax = -HUGE
        zmax = -HUGE

        logger.info(
            f"\nNumber of layers to generate msurf = {self.options.molecule.msurf} ..."
        )

        natms = 0
        latms = 0
        for ia in range(0, matms, 3):
            is_inc = True
            for ib in range(len(axyz_inc)):
                dxyz2 = (
                    (axyz_inp[ia][0] - axyz_inc[ib][0]) ** 2
                    + (axyz_inp[ia][1] - axyz_inc[ib][1]) ** 2
                    + (axyz_inp[ia][2] - axyz_inc[ib][2]) ** 2
                )
                if is_inc and dxyz2 < (self.options.shape.dmin**2):
                    is_inc = False
                    break
            if is_inc:
                latms += 1
                atms_inc.append(atms_inp[ia])
                axyz_inc.append(axyz_inp[ia])
                for isf in range(self.options.molecule.msurf):
                    mplace = 1
                    if len(self.options.molecule.cumulative_fracs) > 0:
                        mplace = len(self.options.molecule.cumulative_fracs[isf])
                    if latms == 1:
                        logger.info(
                            f"\n... generating layer {isf} with mplace = {mplace} ..."
                        )
                    iam = ia
                    iap = ia + isf + 1
                    if isf > 0:
                        iam = iap
                        iap -= 1
                        atms_inc.append(atms_inp[iam])
                        axyz_inc.append(axyz_inp[iam])
                    else:
                        atms_inc.append(atms_inp[iap])
                        axyz_inc.append(axyz_inp[iap])
                    tvec = Vec3(
                        axyz_inp[iap][0] - axyz_inp[iam][0],
                        axyz_inp[iap][1] - axyz_inp[iam][1],
                        axyz_inp[iap][2] - axyz_inp[iam][2],
                    )
                    m = 0
                    if mplace > 1:
                        frnd = random.random()
                        while frnd > self.options.molecule.cumulative_fracs[0][m]:
                            m += 1

                    self.mols_in[m][0].alignBoneToVec(
                        tvec,
                        is_flatxz=self.options.flags.fxz,
                        is_invert=self.options.flags.rev,
                        be_verbose=True,
                    )
                    self.options.molecule.mint = []
                    self.options.molecule.mext = []  # Next two lines append to list:
                    self.options.molecule.mint.append(
                        self.mols_in[m][0].bone_int
                    )  # index of backbone interior atom - 38 'C12' for SDS (CHARMM-36)
                    self.options.molecule.mext.append(
                        self.mols_in[m][0].bone_ext
                    )  # index of backbone exterior atom - 0 for 'S1' or 5 'C1'  for SDS (CHARMM-36)
                    vec0 = np.array(
                        [axyz_inp[iap][0], axyz_inp[iap][1], axyz_inp[iap][2]]
                    )  # nm

                    vec0 -= tvec.arr3() * DMIN4 / tvec.norm()
                    latms2 = latms / 2
                    if (latms2 - float(int(latms2))) > TINY:
                        vec0 -= tvec.arr3() * DMIN4 * 0.5 / tvec.norm()

                    mlast = len(self.mols_out[m].items)
                    self.mols_out[m].addItem(
                        Molecule(
                            mindx=mlast,
                            aname=self.mols_in[m].name,
                            atype="output",
                        )
                    )
                    iatms = len(self.mols_in[m][0].items)
                    for i in range(iatms):
                        vec2 = (
                            self.mols_in[m][0].items[i].rvec.arr3()
                            - self.mols_in[m][0]
                            .items[self.options.molecule.mext]
                            .rvec.arr3()
                        )
                        vec1 = vec2 + vec0
                        if xmin > vec1[0]:
                            xmin = vec1[0]
                        if ymin > vec1[1]:
                            ymin = vec1[1]
                        if zmin > vec1[2]:
                            zmin = vec1[2]
                        if xmax < vec1[0]:
                            xmax = vec1[0]
                        if ymax < vec1[1]:
                            ymax = vec1[1]
                        if zmax < vec1[2]:
                            zmax = vec1[2]
                        # add new molecule to the output
                        self.mols_out[m].items[mlast].addItem(
                            Atom(
                                aname=self.mols_in[m][0].items[i].name,
                                atype=self.mols_in[m][0].items[i].type,
                                aindx=natms,
                                arvec=list(vec1),
                            )
                        )
                        # logger.info(f"{sname}:: Added {self.mols_out[m].items[mlast].items[-1]}")
                        natms += 1

        matms = len(atms_inc)

        logger.info(
            f"\nTotal number of mesh points = {len(axyz_inc)} included from '{dfinp}'\n"
        )
        logger.info(
            f"Total number of mesh atoms  = {len(atms_inc)} included from '{dfinp}'\n"
        )
        logger.info(f"Total number of mols atoms  = {natms} generated for '{dfinp}'\n")

        fname = "config-waves_n" + str(natms) + ".xyz"
        fmode = "w"
        fcode = "utf-8"
        try:
            fio = open(fname, fmode, encoding=fcode)
        except (IOError, EOFError) as err:
            logger.error(
                f"Oops! Could not open file '{fname}' in mode '{fmode}' - FULL STOP!!!\n"
            )
            raise err
        except Exception as e:
            logger.error(
                f"Oops! Unknown error while opening file '{fname}' "
                f"in mode '{fmode}' - FULL STOP!!!\n"
            )
            raise e
        ntot = matms
        fio.write(str(ntot) + "\n")
        fio.write("XYZ coordinates for atoms on a surface'\n")
        for m in range(ntot):
            aname = atms_inc[m]
            line = "{:>4}".format(aname) + "".join(
                "{:>14.5f}{:>15.5f}{:>15.5f}".format(*axyz_inc[m])
            )
            fio.write(line + "\n")
        fio.close()

        self.options.shape.sbuff = 0.0
        self.cell.dims_from_vec(Vec3(xmax - xmin, ymax - ymin, zmax - zmin))
        logger.debug(f"MolSys cell upon setup = {self.cell}\n")

    def _gen_ball(self, ovec: Vec3) -> None:
        shape = Ball(
            isvesicle=self.options.shape.stype.is_vesicle,
            layers=self.options.shape.layers.as_list,
            rint=self.options.shape.rmin_list,
            dmin=self.options.shape.dmin_list,
            ovec=ovec,
            mols_inp=self.mols_in,
            mols_out=self.mols_out,
        )

        if (
            self.options.shape.fill is Fill.RINGS
            or self.options.shape.fill is Fill.RINGS0
        ):
            shape.makeRings(
                nlring=self.options.shape.lring,
                frcl=self.options.molecule.cumulative_fracs,
                fill=self.options.shape.fill.name.lower(),
                is_flatxz=self.options.flags.fxz,
                is_invert=self.options.flags.rev,
                # is_pinned=self.options.shape.stype.is_pinned,
            )

        elif self.options.shape.fill is Fill.FIBO:
            shape.makeFibo(
                nmols=self.options.shape.nmols,
                frcl=self.options.molecule.cumulative_fracs,
                is_flatxz=self.options.flags.fxz,
                is_invert=self.options.flags.rev,
                # is_pinned=self.options.shape.stype.is_pinned,
            )

        self._calc_mols_num()
        self.writer_handler.update_cavr_suffix(shape.getRint(), self.options.shape.rmin)

        self.writer_handler.update_nmr_suffix(self.mols_total)

        if shape.getNmols() != self.mols_total:
            logger.info(
                f"\nInconsistent Nmols = {shape.getNmols()} != {self.mols_total} !.."
            )

        # self.cell.expand_gbox()
        self.cell.max_cube_box()

    def _gen_rod(self, ovec: Vec3) -> None:
        shape = Rod(
            nturns=self.options.shape.turns,
            rint=self.options.shape.rmin,
            dmin=self.options.shape.dmin,
            ovec=ovec,
            mols_inp=self.mols_in,
            mols_out=self.mols_out,
        )
        shape.makeNew(
            nlring=self.options.shape.lring,
            frcl=self.options.molecule.cumulative_fracs,
            is_flatxz=self.options.flags.fxz,
            is_invert=self.options.flags.rev,
        )

        self._calc_mols_num()
        self.writer_handler.update_nmr_suffix(self.mols_total)

    def _gen_bilayer(self) -> None:
        shape = Layer(
            mols_inp=self.mols_in,
            mols_out=self.mols_out,
            nside=self.options.membrane.nside,
            layer_type="bilayer",
            frcs=self.options.molecule.norm_fracs,
        )
        shape.make(
            zsep=self.options.membrane.zsep,
            dmin=self.options.shape.dmin,
            layer_type="bilayer",
            frcs=self.options.molecule.norm_fracs,
        )

    def _gen_monolayer(self) -> None:
        shape = Layer(
            mols_inp=self.mols_in,
            mols_out=self.mols_out,
            nside=self.options.membrane.nside,
            layer_type="monolayer",
            frcs=self.options.molecule.norm_fracs,
        )
        shape.make(
            zsep=self.options.membrane.zsep,
            dmin=self.options.shape.dmin,
            layer_type="monolayer",
            frcs=self.options.molecule.norm_fracs,
        )

    def _gen_lattice(self) -> None:
        shape = Lattice(
            [
                self.options.lattice.nlatx,
                self.options.lattice.nlaty,
                self.options.lattice.nlatz,
            ]
        )
        shape.make(
            gbox=self.cell.dims_vec,
            mols_inp=self.mols_in,
            mols_out=self.mols_out,
            alpha=self.options.angle.alpha,
            theta=self.options.angle.theta,
            hbuf=self.options.shape.sbuff,
            ishape=self.options.shape.stype.ishape,
        )

    def _gen_ring(self, ovec: Vec3) -> None:
        shape = Ring(
            rint=self.options.shape.rmin,
            dmin=self.options.shape.dmin,
            ovec=ovec,
            mols_inp=self.mols_in,
            mols_out=self.mols_out,
        )

        shape.makeNew(
            alpha=self.options.angle.alpha,
            theta=self.options.angle.theta,
            nmols=self.options.shape.lring,
            frcs=self.options.molecule.cumulative_fracs,
            is_flatxz=self.options.flags.fxz,
            is_invert=self.options.flags.rev,
        )

    def _backbone_director(self):
        # AB: check for the (back-)bone specs (mint/mext) and reset if needed
        mol_opts = self.options.molecule
        isreset_mint = False
        if len(mol_opts.mint) < len(self.mols_in):
            logger.warning(
                f"The number of mint indices {len(mol_opts.mint)} "
                f"< {len(self.mols_in)} (number of species read in) - resetting ..."
            )
            mol_opts.mint = []
            isreset_mint = True
        isreset_mext = False
        if len(mol_opts.mext) < len(self.mols_in):
            logger.warning(
                f"The number of mext indices {len(mol_opts.mext)} "
                f"< {len(self.mols_in)} (number of species read in) - resetting ..."
            )
            mol_opts.mext = []
            isreset_mext = True
        if self.options.shape.stype.is_backboned:
            # AB: figure out the (back-)bone vectors for all species where needed
            for m in range(len(self.mols_in)):
                # AB: assuming atom indexing starts from 'head-group'
                # AB: take the first (usually 'heavy') atom as (back-)bone 'head'
                mbeg = 0
                mend = self.mols_in[m][0].nitems - 1
                if isreset_mext:
                    # AB: alternative 'defaults'
                    # if self.mols_in[m][0].name == 'SDS':
                    #     mbeg = 5  # the first C(H2) on SDS
                    # elif self.mols_in[m][0].name in {'CTA', 'DTA'}:
                    #     mbeg = 13  # the first C(H2) on CTAB(s)
                    # elif ...
                    if self.mols_in[m][0].name in mol_opts.resnames:
                        for ia in range(self.mols_in[m][0].nitems):
                            if self.mols_in[m][0][ia].name[0:1] in [
                                "S",
                                "N",
                                "C",
                            ]:
                                mbeg = ia
                                break
                    mol_opts.mext.append(mbeg)
                else:
                    mbeg = mol_opts.mext[m]
                # MS: if using full atom model of known molecules, can immediately identify last
                #     'heavy' atom in (back)-bone - otherwise (especially for CG representations)
                #     need to scan through particles (backwards) to find last one with a 'heavy' atom
                if isreset_mint:
                    mlen = len(self.mols_in[m][0])
                    if self.mols_in[m][0].name == "SDS" and mlen == 42:
                        mend = 38  # terminal C(H3) on SDS
                    elif self.mols_in[m][0].name == "CTA" and mlen == 44:
                        mend = 40  # terminal C(H3) on C(10)TAB
                    elif self.mols_in[m][0].name == "DTA" and mlen == 50:
                        mend = 46  # terminal C(H3) on C(12)TAB=DTAB
                    elif self.mols_in[m][0].name in mol_opts.resnames:
                        for ia in range(self.mols_in[m][0].nitems):
                            if self.mols_in[m][0][mend - ia].name[0:1] in [
                                "C",
                                "N",
                                "S",
                            ]:
                                mend -= ia
                                break
                    mol_opts.mint.append(mend)
                else:
                    mend = mol_opts.mint[m]

                isBackOrder = self.options.flags.rev
                if mend < mbeg:
                    isBackOrder = not isBackOrder
                    mend = mol_opts.mext[m]
                    mbeg = mol_opts.mint[m]

                for n in range(len(self.mols_in[m])):
                    self.mols_in[m][n].setBoneBeg(mbeg)
                    self.mols_in[m][n].setBoneEnd(mend)
                    self.mols_in[m][n].setBoneOrder(isBackOrder)

            logger.debug(
                f"Setting molecule 'bone' indices: {mol_opts.mint} ... {mol_opts.mext} ->  "
                f"{str([mol.getBoneInt() for mols in self.mols_in for mol in mols])} ... "
                f"{str([mol.getBoneExt() for mols in self.mols_in for mol in mols])} \n"
            )

    def _generate_from_molset(
        self,
        ovec: Vec3 | None = None,
    ) -> list[MoleculeSet]:
        """Changes the state of mols_out"""

        ##### - Backbone directors - START
        self._backbone_director()
        ##### - Backbone directors - DONE

        ##### - Shape generation - START
        if ovec is None:
            ovec = Vec3()

        if self.options.shape.stype.is_waves:
            self._gen_waves()
            self._calc_mols_num()

        elif self.options.shape.stype.is_vesicle:
            self._gen_ball(ovec)

        elif self.options.shape.stype.is_ball:
            self._gen_ball(ovec)

        elif self.options.shape.stype.is_rod:
            self._gen_rod(ovec)

        elif self.options.shape.stype.is_bilayer:
            self._gen_bilayer()
            self._calc_mols_num()

        elif self.options.shape.stype.is_monolayer:
            self._gen_monolayer()
            self._calc_mols_num()

        elif self.options.shape.stype.is_lattice:
            self._gen_lattice()
            self._calc_mols_num()

        elif self.options.shape.stype.is_ring:
            self._gen_ring(ovec)
            self._calc_mols_num()

        else:
            logger.warning(
                f"The shape {self.options.shape.stype} is unknown to the generator"
            )

        ##### - Structure placement - START
        if not self.options.shape.stype.is_lattice:
            placer = StructurePlacer(self.mols_out, self.cell, self.options)
            placer.place()
        ##### - Structure placement - DONE

        return self.mols_out

    def read_input(
        self,
        input_options: Optional[InputOptions] = None,
        mol_names: Optional[tuple[str, ...]] = None,
        mol_ids: Optional[tuple[int, ...]] = None,
        lenscale: Optional[float] = None,
    ) -> None:
        if input_options is None:
            input_options = self.options.input
        if mol_names is None:
            mol_names = tuple(self.options.molecule.resnames)
        if mol_ids is None:
            mol_ids = tuple(self.options.molecule.molids)
        if lenscale is None:
            lenscale = self.options.base.ldpd

        self.mols_in = self.reader_handler.read_input(
            self.cell, input_options, mol_names, mol_ids, lenscale
        )

    def generate_smiles(self):
        """Modifies mols_out"""
        if not self.options.input.is_smiles:
            raise ValueError("Can't generate smiles with non-smiles input")

        # SMILES style input for molecules to be generated from scratch
        smiles = []
        snames = []
        rems_inp = []
        dims = Vec3(0.0, 0.0, 0.0)

        fsml = smlFile(self.options.input.full_path)
        fsml.readInSmiles(
            rems_inp,
            smiles,
            snames,
            dims,
            self.options.molecule.resnames,
            self.options.molecule.molids,
        )  # , verbose=True)

        self.cell.dims_from_vec(dims)

        # if options.output.ext == SGRO:
        #    rscale = 0.1  # angstrom -> nm

        if len(self.options.base.cis) > 0:
            logger.info(
                f"Will generate molecules from scratch with SMILES: {smiles} "
                "with double bond 'kinks' for atoms"
                f" {self.options.base.cis}\n"
            )
        else:
            logger.info(
                f"Will generate molecules from scratch with SMILES: {smiles} "
                f"without double bond 'kinks'\n"
            )

        for i in range(len(smiles)):
            smile = ""
            if isinstance(smiles[i], list):
                # AB: in case of more than one SMILES string
                for j in range(len(smiles[i])):
                    # AB: in case of more than one isomer(s)
                    # with the same chemical formula
                    smile = smiles[i][j][0]
                    smlnm = smiles[i][j][1]
                    chemf = smiles[i][j][2]

                    if j == 0:  # create only one MoleculeSet per chemical formula
                        self.mols_out.append(
                            MoleculeSet(i, 0, sname=smlnm, stype="output")
                        )
                        # logger.debug(
                        #     f"Added {self.mols_out[i]} to the output list of species"
                        # )

                    logger.debug(
                        f"\nCalling  Smiles().getMolecule('{smile}', '{smlnm}') ...\n"
                    )
                    self.mols_out[i].addItem(
                        Smiles(smile=smile, name=smlnm).getMolecule(
                            smile=smile,
                            aname=smlnm[:5],
                            sdkinks=self.options.base.cis,
                            putHatoms=True,
                            withTopology=False,  # True,
                            alignZ=self.options.flags.alignz,
                            verbose=False,
                        )
                    )
                    logger.debug(
                        f"\n Added new molecule {i} based on SMILES '{smile}' \n"
                        f" {self.mols_out[i][-1]}', chemf = '{chemf}', natoms = {len(self.mols_out[i][-1])} ...\n"
                    )
                    # self.mols_out[i][-1].refresh() #updateRvecs()
                    # logger.info(f"\n{sname}::main(): Refreshed molecule {i} based on SMILES '{smile}' \n"
                    #      f" {self.mols_out[i][-1]}', chemf = '{chemf}', natoms = {len(self.mols_out[i][-1])} ...\n")
                    # sys.exit(0)
            else:
                # AB: in case of only one SMILES string (seems to be deprecated)
                smile = smiles[i][0]
                smlnm = smiles[i][1]
                chemf = smiles[i][2]

                self.mols_out.append(MoleculeSet(0, 0, sname=smlnm, stype="output"))
                logger.info(f"Added {self.mols_out[i]} to the output list of species")

                logger.debug(
                    f"\n Calling  Smiles().getMolecule('{smile}', '{smlnm}') ...\n"
                )
                self.mols_out[i].addItem(
                    Smiles(smile=smile, name=smlnm).getMolecule(
                        smile=smile,
                        aname=smlnm[:5],
                        sdkinks=self.options.base.cis,
                        putHatoms=True,
                        verbose=False,
                    )
                )
                logger.debug(
                    f"\n Added new molecule {i} based on SMILES '{smile}' - \n"
                    f" name = '{self.mols_out[i][-1].name}', chemf = '{chemf}', natoms = {len(self.mols_out[i][-1])} ...\n"
                )
        placer = StructurePlacer(self.mols_out, self.cell, self.options)
        placer.place()

    def generate_shape(self):
        for idx, name in enumerate(self.options.molecule.resnames):
            new_set = MoleculeSet(
                idx,
                0,
                sname=name,
                stype="output",
            )
            self.mols_out.append(new_set)
            logger.info(f"Added {new_set} to the output list of species\n")
        self.order_species()
        self._generate_from_molset()

    def generate_densities(self):
        self.order_species()

        # and isinstance(options.shape.density_names, list) \
        # and len(options.shape.density_names) > 0:

        logger.debug(
            f"\nDensNames = {self.options.density.names} - doing density calcs ..."
        )

        rgrid = self.options.shape.dens_range

        molsys = MolecularSystem(
            sname="mols_inp",
            stype="input",
            molsets=self.mols_in,
            vbox=self.cell.dims_vec,
        )

        mtot = molsys.getMass()
        isElemMass = molsys.setMassElems()
        if not isElemMass:
            logger.info(
                f"\nMolSys failed to reset mass (a.u.) of all "
                f"{int(mtot)} atoms -> {molsys.getMass()} "
                f"(isMassElems = {molsys.isMassElems})"
            )
        else:
            logger.info(
                f"\nMolSys resetting mass (a.u.) of all "
                f"{int(mtot)} atoms -> {molsys.getMass()} "
                f"(isMassElems = {molsys.isMassElems})"
            )

        # if options.input.is_gro:
        # rcom, rcog = molsys.getRvecs(isupdate=True)
        rcom = molsys.items[0].getRcom(isupdate=True)
        rcog = molsys.items[0].getRcog(isupdate=True)
        logger.debug(f"\nMolSys(inp) initial Rcom[0] (mset sep.calc) = {rcom}")
        logger.debug(f"MolSys(inp) initial Rcog[0] (mset sep.calc) = {rcog}")

        rcom, rcog = molsys.getRvecs(isupdate=True)
        logger.debug(f"\nMolSys(inp) initial Rcom[:] (msys all.calc) = {rcom}")
        logger.debug(f"MolSys(inp) initial Rcog[:] (msys all.calc) = {rcog}")

        # AB: center the system at the origin
        # bmin, bmax = molsys.getDims()
        # bbox = np.array(bmax) - np.array(bmin)
        # borg = (np.array(bmax) + np.array(bmin))*0.5
        # rcob = Vec3(*borg)

        molsys.moveBy(-self.cell.hbox_vec)
        logger.info("\nMoved the box to the origin ...\n")

        rcom = molsys.items[0].getRcom(isupdate=True)
        rcog = molsys.items[0].getRcog(isupdate=True)
        logger.debug(f"\nMolSys(inp) initial R'com[0] (mset sep.calc) = {rcom}")
        logger.debug(f"MolSys(inp) initial R'cog[0] (mset sep.calc) = {rcog}")

        rcom, rcog = molsys.getRvecs(isupdate=True)
        logger.debug(f"\nMolSys(inp) initial R'com[:] (msys all.calc) = {rcom}")
        logger.debug(f"MolSys(inp) initial R'cog[:] (msys all.calc) = {rcog}")

        if self.options.molecule.resnames[-1] == "TIP3":
            rcom_pbc = Vec3()
            rcog_pbc = Vec3()
            rcom_pbc1 = Vec3()
            rcog_pbc1 = Vec3()
            mass_mset = 0.0
            mass_mset1 = 0.0
            for im, molset in enumerate(molsys.items):  # [:-1]):
                # AB: testing / debugging
                rcom_mset = Vec3()
                rcog_mset = Vec3()
                for mol in molset:
                    rcom_mol, rcog_mol = mol.getRvecs(
                        isupdate=True, box=self.cell.dims_vec, isMolPBC=True
                    )
                    rcom_mset += rcom_mol * mol.getMass()
                    rcog_mset += rcog_mol
                rcom_mset /= molset.getMass()
                rcog_mset /= float(len(molset.items))
                if im < len(molsys.items) - 1:
                    rcom_pbc += rcom_mset * molset.getMass()
                    rcog_pbc += rcog_mset
                    mass_mset += molset.getMass()
                else:
                    rcom_pbc1 += rcom_mset * molset.getMass()
                    rcog_pbc1 += rcog_mset
                    mass_mset1 += molset.getMass()

            rcom_pbc /= mass_mset
            rcog_pbc /= float(len(molsys.items[:-1]))
            logger.debug(
                f"\nMolSet *PBC* Rcom[0] (msys tst.calc) = {rcom_pbc} - initial"
            )
            logger.debug(f"MolSet *PBC* Rcog[0] (msys tst.calc) = {rcog_pbc} - initial")
            rcom_pbc1 /= mass_mset1
            rcog_pbc1 /= float(len(molsys.items[-1]))
            logger.debug(
                f"\nMolSet *PBC* Rcom[:] (msys tst.calc) = {rcom_pbc1} - initial"
            )
            logger.debug(f"MolSet *PBC* Rcog[:] (msys tst.calc) = {rcog_pbc1} - initial")
        else:
            rcom_pbc, rcog_pbc = molsys.getRvecs(
                isupdate=True, box=self.cell.dims_vec
            )  # , isMolPBC=True)
            logger.debug(
                f"\nMolSys *PBC* Rcom[1] (no water all.calc) = {rcom_pbc} - initial"
            )
            logger.debug(
                f"MolSys *PBC* Rcog[1] (no water all.calc) = {rcog_pbc} - initial"
            )

        # AB: just a test
        rpbc = molsys.getRcomPBC(self.cell.dims_vec)
        logger.info(
            f"\nMolSys *PBC* RcomPBC (msys) = {rpbc} "
            f"<-> Rcom[0] = {molsys.items[0].getRcomPBC(self.cell.dims_vec)} "
        )
        rpbc = molsys.getRcogPBC(self.cell.dims_vec)
        logger.info(
            f"MolSys *PBC* RcogPBC (msys) = {rpbc} "
            f"<-> Rcog[0] = {molsys.items[0].getRcogPBC(self.cell.dims_vec)} "
        )

        if self.options.base.origin is ShapeOrigin.COB:
            org = self.cell.hbox_vec
        elif self.options.base.origin is ShapeOrigin.COM:
            org = rcom_pbc
        else:
            org = rcog_pbc

        molsys.moveBy(-org)
        logger.info(f"\nMoved COM/COG to the origin by {org} ...\n")
        org = Vec3()

        # AB: just a test
        rpbc = molsys.getRcomPBC(self.cell.dims_vec)
        logger.info(
            f"\nMolSys *PBC* Rcom = {rpbc} "
            f"<-> Rcom[0] = {molsys.items[0].getRcomPBC(self.cell.dims_vec)} "
        )
        rpbc = molsys.getRcogPBC(self.cell.dims_vec)
        logger.info(
            f"MolSys *PBC* Rcog = {rpbc} "
            f"<-> Rcog[0] = {molsys.items[0].getRcogPBC(self.cell.dims_vec)} "
        )

        if self.options.molecule.resnames[-1] == "TIP3":
            rcom_pbc = Vec3()
            rcog_pbc = Vec3()
            mass_mset = 0.0
            for im, molset in enumerate(molsys.items[:-1]):
                rcom_mset, rcog_mset = molset.getRvecs(
                    isupdate=True, box=self.cell.dims_vec, isMolPBC=True
                )
                logger.debug(
                    f"\nMolSet *PBC* Rcom[{im}] (mset tst.calc) = {rcom_mset} "
                    f"for {molset.name} of {molset.getMass()} m.a.u.- final"
                )
                logger.debug(
                    f"MolSet *PBC* Rcog[{im}] (mset tst.calc) = {rcog_mset} "
                    f"for {molset.name} of {molset.nitems} atoms - final"
                )
                mass_mset += molset.getMass()
                rcom_pbc += rcom_mset * molset.getMass()
                rcog_pbc += rcog_mset
            rcom_pbc /= mass_mset
            rcog_pbc /= float(len(molsys.items))
            logger.info(f"\nMolSet *PBC* R'com[:] (msys tst.calc) = {rcom_pbc} - final")
            logger.info(f"MolSet *PBC* R'cog[:] (msys tst.calc) = {rcog_pbc} - final")
        else:
            rcom_pbc, rcog_pbc = molsys.getRvecs(
                isupdate=True, box=self.cell.dims_vec, isMolPBC=True
            )
            logger.info(f"\nMolSys *PBC* R'com (no water all.calc) = {rcom_pbc} - final")
            logger.info(f"MolSys *PBC* R'cog (no water all.calc) = {rcog_pbc} - final")

        # AB: just a test
        rpbc = molsys.getRcomPBC(self.cell.dims_vec)
        logger.info(f"\nMolSys *PBC* RcomPBC (msys) = {rpbc} - total")
        rpbc = molsys.getRcogPBC(self.cell.dims_vec)
        logger.info(f"MolSys *PBC* RcogPBC (msys) = {rpbc} - total")

        inpName = self.options.input.file[:-4]
        sframe = ""
        if "frame" in inpName:
            iframe = inpName.find("frame")
            sframe = "_" + inpName[iframe:]
            inpName = inpName[:iframe]

        fsfx = (
            "Rc"
            + str(rgrid[0])
            + "-"
            + str(rgrid[1])
            + "-"
            + str(rgrid[2])
            + "nm_"
            + self.options.base.origin.name.lower()
        )
        if "msys" in self.options.density.names:
            inpName += fsfx + "_msys" + sframe
            self.options.density.names.remove("msys")
            molsys.radialDensities(
                rorg=org,
                rmin=rgrid[1],
                rmax=rgrid[0],
                dbin=rgrid[2],
                clist=self.options.molecule.resnames,
                dlist=self.options.density.names,
                bname=inpName,
            )
            # bname=options.input.file[:-4]+fsfx+'_msys')
        if "mset" in self.options.density.names:
            inpName += fsfx + "_mset_"  # +molset.name+sframe
            self.options.density.names.remove("mset")
            for molset in molsys.items:
                inpNameSet = inpName + molset.name + sframe
                molsys.radialDensities(
                    rorg=org,
                    rmin=rgrid[1],
                    rmax=rgrid[0],
                    dbin=rgrid[2],
                    clist=self.options.molecule.resnames,
                    dlist=self.options.density.names,
                    bname=inpNameSet,
                )
                # bname=options.input.file[:-4]+fsfx+'_mset_'+molset.name)

        self.mols_out = molsys.items
        self.writer_handler.dfout.replace(".gro", "_PBCmols.gro")

    def dump_file(self):
        self.writer_handler.write_output(self.mols_out, self.cell)


def configure_logging(level=None):
    logger = logging.getLogger("__main__")

    if logger.hasHandlers() and level is None:
        logger.debug(f"Logger was already configured: {logger}, {logger.handlers}")
        return logger

    if not logger.hasHandlers():
        formatter = logging.Formatter(
            "{levelname}! {filename}.{funcName}:{lineno}::\n    {message}", style="{"
        )
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        console_handler.setLevel(logging.DEBUG)
        logger.addHandler(console_handler)

    if level is None:
        level = logging.WARNING

    logger.setLevel(level)
    logger.debug(f"Logger {logger} was configured with {logger.handlers}")

    return logger
