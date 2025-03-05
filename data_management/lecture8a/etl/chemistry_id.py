class Element:
    def __init__(self, symbol, id):
        self.symbol = symbol
        self.id = id
        
class Molecule:
    def __init__(self, id):
        self.elements= {} # Map from element to number of that element in the molecule
        self.id=id
        
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
    
class System: # This will be our factory
    def __init__(self):
        self.reactions=[]
        self.elements=[]
        self.molecules=[]
        
    def add_element(self, symbol):
        new_element = Element(symbol, len(self.elements))
        self.elements.append(new_element)
        return new_element
    
    def add_molecule(self):
        new_molecule = Molecule(len(self.molecules))
        self.molecules.append(new_molecule)
        return new_molecule
    
    def add_reaction(self):
        new_reaction=Reaction()
        self.reactions.append(new_reaction)
        return new_reaction

    def save(self):
                    
        result = {
            'elements' : [element.symbol
                          for element in self.elements],
            'molecules' : {
                molecule.id:
                    {element.id: number
                          for element, number
                          in molecule.elements.items()}
                    for molecule in self.molecules},
            'reactions' : [{
                'reactants' : {
                        reactant.id : stoich
                        for reactant, stoich
                        in reaction.reactants.items()
                },
                'products' : {
                    product.id : stoich
                        for product, stoich
                        in reaction.products.items()
                    
                }}
                for reaction in self.reactions]
            }

        
        return result

    def __str__(self):
        return str(self.to_struct()).replace("'",'"')
