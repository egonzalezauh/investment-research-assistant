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


# Week 4 — Talking to an LLM from code

I learned how to call the Gemini API from Python, how to stream its answer,
and how to build a small CLI that summarizes a stock data file.

## What I learned

- **Wrapper** — `llm.py` is the only file that knows how to talk to Gemini.
  The rest of the project just calls `preguntar()` or `preguntar_stream()`,
  so changing the provider later means changing one file.

- **Streaming** — with `stream=True` the API sends many small events instead
  of one big answer. Only the `step.delta` events of type `text` carry words,
  so I yield those one by one, exactly like the CSV generator from Week 1.

- **Incomplete streams** — a stream can end without warning and leave the text
  cut in half. The last event, `interaction.completed`, is the proof that it
  finished. If it never arrives, the code raises an error.

- **Cost log** — every call adds one line to `cost.jsonl` (model, timestamp
  and tokens). I learned that "thinking" tokens are billed too: in one call,
  1,361 of 2,858 tokens were thoughts, not the visible answer.

- **CLI** — `argparse` reads what I type in the terminal, so the program can
  receive a file path as an argument instead of having it written in the code.

- **Check the model** — I recalculated the numbers from the summary and they
  matched the CSV, but an LLM sounds just as sure when it is wrong.

## How to run

```bash
# put GEMINI_API_KEY=your_key in a .env file first (never commit it)
uv run python -m semana1_python.cli data/precios_diarios.csv
```

The CLI only sends the first 20 rows to the model, because the full file
(91,680 rows) would cost millions of tokens.

## Vocabulary of the week

wrapper, stream, chunk, token, argument, events


MIT License — datos 100% sintéticos, uso educativo.
