-- Query 1: Top 10 cattle meat producers in 2024
SELECT area, value AS tonnes
FROM livestock_production
WHERE item = 'Meat of cattle with the bone, fresh or chilled'
  AND element = 'Production'
  AND unit = 't'
  AND year = 2024
ORDER BY value DESC
LIMIT 10;

-- Query 2: Fastest growth in chicken meat production, 2014 to 2024
SELECT a.area,
       a.value AS tonnes_2014,
       b.value AS tonnes_2024,
       ROUND((b.value - a.value) * 100.0 / a.value, 1) AS pct_growth
FROM livestock_production a
JOIN livestock_production b
  ON a.area = b.area AND a.item = b.item AND a.element = b.element AND a.unit = b.unit
WHERE a.item = 'Meat of chickens, fresh or chilled'
  AND a.element = 'Production'
  AND a.unit = 't'
  AND a.year = 2014
  AND b.year = 2024
  AND a.value >= 1000
ORDER BY pct_growth DESC
LIMIT 10;

-- Query 3: Total hen egg production across Africa (tonnes)
SELECT year, ROUND(SUM(value)) AS total_tonnes
FROM livestock_production
WHERE item = 'Hen eggs in shell, fresh'
  AND element = 'Production'
  AND unit = 't'
  AND year IN (1964, 1984, 2004, 2024)
GROUP BY year
ORDER BY year;