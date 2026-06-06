-- ====================================
-- Silver Layer Validation
-- ====================================

SELECT COUNT(*) total_records
FROM silver_transactions;

SELECT COUNT(*) late_events
FROM silver_transactions
WHERE late_event = TRUE;

SELECT
    country,
    COUNT(*) total_transactions
FROM silver_transactions
GROUP BY country
ORDER BY total_transactions DESC;

SELECT
    device_type,
    COUNT(*) total_transactions
FROM silver_transactions
GROUP BY device_type
ORDER BY total_transactions DESC;

SELECT
    AVG(amount) avg_transaction_amount
FROM silver_transactions;

SELECT
    MAX(amount) highest_transaction
FROM silver_transactions;
