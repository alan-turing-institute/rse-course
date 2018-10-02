#!/usr/bin/env python
from argparse import ArgumentParser
if __name__ == "__main__":
    parser = ArgumentParser(description = "Generate appropriate greetings")
    parser.add_argument('--title', '-t')
    parser.add_argument('--polite','-p', action="store_true")
    parser.add_argument('personal')
    parser.add_argument('family')
    arguments= parser.parse_args()
    
    greeting= "How do you do, " if arguments.polite else "Hey, "
    if arguments.title:
        greeting+=arguments.title+" "
    greeting+= arguments.personal + " " + arguments.family +"."
    print(greeting)
