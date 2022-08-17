from greetings.greeter import greet


def test_greeter():
    inputs = [
        {"personal": "James", "family": "Hetherington"},
        {"personal": "James", "family": "Hetherington", "polite": True},
        {"personal": "James", "family": "Hetherington", "title": "Dr"},
    ]
    outputs = [  # codes like \x1b[32m are colours
        "\x1b[40m\x1b[33mHey, \x1b[47m\x1b[1m\x1b[31mJames Hetherington",
        "\x1b[40m\x1b[33mHow do you do, \x1b[47m\x1b[1m\x1b[31mJames Hetherington",
        "\x1b[40m\x1b[33mHey, \x1b[44m\x1b[37mDr \x1b[47m\x1b[1m\x1b[31mJames Hetherington",
    ]
    for inp, out in zip(inputs, outputs):
        assert greet(**inp) == out
