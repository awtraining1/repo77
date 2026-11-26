"""Formatting functions for the customer usage report."""

from collections.abc import Sequence

from customer_app.models import CustomerUsage
from customer_app.pricing import calculate_monthly_charge


def build_customer_report(customers: Sequence[CustomerUsage]) -> list[str]:
    """Return consistently formatted customer rows sorted by customer ID."""
    report_rows: list[str] = []
    for customer in sorted(customers, key=lambda item: item.customer_id):
        charge = calculate_monthly_charge(customer)
        report_rows.append(
            f"{customer.customer_id} | {customer.customer_name} | "
            f"{customer.plan} | {customer.monthly_units:,} units | ${charge:,.2f}"
        )
    return report_rows
