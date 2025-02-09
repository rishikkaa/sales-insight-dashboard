import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to SQLite database (or create it if not exists)
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Create sales table
cursor.execute('''CREATE TABLE IF NOT EXISTS sales (
                    id INTEGER PRIMARY KEY,
                    product TEXT,
                    quantity INTEGER,
                    price REAL,
                    date TEXT)''')
conn.commit()

# Insert sample sales data
data = [
    ("Product A", 10, 15.99, "2024-02-01"),
    ("Product B", 5, 25.50, "2024-02-02"),
    ("Product A", 7, 15.99, "2024-02-03"),
    ("Product C", 8, 10.99, "2024-02-04"),
    ("Product B", 3, 25.50, "2024-02-05")
]
cursor.executemany("INSERT INTO sales (product, quantity, price, date) VALUES (?, ?, ?, ?)", data)
conn.commit()

# Fetch sales data
df = pd.read_sql("SELECT product, SUM(quantity) as total_quantity FROM sales GROUP BY product", conn)
print(df)

# Plot sales data
df.plot(kind='bar', x='product', y='total_quantity', legend=False, color='skyblue')
plt.title("Total Sales per Product")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.show()

# Close connection
conn.close()
