//write a SQL query to list the names of all people who have directed a movie that received a rating of at least 9.0
SELECT name from people
JOIN directors ON people.id = directors.person_id
JOIN movies ON directors.movie_id = movies.id
JOIN ratings on movies.id = ratings.movie_id
WHERE rating >= 9;