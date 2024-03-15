-- =====
-- ======

SELECT 'city', AVG('value') AS avg_tempo
FROM 'temporatures'
GROUP BY 'city'
ORDER BY 'avg_tempo' DESC;
