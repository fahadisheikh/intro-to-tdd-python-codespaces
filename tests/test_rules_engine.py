from fizzbuzz import fizzbuzz, label_for, is_multiple, DEFAULT_RULES

def test_passthrough_when_no_rules_match():
    assert label_for(1, []) == "1"

def test_default_rules_keep_classic_behavior():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"

BazzRules = [*DEFAULT_RULES, (is_multiple(7), "Bazz")]

def test_extend_with_bazz_rule():
    assert label_for(7, BazzRules) == "Bazz"
    assert label_for(21, BazzRules) == "FizzBazz"
