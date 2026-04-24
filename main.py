# CodeGrade step0
# Run this cell without changes
# SQL Library and Pandas Library
import sqlite3
import pandas as pd
# Connect to the database
conn = sqlite3.connect('data.sqlite')
pd.read_sql("""SELECT * FROM sqlite_master""", conn)
# CodeGrade step1
# Replace None with your code
df_boston = pd.read_sql("""
SELECT firstName, lastName
FROM employees
JOIN offices ON employees.officeCode = offices.officeCode
WHERE city = 'Boston'
""", conn)
df_boston

 
# CodeGrade step2
# Replace None with your code
df_zero_emp = pd.read_sql("""
    SELECT o.officeCode, o.city
    FROM offices o
    LEFT JOIN employees e ON o.officeCode = e.officeCode
    WHERE e.employeeNumber IS NULL
""", conn)
df_zero_emp

# CodeGrade step3
# Replace None with your code
df_employee = pd.read_sql("""
    SELECT e.firstName, e.lastName, o.city, o.state
    FROM employees e
    LEFT JOIN offices o ON e.officeCode = o.officeCode
    ORDER BY e.firstName, e.lastName
""", conn)
df_employee

# CodeGrade step4
# Replace None with your code
df_contacts = pd.read_sql("""
    SELECT c.contactFirstName, c.contactLastName, c.phone, c.salesRepEmployeeNumber
    FROM customers c
    LEFT JOIN orders o ON c.customerNumber = o.customerNumber
    WHERE o.orderNumber IS NULL
    ORDER BY c.contactLastName
""", conn)
df_contacts

# CodeGrade step5
# Replace None with your code
df_payment = pd.read_sql("""
    SELECT c.contactFirstName, c.contactLastName, p.amount, p.paymentDate
    FROM customers c
    JOIN payments p ON c.customerNumber = p.customerNumber
    ORDER BY CAST(p.amount AS REAL) DESC
""", conn)
df_payment
# CodeGrade step6
# Replace None with your code
df_credit = pd.read_sql("""
    SELECT e.employeeNumber, e.firstName, e.lastName, COUNT(c.customerNumber) as num_customers
    FROM employees e
    JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber
    GROUP BY e.employeeNumber
    HAVING AVG(c.creditLimit) > 90000
    ORDER BY num_customers DESC
""", conn)
df_credit



# CodeGrade step7
# Replace None with your code
df_product_sold = pd.read_sql("""
    SELECT p.productName, COUNT(od.orderNumber) as numorders, SUM(od.quantityOrdered) as totalunits
    FROM products p
    JOIN orderdetails od ON p.productCode = od.productCode
    GROUP BY p.productCode
    ORDER BY totalunits DESC
""", conn)
df_product_sold

# CodeGrade step8
# Replace None with your code
df_total_customers = pd.read_sql("""
    SELECT p.productName, p.productCode, COUNT(DISTINCT o.customerNumber) as numpurchasers
    FROM products p
    JOIN orderdetails od ON p.productCode = od.productCode
    JOIN orders o ON od.orderNumber = o.orderNumber
    GROUP BY p.productCode
    ORDER BY numpurchasers DESC
""", conn)
df_total_customers

# CodeGrade step9
# Replace None with your code
df_customers = pd.read_sql("""
    SELECT o.officeCode, o.city, COUNT(c.customerNumber) as n_customers
    FROM offices o
    JOIN employees e ON o.officeCode = e.officeCode
    JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber
    GROUP BY o.officeCode
""", conn)
df_customers

# CodeGrade step10
# Replace None with your code
df_under_20 = pd.read_sql("""
    SELECT DISTINCT e.employeeNumber, e.firstName, e.lastName, o.city, o.officeCode
    FROM employees e
    JOIN offices o ON e.officeCode = o.officeCode
    JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber
    JOIN orders ord ON c.customerNumber = ord.customerNumber
    JOIN orderdetails od ON ord.orderNumber = od.orderNumber
    WHERE od.productCode IN (
        SELECT p.productCode
        FROM products p
        JOIN orderdetails od2 ON p.productCode = od2.productCode
        JOIN orders o2 ON od2.orderNumber = o2.orderNumber
        GROUP BY p.productCode
        HAVING COUNT(DISTINCT o2.customerNumber) < 20
    )
""", conn)
df_under_20

# Run this cell without changes

conn.close()









