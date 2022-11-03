-- Select score and name from db
SELECT score, name FROM second_table
	WHERE name IS NOT NULL
	ORDER BY score DESC;
