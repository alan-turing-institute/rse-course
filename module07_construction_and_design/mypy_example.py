def hello(name: str, greet: str = "Hello", rep: int = 1) -> str:
    message: str = ""
    for _ in range(rep):
        message += f"{greet} {name}\n"
    return message


print(hello("Bob", 5))
