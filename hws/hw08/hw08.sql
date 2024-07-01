CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name, size FROM dogs JOIN sizes
        WHERE height <= max AND height > min;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT child FROM parents JOIN dogs
        WHERE parent = name ORDER BY height DESC;


-- Filling out this helper table is optional
CREATE TABLE siblings AS
    SELECT with_same_parent.child_a AS one_name, with_same_parent.child_b AS another_name, size FROM 
    (SELECT a.child AS child_a, b.child AS child_b FROM parents AS a JOIN parents AS b
            WHERE a.child < b.child AND a.parent = b.parent) AS with_same_parent JOIN
    (SELECT c.name AS name_c, d.name AS name_d, c.size AS size FROM size_of_dogs AS c JOIN size_of_dogs AS d
            WHERE c.size = d.size) AS same_size_dogs
    WHERE with_same_parent.child_a= same_size_dogs.name_c AND with_same_parent.child_b = same_size_dogs.name_d;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
    SELECT one_name || " and " || another_name || " are " || size || " siblings " FROM siblings; 


-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks_helper(dogs, stack_height, last_height, n);

-- Add your INSERT INTOs here
INSERT INTO stacks_helper 
    SELECT name, height, height, 1 FROM dogs;
INSERT INTO stacks_helper
    SELECT dogs || " ," || name, stack_height + height, height, 2 FROM stacks_helper JOIN dogs
    WHERE dogs NOT LIKE "%" || name || "%" AND height >= last_height;
INSERT INTO stacks_helper
    SELECT dogs || " ," || name, stack_height + height, height, 3 FROM stacks_helper JOIN dogs
    WHERE dogs NOT LIKE "%" || name || "%" AND height >= last_height;
INSERT INTO stacks_helper
    SELECT dogs || " ," || name, stack_height + height, height, 4 FROM stacks_helper JOIN dogs
    WHERE dogs NOT LIKE "%" || name || "%" AND height >= last_height;

CREATE TABLE stacks AS
  SELECT dogs, stack_height FROM stacks_helper
    WHERE n = 4 AND stack_height >= 170 ORDER BY stack_height;

