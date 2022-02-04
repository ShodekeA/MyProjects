
use world
--1
select COUNT(ID) from city
where countrycode = "USA"

--2
select NAME COUNTRY_NAME, lifeExpectancy, POPULATION from country
where name = "Argentina"

--3
select name, lifeExpectancy from country 
where lifeExpectancy is not null 
order by lifeExpectancy asc
limit 1

--4
SELECT ci.Name
FROM city AS ci
JOIN country as co
ON ci.id = co.capital
WHERE ci.countryCode = "ESP"

SELECT co.name Country_Name, ci.Name Capital_city
FROM city ci, country co
where ci.id = co.capital and ci.countryCode = "ESP"

--5
select c.name, ctl.language, c.region from country c, COUNTRYLANGUAGE ctl
where ctl.countrycode = c.Code and c.Region like "%Southeast%"

select c.name, ctl.language, c.region 
from country c
JOIN COUNTRYLANGUAGE ctl
ON ctl.countrycode = c.Code and c.Region like "%Southeast%"

--6
select name CITY_NAME from city
where name like "F%"
limit 25

--7
select count(ci.name) Chinese_Cities from country co, city ci
where co.name = "China" and co.code = ci.countrycode

select ci.name, co.code from country co, city ci
where co.name = "China" and co.code = ci.countrycode


--8
select name, population from country
where population > 0
order by population asc
limit 1

--9
select count(code) from country

--10
select name Country_name, population from country
order by population desc
limit 10

-- 11
select ci.name, ci.population from city ci, country co
where co.name = "Japan" and co.code = ci.countrycode
order by ci.population desc
limit 5

--12
select name, code from country
where Headofstate like "%Elisabeth%"

--13

select code, name, population/surfacearea as POP_TO_AREA from country
where population is not null and surfaceArea is not null and population > 0
order by POP_TO_AREA asc
limit 10

--14

select DISTINCT Language
from COUNTRYLANGUAGE
order by language

--15
SELECT CODE, NAME FROM COUNTRY
WHERE GNP > 0 
ORDER BY gnp desc
limit 10

--16

select name Country_name, code, region, surfacearea
from country
order by surfacearea desc
limit 10

--17

select * from COUNTRYLANGUAGE
where language = "French" and percentage > 50

--18

select name Country_Name, lifeExpectancy from country
where lifeExpectancy is not null
order by lifeExpectancy asc
limit 1

--19

select governmentForm , count(governmentForm) 
from country
group by governmentForm
order by count(governmentForm) desc
limit 1


--20
select COUNT(*) from country
where IndepYear >= "1970"

 

select * from cITY
limit 1
select * from country 
limit 10
SELECT * FROM COUNTRYLANGUAGE
LIMIT 1

