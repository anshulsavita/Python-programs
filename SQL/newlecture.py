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

alter table
--------------
alter table <tablename>
add column <colname> <type>(size) [after]/[before] 

alter table category
add column icon text 
[modify column <colname> <type>(size)]
[drop column <colname>]
[change <old_column> to <new_column><type>(size)]


update  <tablename>
set <colname>=<value>,<colname>=<value>,...
[where <condition>]
[where <colname>[not] like '_%']
[where <colname>[not] like in(v1,v2,v3)]

delete from  <tablename>
[where <condition>]
[where <colname>[not] like '_%']
[where <colname>[not] like in(v1,v2,v3)]

'''
