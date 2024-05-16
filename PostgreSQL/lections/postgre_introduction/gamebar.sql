CREATE TABLE employees(
	id serial NOT NULL PRIMARY KEY,
	first_name varchar(30),
	last_name varchar(50),
	hiring_date date default '2023-01-01',
	salary numeric(10, 2),
	devices_number integer
);

CREATE TABLE departments(
	id serial NOT NULL PRIMARY KEY,
	name varchar(50),
	code char(3),
	description text
);

CREATE TABLE issues(
	id serial PRIMARY KEY UNIQUE,
	description varchar(150),
	date date,
	start timestamp
);

ALTER TABLE employees
ADD middle_name varchar(50)

ALTER TABLE employees
ALTER COLUMN salary SET NOT NULL,
ALTER COLUMN salary SET DEFAULT 0,
ALTER COLUMN hiring_date SET NOT NULL;

ALTER TABLE employees
ALTER COLUMN  middle_name TYPE VARCHAR(100);
