'''
Tables -->
----------------------------------------------------------
supplier -->
SupplierID PK, CompanyName, ContactName, ContactTitle, Address, City, Region, 
PostalCode, Country, Phone, Fax, HomePage, Products

category -->
CategoryID PK, CategoryName, Description

products -->
ProductID PK, ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitPrice,
 UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued

employess -->
EmployeeID PK, LastName, FirstName, Title, TitleOfCourtesy, BirthDate, HireDate,
 Address, City, Region, PostalCode, Country, HomePhone, Extension, Photo, Notes,
   ReportsTo, PhotoPath, FullName, Gender

orders -->
OrderID PK, CustomerID FK, EmployeeID FK, OrderDate, RequiredDate, ShippedDate, ShipVia,
Freight, ShipName, ShipAddress, ShipCity, ShipRegion, ShipPostalCode, ShipCountry,
ProductID FK, UnitPrice, Quantity, Discount, Total_Amount
--------------------------------------------------------

Question -- Write a SQL query to find the Order ID, Order Date, Customer Name, and Product Name for all orders where the product name is ‘Chai’.
    
    - SELECT orders.OrderID,orders.OrderDate,customers.ContactName,products.productname FROM orders,customers,products
    where products.ProductID=orders.ProductID and customers.customerid=orders.CustomerID and
    products.ProductName='Chai'

Question -- Which employees deal with customers from France?
    
    - select orders.orderid,employees.FirstName,customers.ContactName,customers.City,customers.country from employees,customers,orders
    where employees.EmployeeID=orders.EmployeeID and customers.CustomerID=orders.CustomerID and
    customers.Country='France'

Question -- Display the customer name and employee name for customers and employees who are from the same city and country.
    
    - select employees.FirstName,customers.ContactName,customers.City from employees,customers
    where employees.city=customers.city 

Question -- Find the total amount of sales for the product "Tofu"
    
    - select sum(Total_Amount) from products,orders where products.ProductID=orders.ProductID and
    products.ProductName='Tofu' 

    
'''