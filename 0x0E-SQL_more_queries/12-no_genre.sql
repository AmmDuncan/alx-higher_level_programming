-- Show all shows
SELECT title, genre_id
FROM tv_shows ts LEFT OUTER JOIN tv_show_genres tsg
ON ts.id = tsg.show_id
WHERE genre_id IS NULL
ORDER BY title ASC, genre_id ASC;
