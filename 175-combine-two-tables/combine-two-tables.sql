# Write your MySQL query statement below
SELECT 
    lastname,
    firstname,
    city,
    state
FROM Person 
LEFT JOIN Address
ON Person.personId=
Address.personid;
