# coding: utf-8
# Copyright (c) Max-Planck-Institut für Eisenforschung GmbH - Computational Materials Design (CM) Department
# Distributed under the terms of "New BSD License", see the LICENSE file.

import numpy as np
import os
import subprocess

from pyiron_vasp.vasp.volumetric_data import VaspVolumetricData


__author__ = "Sudarsan Surendralal"
__copyright__ = (
    "Copyright 2021, Max-Planck-Institut für Eisenforschung GmbH - "
    "Computational Materials Design (CM) Department"
)
__version__ = "1.0"
__maintainer__ = "Sudarsan Surendralal"
__email__ = "surendralal@mpie.de"
__status__ = "production"
__date__ = "May 1, 2021"


class Bader:
    """
    Module to apply the Bader charge partitioning scheme to finished DFT jobs. This module is interfaced with the
    `Bader code`_ from the Greame Henkelmann group.

    .. _Bader code: http://theory.cm.utexas.edu/henkelman/code/bader
    """

    def __init__(self, structure, working_directory):
        """
        Initialize the Bader module

        Args:
            job (pyiron_atomistics.dft.job.generic.GenericDFTJob): A DFT job instance (finished/converged job)
        """
        self._working_directory = working_directory
        self._structure = structure

    def _create_cube_files(self):
        """
        Create CUBE format files of the total and valce charges to be used by the Bader program
        """
        cd_val, cd_total = get_valence_and_total_charge_density(
            working_directory=self._working_directory
        )
        cd_val.write_cube_file(
            filename=os.path.join(self._working_directory, "valence_charge.CUBE")
        )
        cd_total.write_cube_file(
            filename=os.path.join(self._working_directory, "total_charge.CUBE")
        )

    def compute_bader_charges(self, extra_arguments=None):
        """
        Run Bader analysis on the output from the DFT job

        Args:
            extra_arguments (str): Extra arguments to the Bader program

        Returns:
            tuple: Charges and volumes as numpy arrays

        """
        self._create_cube_files()
        error_code = call_bader(
            foldername=self._working_directory, extra_arguments=extra_arguments
        )
        if error_code > 0:
            self._remove_cube_files()
            raise ValueError("Invoking Bader charge analysis failed!")
        self._remove_cube_files()
        return self._parse_charge_vol()

    def _remove_cube_files(self):
        """
        Delete created CUBE files
        """
        os.remove(os.path.join(self._working_directory, "valence_charge.CUBE"))
        os.remove(os.path.join(self._working_directory, "total_charge.CUBE"))

    def _parse_charge_vol(self):
        """
        Parse Bader charges and volumes

        Returns:
            tuple: charges and volumes

        """
        filename = os.path.join(self._working_directory, "ACF.dat")
        return parse_charge_vol_file(structure=self._structure, filename=filename)


def call_bader(foldername, extra_arguments=None):
    """
    Call the Bader program inside a given folder

    Args:
        foldername (str): Folder path
        extra_arguments (str): Extra arguments to the Bader program

    Returns:
        int: Result from the subprocess call (>0 if an error occurs)

    """
    if extra_arguments is None:
        extra_arguments = ""
    cmd = "bader valence_charge.CUBE -ref total_charge.CUBE {0}".format(extra_arguments)
    return subprocess.call(cmd, shell=True, cwd=foldername)


def parse_charge_vol_file(structure, filename="ACF.dat"):
    """
    Parse charges and volumes from the output file

    Args:
        structure (pyiron_atomistics.atomistics.structure.atoms.Atoms): The snapshot to be analyzed
        filename (str): Filename of the output file

    Returns:
        tuple: charges and volumes

    """
    with open(filename, errors="ignore") as f:
        lines = f.readlines()
        charges = np.genfromtxt(lines[2:], max_rows=len(structure))[:, 4]
        volumes = np.genfromtxt(lines[2:], max_rows=len(structure))[:, 6]
    return charges, volumes


def get_valence_and_total_charge_density(working_directory):
    """
    Gives the valence and total charge densities

    Returns:
        tuple: The required charge densities
    """
    cd_core = VaspVolumetricData()
    cd_total = VaspVolumetricData()
    cd_val = VaspVolumetricData()
    if os.path.isfile(working_directory + "/AECCAR0"):
        cd_core.from_file(working_directory + "/AECCAR0")
        cd_val.from_file(working_directory + "/AECCAR2")
        cd_val.atoms = cd_val.atoms
        cd_total.total_data = cd_core.total_data + cd_val.total_data
        cd_total.atoms = cd_val.atoms
    return cd_val, cd_total
