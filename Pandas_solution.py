import sqlite3
import pandas as pd

try:
    conn = sqlite3.connect('Data_Engineer_ETL_Assignment.db')

    cursor = conn.cursor()

    query = '''
        SELECT c.customer_id as Customer, c.age as Age, i.item_name, SUM(o.quantity) AS Total_quantity
        FROM Customers c
        JOIN Sales s ON c.customer_id = s.customer_id
        JOIN Orders o ON s.sales_id = o.sales_id
        JOIN Items i ON o.item_id = i.item_id
        WHERE c.age >= 18 AND c.age <= 35
        GROUP BY c.customer_id, i.item_name
        HAVING total_quantity > 0
    '''

    df = pd.read_sql_query(query, conn)

    df.to_csv('customer_item_quantities.csv', sep=';', index=False)

except sqlite3.Error as e:
    print("SQLite error occurred:", e)

except pd.errors.ParserError as e:
    print("Pandas error occurred:", e)

except Exception as e:
    print("An error occurred:", e)

finally:
    try:
        conn.close()
    except NameError:
        pass
