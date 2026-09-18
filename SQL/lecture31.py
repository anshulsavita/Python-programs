# orders--
# OrderID, CustomerID, EmployeeID, OrderDate, RequiredDate, ShippedDate, ShipVia,
# Freight, ShipName, ShipAddress, ShipCity, ShipRegion, ShipPostalCode, ShipCountry,
# ProductID, UnitPrice, Quantity, Discount, Total_Amount

# select orders.orderid,orders.orderdate,customers.ContactName from products,customers,orders where products.ProductID=orders.ProductID and
# customers.CustomerID=orders.CustomerID and products.productname='chai'

# employeename,customername and city

# SELECT employees.FirstName,employees.LastName,customers.ContactName,customers.city FROM employees,customers,orders where
# orders.CustomerID=customers.CustomerID and employees.EmployeeID=orders.EmployeeID and customers.country='France'

# select customers.contactname, employees.FirstName, customers.city from customers,employees where employees.city=customers.city