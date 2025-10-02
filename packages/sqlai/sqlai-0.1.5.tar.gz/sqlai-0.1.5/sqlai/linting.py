rules = """
- Uppercase: SQL keywords (e.g., SELECT), function names (e.g., SUM()), literals (NULL, TRUE, FALSE), and data types (e.g., INT, VARCHAR).
- Lowercase: Column names and identifiers.
- Enforce a maximum line length of 500 characters.
- Use 4 spaces per indentation level, never tabs.
- Place SQL keywords (SELECT, FROM etc) at the start of a new line, left-aligned.
- Indent selected columns one level under SELECT, with one column per line.
- Indent JOIN conditions (ON ...) one level under the JOIN keyword.
- Indent subqueries one level more than the surrounding query.
- Align closing parentheses with the line containing the corresponding opening keyword (SELECT, FROM, etc.).
"""