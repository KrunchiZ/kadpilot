"""Application settings — minimal config.
prompt_model.py handles env vars and API keys.
"""
import os
from pathlib import Path

DEV = os.getenv("DEV") == "true"

DB_PATH = Path("../../data/3_gold/credit_cards.db") if DEV else Path("/app/data/3_gold/credit_cards.db")

DEFAULT_LLM_PROVIDER = os.getenv("LLM_PROVIDER", "gemini")

RATE_LIMITS_PATH = Path(__file__).parent.parent / "rag" / "rate_limits.txt"
