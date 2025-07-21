
# Task 4: List Comprehensions with Sales Data

sales_data = [
    {'product': 'Laptop', 'q1': 150, 'q2': 180, 'q3': 160, 'q4': 200},
    {'product': 'Mouse', 'q1': 300, 'q2': 280, 'q3': 320, 'q4': 350},
    {'product': 'Keyboard', 'q1': 200, 'q2': 190, 'q3': 210, 'q4': 230},
    {'product': 'Monitor', 'q1': 80, 'q2': 95, 'q3': 85, 'q4': 110},
    {'product': 'Headphones', 'q1': 120, 'q2': 140, 'q3': 130, 'q4': 160}
]

# Task 4a
annual_sales = [
    {'product': product['product'],
     'total_sales': product['q1'] + product['q2'] + product['q3'] + product['q4']}
    for product in sales_data
]

print("Annual Sales Totals:")
for item in annual_sales:
    print(f"  {item['product']}: {item['total_sales']} units")

# Task 4b
high_performers = [product['product']
                   for product in annual_sales if product['total_sales'] > 600]

print("High-Performing Products (>600 units):")
for product in high_performers:
    print(f"  {product}")

# Task 4c
growth_analysis = [
    {
        'product': product['product'],
        'growth_percentage': ((product['q4'] - product['q1']) / product['q1']) * 100
    }
    for product in sales_data if product['q4'] > product['q1']
]

print("Products with Positive Growth (Q4 vs Q1):")
for item in growth_analysis:
    print(f"  {item['product']}: {item['growth_percentage']:.1f}% growth")
