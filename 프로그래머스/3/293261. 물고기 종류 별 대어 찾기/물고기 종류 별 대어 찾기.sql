SELECT ID, FISH_NAME, LENGTH
FROM FISH_INFO F
JOIN FISH_NAME_INFO N
ON F.FISH_TYPE = N.FISH_TYPE
WHERE LENGTH = (SELECT MAX(LENGTH)
               FROM FISH_INFO
               WHERE FISH_TYPE = F.FISH_TYPE)
ORDER BY 1 ASC;

