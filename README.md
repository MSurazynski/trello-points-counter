# trello-points-counter

A simple Python script that computes card point statistics for one Trello board.

It searches card titles for point values matching:

```regex
\[\d+\]
```

It computes:

- total points
- on-time points
- overdue points
- points per member

It also updates a configured Trello card with the computed stats.

## Project structure

```text
trello-points-counter/
├── app/
│   ├── config.py
│   └── main.py
├── Dockerfile
├── pyproject.toml
├── uv.lock
└── README.md
```

## Configuration

Create or update `app/config.py` with:

```python
API_KEY = "..."
API_TOKEN = "..."
BOARD_ID = "..."
ON_TIME_LIST = "..."
OVERDUE_LIST = "..."
STATS_LIST = "..."
STATS_CARD = "..."
```

## Run locally with uv

```bash
uv sync
uv run python app/main.py
```

## Run with Docker

Build the image:

```bash
docker build -t trello-points-counter .
```

Run the container:

```bash
docker run --rm trello-points-counter
```

If Docker requires root on your system, use `sudo`:

```bash
sudo docker build -t trello-points-counter .
sudo docker run --rm trello-points-counter
```

## Notes

- Dependencies are managed with `uv` using `pyproject.toml` and `uv.lock`.
- The application entry point is `app/main.py`.
- The Trello stats card is updated using the configured `STATS_CARD` value.

