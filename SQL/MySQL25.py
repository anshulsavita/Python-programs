"""
word meanings-->
---------------------------------------------------------
ALTER → Changes the structure of an existing table.
DROP → Completely deletes a table/database.
TRUNCATE → Deletes all data from a table but keeps the table structure.
GRANT → Gives permissions to a user.
REVOKE → Removes permissions from a user.
COMMIT → Permanently saves changes.
ROLLBACK → Undoes changes that haven't been committed.
SAVEPOINT → Creates a point you can roll back to later within a transaction.
Retrieve data → get data from the database.
------------------------------------------------------------
Schema --> Group of tables (Database)
    - inside Schema we create tables
Table --> A table is a structure that stores data in rows and columns, like a spreadsheet.

SQL --> Structured Quiry Language
    -SQL is a language used to store, retrieve, and manage data in databases.
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

    --DQL (Data Query Language.) -->(*We will study it later)
        => Retrieves data
        => Search data

    --TCL (Transaction Control Language.) -->(*We will study it later)
        => Commit
        => RollBack
        => SavePoint

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
        - Unique --> Data should be unique but allow null entries.
        - not null --> Null/Blank entries not allowed
        - null(default) --> Allow Null entries
        - auto_increment --> Will generate primary key implicitly.
        - default --> Set default value for column.
    
    - Use of it --> 
    create table employees ( employeeid int primary key,
    employeename varchar(100) not null,gender varchar(6) not null,
    city varchar(45),dob date not null,salary decimal(10,2) not null,mobileno varchar(13) unique)
"""