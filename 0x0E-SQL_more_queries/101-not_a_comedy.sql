-- Select all shows not comedy
SELECT DISTINCT
	t.title
FROM
	tv_shows t
	LEFT JOIN tv_show_genres tvg ON t.id = tvg.show_id
	LEFT JOIN tv_genres g ON tvg.genre_id = g.id
WHERE
	g.name IS NULL
	OR "Comedy" NOT IN(
		SELECT
			gs.name FROM tv_shows tv
		LEFT JOIN tv_show_genres tvg ON t.id = tvg.show_id
		LEFT JOIN tv_genres gs ON tvg.genre_id = gs.id)
ORDER BY t.title;