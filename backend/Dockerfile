FROM python:3.14-slim

# Copy uv binary
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Copy dependencies
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen --no-install-project

# Download and cache all-MiniLM-L6-v2:
ENV HF_TOKEN=$HF_TOKEN
ENV SENTENCE_TRANSFORMERS_HOME=/app/.cache/sentence_transformers
RUN uv run python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')"

# Copy source code
COPY data/ ./data/
COPY sql/ ./sql/
COPY src/ ./src/

EXPOSE 8001

ENTRYPOINT ["uv", "run", "uvicorn"]
CMD ["--app-dir", "src", "--host", "0.0.0.0", "--port", "8001", "app:app"]
