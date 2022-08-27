SELECT department,
       employee,
       salary
  FROM (
    SELECT d.name AS department,
           e.name AS employee,
           e.salary,
           MAX(e.salary) OVER (PARTITION BY d.id) AS max_salary
      FROM Employee e JOIN Department d
          ON e.departmentId = d.id
) AS _
 WHERE salary = max_salary;