from argparse import ArgumentParser

from .greeter import greet  # Note relative import


def process():
    parser = ArgumentParser(description="Generate appropriate greetings")

    parser.add_argument("--title", "-t")
    parser.add_argument("--polite", "-p", action="store_true")
    parser.add_argument("personal")
    parser.add_argument("family")

    args = parser.parse_args()

    print(greet(args.personal, args.family, args.title, args.polite))


if __name__ == "__main__":
    process()
