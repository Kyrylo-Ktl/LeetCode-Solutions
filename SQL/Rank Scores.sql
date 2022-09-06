SELECT s1.score,
       COUNT(s2.score) AS "Rank"
  FROM Scores s1,
      (SELECT DISTINCT score FROM Scores) s2
 WHERE s1.score <= s2.score
 GROUP BY s1.id
 ORDER BY s1.score DESC;