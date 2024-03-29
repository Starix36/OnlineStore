import pandas as pd

# Load the data from the CSV file into a pandas DataFrame
data = pd.read_csv('orders.csv')

# Convert 'order_date' column to datetime format
data['order_date'] = pd.to_datetime(data['order_date'])

# Compute the total revenue generated by the online store for each month
data['order_month'] = data['order_date'].dt.to_period('M')
revenue_by_month = data.groupby('order_month')['product_price'].sum()

# Compute the total revenue generated by each product
revenue_by_product = data.groupby('product_name')['product_price'].sum()

# Compute the total revenue generated by each customer
revenue_by_customer = data.groupby('customer_id')['product_price'].sum()

# Identify the top 10 customers by revenue generated
top_10_customers = revenue_by_customer.nlargest(10)

# Display the results
print("Total revenue generated by the online store for each month:")
print(revenue_by_month)

print("\nTotal revenue generated by each product:")
print(revenue_by_product)

print("\nTotal revenue generated by each customer:")
print(revenue_by_customer)

print("\nTop 10 customers by revenue generated:")
print(top_10_customers)
