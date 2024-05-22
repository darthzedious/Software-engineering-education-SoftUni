CREATE VIEW try AS 
SELECT e.first_name,
e.last_name,
e.salary,
NULL AS room_id,
NULL AS name
FROM employees as e
	
UNION ALL
	
SELECT
c.first_name,
c.last_name,
NULL AS salary,
c.room_id,
null as name
from clients as c

UNION ALL

SELECT null as first_name,
null as last_name,
null as salary,
null as room_id,
d.name
from departments as d;

SELECT * from try;

