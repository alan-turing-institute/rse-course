from greetings.greeter import greet


def test_greeter():
    inputs = [
        {"personal": "James", "family": "Hetherington"},
        {"personal": "James", "family": "Hetherington", "polite": True},
        {"personal": "James", "family": "Hetherington", "title": "Dr"},
    ]
    outputs = [  # codes like \x1b[32m are colours
        "\x1b[32mHey, \x1b[31mJames Hetherington.",
        "\x1b[32mHow do you do, \x1b[31mJames Hetherington.",
        "\x1b[32mHey, \x1b[34mDr \x1b[31mJames Hetherington.",
    ]
    for inp, out in zip(inputs, outputs):
        assert greet(**inp) == out
