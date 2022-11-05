-- List all genres by rating
SELECT
	g.name,
	SUM(rate) AS rating
FROM
	tv_shows t
	INNER JOIN tv_show_genres tvg ON t.id = tvg.show_id
	INNER JOIN tv_show_ratings tvr ON t.id = tvr.show_id
	INNER JOIN tv_genres g ON tvg.genre_id = g.id
GROUP BY g.name
ORDER BY rating DESC
