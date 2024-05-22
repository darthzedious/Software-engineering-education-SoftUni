SELECT 
	id,
	first_name,
	last_name
from employees
WHERE middle_name is NULL
LIMIT 3;