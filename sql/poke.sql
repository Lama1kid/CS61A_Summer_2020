create table
    ints as 
        select 5 union
        select n+1 from ints where n < 15;
