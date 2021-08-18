-- write a SQL query to list the titles of the five highest rated movies (in order) that Chadwick Boseman starred in, starting with the highest rated.
SELECT movies.title FROM movies JOIN ratings ON movies.id = ratings.movie_id WHERE movies.id IN (SELECT stars.movie_id FROM stars WHERE stars.person_id IN (SELECT people.id FROM people WHERE people.name = "Chadwick Boseman"))

ORDER BY rating DESC
LIMIT 5