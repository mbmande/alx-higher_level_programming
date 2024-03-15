-- ====
select `state`, MAX(`value`) AS `high_tempo`
FROM `temperature`
GROUP BY `state`
ORDER BY `state`;
