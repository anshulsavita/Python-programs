'''
select statement
----------------
syntax-->
    - select [*]/[<colname>,<colname>.....] from <table>

    - [where <condition>]
    - [where <colname> [not] like 'pattern%_']
    - [where <colname> [not] between v1 and v2]  --> v1 & v2 represent value1 & value
    - [where <colname> [not] in (v1,v2,v3,v4)]
    - [order by <coll>,<col2>....[desc]]
    - [group by <coll>,<col2>....]
    - [having <condition>]


* represents all columns
_ represent one character
% represent all Characters

operators -->
    -> +,-,*,/,%
    -> >,<,<=,>=,=,!=
    -> is null
    -> is not null
    -> and, or, not

select * from employees 
    --> it will show all the columns

select employeename,city from employees
    --> it will show name and city

select employeename,city,salary,salary+1000 from employees
******or*****
select employeename,city,salary,salary+1000 'Bonus' from employees
*****or******
select employeename,city,salary,salary+1000 as 'Bonus' from employees
    --> it will show name,city,salary and a temporary column(salary+1000 or Bonus) who show 1000 incremented salary.
    --> we cant use temporary colums in quaries

ex =>
    select employeename,city,salary,salary*25/100 as 'DA',
    salary*20/100 as 'HRA',(salary*25/100)+(salary*20/100) as 'Total'
    from employees

    
search -->

select * from employees
where employeeid=300
    --> this will find data of that employee id

select * from employees
where city='Mumbai' 
    --> this will find data of that employee who is from Mumbai (it is not case sensitive)
    
select * from employees
where city='Mumbai' or city='gwalior'
    --> this will find who is from mumbai or gwalior

select employeename,city from employees
where salary>=50000 and salary<=100000
    --> this will show name and city of those employee is salary is between 50000,100000

select employeename,city,salary,salary+5000 as 'Bonus from employees
where city='Mumbai'
    --> this will increment 5000 in salary of that employee who is from mumbai

select * from employees
where employeename='r'
        or
select * from employees
where employeename like 'r'
    --> will find whose name is r

select * from employees
where employeename like 'r%'
    --> this will find data of that employee whose name starts with r, 

select * from employees
where employeename like 'amit%'
    --> starts with amit.

select * from employees
where employeename like '%sharma'
    --> will find whose ends with sharma

select * from employees
where employeename like '%a%'        
    --> will find those name who have a in between of their name(it could be anywhere)
        
select * from employees
where employeename like '__o%'
    --> first and second character may be anything (because of _ and i have use 2 of them) and their whould be o and then anyting 

select * from employees
where employeename like '_______________'        
    --> will find name which has exactly 15 characters(because i have use 15 underscore)
                        
select * from employees
where employeename like '_e_e%'                    
    --> will find those name who have 'e' 2nd character and 4th. 
                                    
select * from employees
where employeename not like 'r%'                                         
    --> will find those name who did not starts with r.

select * from employees
where city not like 'mumbai' and city not like 'pune'
    --> who is not from mumbai and pune                
                                
select * from employees
where city in ('mumbai','gwalior')
    --> will find who is from mumbai or pune                     
                                            
select * from employees
where city not in ('mumbai','gwalior')
    --> will find who is not from mumbai or pune    
                                                    
**we will only use (like) when we want to do pattern matching.                 
'''