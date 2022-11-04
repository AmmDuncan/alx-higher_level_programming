-- Show all shows
SELECT title, genre_id
FROM tv_shows ts LEFT JOIN tv_show_genres tsg
ON ts.id = tsg.show_id
ORDER BY title ASC, genre_id ASC;
