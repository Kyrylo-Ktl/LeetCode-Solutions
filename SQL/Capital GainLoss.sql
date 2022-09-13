SELECT stock_name,
       SUM(IF(operation='Buy', -price, price)) AS capital_gain_loss
  FROM Stocks
 GROUP BY stock_name;
