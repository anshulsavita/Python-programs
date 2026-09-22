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

customers -->
CustomerID, CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode,
Country, Phone, Fax
---------------------------------------------------------------

Question -- Product Name and Total Sales — Which product was sold in what quantity?

    - select products.productname,sum(orders.Total_Amount) as 'Total Sale' from products,orders where
    products.ProductID=orders.ProductID group by products.productName

Question -- How many times was each product sold?

    - select products.productname,sum(orders.Total_Amount) as 'Total Sale',count(*) from products,orders where
    products.ProductID=orders.ProductID group by products.productName

Question -- How much money do we earn from each country?

    - select customers.Country,sum(orders.Total_Amount) as 'Total Sale' from orders,customers
    where customers.CustomerID=orders.CustomerID group by customers.country

    ******or****

    - select orders.shipcountry,sum(orders.total_amount) from orders group by orders.shipcountry

Question --  How many times did each employee serve customers?

    - select customers.ContactName,employees.FirstName,count(*) from customers,employees,orders
    where customers.CustomerID=orders.CustomerID and employees.EmployeeID=orders.EmployeeID group by orders.CustomerID,orders.employeeid

Question -- Which product was sold by which employee, and for what amount?

    - select employees.FirstName,products.ProductName,sum(orders.Total_Amount) as 'Total Amount'
    from employees,products,orders where employees.EmployeeID=orders.EmployeeID
    and products.ProductID=orders.ProductID group by orders.EmployeeID,orders.ProductID

'''