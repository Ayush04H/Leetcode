SELECT 
    b.Score, 
	(SELECT COUNT(DISTINCT a.Score) FROM Scores a WHERE b.Score <= a.Score) as `Rank`
FROM Scores b ORDER BY `Rank`