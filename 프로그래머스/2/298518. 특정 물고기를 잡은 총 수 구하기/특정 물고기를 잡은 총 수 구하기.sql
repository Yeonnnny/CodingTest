SELECT COUNT(*) AS FISH_COUNT
FROM FISH_INFO I
JOIN FISH_NAME_INFO NI
ON I.FISH_TYPE = NI.FISH_TYPE
WHERE FISH_NAME IN ('BASS', 'SNAPPER');