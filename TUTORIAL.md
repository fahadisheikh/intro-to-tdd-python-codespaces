# Intro to TDD — FizzBuzz (Python + pytest)

## Fizz Buzz Exercise:

Given an integer n, for every positive integer i <= n, the task is to print,

    "FizzBuzz" if i is divisible by 3 and 5,
    "Fizz" if i is divisible by 3,
    "Buzz" if i is divisible by 5

Output for first 15 numbers:
```
    1: 1
    2: 2
    3: FIZZ
    4: 4
    5: BUZZ
    6: FIZZ
    7: 7
    8: 8
    9: FIZZ
    10: BUZZ
    11: 11
    12: FIZZ
    13: 13
    14: 14
    15: FIZZBUZZ
```


## TDD in one minute
**Red–Green–Refactor:**

- **Red:** Write a *failing* test that states the desired behavior. The red failure proves the test can catch the absence of that behavior.
- **Green:** Write the *smallest possible* implementation to make that test pass. Don’t chase elegance yet—just reach green.
- **Refactor:** With tests green as a safety net, improve names, remove duplication, and clarify design *without changing behavior*.
This tutorial labels each change explicitly as **Step: Red**, **Step: Green**, or **Step: Refactor**, taking tiny, observable steps that keep feedback fast.


---

## Step 1 — Echo the number

### Step: Red — `test/fizzbuzz/test_fizzbuzz.py`
```python
from fizzbuzz.fizzbuzz import fizzbuzz

def test_returns_same_number_initially():
    assert fizzbuzz(1) == 1
    assert fizzbuzz(2) == 2
```

### Step: Green — `src/fizzbuzz/fizzbuzz.py`
```python
def fizzbuzz(n: int):
    return n
```

### Step: Refactor
*(none)*

---

## Step 2 — 3 → "FIZZ"

### Step: Red — `test/fizzbuzz/test_fizzbuzz.py` (append)
```python
def test_multiples_of_three_are_FIZZ():
    assert fizzbuzz(3) == "FIZZ"
    assert fizzbuzz(6) == "FIZZ"
```

### Step: Green — `src/fizzbuzz/fizzbuzz.py`
```python
def fizzbuzz(n: int):
    if n % 3 == 0:
        return "FIZZ"
    return n
```

### Step: Refactor — `test/fizzbuzz/test_fizzbuzz.py`
```python
def test_returns_same_number_initially():
    for n, expected in [(1, 1), (2, 2)]:
        assert fizzbuzz(n) == expected

def test_multiples_of_three_are_FIZZ():
    for n in (3, 6, 9):
        assert fizzbuzz(n) == "FIZZ"
```

---

## Step 3 — 5 → "BUZZ"

### Step: Red — `test/fizzbuzz/test_fizzbuzz.py` (append)
```python
def test_multiples_of_five_are_BUZZ():
    for n in (5, 10, 20):
        assert fizzbuzz(n) == "BUZZ"
```

### Step: Green — `src/fizzbuzz/fizzbuzz.py`
```python
def fizzbuzz(n: int):
    if n % 3 == 0:
        return "FIZZ"
    if n % 5 == 0:
        return "BUZZ"
    return n
```

### Step: Refactor — `test/fizzbuzz/test_fizzbuzz.py`
```python
import pytest
from fizzbuzz.fizzbuzz import fizzbuzz

@pytest.mark.parametrize("n, expected", [(1, 1), (2, 2)])
def test_returns_same_number_initially(n, expected):
    assert fizzbuzz(n) == expected

@pytest.mark.parametrize("n", [3, 6, 9])
def test_FIZZ(n):
    assert fizzbuzz(n) == "FIZZ"

@pytest.mark.parametrize("n", [5, 10, 20])
def test_BUZZ(n):
    assert fizzbuzz(n) == "BUZZ"
```

---

## Step 4 — 3 & 5 → "FIZZBUZZ" (with `parametrize`)

### Step: Red — `test/fizzbuzz/test_fizzbuzz.py` (append)
```python
import pytest

@pytest.mark.parametrize("n", [15, 30, 45])
def test_FIZZBUZZ(n):
    assert fizzbuzz(n) == "FIZZBUZZ"
```

### Step: Green — `src/fizzbuzz/fizzbuzz.py`
```python
def fizzbuzz(n: int):
    if n % 3 == 0 and n % 5 == 0:
        return "FIZZBUZZ"
    if n % 3 == 0:
        return "FIZZ"
    if n % 5 == 0:
        return "BUZZ"
    return n
```

### Step: Refactor
*(none)*

---

## Step 6 — Simple `main.py` (direct build, shows the type issue)

```python
from fizzbuzz.fizzbuzz import fizzbuzz

def main():
    for i in range(1, 6):
        line = str(i) + ": " + fizzbuzz(i)  
        print(line)

if __name__ == "__main__":
    main()
```


---

## Step 7 — Driver: `generate_sequence` returns an array; main prints it

### Step: Red — `test/driver/test_driver.py`
```python
from driver import generate_sequence

def test_generate_sequence_first_three():
    assert generate_sequence(1, 3) == ["1: 1", "2: 2", "3: FIZZ"]
```

### Step: Green — `src/fizzbuzz/fizzbuzz.py` and `src/driver/__init__.py`
`src/fizzbuzz/fizzbuzz.py`
```python
def fizzbuzz(n: int) -> str:
    if n % 3 == 0 and n % 5 == 0:
        return "FIZZBUZZ"
    if n % 3 == 0:
        return "FIZZ"
    if n % 5 == 0:
        return "BUZZ"
    return str(n)  # normalize
```

`src/driver/__init__.py`
```python
from fizzbuzz.fizzbuzz import fizzbuzz

def generate_sequence(start: int, end_inclusive: int):
    lines = []
    for i in range(start, end_inclusive + 1):
        lines.append(str(i) + ": " + fizzbuzz(i))
    return lines
```

### Step: Refactor — `src/main.py`
```python
from driver import generate_sequence

def main():
    # main stays simple; just print the array
    print(*generate_sequence(1, 100), sep="\n")

if __name__ == "__main__":
    main()
```

---