-- Write a SQL query to get the nth highest salary from the Employee table.

-- +----+--------+
-- | Id | Salary |
-- +----+--------+
-- | 1  | 100    |
-- | 2  | 200    |
-- | 3  | 300    |
-- +----+--------+
-- For example, given the above Employee table, the nth highest salary where n = 2 is 200. If there is no nth highest salary, then the query should return null.


CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
    SELECT max(Salary) AS "SecondHighestSalary"
    FROM Employee e1
    WHERE (N - 1) = (
        SELECT COUNT(DISTINCT(e2.Salary))
        FROM Employee e2
        WHERE e2.Salary > e1.Salary
    )
  );
END