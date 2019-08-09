"""
geometry_anamysis.py
This module contains the geometry analysis project.
"""

import numpy
import os
import sys

def open_xyz(filename):
    """
    Opens and processes a standard xyz file.
    Returns symbols and numpy array of coordinates.
    """
    xyz_file = numpy.genfromtxt(fname=filename, skip_header = 2, dtype = 'unicode')
    symbols = xyz_file[:,0]
    coordinates = xyz_file[:,1:]
    coordinates = coordinates.astype(numpy.float)

    return symbols, coordinates

def calculate_distance(atom1_coord, atom2_coord):
    """
    This function takes the coordinates of two atoms and calculates the distances between them.
    Inputs: atom1_coord, atom2_coord
    Return: distance
    """
    x_distance = atom1_coord[0] - atom2_coord[0]
    y_distance = atom1_coord[1] - atom2_coord[1]
    z_distance = atom1_coord[2] - atom2_coord[2]
    distance = numpy.sqrt(x_distance**2 + y_distance**2 + z_distance**2)
    return distance

def bond_check(distance,minimum=0,maximum=1.5):
    """
    This function accepts a single distance (one number) and checks to see if it is between
    the specified minimum (default: 0 angstroms) and maximum (default: 1.5 angstroms) values.
    """
    if distance > minimum and distance < maximum:
        return(True)
    else:
        return(False)

if __name__ == "__main__":
    print(F"Running {sys.argv[0]}")

    if len(sys.argv) <2:
        raise NameError("Incorrect input! Please specify an xyz file to be analyzed.")

    file_location = sys.argv[1]

    symbols, coordinates = open_xyz(file_location)
    num_atoms = len(symbols)
    for num1 in range(0, num_atoms):
        for num2 in range(0, num_atoms):
            if num1<num2:
                bond_length_12 = calculate_distance(coordinates[num1], coordinates[num2])
                if bond_check(bond_length_12) is True:
                    print(F'{symbols[num1]} to {symbols[num2]}: {bond_length_12:.3f}')
