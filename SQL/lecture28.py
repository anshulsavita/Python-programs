'''
syntax-->
    - select [*]/[<colname>,<colname>.....] from <table>

    - [where <condition>]
    - [where <colname> [not] like 'pattern%_']
    - [where <colname> [not] between v1 and v2]  --> v1 & v2 represent value1 & value
    - [where <colname> [not] in (v1,v2,v3,v4)]
    - [order by <coll>,<col2>....[desc]]
    - [group by <col1>,<col2>....]
    - [having <condition>]

select * from employees where salary between 10000 to 20000
    --> will print data whose salary between 10000 and 20000, 10000,20000 will also be included.

select * from employees where dob between '2000-1-1' to '2026-12-31'
    --> will print data

select * from employees order by employeename
    --> will print employeename in asscending order

select * from employees order by employeename desc
    --> will print employeename in descinding order
------------------------------------------------
**** Aggregate function ****** --> mainly work with group
min(col)
    --> will print minimum values in a group
max(col)
    --> will print maximum values in a group
sum(col) 
    --> will print sum of all the numbers in a coloum of a group
avg(col) 
    --> will print average value of a group, not include null
count(col) 
    --> will count number of entries in a coloum, will not count null entries
count(*)
    --> will count number of entries in a coloum, will count null entries also
-------------------------------------------------
select max(salary) from employees
    --> print max salary from all the employees
select min(salary) from employees
    --> print min salary
select sum(salary) from employees
    --> will print sum of all the salaries
select avg(salary) from employees
    --> will print avegrage salary 

select count(salary) from employees
    --> it will count number of employees who get salary, null entries will not be count
select count(*) from employees
    --> it will count number of employees, null entries will not be count

------------------------------------------------

select count(*) as 'Male_employees' from employees where gender = 'Male'
    - count how many male employee are in our company

select sum(salary) from employees where gender = 'Male'
    - how much salary we gave to our male employees

select employeename, sum(salary) from employees where gender = 'Male'
    - here we are performing a multicolumn result(employeename) with a single column result [sum(saalary)] which is a wrong method to perform never do this.

-----------------------------------------------
group by -->
-----------
select city from employees group by city 
    --> it will make grop of city and show every city one time.

select city,count(*) from employees group by city 
    --> it will print city and how many employees are from there.
    
select city,count(*),sum(salary) from employees group by city 
    --> it will print city and how many employees are from there and sum of ther salary.

select city,gender,count(*),sum(salary) from employees group by city,gender
    - For every unique city-gender combination, count employees and calculate their total salary.
------------
having -->
-----------
select city,gender,count(*),sum(salary) from employees group by city,gender
having sum(salary)>500000
    - which group we gave salary more than 500000
    - with having (like) will not work, >,<,+,-... they will work
------------------------------------------------------------------------

select * from customers where region is null
    --> will show data whode region(this is coll) is null
select * from customers where region is not null
    --> will show data whose region is not null

select count(*) from customers where contactTitle='Sales Representative'
    --> it will count total no of sales represebtative

select country,count(*) from customers where country in ('USA','Brazil') group by country
    --> will count how many customers are from usa and brazil

















'''