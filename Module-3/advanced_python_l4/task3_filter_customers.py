
# Task 3: Filter Function with Customer Data

customers = [
    {'name': 'Alice Johnson', 'total_spent': 1250, 'orders': 8, 'vip_member': True},
    {'name': 'Bob Smith', 'total_spent': 750, 'orders': 12, 'vip_member': False},
    {'name': 'Carol Davis', 'total_spent': 2100, 'orders': 15, 'vip_member': True},
    {'name': 'David Wilson', 'total_spent': 450, 'orders': 3, 'vip_member': False},
    {'name': 'Emma Brown', 'total_spent': 980, 'orders': 7, 'vip_member': False},
    {'name': 'Frank Miller', 'total_spent': 1800, 'orders': 20, 'vip_member': True}
]

premium_customers = list(filter(lambda c: (c['total_spent'] >= 1000 and c['orders'] >= 5) or c['vip_member'], customers))

print("Premium Customers for Special Promotion:")
for customer in premium_customers:
    print(f"  {customer['name']} - Spent: ${customer['total_spent']}, Orders: {customer['orders']}")
