class Molecule:
    def __init__(self, name, symbols, charge=0.0):
        # argument with a default value should always be the last ones.
        # arguement without a defulat value is called a positional argumenta
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("Name is not a string.")
        self.charge = charge
        self.symbols = symbols

    def __str__(self):
        return 'name: '+ self.name + '\ncharge: ' + str(self.charge) + '\nsymbols: ' + str(self.symbols)



def main():
    water = Molecule("water_molecule", 0.0, ["H", "O", "O"])
    print(water)
    print(water.__dict__)

    helium = Molecule(charge = 1.0, name = "helium", symbols = "He")
    print(helium)
    print(helium.__dict__)
    #hydrogen = Molecule(0.0, 0.0, ["H"])

if __name__ =='__main__':
    main()
