import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
sales = pd.read_csv("sales.csv")

# Pivot table: Sales by Product, Region, Time
sales_pivot = pd.pivot_table(sales, values='Sales',
                             index=['Product', 'Region', 'Time'],
                             aggfunc='sum')
print(sales_pivot)

# Plot
sales_pivot.plot(kind='bar')
plt.show()

# Sales by Region and Product
sales_pivot_region_product = pd.pivot_table(sales, values='Sales',
                                            index=['Region', 'Product'],
                                            aggfunc='sum')
print(sales_pivot_region_product)

sales_pivot_region_product.plot(kind='bar', figsize=(10,6))
plt.title("Total Sales by Region and Product")
plt.xlabel("Region and Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# Sales by Time and Product
print(pd.pivot_table(sales, values='Sales',
                     index=['Time', 'Product'],
                     aggfunc='sum'))

# Pivot with Region as column
print(pd.pivot_table(sales, values='Sales',
                     index=['Product', 'Time'],
                     columns='Region',
                     aggfunc='sum'))
