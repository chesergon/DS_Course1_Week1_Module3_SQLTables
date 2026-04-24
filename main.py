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
SELECT firstName,lastName
FROM employees
 JOIN offices ON employees.officeCode = offices.officeCode
  WHERE city  ='Boston'


""",conn)
df_boston


# CodeGrade step2
# Replace None with your code
df_zero_emp =  pd.read_sql(""" 
SELECT *
FROM offices
 LEFT JOIN employees ON offices.officeCode = employees.officeCode
 GROUP BY offices.officeCode
 HAVING COUNT(employees.employeeNumber) = 0
 """,conn)
df_zero_emp

# CodeGrade step3
# Replace None with your code
df_employee = pd.read_sql("""
SELECT 
employees.firstName,
employees.lastName,
offices.city,
offices.state
FROM employees 
LEFT JOIN offices ON offices.officeCode =  employees.officeCode
GROUP BY employees.firstName ,employees.lastName

""",conn)
df_employee


# CodeGrade step4
# Replace None with your code
df_contacts= pd.read_sql("""
SELECT DISTINCT
customers.contactfirstName,
customers.contactLastName,
customers.phone,
customers.salesRepEmployeeNumber
FROM customers
LEFT JOIN orders ON orders.customerNumber = customers.customerNumber
WHERE orders.customerNumber IS NULL
ORDER BY customers.contactLastName ASC
""", conn)
df_contacts
df_product_sold = pd.read_sql("""
SELECT 
   products.productName,
   products.productCode,
   SUM(orderdetails.quantityOrdered) AS totalunits
FROM products
JOIN orderdetails ON orderdetails.productCode = products.productCode
GROUP BY products.productCode, products.productName
""", conn)
df_product_sold


# CodeGrade step5
# Replace None with your code
df_payment =pd.read_sql(""" 
SELECT 
       customers.contactFirstName,
       customers.contactLastName,
       CAST (payments.amount AS FLOAT)AS amount,
       payments.paymentDate
FROM customers
JOIN payments ON  payments.customerNumber = customers.customerNumber
ORDER BY CAST( payments.amount AS FLOAT)DESC


""",conn)
df_payment
df_contacts = pd.read_sql("""
SELECT 
    customers.contactFirstName,
    customers.contactLastName,
    customers.phone,
    customers.salesRepEmployeeNumber
FROM customers
WHERE customers.customerNumber NOT IN (
 SELECT DISTINCT customerNumber FROM orders)
ORDER BY customers.contactLastName ASC

""", conn)
df_contacts


# CodeGrade step6
# Replace None with your code
df_credit = pd.read_sql(""" 
SELECT 
        employees.employeeNumber,
        employees.firstName,
        employees.lastName,
        COUNT(customers.customerNumber) AS number_of_customers
    FROM employees
    JOIN customers ON customers.salesRepEmployeeNumber = employees.employeeNumber
    GROUP BY employees.employeeNumber, employees.firstName, employees.lastName
    HAVING AVG(CAST(customers.creditLimit AS FLOAT)) > 90000
    ORDER BY number_of_customers ASC
""",conn)
df_credit

# CodeGrade step6
# Replace None with your code
df_credit = pd.read_sql(""" 
SELECT 
        employees.employeeNumber,
        employees.firstName,
        employees.lastName,
        COUNT(customers.customerNumber) AS number_of_customers
    FROM employees
    JOIN customers ON customers.salesRepEmployeeNumber = employees.employeeNumber
    GROUP BY employees.employeeNumber, employees.firstName, employees.lastName
    HAVING AVG(CAST(customers.creditLimit AS FLOAT)) > 90000
    ORDER BY number_of_customers ASC 
""",conn)
df_credit

# CodeGrade step8
# Replace None with your code
df_total_customers = pd.read_sql("""
    SELECT 
        products.productName,
        products.productCode,
        COUNT(DISTINCT orders.customerNumber) AS numpurchasers
    FROM products
    JOIN orderdetails ON orderdetails.productCode = products.productCode
    JOIN orders ON orders.orderNumber = orderdetails.orderNumber
    GROUP BY products.productCode, products.productName
    ORDER BY numpurchasers DESC
""", conn)
df_total_customers

# CodeGrade step9
# Replace None with your code
df_customers = pd.read_sql("""
    SELECT 
        offices.officeCode,
        offices.city,
        COUNT(customers.customerNumber) AS n_customers
    FROM offices
    JOIN employees ON employees.officeCode = offices.officeCode
    JOIN customers ON customers.salesRepEmployeeNumber = employees.employeeNumber
    GROUP BY offices.officeCode, offices.city
    ORDER BY n_customers DESC
""", conn)

df_customers

# CodeGrade step9
# Replace None with your code
df_customers = pd.read_sql("""
    SELECT 
        offices.officeCode,
        offices.city,
        COUNT(customers.customerNumber) AS n_customers
    FROM offices
    JOIN employees ON employees.officeCode = offices.officeCode
    JOIN customers ON customers.salesRepEmployeeNumber = employees.employeeNumber
    GROUP BY offices.officeCode, offices.city
    ORDER BY n_customers DESC
""", conn)

df_customers

# CodeGrade step10
# Replace None with your code
df_under_20 =pd.read_sql ("""
    WITH underperforming_products AS (
        SELECT 
            products.productCode,
            COUNT(DISTINCT orders.customerNumber) AS numpurchasers
        FROM products
        JOIN orderdetails ON orderdetails.productCode = products.productCode
        JOIN orders ON orders.orderNumber = orderdetails.orderNumber
        GROUP BY products.productCode
        HAVING COUNT(DISTINCT orders.customerNumber) < 20
    )
    SELECT DISTINCT
        employees.employeeNumber,
        employees.firstName,
        employees.lastName,
        offices.city,
        offices.officeCode
    FROM employees
    JOIN offices ON offices.officeCode = employees.officeCode
    JOIN orderdetails ON orderdetails.productCode IN (SELECT productCode FROM underperforming_products)
    JOIN orders ON orders.orderNumber = orderdetails.orderNumber
    JOIN customers ON customers.customerNumber = orders.customerNumber
    WHERE customers.salesRepEmployeeNumber = employees.employeeNumber
""", conn)

df_under_20

# Run this cell without changes

conn.close()
