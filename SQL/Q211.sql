SELECT id FROM ticket WHERE first_number = 4 AND second_number = 16 AND third_number = 28 AND fourth_number = 30 AND fifth_number = 45 AND sixth_number = 47;
SELECT id FROM ticket WHERE second_number = first_number + 1 AND third_number = second_number + 1 AND fourth_number = third_number + 1 AND fifth_number = fourth_number + 1 AND sixth_number = fifth_number + 1;
SELECT id FROM ticket WHERE first_number IN (3, 4, 9, 10, 14, 15, 20, 25, 26, 31, 36, 37, 41, 42, 47, 48);
SELECT id FROM ticket WHERE first_number = 36 OR second_number = 36 OR third_number = 36 OR fourth_number = 36 OR fifth_number = 36 OR sixth_number = 36;
