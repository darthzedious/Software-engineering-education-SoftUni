CREATE TABLE minions_birthdays(
	id serial UNIQUE NOT NULL,
	name VARCHAR(150),
	date_of_birth DATE,
	age INTEGER,
	present VARCHAR(100),
	party timestamptz
);
