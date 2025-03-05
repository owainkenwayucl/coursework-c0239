from chemistry import Element, Molecule, Reaction, session, add_items, create_tables

def tiny_db():
    oxygen = Element(symbol='O')
    hydrogen = Element(symbol='H')
    water = Molecule(name='water')
    oxygen_m = Molecule(name='oxygen')
    hydrogen_m = Molecule(name='hydrogen')

    water.add_atom(1, oxygen)
    water.add_atom(2, hydrogen)
    oxygen_m.add_atom(2, oxygen)
    hydrogen_m.add_atom(2, hydrogen)
    
    water_formation = Reaction()
    water_formation.add_participant(-2, hydrogen_m)
    water_formation.add_participant(-1, oxygen_m)
    water_formation.add_participant(2, water)

    water_breakup = Reaction()
    water_breakup.add_participant(2, hydrogen_m)
    water_breakup.add_participant(1, oxygen_m)
    water_breakup.add_participant(-2, water)
   
    return [water_formation, water_breakup]

def test_model_duplicated():
    with sqlite() as db:
        create_tables(db)
        s = session(db)
        add_items(tiny_db()+tiny_db(), s)
        s.commit()