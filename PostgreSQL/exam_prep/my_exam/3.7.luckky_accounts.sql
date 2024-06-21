SELECT 	
	CONCAT_WS(' ', a.id, a.username) AS id_username,
	a.email

FROM accounts as a

JOIN accounts_photos as ap
	ON ap.account_id = a.id

WHERE ap.account_id = ap.photo_id
ORDER BY id_username;