'''
Suppose:-
student database -->
----------------
rollno 
name 
dob 
gender 
class 
section 

student=50

test
------
testid pk
rollno fk
date
subject
mo -->(marks obtained)

27 student gives test

***now, by using joins(inner join --> which we are using in previous lectures) we can only find those student who either have given test or not
but if we want to find all students information like if someone has given test then their marks will print else in place of marks their will be null***

***so for that we use techniques like left join or right join, following are the all those techniques.***
----------------------------
INNER JOIN 
--------------
1. INNER JOIN = Keep ONLY the rows that have a match in both tables.

Suppose:-

Customers
ID	Name
1	Anshul
2	Rahul
3	Aman

Orders
OrderID	CustomerID
101	1
102	2
103	1
104	5

Customer 5 doesn't exist in customers.

So INNER JOIN will give:

Name	OrderID
Anshul	101
Rahul	102
Anshul	103

It ignores unmatched data.

Syntax -->
SELECT columns
FROM table1
INNER JOIN table2
ON table1.column = table2.column;
---------------------------------------------
2. LEFT JOIN -->
LEFT JOIN = Keep ALL rows from the LEFT table, and bring matching rows from the RIGHT table.

Suppose:-
Customers
ID	Name
1	Anshul
2	Rahul
3	Aman
Orders
OrderID	CustomerID
101	1
102	2

If customers is the LEFT table:

Result:

Name	OrderID
Anshul	101
Rahul	102
Aman	NULL

Why?

Aman doesn't have an order, but we still keep Aman because customers is the LEFT table.

Syntax -->
SELECT columns
FROM table1
LEFT JOIN table2
ON table1.column = table2.column;
-------------------------------------------------------
3. RIGHT JOIN -->
RIGHT JOIN = Keep ALL rows from the RIGHT table, and bring matching rows from the LEFT table.

Everything from orders is kept, even if there isn't a matching customer.

Syntax -->
SELECT columns
FROM table1
RIGHT JOIN table2
ON table1.column = table2.column;
----------------------------------------------------
4. FULL OUTER JOIN -->

Keep everything from both tables.
So:- LEFT + RIGHT = FULL OUTER JOIN

However, MySQL does not directly support FULL OUTER JOIN like some other database systems do. It can be achieved using LEFT JOIN + RIGHT JOIN with UNION.

Syntax -->
SELECT columns
FROM table1
FULL OUTER JOIN table2
ON table1.column = table2.column
WHERE condition;
----------------------------------------------------------
ex --> inner join
SELECT product.productid,product.productname,product.rate,sales.qty 
FROM product
inner join sales
on product.productid=sales.productid

ex --> left join
SELECT product.productid,product.productname,product.rate,sales.qty 
FROM product
left join sales
on product.productid=sales.productid

ex --> right join
SELECT product.productid,product.productname,product.rate,sales.qty 
FROM product
right join sales
on product.productid=sales.productid
-----------------------------------------------------------

******sub queries --> Subquery is a query written inside another query.
    - When we need to get records from one table, but the condition depends on information from another table, we use a subquery.
benifite --> fast work
----------------------

suppose:-

states
----------
stateid pk
statename

cities
-------
cityid pk
stateid fk
cityname

place
----------
placeid pk
cityid fk
placename


Question --> Which cities are located in Madhya Pradesh?

    - select cityname from cities where stateid in (select stateid from states where statename='Madhya Pradesh' )

Question --> Which places are located in Gwalior?

    - select placename from places where cityid in (select cityid from cities where cityname='Gwalior')

Question --> In which state is Gwalior located?

    - select statename from states where stateid in (select stateid from cities where cityname='Gwalior' )

Question --> In which state is Hajira located?

    - select statename from states where stateid in (select stateid from cities where cityid in (select cityid from place where placename='Hajira') )

Question --> Which employees handled/sold Tofu? --> tofu is in power_bi database

    - select fullname from employees where employeeid in (select employeeid  from orders where productid in (select productid from products where productname='Tofu'))
    
'''