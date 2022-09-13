SELECT emp.name AS Employee
  FROM Employee emp JOIN Employee man
    ON emp.managerId = man.id
 WHERE emp.salary > man.salary;
