import numpy as np
import MDAnalysis
import mdtraj as md
from abc import ABC, abstractmethod

class TrajectoryAdapter(ABC):
    
    @abstractmethod
    def radius_of_gyration(self):
        pass

    @abstractmethod
    def center_of_mass(self):
        pass


class MDTrajAdapter(TrajectoryAdapter):
    def __init__(self, filename):
        self.trajectory = md.load(filename)
        print('Using MDTraj.')

    @property
    def radius_of_gyration(self):
        return 10*md.compute_rg(self.trajectory)
    
    @property
    def center_of_mass(self):
        return 10*md.compute_center_of_mass(self.trajectory)

class MDAnalysisAdapter(TrajectoryAdapter):
    def __init__(self, filename):
        self.universe = MDAnalysis.Universe(filename)
        self.trajectory = self.universe.trajectory
        print('Using MDAnalysis.')

    @property
    def radius_of_gyration(self):
        rg_by_frame = np.empty(len(self.trajectory.trajectory))
        for ts in self.trajectory.trajectory:
            rg_by_frame[ts.frame] = self.trajectory.atoms.radius_of_gyration()
        return rg_by_frame

    @property
    def center_of_mass(self):
        rg_by_frame = np.ndarray(shape=(len(self.trajectory.trajectory), 3))
        for ts in self.trajectory.trajectory:
            rg_by_frame[ts.frame] = self.trajectory.atoms.center_of_mass(compound = 'segments')
        return rg_by_frame     

mdt = MDTrajAdapter('./protein.pdb')
print(mdt.radius_of_gyration)
print(mdt.center_of_mass)

mda = MDAnalysisAdapter('./protein.pdb')
print(mda.radius_of_gyration)
print(mda.center_of_mass)