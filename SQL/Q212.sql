SELECT word FROM dictionary WHERE word LIKE '%AR' AND length(word) = 3;
SELECT word FROM dictionary WHERE word LIKE 'T_S%';
SELECT word FROM dictionary WHERE word LIKE '%Q%U%' AND word NOT LIKE '%Q%U%U%' AND word NOT LIKE '%Q%Q%' AND word NOT LIKE '%U%U%';
SELECT word FROM dictionary WHERE (word LIKE '____Z%' OR word LIKE '___Z_%' OR word LIKE '__Z__%' OR word LIKE '_Z___%' OR word LIKE 'Z____%') AND length(word) >= 5;
