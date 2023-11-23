<<<<<<< HEAD
-- script that prepares a MySQL server for AirBnB_clone_v2

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
=======
--Prepares a mysql server for testing this project--
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db. * TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema . * ON 'hbnb_test'@'localhost';
>>>>>>> upstream/master
