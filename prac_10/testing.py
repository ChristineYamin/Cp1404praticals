"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""


import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""

    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    test_car = Car(fuel=10)
    assert test_car.fuel == 10, "Car does not set fuel correctly with passed-in value"

    test_car = Car()
    assert test_car.fuel == 0, "Car does not set fuel correctly with default value"


def format_as_sentence(phrase):
    """
    Format a phrase as a sentence, starting with a capital and ending with a single full stop.
    """

    # Capitalize the first letter of the phrase
    formatted_phrase = phrase.capitalize()

    # Add a full stop at the end if there isn't one already
    if formatted_phrase[-1] != '.':
        formatted_phrase += '.'

    return formatted_phrase


run_tests()

doctest.testmod()


doctest.run_docstring_examples(format_as_sentence, globals())


