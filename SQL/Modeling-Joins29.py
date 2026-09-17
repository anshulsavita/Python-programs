'''
select 'Hello student' as message
    - will print message
--------------------------

******Data Modeling -->

product
-----------------
product_iD pk, productname,productrate,stock
1  pepsi  56      10
2  Real Juice 78  50
3  Fanta  25   12
4  Coke 89    10

bill
--------
billno pk,  billdate,  shoplocation,   coutumername
1000   2026/09/14  Thatipur   Harry
1001   2026/9/14   Thatipur   naman

Sales
-------
Transactionid PK,  productid  FK,   billno FK,   Qtysale
1  4  1000  3
2  1  1000  3
3  2  1001  2

***********************************

joins --> use to merge more then one table
-----------

product 
--------
product_id pk, productname,rate,stock
1  pepsi  56      10
2  Real Juice 78  50
3  Fanta  25   12
4  Coke 89    10

Sales 
---------
productid   qtysale
1           5
4           7
3           10

now by using joins -->

select product.*,sales.* from products  
    - this will done matrix multiplication (Cartision product --> row multiply by column)
    - output -->
        1, pepsi,56,10,1,5
        1,pepsi,56,10,4,7
        1,pepsi,56,10,3,10
        2,Real jiuce, 78,50,1,5....
        ..........

select product.*,sales.*,product.rate*sales.qtysale as 'Amount' from products,sales where product.productid=sales.productid
    - This will show those record which we have soled and their Amount
    - this is joins

'''