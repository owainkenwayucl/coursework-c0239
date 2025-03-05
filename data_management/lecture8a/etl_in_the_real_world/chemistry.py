from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.orm import relationship, declarative_base

#engine = create_engine('sqlite:///molecules.db')
Base = declarative_base()

class AtomsPerMolecule(Base):
    __tablename__ = "_atoms_per_molecule_"
    symbol: Mapped[str] = mapped_column(ForeignKey("elements.symbol"), primary_key=True)
    name: Mapped[str] = mapped_column(ForeignKey("molecules.name"), primary_key=True)
    number: Mapped[int]
    molecule: Mapped["Molecule"] = relationship(back_populates="elements")
    element: Mapped["Element"] = relationship(back_populates="molecules")

class Element(Base):
    __tablename__ = "elements"
    symbol: Mapped[str] = mapped_column(primary_key=True)
    molecules: Mapped[List["AtomsPerMolecule"]] = relationship(back_populates="element")

class Participant(Base):
    __tablename__ = "participant"
    reaction_id: Mapped[int] = mapped_column(ForeignKey("reactions.id"), primary_key=True)
    name: Mapped[str] = mapped_column(ForeignKey("molecules.name"), primary_key=True)
    molecule : Mapped["Molecule"]= relationship(back_populates='reactions')
    reaction : Mapped["Reaction"]= relationship(back_populates = 'molecules')
    stoichiometry: Mapped[int]

class Molecule(Base):
    __tablename__ = "molecules"
    name: Mapped[str] = mapped_column(primary_key=True)
    elements: Mapped[List["AtomsPerMolecule"]] = relationship(back_populates="molecule")
    reactions: Mapped[List["Participant"]] = relationship(back_populates= "molecule")
    def add_atom(self, number, atom):
        result = AtomsPerMolecule(number = number)
        result.element = atom
        self.elements.append(result)
        return result 

class Reaction(Base):
    __tablename__ = "reactions"
    id : Mapped[int]= mapped_column(primary_key=True)
    molecules : Mapped[List[Participant]] = relationship(back_populates = "reaction")
    def add_participant(self, stoichiometry, molecule):
        result = Participant(stoichiometry=stoichiometry)
        result.molecule=molecule
        self.molecules.append(result)
        return result