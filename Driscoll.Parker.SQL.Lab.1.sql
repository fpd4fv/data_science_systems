#SElECT * FROM northwind.customers;
#1. Write a query to get product name and quantity/unit
Select product_name , quantity_per_unit From products;

#2. Write a query to get current product list (Product ID and name).
Select northwind.products.product_name , northwind.products.quantity_per_unit 
FROM northwind.products;

#3. write a query to get discontinued product list (Product ID and name)
SELECT northwind.products.product_name, northwind.products.id 
FROM northwind.products 
WHERE discontinued = '1';


#4. Write a query to get most expense and least expensive Product list (name and unit price). 
SELECT distinct northwind.products.product_name, northwind.products.id 
FROM northwind.products 
JOIN northwind.order_details 
ON northwind.products.id = northwind.order_details.product_id 
WHERE unit_price= (Select MAX(unit_price) 
FROM northwind.order_details) OR (Select MIN(unit_price) FROM northwind.order_details);
#???? this returns a list of 26 products not 2. Problem?

#5. Write a query to get Product list (id, name, unit price) where current products cost less than $20.
SELECT distinct northwind.products.product_name, northwind.products.id, order_details.unit_price 
FROM northwind.products 
JOIN order_details ON northwind.products.id = northwind.order_details.product_id 
WHERE northwind.order_details.unit_price <20;
 


#6 Write a query to get Product list (id, name, unit price) where products cost between $15 and $25.
SELECT distinct northwind.products.id, northwind.products.product_name, northwind.products.list_price FROM northwind.products JOIN order_details
ON northwind.products.id = northwind.order_details.product_id WHERE northwind.order_details.unit_price <25 AND northwind.order_details.unit_price > 15;
## change to select unit price


#7 Write a query to get Product list (name, unit price) of above average price.
SELECT distinct northwind.products.product_name, northwind.products.id , order_details.unit_price
FROM northwind.products 
JOIN order_details
ON northwind.products.id = northwind.order_details.product_id WHERE northwind.order_details.unit_price > (SELECT AVG(unit_price) FROM order_details);

#8 Write a query to get Product list (name, unit price) of ten most expensive products.
Select distinct northwind.products.product_name, northwind.products.list_price FROM northwind.order_details JOIN northwind.products
ON products.id = order_details.product_id ORDER by list_price desc LIMIT 10;

#9 Write a query to count current and discontinued products.
Select discontinued,COUNT(*) AS 'current' FROM northwind.products GROUP BY discontinued;

#10 Write a query to get Product list (name, units on order, units in stock) of stock is less than the quantity on order.
Select products.product_name, order_details.quantity AS quantity_ordered, inventory_transactions.quantity AS stock_quantity FROM products
JOIN order_details JOIN inventory_transactions ON products.id=order_details.product_id AND order_details.product_id=inventory_transactions.product_id
WHERE inventory_transactions.quantity < order_details.quantity;