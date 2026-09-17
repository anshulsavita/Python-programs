
'''
-------------
join
-----------------
if inside join we do not use codition(where) then the query become useless and worse query
    ex --> select product.*,sales.* from products 
else:
    ex --> select product.*,sales.*,product.rate*sales.qtysale as 'Amount' from products,sales where product.productid=sales.productid

    ex --> select product.productid,product.productname,product.rate,sales.qty,
    product.rate*sales.qty as 'Amount' from product,sales 
    where product.productid=sales.productid

foreign key --> A column in one table that links to the Primary Key of another table to create a relationship between them.
    - only primary can be a foriegn key

to crate a foreign key -->
    - right click on table
    - create a table then make all the recuired columns
    - then look at the middle bottom we can see Forsign Keys click on that
    - fill Foreign key Name (we can name it anything)
    - then fill Referenced Table (for which table we are creating that foreign key in our current case it is pepsiemployees.product)
    - then fill, from which column we want to link it 
    - then fill foreign key options --> On Delete --> CASCADE
    - CASCADE mean if i will remove anything from master table their all records will be automatically deleted.

--------------------------------------------
supplier -->
SupplierID PK, CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode, Country, Phone, Fax, HomePage, Products

category
CategoryID PK, CategoryName, Description

products -->
ProductID PK, ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitPrice, UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued
--------------------------------------------
# print productname and unitprice who sell Beverages in power_bi schema

    - SELECT products.productname,products.unitprice FROM products,categories 
    where  products.categoryid=categories.categoryid and categories.CategoryName='Beverages'

# question --> print categoryname,productname and unitprice who sell Beverages or seafood in power_bi schema

    - SELECT categories.CategoryName,products.productname,products.unitprice FROM products,categories 
    where  products.categoryid=categories.categoryid and categories.CategoryName in ('Beverages','seafood')

# question --> companyname = specialty Biscuits, Ltd. , which products are sold by this company.

    - SELECT products.productname FROM products,suppliers   
    where  products.SupplierID= suppliers.SupplierID and suppliers.CompanyName = 'Specialty Biscuits, Ltd.'

# Question --> category = 'Beverages', print Company names of all suppliers that provide Beverages.
    - SELECT suppliers.CompanyName FROM products,suppliers,categories 
    where  products.SupplierID= suppliers.SupplierID and products.CategoryID=categories.CategoryID
    and categories.CategoryName='Beverages'


'''