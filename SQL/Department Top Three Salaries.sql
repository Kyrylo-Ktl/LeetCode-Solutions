SELECT d.Name AS Department,
       a.Name AS Employee,
       a.Salary
  FROM (
    SELECT e.*,
           DENSE_RANK() OVER (PARTITION BY DepartmentId ORDER BY Salary DESC) AS DepSalRank
      FROM Employee e
) a JOIN Department d
    ON a.DepartmentId = d. Id
 WHERE DepSalRank <= 3;
