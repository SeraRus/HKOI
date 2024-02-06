SELECT subject, ((test_one + test_two)*0.2 + final_exam*0.6) AS weighted_total FROM report;
SELECT subject FROM report WHERE ((test_one + test_two)*0.2 + final_exam*0.6) >= 90;
SELECT subject FROM report WHERE final_exam >= test_two AND final_exam >= test_one;
SELECT subject FROM report WHERE ABS(test_one - test_two) > 10;
