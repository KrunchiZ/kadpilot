SELECT 
    SUM(CASE WHEN cashback != 'N/A' THEN 1 ELSE 0 END) AS Cashback,
    SUM(CASE WHEN petrol != 'N/A' THEN 1 ELSE 0 END) AS Petrol,
    SUM(CASE WHEN rewards != 'N/A' THEN 1 ELSE 0 END) AS Rewards,
    SUM(CASE WHEN travel != 'N/A' THEN 1 ELSE 0 END) AS Travel
FROM credit_cards;