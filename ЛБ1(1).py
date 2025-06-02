sales = [
    {"продукт": "яблука", "кількість": 20, "ціна": 10},
    {"продукт": "банани", "кількість": 15, "ціна": 8},
    {"продукт": "груші", "кількість": 5, "ціна": 20},
    {"продукт": "яблука", "кількість": 30, "ціна": 10},
    {"продукт": "апельсини", "кількість": 10, "ціна": 15}
]

def calculate_revenue(sales_list):
    revenue_dict = {}
    for sale in sales_list:
        product = sale["продукт"]
        revenue = sale["кількість"] * sale["ціна"]
        revenue_dict[product] = revenue_dict.get(product, 0) + revenue
    return revenue_dict

total_revenue = calculate_revenue(sales)
print("Загальний дохід по продуктах:", total_revenue)
Add commentMore actions
high_revenue = [product for product, income in total_revenue.items() if income > 1000]
print("Продукти з доходом > 1000:", high_revenue)