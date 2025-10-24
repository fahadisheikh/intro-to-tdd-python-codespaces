import pytest
from fizzbuzz import fizzbuzz

def test_returns_number_as_string():
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(2) == "2"

@pytest.mark.parametrize("n", [3, 6, 9])
def test_fizz_for_multiples_of_three(n):
    assert fizzbuzz(n) == "Fizz"

@pytest.mark.parametrize("n", [5, 10, 20])
def test_buzz_for_multiples_of_five(n):
    assert fizzbuzz(n) == "Buzz"

@pytest.mark.parametrize("n", [15, 30, 45])
def test_fizzbuzz_for_multiples_of_three_and_five(n):
    assert fizzbuzz(n) == "FizzBuzz"
