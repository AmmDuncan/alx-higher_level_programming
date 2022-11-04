-- Count shows by genre
SELECT g.name as genre, COUNT(*) as number_of_shows
FROM tv_genres g INNER JOIN tv_show_genres tvg
ON g.id = tvg.genre_id
GROUP BY g.name
ORDER BY number_of_shows DESC;
