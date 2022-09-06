SELECT ip_range
  FROM port_scans
 WHERE (
     scan_status IN ('new', 'processing') OR DATE_PART('day', NOW() - TO_TIMESTAMP(last_timestamp))
     ) AND id <= (
    SELECT COALESCE(MIN(id), 999999999)
      FROM (
        SELECT id,
               SUM(POWER(2, 32 - SPLIT_PART(ip_range, '/', 2)::INTEGER)) OVER (ORDER BY id) AS cumsum
          FROM port_scans
         WHERE scan_status IN ('new', 'processing') OR
               DATE_PART('day', NOW() - TO_TIMESTAMP(last_timestamp))
    ) AS ips_cumsum
     WHERE cumsum >= 150000
);