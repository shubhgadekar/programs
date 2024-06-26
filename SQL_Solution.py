import sqlite3
import csv

try:
    conn = sqlite3.connect('Data_Engineer_ETL_Assignment.db')
    cursor = conn.cursor()

    query = """SELECT c.customer_id as Customer, c.age as Age, i.item_name, SUM(o.quantity) AS Total_quantity
        FROM Customers c
        JOIN Sales s ON c.customer_id = s.customer_id
        JOIN Orders o ON s.sales_id = o.sales_id
        JOIN Items i ON o.item_id = i.item_id
        WHERE c.age >= 18 AND c.age <= 35
        GROUP BY c.customer_id, i.item_name
        HAVING total_quantity > 0"""

    cursor.execute(query)

    columns = [description[0] for description in cursor.description]

    with open('sqloutput.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(columns)
        
        results = cursor.fetchall()
        for row in results:
            writer.writerow(row)

except sqlite3.Error as e:
    print("SQLite error:", e)

except Exception as e:
    print("Error:", e)

finally:
    try:
        cursor.close()
    except:
        pass
    try:
        conn.close()
    except:
        pass
