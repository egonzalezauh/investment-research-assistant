# Week 1 — Python: generators, decorators, pytest

A small project to learn how to read large CSV files efficiently and how to
test code properly. It was a fun experience: very hard at the beginning, but
it became easy with practice.

## What I learned

- **Generators** — functions that use `yield` to deliver one row at a time
  instead of loading the whole file into memory. They only keep track of
  where they left off. Once you finish iterating a generator, it is
  exhausted and you have to start over with a new one.

- **Decorators** — a function that *wraps* another function. Calling the
  wrapped function runs the decorator logic first, then the original
  function, then the decorator's closing logic (for example, printing how
  long the call took). Useful for behavior you want to run before or after
  a function without touching its code.

- **Fixtures** — reusable setup code marked with `@pytest.fixture`. They
  save you from writing the same instructions over and over again in every
  test (here: creating a tiny temporary CSV with known data).

- **Tests** — functions whose names start with `test_`. Each one has an
  input, some steps, and validations made with `assert`. If an assertion
  is false, pytest marks the test as failed and shows the exact line.

## How to run

```bash
uv run pytest                                        # run all tests
uv run python src/semana1_python/main.py             # generator vs. list race
```

## Vocabulary of the week

row, header, wraps, exhausted, assertion, temporary directory


MIT License — proyecto de estudios personales.