import numpy as np

class LJ:
    def __init__(self, epsilon, sigma):
        self.sigma = sigma
        self.epsilon = epsilon
    
    def get_energy(self, r):
        return 4 * self.epsilon * ((self.sigma / r) **12 - (self.sigma / r) ** 6)

class Buckingham:
    def __init__(self, rho, A, C):
        self.rho = rho
        self.A = A
        self.C = C

    def get_energy(self, r):
        return self.A * np.exp(-r / self.rho) - self.C / r ** 6

def potential_factory(potential_type, **kwargs):  # different types of potential take in different number of args
    if potential_type == 'LJ':
        return LJ(**kwargs)
    elif potential_type == 'Buckingham':
        return Buckingham(**kwargs)
    else:
        raise TypeError('Potential type not recognized.')

def main():
    potential = potential_factory('Buckingham', A=4.0, rho=10.0, C=10)
    print(potential.get_energy(r=10.0))

if __name__ == '__main__':
    main()
