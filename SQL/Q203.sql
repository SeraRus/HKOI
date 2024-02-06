SELECT model_name FROM computer WHERE cpu_cores >= 8;
SELECT model_name FROM computer WHERE ssd != hdd;
SELECT model_name FROM computer WHERE ram/cpu_cores < 4;
SELECT ssd + hdd AS total_storage FROM computer WHERE model_name = 'BananaBook Pro 14';
