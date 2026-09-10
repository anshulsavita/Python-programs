'''
syntax for create table-->

create table <table name>
(<col name> <type>(size) <constraints>,
<col name> <type>(size) <constraints>,
<col name> <type>(size) <constraints>,
......)

--> we can put upto 2000 characters in varchar

-->use of create table**
if (database is default set)
    create table products(productid int primary key,
    companyname varchar(100) not null,
    productname varchar(50) not null,
    productrate decimal(10,2) not null,
    productoffer decimal(10,2),
    dimension varchar(100),
    description text,
    mfdate date not null)

else:
    create table pepsiemployee.products(productid int primary key,
    companyname varchar(100) not null,
    productname varchar(50) not null,
    productrate decimal(10,2) not null,
    productoffer decimal(10,2),
    dimension varchar(100),
    description text,
    mfdate date not null)

insert-->
    - value will be stored according to sequence
    - date and text will always in single cotes
---------
Syntax(1) -->
    insert into <table> value(value1,value2,value3...)

        ex => insert into products values(100,'pepsico Ltd','Lays',50,0
        'w:200gms width 6x4','xxxxxxxx','2026/7/7')

Syntax(2) --> if we don't have sequence and also if we want to leave some data.
    insert into <table>(<colname>,<colname>...) value(value1,value2,value3...)
    
        ex => insert into products(companyname,productrate,productid,mfdate,productname) 
        values('Pepsico Ltd',25,200,'2026/7/6','Pepsi',20)

**practice*
tablename => students
colum name =>
    rollno varchar  pk
    studentname vc nn
    fathername vc
    gender vc nn
    dob date nn
    address text
    city vc nn
    email vc unique
    mobile vc unique
    class vc nn
    section vc nn
    feedeposite decimal nn

-insert query
'''