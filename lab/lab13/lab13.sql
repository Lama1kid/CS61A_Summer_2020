.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet FROM students WHERE color = 'blue' and pet = 'dog';

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song FROM students WHERE color = 'blue' and pet = 'dog';


CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color, b.color FROM students AS a JOIN students AS b 
        WHERE a.time < b.time AND a.song = b.song AND a.pet = b.pet;


CREATE TABLE sevens AS
  SELECT seven FROM students JOIN numbers
        WHERE students.time = numbers.time AND students.number = 7 AND numbers.'7' = 'True';


CREATE TABLE favpets AS
  SELECT pet, count(*) FROM students
        GROUP BY pet ORDER BY count(*) DESC limit 10;


CREATE TABLE dog AS
  SELECT * FROM favpets WHERE pet = 'dog';


CREATE TABLE bluedog_agg AS
  SELECT song, count(*) FROM bluedog_songs
        GROUP BY song ORDER BY count(*) DESC;


CREATE TABLE instructor_obedience AS
  SELECT seven, instructor, count(*) FROM students
        WHERE seven = '7' GROUP BY instructor ORDER BY count(*);

