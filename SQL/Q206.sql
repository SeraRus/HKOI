SELECT name FROM cake ORDER BY name;
SELECT name, weight FROM cake ORDER BY weight;
SELECT name, price FROM cake WHERE weight < 1000 ORDER BY price;
SELECT name, (price - cost) AS gross_profit FROM cake ORDER BY gross_profit DESC;
