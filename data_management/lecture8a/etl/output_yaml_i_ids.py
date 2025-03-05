from chemistry_id import Molecule, Element, Reaction, System

if __name__ == '__main__':
    h = Element('H',1)
    c = Element('C',16)
    o = Element('O',12)

    carbon_dioxide = Molecule(1)
    carbon_dioxide.add_element(c,1)
    carbon_dioxide.add_element(o,2)

    oxygen = Molecule(2)
    oxygen.add_element(o,2)

    hydrogen = Molecule(3)
    hydrogen.add_element(h,2)

    water = Molecule(4)
    water.add_element(h,2)
    water.add_element(o,1)

    glucose = Molecule(5)
    glucose.add_element(c,6)
    glucose.add_element(h,12)
    glucose.add_element(o,6)

    methane = Molecule(5)
    methane.add_element(c,1)
    methane.add_element(h,4)

    burning_glucose = Reaction()
    burning_glucose.add_reactant(glucose,1)
    burning_glucose.add_reactant(oxygen,6)
    burning_glucose.add_product(carbon_dioxide, 6)
    burning_glucose.add_product(water, 6)

    burning_hydrogen = Reaction()
    burning_glucose.add_reactant(hydrogen,2)
    burning_glucose.add_reactant(oxygen,1)    
    burning_glucose.add_product(water, 2)

    burning_methane = Reaction()
    burning_methane.add_reactant(methane,1)
    burning_methane.add_reactant(oxygen, 2)
    burning_methane.add_product(carbon_dioxide,1)
    burning_methane.add_product(water,2)

    reactions = System()
    reactions.add_reaction(burning_glucose)
    reactions.add_reaction(burning_hydrogen)
    reactions.add_reaction(burning_methane)

    print(yaml.dump(reactions.save()))