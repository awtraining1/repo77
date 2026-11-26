"""Data models used by the customer reporting application."""

from dataclasses import dataclass
from typing import Literal

Plan = Literal["standard", "premium", "enterprise"]


@dataclass(frozen=True)
class CustomerUsage:
    """Represent one customer's plan and monthly usage."""

    customer_id: str
    customer_name: str
    plan: Plan
    monthly_units: int
