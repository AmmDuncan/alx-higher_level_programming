-- Get dexter movie genres
SELECT g.name 
FROM tv_shows t
	INNER JOIN tv_show_genres tvg
		ON t.id = tvg.show_id
	INNER JOIN tv_genres g
		ON tvg.genre_id = g.id
WHERE title = "Dexter"
ORDER BY g.name
