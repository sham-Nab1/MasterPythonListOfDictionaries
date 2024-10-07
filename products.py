# List of product dictionaries
products = [
    {"ID": 1, "Name": "Laptop", "Category": "Electronics", "Price": 750, "Stock": 50, "Supplier Email": "supplier1@gmail.com"},
    {"ID": 2, "Name": "Desk Chair", "Category": "Furniture", "Price": 100, "Stock": 200, "Supplier Email": "supplier2@gmail.com"},
    {"ID": 3, "Name": "Smartwatch", "Category": "Electronics", "Price": 200, "Stock": 150, "Supplier Email": "supplier3@gmail.com"},
    {"ID": 4, "Name": "Notebook", "Category": "Stationery", "Price": 5, "Stock": 500, "Supplier Email": "supplier4@gmail.com"},
    {"ID": 5, "Name": "Running Shoes", "Category": "Apparel", "Price": 80, "Stock": 100, "Supplier Email": "supplier5@gmail.com"}
]

# Print product data
for product in products:
    print(f"ID: {product['ID']}, Name: {product['Name']}, Category: {product['Category']}, "
          f"Price: {product['Price']}, Stock: {product['Stock']}, Supplier Email: {product['Supplier Email']},")
