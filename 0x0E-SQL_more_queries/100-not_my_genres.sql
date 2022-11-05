-- Select genres not linked to the show Dexter
SELECT DISTINCT g.name
FROM tv_genres g INNER JOIN tv_show_genres tvg
ON g.id = tvg.genre_id
WHERE g.name NOT IN (
	SELECT g.name
	FROM tv_genres g 
	INNER JOIN tv_show_genres tvg
		ON g.id = tvg.genre_id
	INNER JOIN tv_shows t
		ON tvg.show_id = t.id
	WHERE t.title = 'Dexter'
)
ORDER BY g.name;
