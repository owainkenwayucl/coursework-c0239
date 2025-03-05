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

class FakeSaveBinary: # Pretend binary-style writing to a list
    # to make it easier to read at first.    
    def save(self, system, buffer):
        buffer.append(len(system.elements))
        for element in system.elements:
            buffer.append(element.symbol)
        
        buffer.append(len(system.molecules))
        for molecule in system.molecules:
            buffer.append(len(molecule.elements))
            for element, number in molecule.elements.items():
                buffer.append(element.id)
                buffer.append(number)
        
        buffer.append(len(system.reactions))
        for reaction in system.reactions:
            buffer.append(len(reaction.reactants))
            for reactant, stoich in reaction.reactants.items():
                buffer.append(reactant.id)
                buffer.append(stoich)
            buffer.append(len(reaction.products))
            for product, stoich in reaction.products.items():
                buffer.append(product.id)
                buffer.append(stoich)