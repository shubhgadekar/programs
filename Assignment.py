import sqlite3
import pandas as pd

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Customer (
                    customer_id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL
                  )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Sales (
                    sales_id INTEGER PRIMARY KEY,
                    customer_id INT NOT NULL,
                    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
                    );''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Items (
                    item_id INTEGER PRIMARY KEY,
                    item_name VARCHAR(255)
                    );''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Orders (
                    order_id INTEGER PRIMARY KEY,
                    sales_id INTEGER NOT NULL,
                    item_id INTEGER NOT NULL,
                    quantity INTEGER,
                    FOREIGN KEY (sales_id) REFERENCES Sales(sales_id),
                    FOREIGN KEY (item_id) REFERENCES Items(item_id)
                    );''')

customers_data = [
    ('A', 30),
    ('B', 25),
    ('C', 35)
]
sales_data = [
    (1,1),
    (2,2),
    (3,2),
    (4,3),
    (5,3)
]
orders_data = [
    (1,1,1,10),
    (2,2,1,1),
    (3,2,2,1),
    (4,2,3,1),
    (5,3,3,2)
]
items_data = [
    (1,"x"),
    (2, "y"),
    (3, "z")
]

cursor.executemany('INSERT INTO customer (name, age) VALUES (?, ?)', customers_data)
cursor.executemany('INSERT INTO sales (sales_id,customer_id) VALUES (?, ?)', sales_data)
cursor.executemany('INSERT INTO orders (order_id, sales_id, item_id, quantity) VALUES (?, ?, ?, ?)', orders_data)
cursor.executemany('INSERT INTO items (item_id,item_name) VALUES (?, ?)', items_data)

conn.commit()

query = '''
    SELECT c.customer_id as Customer, c.age as Age, i.item_name, SUM(o.quantity) AS Total_quantity
    FROM Customer c
    JOIN Sales s ON c.customer_id = s.customer_id
    JOIN Orders o ON s.sales_id = o.sales_id
    JOIN Items i ON o.item_id = i.item_id
    WHERE c.age >= 18 AND c.age <= 35
    GROUP BY c.customer_id, i.item_name
    HAVING total_quantity > 0
'''

df = pd.read_sql_query(query, conn)

df.to_csv('customer_item_quantities.csv', sep=';', index=False)

# Close the connection
conn.close()
