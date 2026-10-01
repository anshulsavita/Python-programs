'''
select * from power_bi.products limit 1

select * from power_bi.products limit 10,2
    - 10th row ke baad 2 rows show ho jayenge

***********Functions********
---------------------------------
select ascii('A')
    - 65

select bin(25)
    - convert in binary

select bit_length('Text')
    - kitne bit consume karta hai

select cast(char(65) as char)
    - it will print A

select cast(char(97) as char)
    - it will print a

select cast(char(97,98,99,100) as char)
    - it will print abcd

select char_length(Gwalior')
    - print length

select * from products where char_length(productname)>=5
    - will print productname whose char length is 5 or greater

select concat(firstname,' ',lastname) as employeename from power_bi.employees;
    - will concatinate two or more strings

select concat_ws(' ',firstname,lastname) as employeename from power_bi.employees;
    - will concatinate two or more strings and add seprater in bewtween which was in first place

select concat_ws('#',firstname,lastname) as employeename from power_bi.employees;
    - will concatinate and # will be in middle

select elt(2,'This','is','me')
    - will print nth element, in our case it will print 2

Field()--> will return index of perticular str 
    - field(str,str1,str2,str3,...)
    Eg. --> select field('Agra','Gwalior','Indore','Agra','Morena')

select find_in_set('Agra','Gwalior,Indore,Agra,Morena')
    - will return index or perticular str from another str (that str will be seprated by ',')
    
select format('1000000.0000',2)
    - will formats the number x to a formate like '#,###,###.##' and print 1,000,000.00
    
select hex()
    - convert number into Hexa

insert(str,pos,len,newstr)
    select insert('This is test',9,4,'My-SQL')
        - will return 'This is My-SQL'    
    
    select insert('This is test',9,2,'My-SQL')
        - will return 'This is My-SQLst'    
    
Instr(str,substr) --> Tage a string and substring of it as arguments, and return an integer which indicates the position of the first occurance of the substring within the string
    select instr('ramgarh','gar')    
        - will return position (4)
    
Lcase(str) --> convert the characters of a string to lower case characters.
    select lcase('MYTESTSTRING')
        - will return myteststring

left(str,len) --> returns a specified number of characters from the left of a given string.Both the number and 
the string are supplied ih the arguments as str and len of the function
    select select left('firstname',3)
        - will return 'fir'

locate(substr,str,pos) 
    select locate('str','myteststring')
        - will return 5
    
    select locate('the','the man the ai',5)
        - 9 

lower(str) --> convert all the characters in a string to lowercase characters.

lpad('str',len,padstr)
    select lpad('Hello',10,'**')
        - return *****Hello
    select lpad('Hi',1,'**')
            - return H
    
ltrim(str) --> removes the leading space characters of a string passed as argument.
    












    '''