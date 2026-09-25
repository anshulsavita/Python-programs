'''
Question --> Find the Order ID and Order Date of all orders placed by customers from France.

    - select OrderID,OrderDate from orders where CustomerID in (select CustomerID from customers where Country = 'France')

Question --> Find each customer's name and the total amount they have spent, and display the customers in descending order of their total spending.

    - select customers.ContactName,sum(orders.Total_Amount) from customers,orders where orders.CustomerID=customers.CustomerID group by customers.ContactName order by sum(orders.Total_Amount )desc

Question --> Find the names of customers who have never placed any order.

    - select customers.ContactName from customers where customerid not in( select customerid from orders group by customerid)

Question --> Find the contact name of the supplier(s) who supply the product ‘Chai’.

    - select suppliers.ContactName from suppliers,products where suppliers.SupplierID=products.SupplierID and products.ProductName='Chai' group by suppliers.supplierid

Question --> Find the names of employees whose total sales amount is greater than 2000.

    - select employees.FullName,sum(orders.Total_Amount) from employees,orders where employees.EmployeeID=orders.EmployeeID group by employees.EmployeeID having sum(orders.Total_Amount)>2000 

'''