-- Get dexter movie genres
SELECT title 
FROM tv_shows t
	INNER JOIN tv_show_genres tvg
		ON t.id = tvg.show_id
	INNER JOIN tv_genres g
		ON tvg.genre_id = g.id
WHERE g.name = "Comedy"
ORDER BY title;
