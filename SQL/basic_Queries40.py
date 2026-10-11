'''
Foreigen key
-------------------
syntax -->  
create table <tablename> (<colname> <type>(size),<colname><type>(size),....
primary key(colname),
constraint <name>
foreign key (<colname>)
references <tablename>(colname)
on delete [cascade|no action]
on update [cascade|no action]
)

Example -->

category
----------
create table category (categoryid in primary key,categoryname varchar(20))

product
----------
create table products(productid int, categoryid int,productname varchar(20),productrate int,
primary key(productid),
constraint cat_pid
foreign key(categoryid)
references category(categoryid)
on delete cascade)
---------------------------------------------------------------
alter table
--------------
alter table <tablename>
[add column <colname> <type>(size) [after]/[before] <colname>] --> [before] does not work in mysql
[modify column <colname> <type>(size)]
[drop column <colname>]
[rename <old_column> to <new_column>] --> works in newer version
[change <old_column> to <new_column><type>(size)] --> it works in our version


exapmles--> 
1.)
Alter table category
add column icon text

2.)
Alter table category
drop column icon 

3.)
Alter table category
add column icon text after categoryid

4.)
alter table category
change categoryname catname varchar(20)

Update table
---------------
update <tablename>
set <colname>=<value>,<colname>=<value>,...
[where <condition>]
[where <colname>[not] like '_%']
[where <colname>[not] in(v1,v2,v3)]
[where between v1 and v2]

**Note --> always use where conditions

exapmles -->
1.)
update flightsdetails
set types='Business Class'
where flightid=1

2.)
update flightsdetails
set type='Business Class'
where typess='Economy'

3.)
update flightsdetails
set totalseats=100, types='Janta'
where days like '%wed%'

Delete table
--------------
delete from  <tablename>
[where <condition>]
[where <colname>[not] like '_%']
[where <colname>[not] like in(v1,v2,v3)]

Examples -->
1.)
delete from flightsdetails --> will remove whole rows

2.)
delete from faculty
where facultyid=6
    - will remove that row whose facultyid is 6

3.)
delete from faculty
where city in ('mumbai','Pune')

4.)
delete from faculty
where month(dob) between 1 and 3
    - will remove that row whose dob is between jan and march

Note: Delete used for removing rows while Drop used for removing whole table or database(schema).

'''
