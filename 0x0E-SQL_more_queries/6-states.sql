-- Create database for states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
\u htbn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id INT UNIQUE AUTO_INCREMENT,
	name VARCHAR(256)
);
