SELECT COUNT() AS count FROM record WHERE distance = 100;
SELECT COUNT(DISTINCT name) AS count FROM record;
SELECT COUNT() AS count FROM record WHERE distance = 400 AND finish_time <= 60;
SELECT MIN(finish_time) AS fastest_time, ROUND(AVG(finish_time), 2) AS average_time FROM record WHERE distance = 200;
