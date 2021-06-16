"""Python module prints {hello + name} in dict object."""


def say_hello(name: str) -> str:
    """Say hello in str.

    Args:
        name (str): Can be any string value

    Returns:
        str: Hello + name
    """
    return '{"Hello": "' + name + '"}'


def str_to_dict(name: str) -> dict:
    """Convert str to dict.

    Args:
        name (str): Any string value that has key-value pairs

    Returns:
        dict: converts str to dict and returns dict object
    """
    return {"Hello": name}


if __name__ == "__main__":
    print(say_hello("Ryan"))
    print(str_to_dict("Ryan"))
