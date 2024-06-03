CREATE TABLE passports(
	id INTEGER GENERATED ALWAYS AS IDENTITY (START WITH 100 INCREMENT BY 1) PRIMARY KEY,
	nationality VARCHAR(50)
);

INSERT INTO passports(nationality)
VALUES ('N34FG21B'), ('K65LO4R7'), ('ZE657QP2');


CREATE TABLE people(
	id serial primary key,
	first_name VARCHAR(50),
	salary decimal(10, 2),
	passport_id INT,

	CONSTRAINT fk_people_passports
	FOREIGN KEY (passport_id)
	REFERENCES passports(id)
);

INSERT INTO people(first_name, salary, passport_id)
VALUES ('Roberto', 43300.00, 101),
	('Tom', 56100.00, 102),
	('Yana', 60200.00, 100);

SELECT pass.id,
	ppl.id,
	pass.nationality,
	ppl.first_name,
	ppl.salary,
	ppl.passport_id
	FROM passports as pass 
	JOIN people as ppl
	ON pass.id = ppl.passport_id