CREATE VIEW top_paid_employee AS
SELECT * from employees
ORDER BY salary DESC
LIMIT 1;


SELECT * FROM top_paid_employee;