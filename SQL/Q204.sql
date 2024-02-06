SELECT model_name FROM computer WHERE cpu_cores = 4 AND ram = 8;
SELECT model_name FROM computer WHERE ssd + hdd BETWEEN 512 AND 1024;
SELECT model_name FROM computer WHERE cpu_name LIKE 'Intel%' OR cpu_name LIKE 'AMD%';
SELECT model_name FROM computer WHERE (cpu_name LIKE 'Intel%' OR cpu_name LIKE 'AMD%') AND cpu_cores >= 8;
