import pytest
from fizzbuzz import fizzbuzz_function


def test_one():
    actual = fizzbuzz_function(1)
    expected = 1
    assert actual == expected


def test_three():
    actual = fizzbuzz_function(3)
    expected = "Fizz"
    assert actual == expected


def test_five():
    actual = fizzbuzz_function(5)
    expected = "Buzz"
    assert actual == expected


def test_three_not_buzz():
    actual = fizzbuzz_function(3)
    expected = "Buzz"
    assert actual != expected


def test_fifteen():
    actual = fizzbuzz_function(15)
    expected = "FizzBuzz"
    assert actual == expected


def test_twenty_two():
    assert fizzbuzz_function(22) == 22
