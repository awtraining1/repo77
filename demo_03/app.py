"""Run the refactored customer usage report."""

from customer_app.models import CustomerUsage
from customer_app.reporting import build_customer_report

SAMPLE_CUSTOMERS: list[CustomerUsage] = [
    CustomerUsage("C1001", "Acme Manufacturing", "enterprise", 12000),
    CustomerUsage("C1002", "Contoso Health", "standard", 3200),
    CustomerUsage("C1003", "Northwind Retail", "premium", 7500),
]


def main() -> None:
    """Print the customer usage report."""
    print("CUSTOMER USAGE REPORT")
    print("-" * 72)
    print("\n".join(build_customer_report(SAMPLE_CUSTOMERS)))


if __name__ == "__main__":
    main()
