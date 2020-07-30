//write a SQL query to determine the average rating of all movies released in 2012
SELECT avg(rating) FROM ratings
JOIN movies ON ratings.movie_id = movies.id
WHERE year = 2012;