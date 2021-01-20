
class Element:
    def __init__(self, symbol):
        self.symbol = symbol

    def __str__(self):
        return str(self.symbol)


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
