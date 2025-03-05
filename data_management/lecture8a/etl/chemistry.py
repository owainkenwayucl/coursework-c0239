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
     
class System:
    def __init__(self):
        self.reactions=[]
    def add_reaction(self, reaction):
        self.reactions.append(reaction)
        
    def to_struct(self):
        return [x.to_struct() for x in self.reactions]

