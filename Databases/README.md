# QA SQL ASSESSMENT!

## My Answers to the SQL Assessment

### Question 1) Select all Actors from the table.
SELECT first_name, last_name FROM actor;
### Question 2) Find the actor with the first name “John”.
SELECT * FROM actor WHERE first_name = 'John';
### Question 3) Find all actors with the surname “Neeson”.
SELECT * FROM actor WHERE last_name = 'Neeson';
### Question 4) Find all actors with Id numbers divisible by 10.
SELECT * FROM actor WHERE actor_id%10 = 0;
### Question 5) What is the description of the movie with ID of 100?
SELECT description FROM film WHERE film_id = 100;
### Question 6) Find every movie with a rating of “R”.
SELECT * FROM film WHERE rating = 'R';
### Question 7) Find every movie except those with a rating of “R”.
SELECT * FROM film WHERE NOT rating = 'R';
### Question 8) Find the 10 shortest movies.
SELECT * FROM film ORDER BY length ASC LIMIT 10;
### Question 9) Now return only the movie titles.
SELECT title FROM film;
### Question 10) Find all movies with Deleted Scenes.
SELECT * FROM film WHERE special_features = 'Deleted Scenes';
### Question 11) Which last names are not repeated?
SELECT DISTINCT last_name FROM actor;
### Question 12) Which last names appear more than once?
SELECT last_name FROM actor GROUP BY last_name HAVING COUNT(*) > 1;
### Question 13) Which actor has appeared in the most films?
SELECT actor_id FROM film_actor GROUP BY actor_id ORDER BY COUNT(*) DESC LIMIT 1;
### Question 14) Is ‘Academy Dinosaur’ available for rent from Store 1?
SELECT film.film_id, store.store_id FROM film INNER JOIN store ON film.film_id = store.store_id WHERE film_id = 1;
### Question 15) When is ‘Academy Dinosaur’ due?
SELECT film.film_id, rental.return_date FROM film LEFT JOIN rental ON film.film_id AND rental.return_date WHERE film_id = 1 ORDER BY return_date DESC LIMIT 1;
### Question 16) What is that average running time of all the films in the database?
SELECT AVG(length) FROM film;
### Question 17) What is the average running time of films by category?
SELECT AVG(length),  category.category_id FROM film LEFT JOIN category ON film.length AND category.category_id GROUP BY category.category_id;
### Question 18) How many movies have Robots in them?
SELECT COUNT(title) FROM film WHERE description LIKE '%robot%';
### Question 19) Find the movie(s) with the longest runtime.
SELECT film.title, film.length FROM film ORDER BY length ASC;
### Question 20) Count how many movies were released in 2010.
SELECT COUNT(release_year) FROM film WHERE release_year = '2010';
### Question 21)
### Question 22)
### Question 23)
### Question 24)
### Question 25)
### Question 26)
### Question 27)
### Question 28)
### Question 29)
### Question 30)
