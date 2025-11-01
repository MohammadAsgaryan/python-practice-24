# Python Error Handling + Linter

This project demonstrates the difference between **bad** and **good** error handling in Python, and how using a **linter** such as `pylint` or `flake8` helps write cleaner and more professional code.

---

## ✅ What is included?

| File | Description |
|------|-------------|
| `bad_handling.py` | Wrong examples of exception handling (silent errors, wrong exception types, print instead of logging) |
| `good_handling.py` | Fixed and professional examples using logging and correct exception types |

---

## ✅ Why is this important?

Many beginners write code that hides errors or handles them incorrectly, making debugging harder.  
Linters help detect these mistakes automatically and improve code quality.

---

## ✅ Requirements

Install pylint (or flake8):

```bash
pip install pylint

## ✅ Run linter on the files

pylint bad_handling.py
pylint good_handling.py

You will notice:
✅ bad_handling.py gives many warnings
✅ good_handling.py passes with a much cleaner score

## ✅ What this project teaches

✔ Correct usage of try/except
✔ Avoiding empty except blocks
✔ Avoiding wrong exception types
✔ Using logging instead of print
✔ Cleaner and maintainable code
