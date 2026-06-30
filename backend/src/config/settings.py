"""Application settings — minimal config.
prompt_model.py handles env vars and API keys.
"""
import os
import logging
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
	level=logging.INFO,
	format="[%(asctime)s] | %(levelname)s | %(message)s",
	datefmt="%m/%d/%y %H:%M:%S",
)

DEV = os.getenv("DEV") == "true"

DB_PATH = Path("../data/3_gold/credit_cards.db") if DEV else Path("/app/data/3_gold/credit_cards.db")

RATE_LIMITS_PATH = Path(__file__).parent.parent / "rag" / "rate_limits.txt"

logging.info("Database path: %s", DB_PATH.resolve())
logging.info("Rate limits path: %s", RATE_LIMITS_PATH.resolve())