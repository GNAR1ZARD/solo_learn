-- You are working with the library books database.

-- The Books table has the columns id, name, year.

-- The library has new books whose information is stored in another table called "New", however they do not have a year column.

-- Write a query to select the books from both tables, Books and New, combining their data. For the year column of the New books use the value 2022.

-- Also, select only the books that are released after the year 1900. 

-- The result set should contain the name and year columns only, ordered by the name column alphabetically.

SELECT 
    name, 
    year
FROM 
    Books
WHERE 
    year > 1900

UNION

SELECT 
    name, 
    2022 AS year
FROM 
    New

WHERE 
    2022 > 1900 -- This condition is always true, included for consistency

ORDER BY 
    name ASC;
