FROM python:3.14-slim

# Copy uv binary
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Copy dependencies
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen --no-install-project

# Copy source code
COPY src/ ./src/

EXPOSE 8000

ENTRYPOINT ["sh", "-c"]
CMD ["uv run uvicorn --app-dir src --host 0.0.0.0 --port ${PORT:-8000} app:app"]