---
name: python_math_skill
description: Use this skill when the user wants basic math operations implemented or explained in Python, such as add, subtract, multiply, divide, power, factorial, gcd, or lcm. Do not use it for symbolic algebra, advanced numerical computing, or matrix-heavy tasks.
---

# Simple Math Python Skill

This skill provides a small, dependency-free Python math utility module for basic arithmetic and number theory helpers.

## Purpose

Use this skill when the user wants:
- a simple Python math utility library
- small reusable math helper functions
- clear examples of typed Python code
- safe handling of common edge cases such as division by zero

Do not use this skill when the user wants:
- symbolic algebra
- advanced numerical computing
- matrix operations
- NumPy, SciPy, or heavy scientific computing workflows

## Files

- `scripts/math_tools.py`: the main implementation file for basic math utilities

## Instructions

When using this skill:

1. Read `scripts/math_tools.py`.
2. Reuse the functions in that file when they fit the user's request.
3. Prefer simple, typed, dependency-free Python.
4. Keep implementations easy to read and easy to modify.
5. Include short examples when helpful.
6. Handle invalid input safely:
   - division by zero should raise a clear error
   - factorial should reject negative integers
   - factorial should reject non-integer input

## Output Guidelines

- Write production-usable Python with type hints.
- Add concise docstrings.
- Prefer clarity over cleverness.
- Avoid unnecessary dependencies.
- Keep examples minimal and practical.

## Example Use Cases

Use this skill for requests like:
- "Write a small Python math helper library"
- "Show me how to implement factorial in Python"
- "Create a utility module with gcd and lcm"
- "Help me build a beginner-friendly math module"

Do not use this skill for requests like:
- "Solve symbolic equations"
- "Build a matrix library"
- "Do numerical optimization with SciPy"