SELECT event_name, COUNT(DISTINCT class) AS count FROM relay_record GROUP BY event_name;
SELECT event_name, COUNT(DISTINCT class) - COUNT(finish_time) AS count FROM relay_record GROUP BY event_name;
SELECT event_name, MIN(finish_time) AS fastest_time, MAX(finish_time) AS slowest_time, ROUND(AVG(finish_time), 2) AS average_time FROM relay_record GROUP BY event_name;
SELECT event_name, SUM(finish_time) AS total_time FROM relay_record GROUP BY event_name HAVING COUNT(finish_time) >= 3;
