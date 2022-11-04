-- Get shows by genre
SELECT title, g.name
FROM tv_shows t
	LEFT JOIN tv_show_genres tvg
		ON t.id = tvg.show_id
	LEFT JOIN tv_genres g
		ON tvg.genre_id = g.id
ORDER BY title, g.name;
