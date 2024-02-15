import pandas as pd
import sqlite3
import csv

conn = sqlite3.connect('xyz_company.db')

query = """
    SELECT c.customer_id, c.age, i.item_id, SUM(s.quantity) AS total_quantity
    FROM Customer c
    JOIN Orders o ON c.customer_id = o.customer_id
    JOIN Sales s ON o.order_id = s.order_id
    JOIN Items i ON s.item_id = i.item_id
    WHERE c.age >= 18 AND c.age <= 35
    GROUP BY c.customer_id, i.item_id
    HAVING total_quantity > 0
"""

df = pd.read_sql_query(query, conn)
df.to_csv('customer_item_quantities.csv', sep=';', index=False)
conn.close()
