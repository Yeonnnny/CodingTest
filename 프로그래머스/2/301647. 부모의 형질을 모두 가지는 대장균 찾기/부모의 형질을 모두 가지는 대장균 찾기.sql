SELECT C.ID, C.GENOTYPE, P.GENOTYPE AS PARENT_GENOTYPE
FROM ECOLI_DATA P
LEFT OUTER JOIN ECOLI_DATA C
ON P.ID = C.PARENT_ID
WHERE (C.GENOTYPE & P.GENOTYPE) = P.GENOTYPE
ORDER BY 1 ASC;
