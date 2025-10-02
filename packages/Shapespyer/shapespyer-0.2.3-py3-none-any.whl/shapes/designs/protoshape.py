"""
.. module:: protoshape
   :platform: Linux - tested, Windows [WSL Ubuntu] - tested
   :synopsis: provides classes for generating molecular structures of symmetrical shapes

.. moduleauthor:: Dr Andrey Brukhno <andrey.brukhno[@]stfc.ac.uk>

The module contains the following classes: Ring(object) > Ball(Ring) > Rod(Ring)
where `>` denotes inheritance relations: Parent > Child.
"""

# This software is provided under The Modified BSD-3-Clause License (Consistent with Python 3 licenses).
# Refer to and abide by the Copyright detailed in LICENSE file found in the root directory of the library!

##################################################
#                                                #
#  Shapespyer - soft matter structure generator  #
#                                                #
#  Author: Dr Andrey Brukhno (c) 2020 - 2025     #
#          Daresbury Laboratory, SCD, STFC/UKRI  #
#                                                #
##################################################

##from __future__ import absolute_import
__author__ = "Andrey Brukhno"
__version__ = "0.2.0 (Beta)"

# TODO: unify the coding style:
# TODO: CamelNames for Classes, camelNames for functions/methods & variables (where meaningful)
# TODO: hint on method/function return data type(s), same for the interface arguments
# TODO: one empty line between functions/methods & groups of interrelated imports
# TODO: two empty lines between Classes & after all the imports done
# TODO: classes and (lengthy) methods/functions must finish with a closing comment: '# end of <its name>'
# TODO: meaningful DocStrings right after the definition (def) of Class/method/function/module
# TODO: comments must be meaningful and start with '# ' (hash symbol followed by a space)
# TODO: insightful, especially lengthy, comments must be prefixed by develoer's initials as follows:

import logging
import sys
from math import sqrt, sin, cos
from numpy import arange, array, dot, random, arccos
from numpy.linalg import norm

from shapes.basics.globals import TINY, Pi, TwoPi, Degs2Rad, PiOver2
from shapes.stage.protovector import Vec3
from shapes.stage.protoatom import Atom
from shapes.stage.protomolecule import Molecule
# from shapes.stage.protomoleculeset import MoleculeSet

# from shapes.stage.protomoleculeset import MoleculeSet #as MolSet

logger = logging.getLogger("__main__")


class Ring(object):
    """
    Class **Ring(object)** - generates a set of molecules arranged in a 'ring' configuration.

    Parameters
    ----------
    nmols : int
        Number of molecules in a ring
    rint : float [0.0] (nm)
        Radius of the *inner* circle onto which each molecule's
        *internal* (mint) atom is placed
    dmin : float [0.5] (nm)
        Minimum distance between consecutive molecules on the inner circle
    ovec : [float, float, float]
        The *origin* for the generated 'ring' to be centred at
    mols_inp : list[MoleculeSet]
        List of *minimal* molecular sets of *distinct* template molecules (input)
    mols_out : list[MoleculeSet]
        The *final* list of the generated molecular sets (output)
    frcs : list[float]
        List of fractions for *different* molecules (auto-normalised)
    """

    def __init__(
        # TODO: refactor (use dict/tuples/lists?)
        self,
        nmols: int = 0,
        rint: list[float, list] = 0.0,
        dmin: list[float, list] = 0.5,
        ovec: Vec3 = None,
        mols_inp: list = None,
        mols_out: list = None,
        frcs: list = None,
    ):
        self.nmols = nmols
        if isinstance(rint,float):
            self.rint  = rint
            self.rints = [rint,]
        elif isinstance(rint,list):  # or isinstance(rint,tuple):
            self.rint  = rint[0]
            self.rints = rint
        else:
            logger.error("Input Rint is not float nor list - FULL STOP!!!")
            sys.exit(1)

        if isinstance(dmin,float):
            self.dmin  = dmin
            self.dmins = [dmin,]
        elif isinstance(dmin,list):  # or isinstance(dmin,tuple):
            self.dmin  = dmin[0]
            self.dmins = dmin
        else:
            logger.error("Input Dmin is not float nor list - FULL STOP!!!")
            sys.exit(1)

        self.rvorg = ovec
        self.mols_inp = mols_inp
        self.mols_out = mols_out
        self.frcs = frcs
        self.rblen = []

    def __del__(self):
        if self.mols_inp is not None:
            del self.mols_inp
        if self.mols_out is not None:
            del self.mols_out

    def sortMolsInserts(self, mols_order: list = None, frcs: list = None):
        if mols_order is None or frcs is None:
            logger.warning(
                "Undefined molecule placement order and/or fractions "
                "- sorting is skipped..."
            )
            return
        mtot = len(mols_order)
        mspc = len(frcs)
        frcd = [frcs[0]]
        frcd.extend([frcs[mf + 1] - frcs[mf] for mf in range(mspc - 1)])
        ftot = sum(frcd)
        frcd = [frc / ftot for frc in frcd]
        mols_ins = [int(round(frcd[ms] * mtot)) for ms in range(mspc)]
        ntot = sum(mols_ins)
        nvar = ntot - mtot
        logger.debug(f"(0): \n"
                    f"{mols_order}\n"
                    f"{frcs}\n"
                    f"{frcd}\n"
                    f"{float(sum(mols_ins))}\n")
        ftotN = float(sum(mols_ins))
        frcdN = [float(mols_ins[ms]) / ftotN for ms in range(mspc)]
        logger.info(
            f"Check estimated and actual molecule numbers: {ntot} =?= {mtot}\n"
            f"frcd0 = {frcd} -> counts = {mols_ins} -> \nfrcdN = {frcdN}\n "
        )

        if nvar != 0:
            # AB: in case mols' numbers sum up to different total
            fdiff = []
            # ndiff = []  # AB: for testing only
            for ms in range(mspc):
                fdiff.append(abs(float(mols_ins[ms]) / float(ntot) - frcd[ms]))
            # AB: for testing only
            #     ndiff.append(0)
            #     for ns in range(0,mspc):
            #         if mols_ins[ns] != mols_ins[ms]:
            #             ndiff[-1] += 1
            # mdiff = max(ndiff)
            # idiff = ndiff.index(mdiff)
            # cdiff = ndiff.count(mdiff)
            # logger.info(f"Check ndiff = {ndiff} -> mdiff = {mdiff} -> idiff = {idiff}, cdiff = {cdiff}\n")

            mdiff = max(fdiff)
            idiff = fdiff.index(mdiff)
            cdiff = fdiff.count(mdiff)
            logger.debug(
                f"fdiff = {fdiff} \n"
                f"mdiff = {mdiff} -> idiff = {idiff} : cdiff = {cdiff}\n"
            )
            if cdiff > 1:
                idiffs = [ms for ms in range(mspc) if abs(fdiff[ms] - mdiff) < TINY]
                ndiffs = sum(idiffs)
                logger.debug(
                    f"Check idiffs = {idiffs} -> {len(idiffs)} : {ndiffs}\n"
                )
                idiff = idiffs[random.randint(len(idiffs))]
            ninc = 1
            if nvar > 0:
                ninc = -1
            mols_ins[idiff] += ninc
            ntot += ninc
            while ntot != mtot:
                ir = random.randint(mspc)
                mols_ins[ir] += ninc
                ntot += ninc
            ftotN = float(sum(mols_ins))
            frcdN = [float(mols_ins[ms]) / ftotN for ms in range(mspc)]
            fdiff = []
            for ms in range(mspc):
                fdiff.append(abs(frcdN[ms] - frcd[ms]))
            logger.debug(
                f"Check updated and actual molecule numbers: {ntot} =?= {mtot}\n"
                f"frcdN = {frcdN} <- mols_ins = {mols_ins }\n"
                f"fdiff = {fdiff}\n "
            )
        ntot = 0
        mols_idord = [
            io for io in range(len(mols_order)) if mols_order[io] < 0
        ]
        for m in range(mspc):
            for _ in range(mols_ins[m]):
                ir = random.randint(mtot - ntot)
                ntot += 1
                mols_order[mols_idord[ir]] = m
                mols_idord.pop(ir)
        mins = sum([1 for mo in mols_order if mo > -1])
        if mins != ntot:
            logger.info(
                f"# inserted mols {mins} =?= {ntot} # filled in places"
            )
            logger.info(
                "check\n"
                f"mols_order = {mols_order} ({mtot})\n"
                f"mols_ins   = {mols_ins} ({mspc})\n"
            )
            sys.exit(1)
        # else:
        #     logger.info(f"Molecule counts = "
        #           f"{mols_ins} ({len(mols_ins)})\n")
        #     logger.info(f"Finished with \n"
        #           f"mols_order = {mols_order} ({len(mols_order)} =?= {mins})\n"
        #           f"mols_ins   = {mols_ins} ({len(mols_ins)})\n")

    # end of Ring.sortMolsInserts()

    def make(
        # TODO: refactor (use dict/lists/tuples?)
        self,
        rint: float = 0.0,
        alpha: float = 0.0,
        theta: float = 0.0,
        nmols: int = 0,
        mols_inp: list = None,
        mols_out: list = None,
        frcs: list = None,
        is_flatxz: bool = False,
        is_invert: bool = False,
        # is_pinned: bool = False,
        mols_order: list = None,
        be_verbose: bool = False,
    ):
        # , dzmove=0.0):  # for Z-stepping
        """
        Takes a minimal set of distinct molecules as input and populates a Ring object (``self``)
        with molecules placed accordingly.

        :param rint: as above
        :param alpha: azimuth angle
        :param theta: altitude angle
        :param nmols: as above
        :param mols_inp: as above
        :param mols_out: as above
        :return: None (``mols_out = self.mols_out``)
        """

        # check and reset molecule sets if necessary
        if isinstance(mols_inp, list):
            self.mols_inp = mols_inp
        elif isinstance(self.mols_inp, list):
            mols_inp = self.mols_inp
        else:
            raise ValueError(
                "ERROR: Incorrect input containerfor template molecules (not a list)!"
            )

        if isinstance(mols_out, list):
            self.mols_out = mols_out
        elif isinstance(self.mols_out, list):
            mols_out = self.mols_out
        else:
            raise ValueError(
                "ERROR: Incorrect output container"
                "for molecules to be generated (not a list)!"
            )

        if isinstance(frcs, list):
            self.frcs = frcs
        elif isinstance(self.frcs, list):
            frcs = self.frcs
        # else:
        #     raise ValueError(
        #         "ERROR: Incorrect input"
        #         "for molecule fractions (not a list)!"
        #     )
        # flatten the fraction list, if necessary
        mfracs = 0
        if isinstance(frcs, list) and len(frcs) > 0:
            if isinstance(frcs[0], list):
                frcs = frcs[0]
            mfracs = len(frcs)
        mpick = len(mols_inp)

        if nmols < 1:
            if self.nmols < 1:
                logger.warning(
                    f"Max number of molecules in a ring {nmols} too small - "
                    "reset to 1"
                )
                self.nmols = 1
            nmols = self.nmols
        else:
            self.nmols = nmols

        # internal radius of a ring, from the origin
        # to the nearest 'bone' atom (normally 'mint')
        rmin = self.rint
        if rint > TINY:
            rmin = rint

        # initial rotation angles (azimuth/altitude)  [radians]
        arad = alpha * Degs2Rad
        trad = theta * Degs2Rad
        cosa = cos(arad)
        sina = sin(arad)
        cost = cos(trad)
        sint = sin(trad)
        tvec = (cosa * cost, sina * cost, sint)
        rblen = []  # 'bone' length(s) for input molecule(s)
        mmols = len(mols_inp)
        for m in range(mmols):
            rblen.append(norm(mols_inp[m][0].getBoneRvecIntToExt()))
            for n in range(len(mols_inp[m])):
                mols_inp[m][n].alignBoneToVec(
                    tvec, is_flatxz=is_flatxz, is_invert=is_invert
                )  # , be_verbose=True)
        rbmax = max(rblen)

        # generate the shape (ring)
        # Z-shift
        vecz = array([0.0, 0.0, 0.0])
        if isinstance(self.rvorg, Vec3):
            vecz = self.rvorg.arr3()  # array([0.0, 0.0, zshift])
        dphi = TwoPi / float(nmols)
        # rotation angle in the XY plane
        aphi0 = 0.0
        natms = 0

        ntot = 0
        mtot = nmols
        if mfracs > 0:
            if isinstance(mols_order, list):
                ntot = len(mols_order)
                if ntot > nmols:
                    mtot = ntot
                ntot = sum([1 for mo in mols_order if mo < 0])
            else:
                # mols_order = []
                mols_order = [-1 for _ in range(mtot)]
                self.sortMolsInserts(mols_order=mols_order, frcs=frcs)

        # dzstp = dzmove / float(nmols)  # Z-step per molecule
        # the loop produces one ring of molecules (each rotated around Z axis)
        for k in range(nmols):
            aphi = aphi0 + float(k) * dphi
            m = 0
            # AB: new version - random molecule placement within the entire shape (not a ring only)
            if mfracs > 1:
                m = mols_order[ntot]
                mols_order[ntot] = -m - 1
                # AB: random placement on a separate ring:
                # frnd = random.random()
                # while frnd > frcs[m]:
                #    m += 1
            elif mpick > 1:
                m = k % mpick
            ntot += 1

            mlast = len(mols_out[m].items)
            mols_out[m].addItem(
                Molecule(mindx=mlast, aname=mols_inp[m].name, atype="output")
            )

            # bone_int  # index of backbone interior atom
            # 38 'C12' for SDS (CHARMM-36)
            mint = mols_inp[m][0].getBoneInt()

            # bone_ext  # index of backbone exterior atom
            # 1 for 'S1' or 5 'C1'  for SDS (CHARMM-36)
            # mext = mols_inp[m][0].getBoneExt()

            # vector along radial direction + Z-shift
            vec0 = array([cos(aphi), sin(aphi), 0.0]) * rmin + vecz

            if mpick > 1:
                # AB: if more than one species, make sure
                # all head (mext) atoms are placed on the outer surface
                if not is_invert:
                    vec0 = (
                        array([cos(aphi), sin(aphi), 0.0])
                        * (rmin + (rbmax - rblen[m]) * cost)
                        + vecz
                        + array([0.0, 0.0, (rbmax - rblen[m]) * sint])
                    )

            # merely rotate about Z axis
            cosa = cos(aphi)
            sina = sin(aphi)
            rotM = array(
                [[cosa, -sina, 0.0], [sina, cosa, 0.0], [0.0, 0.0, 1.0]]
            )

            # if is_pinned:
            #     vec1 = mols_inp[m][0].items[0].rvec.arr3() -
            #            mols_inp[m][0].items[mint].rvec.arr3()
            #     vec2 = dot(rotM, vec1)
            #     vec1 = vec2 + vec0
            #     #AB: ad hoc implementation for now
            #     if is_invert:
            #         if (vec1[0]**2 + vec1[1]**2 < 7.29) or (vec1[0]**2 + vec1[2]**2 < 7.29) \
            #             or (vec1[1]**2 + vec1[2]**2 < 7.29): continue
            #     else:
            #         if (vec1[0]**2 + vec1[1]**2 < 9.0) or (vec1[0]**2 + vec1[2]**2 < 9.0) \
            #             or (vec1[1]**2 + vec1[2]**2 < 9.0): continue

            matms = len(mols_inp[m][0].items)
            for i in range(matms):
                vec1 = (
                    mols_inp[m][0].items[i].rvec.arr3()
                    - mols_inp[m][0].items[mint].rvec.arr3()
                )
                vec2 = dot(rotM, vec1)
                # check the norm of the rotated vector for consistency
                diff = norm(vec1) - norm(vec2)
                if diff * diff > TINY:
                    logger.warning(
                        f"Vector difference upon rotation about Z: ({i}) = {diff}\n"
                    )
                # add new molecule to the output
                mols_out[m].items[mlast].addItem(
                    Atom(
                        aname=mols_inp[m][0].items[i].name,
                        atype=mols_inp[m][0].items[i].type,
                        aindx=natms,
                        arvec=Vec3(*(vec2 + vec0)),
                    )
                )
                # aindx=natms, arvec=list(vec2 + vec0)))
                natms += 1

    # end of Ring.make()

    def alignMolTo(
        self,
        tvec=(1.0, 0.0, 0.0),
        mol_inp=None,
        is_flatxz=False,
        is_invert=False,
        be_verbose=False,
    ):
        if mol_inp is not None:
            mol_inp.alignBoneToVec(
                tvec, is_flatxz=is_flatxz, is_invert=is_invert, be_verbose=be_verbose
            )

    # end of Ring.alignMolTo()

    def alignMolsTo(
        self,
        tvec=(1.0, 0.0, 0.0),
        mols_inp: list = None,
        is_flatxz=False,
        is_invert=False,
        be_verbose=False,
    ):
        # tvec = (cosa * cost, sina * cost, sint)
        self.rblen = []  # 'bone' length(s) for input molecule(s)
        mmols = len(mols_inp)
        for m in range(mmols):
            self.rblen.append(norm(mols_inp[m][0].getBoneRvecIntToExt()))
            for n in range(len(mols_inp[m])):
                mols_inp[m][n].alignBoneToVec(tvec, is_flatxz, is_invert, be_verbose)

    # end of Ring.alignMolsTo()

    def alignMolsToAngs(
        self,
        alpha=0.0,
        theta=0.0,
        mols_inp: list = None,
        is_flatxz=False,
        is_invert=False,
        be_verbose=False,
    ):
        # initial rotation angles (azimuth/altitude)  [degree -> radian]
        arad = alpha * Degs2Rad
        trad = theta * Degs2Rad
        cosa = cos(arad)
        sina = sin(arad)
        cost = cos(trad)
        sint = sin(trad)
        tvec = (cosa * cost, sina * cost, sint)
        self.alignMolsTo(tvec, mols_inp, is_flatxz, is_invert, be_verbose)

    # end of Ring.alignMolsToAngs()

    def makeNew(
        # TODO: refactor (use dict/lists/tuples?)
        self,
        rint: float = 0.0,
        alpha: float = 0.0,
        theta: float = 0.0,
        nmols: int = 0,
        mols_inp: list = None,
        mols_out: list = None,
        frcs: list = None,
        is_flatxz: bool = False,
        is_invert: bool = False,
        # is_pinned: bool = False,
        mols_order: list = None,
        be_verbose: bool = False,
    ):
        # , dzmove=0.0):  # for Z-stepping
        """
        Takes a minimal set of distinct (template) molecules as input
        and populates 'self.mols_out' with molecules arranged in a **Ring**
        configuration.

        Parameters
        ----------
        nmols : int
            Number of molecules in a ring (can be rest based on 'dmin' and 'rmin')
        rint : float [0.0] (nm)
            Radius of the *inner* circle onto which each molecule's
            *internal* (mint) atom is placed (can be reset based on 'nmols' and 'dmin')
        alpha: float [0.0] (degree)
            Azimuthal angle from the OX axis in the XY plane for all molecule 'bone' vectors
        theta: float [0.0] (degree)
            Altitude (polar) angle from the OZ axis for all molecule 'bone' vectors
        mols_inp : list[MoleculeSet]
            List of *minimal* molecular sets of *distinct* template molecules (input)
        mols_out : list[MoleculeSet]
            The *final* list of the generated molecular sets (output)
        frcs : list[float]
            List of fractions for *different* molecules
        is_flatxz : bool [False]
            Flag to rotate molecule around it's 'bone' vector
            so it is *flattened* in the XZ plane
        is_invert : bool [False]
            Flag to invert each molecule's 'bone' vector by swapping 'mint' and 'mext'.
        mols_order : list[int]
            Auxiliary list of molecule indices defining the order of placement thereof
            (populated and used internally in subclasses of 'Ring')
        Returns
        -------
        None
            Note that ``mols_out = self.mols_out'' being populated.
        """

        # check and reset molecule sets if necessary
        if mols_inp is not None and isinstance(mols_inp, list):
            self.mols_inp = mols_inp
        elif self.mols_inp is not None and isinstance(self.mols_inp, list):
            mols_inp = self.mols_inp
        else:
            raise ValueError(
                "ERROR: Incorrect input containerfor template molecules (not a list)!"
            )

        if mols_out is not None and isinstance(mols_out, list):
            self.mols_out = mols_out
        elif self.mols_out is not None and isinstance(self.mols_out, list):
            mols_out = self.mols_out
        else:
            raise ValueError(
                "ERROR: Incorrect output container"
                "for molecules to be generated (not a list)!"
            )

        if isinstance(frcs, list):
            self.frcs = frcs
        elif isinstance(self.frcs, list):
            frcs = self.frcs
        # else:
        #     raise ValueError(
        #         "ERROR: Incorrect input"
        #         "for molecule fractions (not a list)!"
        #     )
        # flatten the fraction list, if necessary
        mfracs = 0
        if isinstance(frcs, list) and len(frcs) > 0:
            if isinstance(frcs[0], list):
                frcs = frcs[0]
            mfracs = len(frcs)
        mpick = len(mols_inp)

        if nmols < 1:
            if self.nmols < 1:
                logger.warning(
                    f"Number of molecules in a ring is too small - reset: "
                    f"{self.nmols} -> 1"
                )
                # f"Max number of molecules in a ring {nmols} too small - reset to 1")
                self.nmols = 1
            nmols = self.nmols
        else:
            self.nmols = nmols

        # internal radius of a ring = distance from the origin to the centre of the nearest 'bone' atom
        rmin = self.rint
        if rint > TINY:
            rmin = rint
            self.rint = rmin

        # initial rotation angles (azimuth/altitude)  [radians]
        arad = alpha * Degs2Rad
        trad = theta * Degs2Rad
        cosa = cos(arad)
        sina = sin(arad)
        cost = cos(trad)
        sint = sin(trad)
        tvec = (cosa * cost, sina * cost, sint)

        self.alignMolsTo(tvec, mols_inp, is_flatxz, is_invert)
        rbmax = max(self.rblen)

        # generate the shape (ring)
        # Z-shift
        vecz = array([0.0, 0.0, 0.0])
        if isinstance(self.rvorg, Vec3):
            vecz = self.rvorg.arr3()
        dphi = TwoPi / float(nmols)

        ntot = 0
        mtot = nmols
        if mfracs > 0:
            if isinstance(mols_order, list):
                ntot = len(mols_order)
                if ntot > nmols:
                    mtot = ntot
                ntot = sum([1 for mo in mols_order if mo < 0])
            else:
                mols_order = [-1 for _ in range(mtot)]
                self.sortMolsInserts(mols_order=mols_order, frcs=frcs)
            # AB: for testing only
            # frcd = [frcs[0]]
            # frcd.extend([ frcs[mf + 1] - frcs[mf] for mf in range(mfracs - 1) ])
            # print(f"{self.__class__.__name__}.makeNew(): Current fractions = {frcd}")

        # rotation angle in the XY plane
        aphi0 = 0.0
        natms = 0
        # dzstp = dzmove / float(nmols)  # Z-step per molecule
        # the loop produces one ring of molecules (each rotated around Z axis)
        for k in range(nmols):
            aphi = aphi0 + float(k) * dphi

            m = 0
            # AB: random molecule placement within the entire shape
            # i.e. not on a separate ring only
            if mfracs > 1:
                m = mols_order[ntot]
                mols_order[ntot] = -m - 1
            elif mpick > 1:
                m = k % mpick
            ntot += 1

            #print(f"Index m = {m} <? {len(mols_out)}; k = {k} % mpick = {mpick} => {k % mpick}")
            mlast = len(mols_out[m].items)
            mols_out[m].addItem(
                Molecule(mindx=mlast, aname=mols_inp[m].name, atype="output")
            )

            # bone_int  # index of backbone interior atom
            # 38 'C12' for SDS (CHARMM-36)
            mint = mols_inp[m][0].getBoneInt()

            # bone_ext  # index of backbone exterior atom
            # 1 for 'S1' or 5 'C1'  for SDS (CHARMM-36)
            # mext = mols_inp[m][0].getBoneExt()

            # vector along radial direction + Z-shift
            vec0 = array([cos(aphi), sin(aphi), 0.0]) * rmin + vecz

            if mpick > 1:
                # AB: if more than one species, make sure
                # all head (mext) atoms are placed on the outer surface
                if not is_invert:
                    dr = rbmax - self.rblen[m]
                    vec0 += array(
                        [cos(aphi) * cost * dr, sin(aphi) * cost * dr, sint * dr]
                    )

            # merely rotate about Z axis
            cosa = cos(aphi)
            sina = sin(aphi)
            rotM = array(
                [[cosa, -sina, 0.0], [sina, cosa, 0.0], [0.0, 0.0, 1.0]]
            )

            # if is_pinned:
            #     vec1 = mols_inp[m][0].items[0].rvec.arr3() -
            #            mols_inp[m][0].items[mint].rvec.arr3()
            #     vec2 = dot(rotM, vec1)
            #     vec1 = vec2 + vec0
            #     #AB: ad hoc implementation for now
            #     if is_invert:
            #         if (vec1[0]**2 + vec1[1]**2 < 7.29) or (vec1[0]**2 + vec1[2]**2 < 7.29) \
            #             or (vec1[1]**2 + vec1[2]**2 < 7.29): continue
            #     else:
            #         if (vec1[0]**2 + vec1[1]**2 < 9.0) or (vec1[0]**2 + vec1[2]**2 < 9.0) \
            #             or (vec1[1]**2 + vec1[2]**2 < 9.0): continue

            matms = len(mols_inp[m][0].items)
            for i in range(matms):
                vec1 = (
                    mols_inp[m][0].items[i].rvec.arr3()
                    - mols_inp[m][0].items[mint].rvec.arr3()
                )
                vec2 = dot(rotM, vec1)
                # check the norm of the rotated vector for consistency
                diff = norm(vec1) - norm(vec2)
                if diff * diff > TINY:
                    logger.warning(
                        f"Vector difference upon rotation about Z: ({i}) = {diff}\n"
                    )
                # add new molecule to the output
                mols_out[m].items[mlast].addItem(
                    Atom(
                        aname=mols_inp[m][0].items[i].name,
                        atype=mols_inp[m][0].items[i].type,
                        aindx=natms,
                        arvec=Vec3(*(vec2 + vec0)),
                    )
                )
                # aindx = natms, arvec = list(vec2 + vec0)))
                natms += 1

    # end of Ring.makeNew()


# end of class Ring


class Ball(Ring):
    """
    Class **Ball(Ring)** - generates a set of molecules arranged in a 'ball' configuration (a.k.a. spherical micelle).

    Note
    ----
    As a derivative of the 'Ring' class, the 'Ball' class inherits the properties of the 'Ring'
    and extends it with extra features (so refer also to the 'Ring' class):

    Parameters
    ----------
    isvesicle : bool
        **True** redefines the 'Ball' as a spherical *vesicle* rather than a micelle,
        in which case `layers = [2, 1.0, 1.0]` is set automatically.
    layers : [int, float, float]
        int is the number of (mono-)layers (or shells) making up a ball,
        the two floats are scaling factors for dmin and layer radii, respectively,
        in the case of more than one layer.

    Note
    ----
    With `fill="rings0"` or unspecified, Ball.makeRings() method accepts `nlring` as input,
    which is the number of molecules fitting on the 'equator' ring. In this case(s)
    the total number of molecules (`self.nmols`) will be reported upon creation of the ball.

    By default, when `fill` parameter is not specified (`="rings0"`), molecules are placed
    equidistantly on a number, `int(nlring/2)+1`, of equidistant rings parallel to
    the XY plane, which include 'rings' comprised of a single molecule at each pole.
    This corresponds to uniform latitude/longitude filling of the ball, with symmetrical
    placement and population of the rings, over either even or odd number of latitudes.
    If the number of latitudes is odd, the central one coincides with the equator;
    otherwise the equator remains unoccupied.

    Note
    ----
    When `fill="rings"`, the latitudes are chosen differently. In this case the objective
    is to equate the latitudinal and longitudinal distances between the molecules. That is,
    when the number of molecules fitting the equator, `nlring = int(2 Pi rmin / dmin)`, is
    even, the method will produce identical molecule distribution as the above.
    However, when `nlring` is odd, the method will start by populating the 'South pole' with
    one molecule and then placing rings at latitudes separated by exactly `dmin` - the target
    min distance between molecules. The last ring placed will then be half the `dmin`
    distance from the 'North pole' (with unoccupied pole, of course).

    Note
    ----
    With 'fill=fibo', Ball.makeFibo() method accepts 'nmols' as input which specifies
    the total number of molecules in the generated ball structure. In this case molecules
    are placed on the inner spherical surface following the Fibonacci 'spiral'.
    This method of molecule placement aims to maintain average surface density, so
    the distances between neighbour molecules (i.e. `mint` or `mext` atoms) is not constant.
    """

    def __init__(self, isvesicle=False, layers: list = None, *args, **keys):
        super(Ball, self).__init__(*args, **keys)
        self.isvesicle = isvesicle
        if layers is None:
            layers = [1, 1.0, 1.0]
        if isvesicle and layers[0] < 2:
            layers = [2, 1.0, 1.0]
        self.lnring = [self.nmols]  # <- Ring class
        self.lradii = [self.rint]   # <- Ring class
        self.layers = layers #[0]  # for multilayered vesicles
        self.ilayer = 0
        self.lturns = [0]
        self.lnmols = [0]
        self.nmols = 0

    def __del__(self):
        super(Ball, self).__del__()

    def isVesicle(self):
        return self.isvesicle

    def getRint(self):
        return self.rint

    def getLradii(self):
        return self.lradii

    def getLayers(self):
        return self.layers

    def getLayersN(self):
        return self.layers[0]

    def getLayersScaleDmin(self):
        return self.layers[1]

    def getLayersScaleRadii(self):
        return self.layers[2]

    def getNmols(self):
        return self.nmols

    def getLmols(self):
        return self.lnmols

    def getLrings(self):
        return self.lnring

    def getLturns(self):
        return self.lturns

    def make(
        # TODO: refactor (use dict/lists/tuples?)
        self,
        rmin: float = 0.0,
        alpha: float = 0.0,
        theta: float = 0.0,
        nturns: int = 0,
        nlring: int = 0,
        mols_inp: list = None,
        mols_out: list = None,
        frcl: list = None,
        is_flatxz: bool = False,
        is_invert: bool = False,
        # is_pinned: bool = False,
        be_verbose: bool = False,
    ):
        # check and reset molecule sets if necessary
        if isinstance(mols_inp, list):
            self.mols_inp = mols_inp
        elif isinstance(self.mols_inp, list):
            mols_inp = self.mols_inp
        else:
            raise ValueError(
                "ERROR: Incorrect input containerfor template molecules (not a list)!"
            )

        if isinstance(mols_out, list):
            self.mols_out = mols_out
        elif isinstance(self.mols_out, list):
            mols_out = self.mols_out
        else:
            raise ValueError(
                "ERROR: Incorrect output container"
                "for molecules to be generated (not a list)!"
            )

        if isinstance(frcl, list):
            self.frcs = frcl
        elif isinstance(self.frcs, list):
            frcl = self.frcs
        # else:
        #     raise ValueError(
        #         "ERROR: Incorrect input"
        #         "for molecule fractions (not a list)!"
        #     )
        # flatten the fractions list if necessary
        fracs = frcl
        if isinstance(frcl, list) and len(frcl) > 0:
            if isinstance(frcl[0], list):
                fracs = frcl[0]

        # if rmin < TINY: rmin = self.rint
        # if nlring < 10:
        #     logger.error(
        #           f"Requested number of molecules on 'equator' {nlring} < 10 (unsupported) "
        #           f"- FULL STOP!!!")
        #     sys.exit(1)

        # use the initial values of self in case the input is irrelevant
        # and then amend if necessary
        if self.ilayer == 0:
            if rmin < TINY:
                rmin = self.lradii[0]
            else:
                self.lradii[0] = rmin
            if nlring < 1:
                nlring = self.lnring[0]
            else:
                self.lnring[0] = nlring
            self.nmols = 0

        TwoPiOverDmin =  TwoPi / self.dmin
        if nlring < 2 and (rmin - self.dmin) > TINY:
            # nring0 = nlring
            nlring = int(TINY + TwoPiOverDmin * rmin )
            # print(f"{self.__class__.__name__}.makeNew(WARN): "
            #       f"Number of molecules on 'equator' lring = "
            #       f"{nring0} -> {nlring} based on Rmin = {rmin}")
            # f"{self.lnring} -> {nlring}; Rmin -> {rmin} (adjusted)")

        if nlring < 10:
            logger.error(
                f"Requested number of molecules on 'equator' {nlring} < 10 (unsupported)"
                f" - FULL STOP!!!"
            )
            sys.exit(1)
        elif (self.dmin - rmin) > TINY:
            rmin0 = rmin
            rmin = float(nlring) * self.dmin / TwoPi
            logger.warning(
                f"Internal radius of layer {self.ilayer} Rmin = "
                f"{rmin0} -> {rmin} based on lring = {nlring}"
            )

        if nturns < 1:
            nturns = int(nlring / 2) + 1
            # if float(nturns) % 2.0 < TINY: nturns += 1  # make nturns odd
            if nturns < 5:
                logger.error(
                    f"Requested number of rings (turns) in a ball {nturns} < 5 "
                    f"(unsupported) - FULL STOP!!!"
                )
                sys.exit(1)

        if self.ilayer > 0:
            if self.ilayer >= self.getLayersN():
                logger.info(
                    f"Ball is complete with {self.ilayer - 1} =?= {self.getLayersN()} "
                    f"(monolayers)"
                )
                return
            self.lnring.append(nlring)
            self.lturns.append(nturns)
            self.lradii.append(rmin)
        else:
            self.lnring[0] = nlring
            self.lturns[0] = nturns
            self.lradii[0] = rmin

        logger.info(
            f"Number of molecules on 'equator':  lring = {nlring} <-> "
            f"Rmin = {rmin}"
        )
        logger.info(f"Number of rings (turns) in a ball: turns = {nturns}")

        # initial rotation angles (azimuth/altitude)  [radians]
        alpha = 0.0
        theta = -90.0
        dthet = 180.0 / float(nturns - 1)
        rminc = 0.0
        mmols = 1

        # start from the bottom with just one molecule and build up to the top symmetrically if possible
        zsorg = -rmin
        for i in range(nturns):
            logger.debug(
                f"inner: Placing {i}-th ring of {mmols} mols at zorg = {zsorg},"
                f" theta = {theta}, rmin = {rminc}"
            )
            Ring(rint=rminc, dmin=self.dmin, ovec=Vec3(0.0, 0.0, zsorg)).make(
                alpha=alpha,
                theta=theta,
                nmols=mmols,
                mols_inp=mols_inp,
                mols_out=mols_out,
                frcs=fracs,
                is_flatxz=is_flatxz,
                is_invert=is_invert,
                # is_pinned=is_pinned,
            )
            theta += dthet
            zsorg = rmin * sin(theta * Degs2Rad)
            rminc = rmin * cos(theta * Degs2Rad)
            mmols = 1 if rminc < TINY else int(TINY + TwoPiOverDmin * rminc)

        # add the outer layer in the case of vesicle
        if self.ilayer < self.getLayersN() - 1:
            # if self.isvesicle:
            self.ilayer += 1
            # self.isvesicle = (self.ilayer < self.getLayersN()-1)
            # arad = alpha * Degs2Rad  # initial rotation angle (azimuth)  [radians]
            # trad = theta * Degs2Rad  # initial rotation angle (altitude) [radians]
            # cosa = cos(arad)
            # sina = sin(arad)
            # cost = cos(trad)
            # sint = sin(trad)
            # tvec = (cosa * cost, sina * cost, sint)
            rblen = []  # 'bone' length(s) for input molecule(s)
            mmols = len(mols_inp)
            for m in range(mmols):
                rblen.append(norm(mols_inp[m][0].getBoneRvecIntToExt()))
                for n in range(len(mols_inp[m])):
                    mols_inp[m][n].revBoneOrder()
                    # mols_inp[m][n].alignBoneToVec(tvec, is_flatxz=is_flatxz, is_invert=is_invert) #, be_verbose=True)
            rbmax = max(rblen)

            logger.debug(
                f"outer: rmin = {rmin} "
                f"+ {rbmax} + {self.dmin} = {rmin + rbmax + self.dmin}"
            )
            rmin = rmin + rbmax + self.dmin
            nlring = int(rmin * TwoPiOverDmin) # / self.dmin)
            nturns = int(nlring / 2) + 1

            # initial rotation angles (azimuth/altitude)
            alpha = 0.0
            theta = -90.0
            dthet = 180.0 / float(nturns - 1)
            zsorg = -rmin
            rminc = 0.0
            mmols = 1

            # flatten the fractions list if necessary
            if isinstance(frcl, list) and len(frcl) > 1:
                if isinstance(frcl[1], list):
                    fracs = frcl[1]

            for i in range(nturns):
                logger.debug(
                    f"outer: Placing {i}-th ring of {mmols} mols at zorg = {zsorg}, "
                    f"theta = {theta}, rmin = {rminc}"
                )
                Ring(rint=rminc, dmin=self.dmin, ovec=Vec3(0.0, 0.0, zsorg)).make(
                    alpha=alpha,
                    theta=theta,
                    nmols=mmols,
                    mols_inp=mols_inp,
                    mols_out=mols_out,
                    frcs=fracs,
                    is_flatxz=is_flatxz,
                    is_invert=(not is_invert),
                    # is_pinned=is_pinned,
                )
                theta += dthet
                zsorg = rmin * sin(theta * Degs2Rad)
                rminc = rmin * cos(theta * Degs2Rad)
                mmols = 1 if rminc < TINY else int(TINY + TwoPiOverDmin * rminc)

    # end of Ball.make()

    def makeRings(
        # TODO: refactor (use dict/tuples/lists?)
        self,
        rmin: list[float | list] = 0.0,
        nlring: int = 0,
        mols_inp: list = None,
        mols_out: list = None,
        frcl: list = None,
        fill: str = "rings0",
        is_flatxz: bool = False,
        is_invert: bool = False,
        # is_pinned: bool = False,
        be_verbose: bool = False,
    ):
        """
        Takes a minimal set of distinct (template) molecules as input and
        populates 'self.mols_out' with molecules arranged in a **Ball**
        structure.

        Parameters
        ----------
        nlring: int,
            Number of molecules in the largest (equatorial) ring (can be rest based on 'dmin' and 'rmin')
        rmin : float [0.0] (nm)
            Radius of the *inner* circle onto which each molecule's
            *internal* (mint) atom is placed (can be reset based on 'nmols' and 'dmin')
        mols_inp : list[MoleculeSet]
            List of *minimal* molecular sets of *distinct* template molecules (input)
        mols_out : list[MoleculeSet]
            The *final* list of the generated molecular sets (output)
        frcs : list[float]
            List of fractions for *different* molecules
        fill : str ["rings0"],
            The type of *filling* of the spherical surface with **Ring** objects:

            "rings0" (default) places :math:`N_{ring0} = int(\pi r_{min} / d_{min}) + 1`
            rings symmetrically w.r.t. the equator (the equator itself won't
            be populated if the number of altitudes, i.e. the rings created,
            is even for the given parameters),

            "rings" (if specified) relieves the symmetry constraint with
            :math:`N_{ring} = (int(2 \pi r_{min} / d_{min}) + 1)/2` and
            can result in one extra ring on the sphere (for some parameter
            combinations).

        Returns
        -------
        None
            Note that ``mols_out = self.mols_out'' being populated.
        """

        # check and reset molecule sets if necessary
        if isinstance(mols_inp, list):
            self.mols_inp = mols_inp
        elif isinstance(self.mols_inp, list):
            mols_inp = self.mols_inp
        else:
            raise ValueError(
                "ERROR: Incorrect input containerfor template molecules (not a list)!"
            )

        if isinstance(mols_out, list):
            self.mols_out = mols_out
        elif isinstance(self.mols_out, list):
            mols_out = self.mols_out
        else:
            raise ValueError(
                "ERROR: Incorrect output container"
                "for molecules to be generated (not a list)!"
            )

        if isinstance(frcl, list):
            self.frcs = frcl
        elif isinstance(self.frcs, list):
            frcl = self.frcs
        # else:
        #     raise ValueError(
        #         "ERROR: Incorrect input"
        #         "for molecule fractions (not a list)!"
        #     )

        is_rings0 = fill == "rings0"
        # use the initial values of self in case the input is irrelevant
        # and then amend if necessary

        if self.ilayer == 0:
            if isinstance(rmin,float):
                if rmin < TINY:
                    rmin = self.lradii[0]
                else:
                    self.lradii[0] = rmin
            elif isinstance(rmin,list):
                self.rints = rmin
                rmin = self.rints[0]
                self.lradii[0] = rmin
            else:
                logger.error("(0): Rmin not float nor list - FULL STOP!!!")
                sys.exit(1)
            if nlring < 1:
                nlring = self.lnring[0]
            else:
                self.lnring[0] = nlring
            self.nmols = 0

        if len(self.dmins) > 1:
            self.dmin = self.dmins[self.ilayer]
        if len(self.rints) > 1:
            self.rint = self.rints[self.ilayer]
            rmin = self.rint

        TwoPiOverDmin =  TwoPi / self.dmin
        if nlring < 2 and (rmin - self.dmin) > TINY:
            # nring0 = nlring
            nlring = int(TINY + TwoPiOverDmin * rmin)
            # print(f"{self.__class__.__name__}.makeNew(WARN): "
            #       f"Number of molecules on 'equator' lring = "
            #       f"{nring0} -> {nlring} based on Rmin = {rmin}")
            # f"{self.lnring} -> {nlring}; Rmin -> {rmin} (adjusted)")
        if nlring < 10:
            logger.error(
                f"Requested number of molecules on 'equator' {nlring} < 10 "
                f"(unsupported) - FULL STOP!!!"
            )
            sys.exit(1)
        elif (self.dmin - rmin) > TINY:
            rmin0 = rmin
            rmin = float(nlring) * self.dmin / TwoPi
            logger.warning(
                f"Internal radius of layer {self.ilayer} Rmin = "
                f"{rmin0} -> {rmin} based on lring = {nlring}"
            )

        if is_rings0:
            # AB: odl style:
            nturns = int(nlring / 2) + 1
            # if mturns % 2 < TINY: mturns += 1  # ensure nturns is odd
        else:
            # AB: new style
            nturns = nlring

        if self.ilayer > 0:
            if self.ilayer >= self.getLayersN():
                logger.info(
                    f"Ball is complete with {self.ilayer} =?= "
                    f"{self.getLayersN()} (monolayers)"
                )
                return
            self.lnmols.append(nlring)
            self.lnring.append(nlring)
            self.lturns.append(nturns)
            self.lradii.append(rmin)
        else:
            self.lnmols[0] = nlring
            self.lnring[0] = nlring
            self.lturns[0] = nturns
            self.lradii[0] = rmin

        logger.info(
            f"Number of molecules on 'equator':  lring = {nlring} <-> "
            f"Rmin = {rmin}"
        )
        logger.info(f"Number of rings (turns) in a ball: turns = {nturns}")
        logger.info(
            f"Number of (mono-)layers in a ball: layers = {self.ilayer} / "
            f"{self.getLayersN()}"
        )

        nmols = 0
        if is_rings0:
            # AB: old style
            # nturns = int(nlring / 2) + 1
            # if mturns % 2 < TINY: mturns += 1  # ensure nturns is odd
            dthet = Pi / float(nturns - 1)
            theta = -PiOver2
            for mt in range(nturns):
                rminc = rmin * cos(theta)
                mmols = 1 if rminc < TINY else int(TINY + TwoPiOverDmin * rminc)
                nmols += mmols
                theta += dthet
        else:
            # AB: new style
            # nturns = nlring
            dthet = Pi / float(nturns)
            theta = -PiOver2
            ins = True
            for _ in range(nturns + 1):
                if ins:
                    rminc = rmin * cos(theta)
                    mmols = 1 if rminc < TINY else int(TINY + TwoPiOverDmin * rminc)
                    nmols += mmols
                theta += dthet
                ins = not ins
        logger.info(f"Estimated molecule number = {nmols}")
        self.nmols += nmols
        self.lnmols[-1] = nmols

        mols_order = None
        mfracs = 0
        fracs = frcl
        if isinstance(frcl, list):
            lfrc = len(frcl)
            if lfrc > self.ilayer:
                if isinstance(frcl[self.ilayer], list):
                    fracs = frcl[self.ilayer]
            elif lfrc > 0:
                if isinstance(frcl[-1], list):
                    fracs = frcl[-1]
            mfracs = len(fracs)

        if mfracs > 0:
            mols_order = [-1 for m in range(nmols)]
            self.sortMolsInserts(mols_order=mols_order, frcs=fracs)

        # start from the bottom with just one molecule
        # and build up to the top symmetrically if possible

        # initial rotation angles (azimuth/altitude)
        alpha = 0.0
        theta = -90.0

        if is_rings0:
            dthet = 180.0 / float(nturns - 1)
            for k in range(nturns):
                zsorg = rmin * sin(theta * Degs2Rad)
                rminc = rmin * cos(theta * Degs2Rad)
                mmols = 1 if rminc < TINY else int(TINY + TwoPiOverDmin * rminc)
                logger.info(
                    f"Placing {k}-th ring of {mmols} mols at zorg = {zsorg}, "
                    f"theta = {theta}, rmin = {rminc}"
                )
                Ring(rint=rminc, dmin=self.dmin, ovec=Vec3(0.0, 0.0, zsorg)).makeNew(
                    alpha=alpha,
                    theta=theta,
                    nmols=mmols,
                    mols_inp=mols_inp,
                    mols_out=mols_out,
                    frcs=fracs,
                    is_flatxz=is_flatxz,
                    is_invert=is_invert,
                    # is_pinned=is_pinned,
                    mols_order=mols_order,
                )
                theta += dthet
        else:
            dthet = 180.0 / float(nturns)
            i = 0
            ins = True
            for k in range(nturns + 1):
                if ins:
                    zsorg = rmin * sin(theta * Degs2Rad)
                    rminc = rmin * cos(theta * Degs2Rad)
                    mmols = 1 if rminc < TINY else int(TINY + TwoPiOverDmin * rminc)
                    logger.info(
                        f"Placing {i}-th ring of {mmols} mols at zorg = {zsorg}, "
                        f"theta = {theta}, rmin = {rminc}"
                    )
                    Ring(
                        rint=rminc, dmin=self.dmin, ovec=Vec3(0.0, 0.0, zsorg)
                    ).makeNew(
                        alpha=alpha,
                        theta=theta,
                        nmols=mmols,
                        mols_inp=mols_inp,
                        mols_out=mols_out,
                        frcs=fracs,
                        is_flatxz=is_flatxz,
                        is_invert=is_invert,
                        # is_pinned=is_pinned,
                        mols_order=mols_order,
                    )
                    i += 1
                theta += dthet
                ins = not ins

        # add the outer layer in the case of vesicle
        if self.ilayer < self.getLayersN() - 1:
            self.ilayer += 1

            rblen = []  # 'bone' length(s) for input molecule(s)
            mmols = len(mols_inp)
            for m in range(mmols):
                rblen.append(norm(mols_inp[m][0].getBoneRvecIntToExt()))
                for n in range(len(mols_inp[m])):
                    mols_inp[m][n].revBoneOrder()
            rbmax = max(rblen)

            # # AB: adjustment for multicomponent vesicles (hard-coded for now)
            # dscl = 1.2 #1.25 #1.5
            # # AB: scaling dmin as a means to reduce the nmols mismatch between layers
            # self.dmin *= dscl
            # logger.info(
            #       f"Outer layer ({self.ilayer}) rmin -> {rmin} "
            #       f"+ {rbmax} + {self.dmin} * {dscl} = {rmin + rbmax + self.dmin}")
            #       #f"+ {rbmax} + {self.dmin} * {dscl} = {rmin + rbmax + self.dmin * dscl}")
            # rmin = rmin + rbmax + self.dmin #*dscl

            # AB: adjustments for multilayered vesicles
            # AB: scaling dmin to (possibly) reduce mismatch in nmols between layers
            if len(self.dmins) < 2:
                self.dmin *= self.getLayersScaleDmin()  # 1.2 #1.25 #1.5
            # AB: scaling the next layer radius to (possibly) compensate for dmin scaling
            rmin0 = rmin
            if len(self.rints) < 2:
                rmin = (rmin0 + rbmax + self.dmin) * self.getLayersScaleRadii()
                logger.info(
                    f"Outer layer ({self.ilayer}) rmin -> ({rmin0} + {rbmax} "
                    f"+ {self.dmin}) * {self.getLayersScaleRadii()} = {rmin}\n"
                )
            else:
                rmin = rmin0 + rbmax + self.dmins[0]
                logger.info(
                    f"Outer layer ({self.ilayer}) rmin -> {rmin0} + {rbmax}"
                    f" + {self.dmins[0]} = {rmin} -> {self.rints[self.ilayer]}\n"
                )

            self.makeRings(
                rmin, 0, mols_inp, mols_out, frcl, fill, is_flatxz, is_invert
            )  # , is_pinned

    # end of Ball.makeRings()

    def makeFibo(
        # TODO: refactor (use dict/tuples/lists?)
        self,
        rmin: float = 0.0,
        nmols: int = 0,
        mols_inp: list = None,
        mols_out: list = None,
        frcl: list = None,
        is_flatxz: bool = False,
        is_invert: bool = False,
        # is_pinned: bool = False,
        be_verbose: bool = False,
    ):
        # check and reset molecule sets if necessary
        if isinstance(mols_inp, list):
            self.mols_inp = mols_inp
        elif isinstance(self.mols_inp, list):
            mols_inp = self.mols_inp
        else:
            raise ValueError(
                "ERROR: Incorrect input containerfor template molecules (not a list)!"
            )

        if isinstance(mols_out, list):
            self.mols_out = mols_out
        elif isinstance(self.mols_out, list):
            mols_out = self.mols_out
        else:
            raise ValueError(
                "ERROR: Incorrect output container"
                "for molecules to be generated (not a list)!"
            )

        if isinstance(frcl, list):
            self.frcs = frcl
        elif isinstance(self.frcs, list):
            frcl = self.frcs
        # else:
        #     raise ValueError(
        #         "ERROR: Incorrect input"
        #         "for molecule fractions (not a list)!"
        #     )

        # use the initial values of self in case the input is irrelevant
        # if self.ilayer == 0:
        #     if rmin < TINY:
        #         rmin = self.lradii[0]
        #     else:
        #         self.lradii[0] = rmin
        #     self.nmols = 0

        if self.ilayer == 0:
            self.nmols = 0
            if isinstance(rmin,float):
                if rmin < TINY:
                    rmin = self.lradii[0]
                else:
                    self.lradii[0] = rmin
            elif isinstance(rmin,list):
                self.rints = rmin
                rmin = self.rints[0]
                self.lradii[0] = rmin
            else:
                logger.error("(0): Rmin not float nor list - FULL STOP!!!")
                sys.exit(1)

        if len(self.dmins) > 1:
            self.dmin = self.dmins[self.ilayer]
        if len(self.rints) > 1:
            self.rint = self.rints[self.ilayer]
            rmin = self.rint

        isnew = False
        if nmols < 2 and (rmin - self.dmin) > TINY:
            isnew = True
            nmols0 = nmols
            nmols = int(TINY + 3.04 * Pi * rmin**2 / self.dmin**2)
            logger.warning(
                f"Estimated number of molecules for 'ball' of Rmin = {rmin} : "
                f"{nmols0} -> {nmols}"
            )
        if nmols < 10:
            logger.error(
                f"Requested number of molecules for 'ball' {nmols} < 10 "
                f"(unsupported) - FULL STOP!!!"
            )
            sys.exit(1)
        elif (self.dmin - rmin) > TINY:
            rmin0 = rmin
            rmin = sqrt(self.dmin**2 * float(nmols) / (3.05 * Pi))
            logger.warning(
                f"Internal radius of layer {self.ilayer} Rmin = "
                f"{rmin0} -> {rmin} based on nmols = {nmols}"
            )
        if not isnew:
            logger.info(f"Requested number of molecules for 'ball' = {nmols}")

        if self.ilayer > 0:
            self.lnmols.append(nmols)
            self.lnring.append(nmols)
            self.lturns.append(1)
            self.lradii.append(rmin)
        else:
            # consider a whole spiral as one 'ring' = 'turn'
            self.lnmols[0] = nmols
            self.lnring[0] = nmols  # nlring
            self.lturns[0] = 1  # nturns
            self.lradii[0] = rmin
        self.nmols += nmols

        iRange = arange(0, nmols, dtype=float) + 0.5
        tRange = arccos(1 - 2.0 * iRange / float(nmols))
        aRange = Pi * (1 + sqrt(5)) * iRange
        # x,y,z  = cos(aRange) * sin(tRange), sin(aRange) * sin(tRange), cos(tRange)
        # xyz = np.vstack([x, y, z]).T

        mfracs = 0
        fracs = frcl
        # flatten the fractions list if necessary
        if isinstance(frcl, list):
            lfrc = len(frcl)
            if lfrc > self.ilayer:
                if isinstance(frcl[self.ilayer], list):
                    fracs = frcl[self.ilayer]
            elif lfrc > 0:
                if isinstance(frcl[-1], list):
                    fracs = frcl[-1]
            mfracs = len(fracs)
        mpick = len(mols_inp)

        # mols_order = None
        # if mfracs > 0:
        #     mols_order = [-1 for m in range(nmols)]
        #     self.sortMolsInserts(mols_order=mols_order, frcs=fracs)

        # Z-shift
        # vecz = array([0.0, 0.0, 0.0])
        # if isinstance(self.rvorg, Vec3):
        #     vecz = self.rvorg.arr3()

        natms = 0
        ntot = 0
        # dRange = []
        # mVecs  = []
        # sdmin2 = (1.25*self.dmin)**2

        # initial alignment of molecules
        self.alignMolsTo(
            (1.0, 0.0, 0.0), mols_inp, is_flatxz, is_invert
        )  # , be_verbose)
        rbmax = max(self.rblen)

        # generate the Fibonacci 'spiral'
        for imol in range(len(iRange)):
            theta = PiOver2 - tRange[imol]
            alpha = aRange[imol]

            sint = sin(theta)
            cost = cos(theta)
            cosa = cos(alpha)
            sina = sin(alpha)

            m = 0
            if mfracs > 1:
                # m = mols_order[ntot]
                # mols_order[ntot] = -m - 1
                # AB: random placement on a Fibo-spiral:
                frnd = random.random()
                while frnd > fracs[m]:
                    m += 1
            elif mpick > 1:
                m = imol % mpick
            ntot += 1

            # initial alignment of molecule
            self.alignMolTo(
                (cost, 0.0, sint), mols_inp[m][0], is_flatxz, is_invert
            )  # , be_verbose)

            mlast = len(mols_out[m].items)
            mols_out[m].addItem(
                Molecule(mindx=mlast, aname=mols_inp[m].name, atype="output")
            )

            # bone_int  # index of backbone interior atom
            # 38 'C12' for SDS (CHARMM-36)
            mint = mols_inp[m][0].getBoneInt()

            # bone_ext  # index of backbone exterior atom
            # 1 for 'S1' or 5 'C1'  for SDS (CHARMM-36)
            # mext = mols_inp[m][0].getBoneExt()

            x, y, z = (
                cos(aRange[imol]) * sin(tRange[imol]),
                sin(aRange[imol]) * sin(tRange[imol]),
                cos(tRange[imol]),
            )
            vec0 = array([x, y, z]) * rmin
            # vec0 = xyz[imol]*rmin
            # if imol > 0:
            #     #dVecs = mVecs-vec0
            #     for vecD in (mVecs-vec0):
            #         norm2 = vecD[0]*vecD[0] + vecD[1]*vecD[1] + vecD[2]*vecD[2]
            #         if norm2 < sdmin2:
            #             dRange.append(norm2)
            # mVecs.append(vec0)

            if mpick > 1:
                # AB: if more than one species, make sure
                # all head (mext) atoms are placed on the outer surface
                if not is_invert:
                    dr = rbmax - self.rblen[m]
                    vec0 += array([cosa * cost * dr, sina * cost * dr, sint * dr])

            # merely rotate about Z axis
            rotM = array(
                [[cosa, -sina, 0.0], [sina, cosa, 0.0], [0.0, 0.0, 1.0]]
            )

            matms = len(mols_inp[m][0].items)
            for i in range(matms):
                vec1 = (
                    mols_inp[m][0].items[i].rvec.arr3()
                    - mols_inp[m][0].items[mint].rvec.arr3()
                )
                vec2 = dot(rotM, vec1)
                # check the norm of the rotated vector for consistency
                diff = norm(vec1) - norm(vec2)
                if diff * diff > TINY:
                    logger.warning(
                        f"Vector difference upon rotation about Z: ({i}) = {diff}\n"
                    )
                # add new molecule to the output
                mols_out[m].items[mlast].addItem(
                    Atom(
                        aname=mols_inp[m][0].items[i].name,
                        atype=mols_inp[m][0].items[i].type,
                        aindx=natms,
                        arvec=Vec3(*(vec2 + vec0)),
                    )
                )
                # aindx=natms, arvec=list(vec2 + vec0)))
                natms += 1

        # izero = -1
        # if 0.0 in dRange:
        #     izero = dRange.index(0.0)
        # if izero > -1:
        #     logger.warning(f"\nFound {dRange[izero]} distance "
        #           f"for molecule pair {izero}!!!")
        # else:

        # minSep = min(dRange)
        # minIdx = dRange.index(minSep)
        # minSep = sqrt(minSep)
        # maxSep = max(dRange)
        # maxIdx = dRange.index(maxSep)
        # maxSep = sqrt(maxSep)
        # rmin1 = rmin  # * self.dmin / minSep
        # #self.rint = rmin1

        # logger.debug(f"\n({nmols}): "
        #       f"Rmin = {rmin:.5f} ~> {rmin1:.5f}\n"
        #       f"Distances = {minSep} ({minIdx}) ~ {maxSep} ({maxIdx})")

        # add the outer layer in the case of vesicle
        if self.ilayer < self.getLayersN() - 1:
            self.ilayer += 1

            rblen = []  # 'bone' length(s) for input molecule(s)
            mmols = len(mols_inp)
            for m in range(mmols):
                rblen.append(norm(mols_inp[m][0].getBoneRvecIntToExt()))
                for n in range(len(mols_inp[m])):
                    mols_inp[m][n].revBoneOrder()
            rbmax = max(rblen)

            # AB: adjustments for multilayered vesicles
            # AB: scaling dmin to (possibly) reduce mismatch in nmols between layers
            if len(self.dmins) < 2:
                self.dmin *= self.getLayersScaleDmin()  # 1.2 #1.25 #1.5
            # AB: scaling the next layer radius to (possibly) compensate for dmin scaling
            rmin0 = rmin
            if len(self.rints) < 2:
                rmin = (rmin0 + rbmax + self.dmin) * self.getLayersScaleRadii()
                logger.info(
                    f"Outer layer ({self.ilayer}) rmin -> ({rmin0} + {rbmax} "
                    f"+ {self.dmin}) * {self.getLayersScaleRadii()} = {rmin}\n"
                )
            else:
                rmin = rmin0 + rbmax + self.dmins[0]
                logger.info(
                    f"Outer layer ({self.ilayer}) rmin -> {rmin0} + {rbmax} "
                    f"+ {self.dmins[0]} = {rmin} -> {self.rints[self.ilayer]}\n"
                )

            # self.dmin *= self.getLayersScaleDmin()  # 1.2 #1.25 #1.5
            # # AB: scaling the next layer radius to (possibly) compensate for dmin scaling
            # rmin0 = rmin
            # rmin = (rmin0 + rbmax + self.dmin) * self.getLayersScaleRadii()
            # print(
            #     f"\n{self.__class__.__name__}.makeFibo(info): "
            #     f"Outer layer ({self.ilayer}) rmin -> ({rmin0} "
            #     f"+ {rbmax} + {self.dmin}) * {self.getLayersScaleRadii()} = {rmin}\n"
            # )

            self.makeFibo(
                rmin, 0, mols_inp, mols_out, frcl, is_flatxz, is_invert
            )  # , is_pinned

    # end of Ball.makeFibo()


# end of class Ball


class Rod(Ring):
    """
    Class **Rod(Ring)** - generates a set of molecules arranged in a 'rod' configuration (a.k.a. cylindrical micelle).

    Note
    ----
    As a derivative of the 'Ring' class, the 'Rod' class inherits the properties of the 'Ring'
    and extends it with extra features (so refer also to the 'Ring' class):

    Parameters
    ----------
    nturns : int
        Number of circular turns, i.e. stacked rings, making up the cylindrical body of a rod
    ntcaps : int
        Number of turns, i.e. stacked rings (with reducing radius), for the caps of a rod

    Note
    ----
    If ``ntcaps`` = 0 (or not specified), its value is determined automatically in
    `Rod.make()` method, based on ``self.nmols`` - the number of molecules fitting on each ring in the body.
    """

    def __init__(self, ntcaps: int = 0, nturns: int = 0, *args, **keys):
        self.ntcaps = ntcaps
        self.nturns = nturns
        super(Rod, self).__init__(*args, **keys)

    def __del__(self):
        super(Rod, self).__del__()

    def make(
        # TODO: refactor (use dict/tuples/lists?)
        self,
        rmin: float = 0.0,
        alpha: float = 0.0,
        theta: float = 0.0,
        nlring: int = 0,
        ntcaps: int = 0,
        nturns: int = 0,
        mols_inp: list = None,
        mols_out: list = None,
        frcl: list = None,
        is_flatxz: bool = False,
        is_invert: bool = False,
        # is_pinned: bool = False,
        be_verbose: bool = False,
    ):
        # check and reset molecule sets if necessary
        if isinstance(mols_inp, list):
            self.mols_inp = mols_inp
        elif isinstance(self.mols_inp, list):
            mols_inp = self.mols_inp
        else:
            raise ValueError(
                "ERROR: Incorrect input containerfor template molecules (not a list)!"
            )

        if isinstance(mols_out, list):
            self.mols_out = mols_out
        elif isinstance(self.mols_out, list):
            mols_out = self.mols_out
        else:
            raise ValueError(
                "ERROR: Incorrect output container"
                "for molecules to be generated (not a list)!"
            )

        if isinstance(frcl, list):
            self.frcl = frcl
        elif isinstance(self.frcl, list):
            frcl = self.frcl
        # else:
        #     raise ValueError(
        #         "ERROR: Incorrect input"
        #         "for molecule fractions (not a list)!"
        #     )
        # flatten the fractions list if necessary
        if isinstance(frcl, list) and len(frcl) > 0:
            if isinstance(frcl[0], list):
                frcl = frcl[0]

        # use the initial values of self in case the input is irrelevant
        if nlring < 10:
            if self.lnring < 10:
                logger.warning(
                    f"Max number of molecules per ring in a rod {nlring} too "
                    "small - reset to 10"
                )
                self.lnring = 10
            nlring = self.lnring
        else:
            self.lnring = nlring

        if ntcaps < 1:  # ntcaps = self.ntcaps
            if self.ntcaps < 1:
                ntcaps = int(nlring / 2) + 1
                if float(ntcaps) % 2.0 < TINY:
                    # ensure ntcaps is odd
                    ntcaps += 1
                logger.warning(
                    f"Number of turns per cap in a rod {self.ntcaps} too small"
                    f" - reset to {ntcaps}"
                )
                self.ntcaps = ntcaps
            else:
                ntcaps = self.ntcaps
        else:
            self.ntcaps = ntcaps

        if nturns < 1:
            if self.nturns < 1:
                logger.warning(
                    f"Number of rings in a rod {nturns} too small - reset to 1"
                )
                self.nturns = 1
            nturns = self.nturns
        else:
            self.nturns = nturns

        if rmin < TINY:
            rmin = self.rint

        # add the outer layer in the case of vesicle
        # TODO: add a double layer option like for vesicles above
        # if self.isdouble:
        #    print(f"{self.__class__.__name__}.make(outer): rmin = {rmin} "
        #          f"+ {norm(mols_inp[ipick][0].getBoneRvecIntToExt().arr3())} + {self.dmin}")
        #    ....

        # start from the bottom with just one molecule
        # and build up to the top symmetrically if possible

        TwoPiOverDmin =  TwoPi / self.dmin

        # create a bottom semi-sphere cap
        # initial rotation angles (azimuth/altitude)
        alpha = 0.0
        theta = -90.0
        dthet = 180.0 / float(ntcaps - 1)
        zorg0 = -self.dmin * (-0.5 + float(nturns) / 2.0)
        zsorg = zorg0 - rmin
        rminc = 0.0
        mmols = 1
        for i in range(int((ntcaps - 1) / 2)):  # -1):
            logger.info(
                f"(cap1): Placing {i}-th ring of {mmols} mols at zorg = {zsorg}, "
                f"theta = {theta}, rmin = {rminc}"
            )
            dzorg = rmin * sin((theta + dthet) * Degs2Rad)
            Ring(rint=rminc, dmin=self.dmin, ovec=Vec3(0.0, 0.0, zsorg)).make(
                alpha=alpha,
                theta=theta,
                nmols=mmols,
                mols_inp=mols_inp,
                mols_out=mols_out,
                frcs=frcl,
                is_flatxz=is_flatxz,
                is_invert=is_invert,
            )
            theta += dthet
            zsorg = zorg0 + dzorg  # zorg0 + rmin * sin(theta * Degs2Rad)
            rminc = rmin * cos(theta * Degs2Rad)
            mmols = 1 if rminc < TINY else int(TINY + TwoPiOverDmin * rminc)

        # create a cylinder in the middle
        for i in range(nturns):  # -1):
            logger.info(
                f"(tube): Placing {i}-th ring of {nlring} mols at zorg = {zsorg}, "
                f"theta = {theta}, rmin = {rmin}"
            )
            Ring(rint=rmin, dmin=self.dmin, ovec=Vec3(0.0, 0.0, zsorg)).make(
                alpha=alpha,
                theta=theta,
                nmols=nlring,
                mols_inp=mols_inp,
                mols_out=mols_out,
                frcs=frcl,
                is_flatxz=is_flatxz,
                is_invert=is_invert,
                # is_pinned=is_pinned,
            )  # , dzmove=self.dmin)
            zsorg = zsorg + self.dmin

        # create a top semi-sphere cap
        alpha = 0.0
        theta += dthet
        zorg0 = self.dmin * (-0.5 + float(nturns) / 2.0)
        zsorg = zorg0 + rmin * sin(theta * Degs2Rad)
        rminc = rmin * cos(theta * Degs2Rad)
        mmols = 1 if rminc < TINY else int(TINY + TwoPiOverDmin * rminc)
        for i in range(int((ntcaps - 1) / 2)):  # -1):
            logger.info(
                f"(cap2): Placing {i}-th ring of {mmols} mols at zorg = {zsorg}, "
                f"theta = {theta}, rmin = {rminc}"
            )
            dzorg = rmin * sin((theta + dthet) * Degs2Rad)
            Ring(rint=rminc, dmin=self.dmin, ovec=Vec3(0.0, 0.0, zsorg)).make(
                alpha=alpha,
                theta=theta,
                nmols=mmols,
                mols_inp=mols_inp,
                mols_out=mols_out,
                frcs=frcl,
                is_flatxz=is_flatxz,
                is_invert=is_invert,
                # is_pinned=is_pinned,
            )  # , dzmove=dzorg)
            theta += dthet
            zsorg = zorg0 + dzorg  # rmin * sin(theta * Degs2Rad)
            rminc = rmin * cos(theta * Degs2Rad)
            mmols = 1 if rminc < TINY else int(TINY + TwoPiOverDmin * rminc)

    # end of Rod.make()

    def makeNew(
        # TODO: refactor (use dict/tuples/lists?)
        self,
        rmin: float = 0.0,
        alpha: float = 0.0,
        theta: float = 0.0,
        nlring: int = 0,
        ntcaps: int = 0,
        nturns: int = 0,
        mols_inp: list = None,
        mols_out: list = None,
        frcl: list = None,
        is_flatxz: bool = False,
        is_invert: bool = False,
        # is_pinned: bool = False,
        be_verbose: bool = False,
    ):
        import time

        # check and reset molecule sets if necessary
        if isinstance(mols_inp, list):
            self.mols_inp = mols_inp
        elif isinstance(self.mols_inp, list):
            mols_inp = self.mols_inp
        else:
            raise ValueError(
                "ERROR: Incorrect input containerfor template molecules (not a list)!"
            )

        if isinstance(mols_out, list):
            self.mols_out = mols_out
        elif isinstance(self.mols_out, list):
            mols_out = self.mols_out
        else:
            raise ValueError(
                "ERROR: Incorrect output container"
                "for molecules to be generated (not a list)!"
            )

        if isinstance(frcl, list):
            self.frcl = frcl
        elif isinstance(self.frcl, list):
            frcl = self.frcl
        # else:
        #     raise ValueError(
        #         "ERROR: Incorrect input"
        #         "for molecule fractions (not a list)!"
        #     )
        # flatten the fractions list if necessary
        if isinstance(frcl, list) and len(frcl) > 0:
            if isinstance(frcl[0], list):
                frcl = frcl[0]

        # use the initial values of self in case the input is irrelevant
        if nlring < 10:
            if self.lnring < 10:
                logger.warning(
                    f"Max number of molecules per ring in a rod {nlring} too "
                    "small - reset to 10"
                )
                self.lnring = 10
            nlring = self.lnring
        else:
            self.lnring = nlring

        if ntcaps < 1:  # ntcaps = self.ntcaps
            if self.ntcaps < 1:
                ntcaps = int(nlring / 2) + 1
                if float(ntcaps) % 2.0 < TINY:
                    ntcaps += 1  # ensure ntcaps is odd
                logger.warning(
                    f"Number of turns per cap in a rod {self.ntcaps} too small"
                    f" - reset to {ntcaps}"
                )
                self.ntcaps = ntcaps
            else:
                ntcaps = self.ntcaps
        else:
            self.ntcaps = ntcaps

        if nturns < 1:
            if self.nturns < 1:
                logger.warning(
                    f"Number of rings in a rod {nturns} too small - reset to 1"
                )
                self.nturns = 1
            nturns = self.nturns
        else:
            self.nturns = nturns

        if rmin < TINY:
            rmin = self.rint

        # add the outer layer in the case of vesicle
        # TODO: add a double layer option like for vesicles above
        # if self.isdouble:
        #    print(f"{self.__class__.__name__}.makeNew(outer): rmin = {rmin} "
        #          f"+ {norm(mols_inp[ipick][0].getBoneRvecIntToExt().arr3())} + {self.dmin}")
        #    ....

        # start from the bottom with just one molecule
        # and build up to the top symmetrically if possible

        ntcap = int((ntcaps - 1) / 2)
        TwoPiOverDmin = TwoPi / self.dmin

        mols_order = None
        fracs = frcl
        nmols = 0
        if isinstance(frcl, list):
            dthet = Pi / float(ntcaps-1)  # increment of theta between turns
            theta = PiOver2  # initial rotation angle of molecule bones from XY plane (altitude)

            for i in range(int((ntcaps-1)/2)):
                rmint = rmin * cos(theta)
                mmols = 1 if rmint < TINY else int(TINY + TwoPiOverDmin * rmint)
                nmols += mmols
                #print(f"Ring {i} : theta = {theta/Degs2Rad}, rmin = {rmint}, mmols = {mmols}, nmols = {nmols}")
                theta -= dthet

            ntmol = 2*nmols
            mmols = nturns * int(TINY + TwoPiOverDmin * rmin)
            nmols += nmols + mmols
            logger.info(
                f"Estimated molecule number in the rod = {nmols} = {ntmol} + {mmols}"
            )
            self.nmols += nmols
            # self.lnmols[-1] = nmols

            lfrc = len(frcl)
            # if lfrc > self.ilayer:
            #     if isinstance(frcl[self.ilayer], list):
            #         fracs = frcl[self.ilayer]
            # elif lfrc > 0:
            #     if isinstance(frcl[-1], list):
            #         fracs = frcl[-1]

        if len(fracs) > 0:
            mols_order = [ -1 for m in range(nmols)]
            self.sortMolsInserts(mols_order=mols_order, frcs=fracs)

        # create a bottom semi-sphere cap
        # initial rotation angles (azimuth/altitude)
        alpha = 0.0
        theta = -90.0
        dthet = 180.0 / float(ntcaps - 1)
        zorg0 = -self.dmin * (-0.5 + float(nturns) / 2.0)
        zsorg = zorg0 - rmin
        rminc = 0.0
        mmols = 1
        for i in range(ntcap):
            logger.info(
                f"(cap1): Placing {i}-th ring of {mmols} mols at zorg = {zsorg}, "
                f"theta = {theta}, rmin = {rminc}"
            )
            dzorg = rmin * sin((theta + dthet) * Degs2Rad)
            Ring(rint=rminc, dmin=self.dmin, ovec=Vec3(0.0, 0.0, zsorg)).makeNew(
                alpha=alpha,
                theta=theta,
                nmols=mmols,
                mols_inp=mols_inp,
                mols_out=mols_out,
                frcs=fracs,
                is_flatxz=is_flatxz,
                is_invert=is_invert,
                mols_order=mols_order,
            )
            theta += dthet
            zsorg = zorg0 + dzorg
            rminc = rmin * cos(theta * Degs2Rad)
            mmols = 1 if rminc < TINY else int(TINY + TwoPiOverDmin * rminc)

        mmols = int(TINY + TwoPiOverDmin * rmin)
        # create a cylinder in the middle
        for i in range(nturns):
            logger.info(
                f"(tube): Placing {i}-th ring of {nlring} mols at zorg = {zsorg}, "
                f"theta = {theta}, rmin = {rmin}"
            )
            Ring(rint=rmin, dmin=self.dmin, ovec=Vec3(0.0, 0.0, zsorg)).makeNew(
                alpha=alpha,
                theta=theta,
                nmols=mmols,
                mols_inp=mols_inp,
                mols_out=mols_out,
                frcs=fracs,
                is_flatxz=is_flatxz,
                is_invert=is_invert,
                mols_order=mols_order,
            )
            zsorg = zsorg + self.dmin

        # create a top semi-sphere cap
        alpha = 0.0
        theta += dthet
        zorg0 = self.dmin * (-0.5 + float(nturns) / 2.0)
        zsorg = zorg0 + rmin * sin(theta * Degs2Rad)
        rminc = rmin * cos(theta * Degs2Rad)
        mmols = 1 if rminc < TINY else int(TINY + TwoPiOverDmin * rminc)
        for i in range(ntcap):
            logger.info(
                f"(cap2): Placing {i}-th ring of {mmols} mols at zorg = {zsorg}, "
                f"theta = {theta}, rmin = {rminc}"
            )
            dzorg = rmin * sin((theta + dthet) * Degs2Rad)
            Ring(rint=rminc, dmin=self.dmin, ovec=Vec3(0.0, 0.0, zsorg)).makeNew(
                alpha=alpha,
                theta=theta,
                nmols=mmols,
                mols_inp=mols_inp,
                mols_out=mols_out,
                frcs=fracs,
                is_flatxz=is_flatxz,
                is_invert=is_invert,
                mols_order=mols_order,
            )
            theta += dthet
            zsorg = zorg0 + dzorg
            rminc = rmin * cos(theta * Degs2Rad)
            mmols = 1 if rminc < TINY else int(TINY + TwoPiOverDmin * rminc)

    # end of Rod.makeNew()


# end of class Rod
