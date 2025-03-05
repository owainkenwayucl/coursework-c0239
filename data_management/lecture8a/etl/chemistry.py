class Element:
    def __init__(self, symbol):
        self.symbol = symbol
   
class Molecule:
    def __init__(self):
        self.elements= {} # Map from element to number of that element in the molecule
        
    def add_element(self, element, number):
        self.elements[element] = number
    
    def to_struct(self):
        return {x.symbol: self.elements[x] for x in self.elements}
 
    def __str__(self):
        return str(self.to_struct()).replace("'",'"')

class Reaction:
    def __init__(self):
        self.reactants = { } # Map from reactants to stoichiometries
        self.products = { } # Map from products to stoichiometries
        
    def add_reactant(self, reactant, stoichiometry):
        self.reactants[reactant] = stoichiometry
        
    def add_product(self, product, stoichiometry):
        self.products[product] = stoichiometry
        
    def to_struct(self):
        return {
            'reactants' : [x.to_struct() for x in self.reactants],
            'products' : [x.to_struct() for x in self.products],
            'stoichiometries' : list(self.reactants.values())+
                                list(self.products.values())
        }

    def __str__(self):
        return str(self.to_struct()).replace("'",'"')

class System:
    def __init__(self):
        self.reactions=[]
    def add_reaction(self, reaction):
        self.reactions.append(reaction)
        
    def to_struct(self):
        return [x.to_struct() for x in self.reactions]

    def __str__(self):
        return str(self.to_struct()).replace("'",'"')

class DeSerialiseStructure:
    def __init__(self):
        self.elements = {}
        self.molecules = {}
        
    def add_element(self, candidate):
        if candidate not in self.elements:
            self.elements[candidate]=Element(candidate)
        return self.elements[candidate]
    
    def add_molecule(self, candidate):
        if tuple(candidate.items()) not in self.molecules:
            m = Molecule()
            for symbol, number in candidate.items():
                m.add_element(self.add_element(symbol), number)
            self.molecules[tuple(candidate.items())]=m
        return self.molecules[tuple(candidate.items())]
    
    def parse_system(self, json_struct):
        s = System()
        for reaction in json_struct:
            r = Reaction()
            stoichiometries = reaction['stoichiometries']
            for molecule in reaction['reactants']:
                r.add_reactant(self.add_molecule(molecule),
                               stoichiometries.pop(0))
            for molecule in reaction['products']:
                r.add_product(self.add_molecule(molecule),
                               stoichiometries.pop(0))
            s.add_reaction(r)
        return s