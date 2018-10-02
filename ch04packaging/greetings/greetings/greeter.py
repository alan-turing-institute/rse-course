
def greet(personal, family, title="", polite=False):

    """ Generate a greeting string for a person.

    Parameters
    ----------
    personal: str
        A given name, such as Will or Jean-Luc
    family: str
        A family name, such as Riker or Picard
    title: str
        An optional title, such as Captain or Reverend
    polite: bool
        True for a formal greeting, False for informal.

    Returns
    -------
    string
        An appropriate greeting
    """

    greeting= "How do you do, " if polite else "Hey, "
    if title:
        greeting+=title+" "

    greeting+= personal + " " + family +"."
    return greeting
