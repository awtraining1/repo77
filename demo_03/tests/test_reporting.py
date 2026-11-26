from customer_app.models import CustomerUsage
from customer_app.reporting import build_customer_report


def test_report_is_sorted_and_formatted() -> None:
    customers = [
        CustomerUsage("C1002", "Contoso Health", "standard", 3200),
        CustomerUsage("C1001", "Acme Manufacturing", "enterprise", 12000),
    ]
    report = build_customer_report(customers)
    assert report == [
        "C1001 | Acme Manufacturing | enterprise | 12,000 units | $840.00",
        "C1002 | Contoso Health | standard | 3,200 units | $384.00",
    ]
