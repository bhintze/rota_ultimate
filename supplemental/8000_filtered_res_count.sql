SELECT
  `res_type`,
  COUNT(*) AS 'n'
FROM
  `8000_filtered_src`
WHERE 1
GROUP BY
  `res_type`
