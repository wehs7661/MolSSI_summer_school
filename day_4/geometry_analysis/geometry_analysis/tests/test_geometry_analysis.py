"""
Unit and regression test for the geometry_analysis package.
"""

# Import package, test suite, and other packages as needed
import geometry_analysis
import pytest
import sys

import numpy as np

@pytest.fixture()    # not necessarily be put in front of all the cases
# This decorator is used to define things in common (in the folloing case, the 'water') in multiple testing cases
def water_molecule():
    name = 'water'
    symbols = ['H', 'O', 'H']
    coordinates = np.array([[2, 0, 0], [0, 0, 0], [-2, 0, 0]])
    water = geometry_analysis.Molecule(name, symbols, coordinates)

    return water

def test_create_failure():

    name = 25
    symbols = ["H", "O", "H"]
    coordinates = np.zeros([3,3])

    with pytest.raises(TypeError):
        water = geometry_analysis.Molecule(name, symbols, coordinates)

def test_molecule_set_coordaintes(water_molecule):
    """Test that bond linst is rebuilt when we reset coodinates."""

    num_bonds = len(water_molecule.bonds)

    assert num_bonds == 2

    new_coordinates = np.array([[10000, 0, 0], [0, 0, 0], [-2, 0, 0]])
    water_molecule.coodinates = new_coordinates
    new_num_bonds = len(water_molecule.bonds)
    
    assert new_num_bonds == 1
    assert np.array_equal(new_coordinates, water_molecule.coordinates)

def test_geometry_analysis_imported():
    """(To test if the module is imported) Sample test, will always pass so long as import statement worked"""
    assert "geometry_analysis" in sys.modules

def test_calculate_distance():
    """Test the calculate_distance function"""

    r1 = np.array([0, 0, -1])
    r2 = np.array([0, 1, 0])

    expected_distance = np.sqrt(2.)

    calculated_distance = geometry_analysis.calculate_distance(r1, r2)

    assert expected_distance == calculated_distance

def test_calculate_angle_90():
    """Test the caclulate_angle function"""

    rA = np.array([1, 0, 0])
    rB = np.array([0, 0, 0])
    rC = np.array([0, 1, 0])

    expected_angle = 90

    caclulagted_angle = geometry_analysis.calculate_angle(rA, rB, rC, degrees=True)

    assert expected_angle == caclulagted_angle
    
def test_calculate_angle_60():
    """Test another value of the caclulate_angle function"""

    rA = np.array([0, 0, -1])
    rB = np.array([0, 1, 0])
    rC = np.array([1, 0, 0])

    expected_angle = 60

    caclulagted_angle = geometry_analysis.calculate_angle(rA, rB, rC, degrees=True)

    assert np.isclose(expected_angle, caclulagted_angle)    # tolerance can be set by specifying rtol

@pytest.mark.parametrize("p1, p2, p3, expected_angle", [
    (np.array([1, 0, 0]), (np.array([0, 0, 0])),(np.array([0, 1, 0])), 90),
    (np.array([0, 0, -1]), (np.array([0, 1, 0])),(np.array([1, 0, 0])), 60),
])  # decorator for pytest

def test_calculate_angle(p1, p2, p3, expected_angle):

    calculated_angle = geometry_analysis.calculate_angle(p1, p2, p3, degrees = True)
    assert np.isclose(expected_angle, calculated_angle)