"""Pricing rules for customer usage."""

from decimal import Decimal

from customer_app.models import CustomerUsage, Plan

UNIT_RATES: dict[Plan, Decimal] = {
    "standard": Decimal("0.12"),
    "premium": Decimal("0.09"),
    "enterprise": Decimal("0.07"),
}


def calculate_monthly_charge(customer: CustomerUsage) -> Decimal:
    """Calculate a customer's monthly charge using the configured plan rate."""
    unit_rate = UNIT_RATES[customer.plan]
    charge = Decimal(customer.monthly_units) * unit_rate
    return charge.quantize(Decimal("0.01"))
