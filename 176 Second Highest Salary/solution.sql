-- Write a SQL query to get the second highest salary from the Employee table.

-- +----+--------+
-- | Id | Salary |
-- +----+--------+
-- | 1  | 100    |
-- | 2  | 200    |
-- | 3  | 300    |
-- +----+--------+
-- For example, given the above Employee table, the second highest salary is 200. If there is no second highest salary, then the query should return null.

SELECT max(Salary) AS "SecondHighestSalary"
FROM Employee e1
WHERE 1 = (
    SELECT COUNT(DISTINCT(e2.Salary))
    FROM Employee e2
    WHERE e2.Salary > e1.Salary
)

SELECT max(Salary) AS "SecondHighestSalary"
FROM Employee
WHERE Salary <> (SELECT max(Salary) FROM Employee)

SELECT IFNULL((SELECT DISTINCT(Salary) FROM Employee 
ORDER BY Salary DESC LIMIT 1,1), null) as "SecondHighestSalary"