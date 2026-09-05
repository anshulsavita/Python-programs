"""
Schema --> Group of tables (Database)
    - inside Schema we create tables
Table --> A table is a structure that stores data in rows and columns, like a spreadsheet.

SQL --> Structured Quiry Language
--------------------
Types of SQl -->
    --DDL (Data Definition Language.)
        => Schema Designing
        => Table Creation
        => Alter Table/Schema 

    --DML (Data Manipulation Language.)
        => Insertion, Searching, Sorting, Deletion, Updation

    --DCL (Data Control Language.)
        => User Creation
        => Grant/Revoke permission for Table & Schema's.

******DDL******
---------------
    - Create Schema/database.
        - Syntax --> create schema <schema_name>;
    - Create Table
        - Syntax --> 
        create table <table_name> ( <colname> <type>(size) <constraints>,
        <colname> <type>(size) <constraints>, <colname> <type>(size) <constraints>,
        <colname> <type>(size) <constraints>,...............................)

    - constraints --> 
        - Primary Key --> Data Should be unique & not null.
        - Unique --> Data should be unique but alloew null entries.
        - not null --> Null/Blank entries not allowed
        - null(default) --> Allow Null entries
        - auto_increment --> Will generate primary key implicitly.
        - default --> Set default value for column.
    
    - Use of it --> 
    create table employees ( employeeid int primary key,
    employeename varchar(100) not null,gender varchar(6) not null,
    city varchar(45),dob date not null,salary decimal(10,2) not null,mobileno varchar(13) unique)
"""