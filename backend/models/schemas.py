"""Pydantic request/response models."""
from typing import List, Optional, Any, Dict
from pydantic import BaseModel, Field, ConfigDict, field_validator


class ItineraryRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    circuit: str = Field(default="wildlife", min_length=1, max_length=40)
    days: int = Field(default=3, ge=1, le=10)
    style: str = Field(default="Comfort")
    interests: List[str] = Field(default_factory=list, max_length=12)

    @field_validator("style")
    @classmethod
    def valid_style(cls, value: str) -> str:
        if value not in {"Budget", "Comfort", "Premium"}:
            raise ValueError("style must be Budget, Comfort, or Premium")
        return value


class Phrase(BaseModel):
    category: str
    kannada: str
    roman: str
    meaning: str


class DialectResponse(BaseModel):
    key: str
    name: str
    description: str
    phrases: List[Phrase]


class Stop(BaseModel):
    time: str
    name: str
    description: str
    category: str
    cost: int = Field(ge=0)


class DaySchedule(BaseModel):
    day: int
    title: str
    stops: List[Stop]
    route_summary: Optional[Dict[str, Any]] = None
    transfer_from_previous_day: Optional[Dict[str, Any]] = None


class FoodIdea(BaseModel):
    name: str
    where: str
    description: str


class ItineraryResponse(BaseModel):
    circuit_id: str
    circuit_name: str
    region: str
    description: str
    days: int
    style: str
    interests: List[str]
    transit_recommendation: str
    estimated_total: int
    estimated_total_min: Optional[int] = None
    estimated_total_max: Optional[int] = None
    max_days: Optional[int] = None
    requested_days: Optional[int] = None
    daily_budget: int
    budget_breakdown: Optional[Dict[str, Any]] = None
    foods: List[FoodIdea]
    days_schedule: List[DaySchedule]
    notes: List[str]
    route_plan: Optional[Dict[str, Any]] = None
    generated_by: str = "curated-ground-data"
