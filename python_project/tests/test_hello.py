"""Test say_hello() and str_to_dict() functions."""


def test_say_hello():
    """Test Hello + name."""
    from python_project.main import say_hello

    assert '{"Hello": "Ryan"}' == say_hello("Ryan")


def test_str_to_dict():
    """Test str to dict conversion."""
    from python_project.main import str_to_dict

    test_dict = {"Hello": "Ryan"}
    test_hello = str_to_dict("Ryan")

    assert type(test_dict) == type(test_hello)
