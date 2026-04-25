FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /trello-points-counter

ENV UV_LINK_MODE=copy

COPY . .

RUN uv sync --locked --no-dev

CMD ["uv", "run", "python", "app/main.py"]
