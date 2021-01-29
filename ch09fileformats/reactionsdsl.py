

class Element:
    def __init__(self, symbol):
        self.symbol = symbol

    def __str__(self):
        return str(self.symbol)

    def __mul__(self, other):
        """Let Molecule handle the multiplication"""
        return (self / 1) * other

    def __truediv__(self, number):
        """`Element / number => Molecule`"""
        res = Molecule()
        res.add_element(self, number)
        return res


class Molecule:
    def __init__(self):
        self.elements = {}  # Map from element to number of that element in the molecule

    def add_element(self, element, number):
        if not isinstance(element, Element):
            element = Element(element)
        self.elements[element] = number

    @staticmethod
    def as_subscript(number):
        if number == 1:
            return ""
        if number < 10:
            return "_" + str(number)
        return "_{" + str(number) + "}"

    def __str__(self):
        return "".join(
            [
                str(element) + Molecule.as_subscript(self.elements[element])
                for element in self.elements
            ]
        )

    def __mul__(self, other):
        """`Molecule * Element => Molecule`
        `Molecule * Molecule => Molecule`
        """
        if type(other) == Molecule:
            self.elements.update(other.elements)
        else:
            self.add_element(other, 1)
        return self

    def __rmul__(self, stoich):
        """`Number * Molecule => Side`"""
        res = Side()
        res.add(self, stoich)
        return res

    def __add__(self, other):
        """`Molecule + X => Side`"""
        if type(other) == Side:
            other.molecules[self] = 1
            return other
        res = Side()
        res.add(self, 1)
        res.add(other, 1)
        return res


class Side:
    def __init__(self):
        self.molecules = {}

    def add(self, reactant, stoichiometry):
        self.molecules[reactant] = stoichiometry

    @staticmethod
    def print_if_not_one(number):
        if number == 1:
            return ""
        else:
            return str(number)

    def __str__(self):
        return " + ".join(
            [
                Side.print_if_not_one(self.molecules[molecule]) + str(molecule)
                for molecule in self.molecules
            ]
        )

    def __add__(self, other):
        """Side + X => Side"""
        self.molecules.update(other.molecules)
        return self

    def __eq__(self, other):
        res = Reaction()
        res.reactants = self
        res.products = other
        current_system.add_reaction(res)  # Closure!
        return f"Added: '{res}'"


class Reaction:
    def __init__(self):
        self.reactants = Side()
        self.products = Side()

    def __str__(self):
        return str(self.reactants) + " \\rightarrow " + str(self.products)


class System:
    def __init__(self):
        self.reactions = []

    def add_reaction(self, reaction):
        self.reactions.append(reaction)

    def __str__(self):
        return "\\\\ \n".join(map(str, self.reactions))


current_system = System()
