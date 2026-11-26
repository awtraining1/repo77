customers = [
	{
		"customer_id": "C1001",
		"customer_name": "Acme Manufacturing",
		"plan": "enterprise",
		"monthly_units": 12000,
	},
	{
		"customer_id": "C1002",
		"customer_name": "Contoso Health",
		"plan": "standard",
		"monthly_units": 3200,
	},
	{
		"customer_id": "C1003",
		"customer_name": "Northwind Retail",
		"plan": "premium",
		"monthly_units": 7500,
	},
]

for c in customers:
	x = c["monthly_units"]
	if c["plan"] == "enterprise":
		y = 0.07
	elif c["plan"] == "premium":
		y = 0.09
	else:
		y = 0.12
	z = round(x * y, 2)
	print(c["customer_id"], c["customer_name"], c["plan"], x, z)