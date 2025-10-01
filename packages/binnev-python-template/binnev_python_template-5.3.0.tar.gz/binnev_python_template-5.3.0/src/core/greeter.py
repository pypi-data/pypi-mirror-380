def greeting(name: str = "") -> str:
    """
    Greet a person.

    Args:
        name: the name of the person to greet

    Returns:
        A greeting string
    """
    name = name or "world"
    return f"Hello, {name}!"
