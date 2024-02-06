SELECT name, price_twin FROM hotel WHERE stars = 5 AND price_twin IS NOT NULL ORDER BY price_twin DESC;
SELECT name, price_double*6 AS total_cost FROM hotel WHERE price_double IS NOT NULL ORDER BY total_cost;
SELECT name, stars FROM hotel ORDER BY stars DESC, name;
SELECT name, ROUND(CAST(price_double AS FLOAT)/stars, 2) AS cost_per_star FROM hotel WHERE price_double IS NOT NULL ORDER BY cost_per_star, stars DESC
