from typing import Callable, Iterable, Tuple, List

Predicate = Callable[[int], bool]
Rule = Tuple[Predicate, str]


def is_multiple(k: int) -> Predicate:
    return lambda n: n % k == 0


def label_for(n: int, rules: Iterable[Rule]) -> str:
    parts: List[str] = [label for pred, label in rules if pred(n)]
    return "".join(parts) or str(n)


DEFAULT_RULES: List[Rule] = [
    (is_multiple(3), "Fizz"),
    (is_multiple(5), "Buzz"),
]


def fizzbuzz(n: int) -> str:
    return label_for(n, DEFAULT_RULES)
