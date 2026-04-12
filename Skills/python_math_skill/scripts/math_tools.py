from __future__ import annotations

from math import gcd as _gcd


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return a divided by b.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def power(base: float, exponent: float) -> float:
    """Return base raised to the given exponent."""
    return base ** exponent


def factorial(n: int) -> int:
    """Return n factorial.

    Args:
        n: A non-negative integer.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.
    """
    if not isinstance(n, int):
        raise TypeError("factorial() only accepts integers.")
    if n < 0:
        raise ValueError("factorial() is undefined for negative integers.")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def gcd(a: int, b: int) -> int:
    """Return the greatest common divisor of two integers."""
    return _gcd(a, b)


def lcm(a: int, b: int) -> int:
    """Return the least common multiple of two integers."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // _gcd(a, b)


if __name__ == "__main__":
    print("add(2, 3) =", add(2, 3))
    print("subtract(10, 4) =", subtract(10, 4))
    print("multiply(6, 7) =", multiply(6, 7))
    print("divide(8, 2) =", divide(8, 2))
    print("power(2, 5) =", power(2, 5))
    print("factorial(5) =", factorial(5))
    print("gcd(24, 18) =", gcd(24, 18))
    print("lcm(12, 18) =", lcm(12, 18))