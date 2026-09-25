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


# Week 3 — My first API with FastAPI

I learned how the API world works. It is very interesting because, if you
think about it, almost everything digital works with APIs.

## What I learned

- **API** — functions that have a path that can be called by a client,
  in order to check different things: see health status, see holdings from a CSV,
  or check if a ticker is inside those holdings.

- **Params** — parameters that can live inside an API path, like
  `/ticker/{ticker}`. You just add a type hint (`ticker: str`) to the function
  and FastAPI extracts it from the URL automatically.

- **response_model** — a contract: you promise the endpoint returns a
  `list[Holding]` and FastAPI validates every response against it. I got a
  real HTTP 500 when I declared the wrong shape — the server would rather
  fail than lie to the client.

- **Test with APIs** — `TestClient` sends fake requests from inside pytest,
  without a browser or a port, and you assert on status codes and JSON.

## How to run

```bash
uv run uvicorn src.semana1_python.api:app --reload --port 8123
# then open http://127.0.0.1:8123/docs  (interactive docs, auto-generated)
```

## Vocabulary of the week

API, parameters, endpoint, paths, server, response model, status code
(the empty list answer is a 200, not a 404)


MIT License — datos 100% sintéticos, uso educativo.



