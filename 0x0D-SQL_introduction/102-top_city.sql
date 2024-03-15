-- =====
-- ======

SELECT 'city', AVG('value') AS 'tempo'
FROM temperatures'
where 'month' = 7 or 'month' = 8
group by 'city'
order by 'tempo' DESC
limit 3;
