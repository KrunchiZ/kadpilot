"""Pydantic request/response models for the API."""
from typing import Literal
from pydantic import BaseModel, Field


class AskRequest(BaseModel):
	question: str = Field(..., min_length=1, max_length=500)
	top_k: int = Field(default=3, ge=1, le=17)
	llm_provider: Literal["gemini", "ollama"] = "gemini"


class CardUsed(BaseModel):
	card_title: str
	bank: str


class AskResponse(BaseModel):
	answer: str
	cards_used: list[CardUsed]
	provider: str
	top_k: int


class CardSummary(BaseModel):
	card_title: str
	bank: str


class CardsListResponse(BaseModel):
	cards: list[CardSummary]
	total: int
