examples = """
Violation: Missing Commas in SELECT lists
Example: SELECT id, name age FROM users;

Violation: Misplaced Commas in SELECT lists
Example: SELECT id,, name FROM users;

Violation: non-existing functions
Example: SELECT madeupfunc(name) FROM users;

Violation: functions with incorrect number of arguments
Example: SELECT SUBSTR(name) FROM users;

Violation: columns that reference an undefined table or table alias
Example: SELECT u.id FROM users x;

Violation: Forgetting GROUP BY with Aggregates
Example: SELECT department, COUNT(*) FROM employees;

Violation: Unquoted string literals
Example: SELECT * FROM users WHERE country = US;

Violation: Incorrect clause order
Example: SELECT id FROM users ORDER BY name WHERE age > 30;

Violation: Missing SELECT clause
Example: * FROM WHERE age > 30;

Violation: Missing FROM clause
Example: SELECT * WHERE age > 30;

Violation: Missing column alias
Example: SELECT COUNT(*) FROM users;

Violation: Missing parenthesis
Example: SELECT * FROM users WHERE id IN 1, 2);

"""