SELECT visit_date FROM travel_log WHERE city = 'Macau';
SELECT DISTINCT CAST(SUBSTRING(visit_date, 6, 2) AS INT) AS month FROM travel_log WHERE city = 'Tokyo' AND SUBSTRING(visit_date, 1, 4) = '2023';
SELECT DISTINCT city FROM travel_log WHERE SUBSTRING(visit_date, 1, 7) = '2021-03';
SELECT DISTINCT city FROM travel_log WHERE SUBSTRING(visit_date, 1, 4) IN ('2016', '2020');
