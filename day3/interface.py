from abc import ABC, abstractmethod 

class interface_sapmle(ABC):
    
    @abstractmethod
    def sample_method(self, variable1, variable2):
        pass

class implementation(interface_sample):
    def __init__(self):
        pass

    def sample_method(self):
        pass


imp = implementation()

