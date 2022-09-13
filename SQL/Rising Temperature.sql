SELECT DISTINCT a.Id
  FROM Weather AS a,
       Weather AS b
 WHERE a.temperature > b.temperature
   AND DATEDIFF(a.recordDate, b.recordDate) = 1;
