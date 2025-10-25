from src.fizzbuzz.fizzbuzz import fizzbuzz

def test_when_3_then_FIZZ():
    result = fizzbuzz(3)
    assert result == "FIZZ"