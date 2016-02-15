SELECT 
  `pdb_id`,
  `chain`,
  COUNT(*)
FROM
  `8000_filtered_src`
WHERE 1
GROUP BY
  `pdb_id`,
  `chain`
