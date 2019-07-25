#!/usr/bin/env python
"""This code performs Monte Carlo simulation on Lennard-Jones fluid."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from mpl_toolkits.mplot3d import Axes3D


def generate_initial_state(method, file_name=None, num_particles=None, box_length=None):
    """
    This function generate the initial state of a system

    Parameters
    ----------

    method : str
        What method to use when generating initial configurations. options are 'random' or 'file'
    box_length : float/int
        length of simulation box
    n_particles : int
        number of particles in the simulation box
    file_name : str
        string of file to load into the simulation box
    """

    if method is 'random':
        # randomly generate coordinates in the box
        coordinates = box_length * (0.5 - np.random.rand(num_particles, 3))

    elif method is 'file':
        # file obtained from NIST
        coordinates = np.loadtxt(file_name, skiprows=2, usecols=(1, 2, 3))

    return coordinates


def lennard_jones_potential(rij2):
    """
    This function computes the LJ energy between two particles

    Parameters
    ----------

    rij : float
        distance rij between two particles

    Output
    ------
    energy : float
        LJ potential energy
    """

    sig_by_r6 = np.power(1 / rij2, 3)  # rij: square of the distance
    sig_by_r12 = np.power(sig_by_r6, 2)
    energy = 4.0 * (sig_by_r12 - sig_by_r6)

    return energy


def calculate_tail_correction(box_length, cutoff, num_particles):
    """
    This function computes the standard tail energy correction for the LJ potential

    Parameters
    ----------
    box_length : float/int
        length of simulation box
    cutoff: float/int
        the cutoff for the tail energy truncation
    num_particles: int
        number of particles

    Output
    ------
    e_correction: float
        tail correction of energy
    """

    volume = box_length ** 3
    sig_by_cutoff3 = np.power(1 / cutoff, 3)
    sig_by_cutoff9 = np.power(sig_by_cutoff3, 3)
    e_correction = sig_by_cutoff9 - 3.0 * sig_by_cutoff3

    e_correction *= 8.0 / 9.0 * np.pi * num_particles / volume * num_particles

    return e_correction


def minimum_image_distance(r_i, r_j, box_length):
    """
    This function computes the minimum image distance between two particles

    Parameters
    ----------
    r_i: list/array
        the potitional vection of the particle i
    r_j: list/array
        the potitional vection of the particle j
    box_length : float/int
        length of simulation box 

    Outputs
    -------
    rij2: float
        the square of the shortest distance between the two particles and their images
    """

    rij = r_i - r_j
    rij = rij - box_length * np.round(rij / box_length)  # for each dimension
    rij2 = np.dot(rij, rij)

    return rij2


def get_particle_energy(coordinates, box_length, i_particle, cutoff2):
    """
    This function computes the energy of a particle with the rest of the system

    Parameters
    ----------
    coordinates: list/array
        coordinates of the particles
    box_length : float/int
        length of simulation box
    i_particle: int
        the index of selected particle 
    cutoff2: int/float
        the square of the cutoff

    Output
    -------
    e_total = the total energy of the selected particle
    """

    e_total = 0.0   # dimensionless
    i_position = coordinates[i_particle]
    particle_count = len(coordinates)

    for j_particle in range(particle_count):
        if i_particle != j_particle:
            j_position = coordinates[j_particle]
            rij2 = minimum_image_distance(i_position, j_position, box_length)

            if rij2 < cutoff2:  # cutoff2: square of the cutoff
                e_pair = lennard_jones_potential(rij2)
                e_total += e_pair
    return e_total


def calculate_total_pair_energy(coordinates, box_length, cutoff2):
    """
    This function calculate the sum of the pair energy.

    Parameters
    ----------
    coordinates: list/array
        coordinates of the particles
    box_length : float/int
        length of simulation box
    cutoff2: int/float
        the square of the cutoff

    Output
    -------
    e_total = the total energy of the particles pair
    """

    e_total = 0.0
    particle_count = len(coordinates)

    for i_particle in range(particle_count):
        for j_particle in range(i_particle):  # prevent double counting
            r_i = coordinates[i_particle]
            r_j = coordinates[j_particle]
            rij2 = minimum_image_distance(r_i, r_j, box_length)
            if rij2 < cutoff2:
                e_pair = lennard_jones_potential(rij2)
                e_total += e_pair
    return e_total


def accept_or_reject(delta_e, beta):
    """
    This function accepts or rejects a move given the energy difference and system temperature

    Parameters
    ----------
    delta_e : float
        energy difference between between states after a MC move

    beta : float
        inverse system temperature

    Output
    -------
    decision : bool
        Accept or rejects a MC move
    """

    if delta_e < 0.0:
        decision = True
    else:
        random_number = np.random.rand(1)
        p_acc = np.exp(-beta * delta_e)  # acceptance proability

        if random_number < p_acc:
            decision = True
        else:
            decision = False
    return decision


def adjust_displacement(n_trials, n_accept, max_displacement):
    """ 
    Adjust the displacement according to the acceptance ratio

    Parameters
    ----------
    n_trials: int
        number of trials
    n_accept: int
        number of the accepted trials
    max_displacement: int/float
        the maximum of the displacement

    Output
    ------
    n_trials: int
        number of trials
    n_accept: int
        number of the accepted trials
    max_displacement: float
        the maximum of the displacement
    """

    acc_rate = float(n_accept) / float(n_trials)
    if acc_rate < 0.38:
        max_displacement *= 0.8
    elif acc_rate > 0.42:
        max_displacement *= 1.2

    n_trials = 0
    n_accept = 0

    return max_displacement, n_trials, n_accept


def main():
    """The main function"""

    #-----------------#
    # Parameter setup #
    #-----------------#

    reduced_temperature = 0.9
    reduced_density = 0.9
    n_steps = 5000
    freq = 1000
    num_particles = 100
    simulation_cutoff = 3.0
    max_displacement = 0.1
    tune_displacement = True
    build_method = 'random'

    n_trials = 0
    n_accept = 0
    energy_array = np.zeros(n_steps)

    # Calculate box length for given parameter set

    box_length = np.cbrt(num_particles / reduced_density)
    beta = 1.0 / reduced_temperature
    simulation_cutoff2 = np.power(simulation_cutoff, 2)

    #-----------------------#
    # Initialize Simulation #
    #-----------------------#

    coordinates = generate_initial_state(
        build_method, num_particles=num_particles, box_length=box_length)

    total_pair_energy = calculate_total_pair_energy(
        coordinates, box_length, simulation_cutoff2)
    tail_correction = calculate_tail_correction(
        box_length, simulation_cutoff, num_particles)

    for i_step in range(n_steps):

        # update the number MC move attempts
        n_trials += 1

        # select a random particle
        i_particle = np.random.randint(num_particles)

        # generates a random displacement
        random_displacement = (
            2.0 * np.random.rand(3) - 1.0) * max_displacement

        # compute energy difference of moving a single particle
        current_energy = get_particle_energy(
            coordinates, box_length, i_particle, simulation_cutoff2)

        proposed_coordinates = coordinates.copy()
        proposed_coordinates[i_particle] += random_displacement
        proposed_coordinates -= box_length * \
            np.round(proposed_coordinates / box_length)

        proposed_energy = get_particle_energy(
            proposed_coordinates, box_length, i_particle, simulation_cutoff2)

        delta_e = proposed_energy - current_energy

        accept = accept_or_reject(delta_e, beta)

        if accept:
            total_pair_energy += delta_e
            n_accept += 1
            coordinates[i_particle] += random_displacement

        total_energy = (total_pair_energy + tail_correction) / num_particles

        energy_array[i_step] = total_energy

        if np.mod(i_step + 1, freq) == 0:
            print(i_step + 1, energy_array[i_step])

            if tune_displacement:
                max_displacement, n_trials, n_accept = adjust_displacement(
                    n_trials, n_accept, max_displacement)

    rc('font', **{
        'family': 'sans-serif',
        'sans-serif': ['DejaVu Sans'],
        'size': 10
    })
    # Set the font used for MathJax - more on this later
    rc('mathtext', **{'default': 'regular'})
    plt.rc('font', family='serif')

    plt.plot(energy_array[100:])
    plt.title('The potential energy as a function of Monte Carlo steps')
    plt.xlabel('Monte Carlo steps')
    plt.ylabel('Energy (reduced units)')
    if max(energy_array[100:]) >= 10000:
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    plt.grid(True)
    plt.show()

    plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot3D(coordinates[:, 0], coordinates[:, 1], coordinates[:, 2], 'o')
    plt.show()


if __name__ == '__main__':
    main()
