def greet(name: str = "world") -> str:
    return f"Hello, {name}!"

def main() -> None:
    # console script entry point
    import sys
    name = sys.argv[1] if len(sys.argv) > 1 else "world"
    print(greet(name))
