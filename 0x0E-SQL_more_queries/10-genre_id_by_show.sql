-- Show tv shows
SELECT title, genre_id
FROM tv_shows tvs INNER JOIN tv_show_genres tvsg
ON tvs.id = tvsg.show_id
ORDER BY title ASC, genre_id ASC;
