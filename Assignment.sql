CREATE TABLE IF NOT EXISTS Customer (
customer_id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
age INTEGER NOT NULL);
					
CREATE TABLE IF NOT EXISTS Sales (
sales_id INTEGER PRIMARY KEY,
customer_id INT NOT NULL,
FOREIGN KEY (customer_id) REFERENCES Customer(customer_id));
					
CREATE TABLE IF NOT EXISTS Items (
item_id INTEGER PRIMARY KEY,
item_name VARCHAR(255));

CREATE TABLE IF NOT EXISTS Orders (
order_id INTEGER PRIMARY KEY,
sales_id INTEGER NOT NULL ,
item_id INTEGER NOT NULL ,
quantity INTEGER,
FOREIGN KEY (sales_id) REFERENCES Sales(sales_id),
FOREIGN KEY (item_id) REFERENCES Items(item_id)
);

INSERT INTO customer (customer_id, name, age) VALUES (
('A', 30),
('B', 25),
('C', 35));

INSERT INTO sales (sales_id,customer_id) VALUES (
(1,1),
(2,2),
(3,2),
(4,3),
(5,3)
);

INSERT INTO orders (order_id, sales_id, item_id, quantity) VALUES (
(1,1,1,10),
(2,2,1,1),
(3,2,2,1),
(4,2,3,1),
(5,3,3,2)
);

INSERT INTO items (item_id,item_name) VALUES (
(1,"x"),
(2,"y"),
(3,"z")
);

SELECT c.customer_id as Customer, c.age as Age, i.item_name, SUM(o.quantity) AS Total_quantity
FROM Customer c
JOIN Sales s ON c.customer_id = s.customer_id
JOIN Orders o ON s.sales_id = o.sales_id
JOIN Items i ON o.item_id = i.item_id
WHERE c.age >= 18 AND c.age <= 35
GROUP BY c.customer_id, i.item_name
HAVING total_quantity > 0;
