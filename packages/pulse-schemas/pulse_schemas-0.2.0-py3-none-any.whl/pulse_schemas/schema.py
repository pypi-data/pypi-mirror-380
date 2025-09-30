# schemas.py

from typing import List, Optional
from pydantic import BaseModel
from typing_extensions import Literal


# ------------------------
# Core Schemas
# ------------------------

class SimplifiedDemographics(BaseModel):
    age: Optional[int]
    biological_sex: Optional[
        Literal["male", "female", "other", "prefer_not_to_say"]
    ]


class Demographics(BaseModel):
    age: int
    biological_sex: str


class FoodBudget(BaseModel):
    amount: float             # e.g. 200.0
    currency: str             # e.g. "USD", "SGD", "EUR"
    timeframe: str            # e.g. "per week", "per month"


class ProfileSchema(BaseModel):
    user_id: str
    readiness_score: float

    demographics: Demographics
    food_budget: FoodBudget

    dietary_preferences: Optional[List[str]] = []
    allergens: Optional[List[str]] = []
    health_conditions: Optional[List[str]] = []
    goals: Optional[List[str]] = []


class SimplifiedProfileSchema(BaseModel):
    user_id: Optional[str]
    readiness_score: Optional[float]

    demographics: Optional[SimplifiedDemographics]
    dietary_preferences: List[
        Literal[
            "vegan", "vegetarian", "pescatarian",
            "keto", "paleo", "halal", "kosher", "none"
        ]
    ] = []
    allergens: List[
        Literal[
            "peanuts", "tree nuts", "milk", "eggs",
            "fish", "shellfish", "soy", "wheat",
            "sesame", "gluten", "dairy", "latex", "other allergen"
        ]
    ] = []
    health_conditions: List[
        Literal[
            "diabetes", "hypertension", "heart disease",
            "high blood pressure", "cardiovascular disease",
            "respiratory condition", "other health conditions"
        ]
    ] = []
    goals: List[Literal["lose weight", "build muscle", "improve cardio"]] = []

