-- ====================================
-- Bronze Layer Validation
-- ====================================

SELECT COUNT(*) total_transactions
FROM bronze_transactions;

SELECT MIN(event_time) oldest_event,
       MAX(event_time) latest_event
FROM bronze_transactions;

SELECT country,
       COUNT(*) transaction_count
FROM bronze_transactions
GROUP BY country
ORDER BY transaction_count DESC;

SELECT device_type,
       COUNT(*) transaction_count
FROM bronze_transactions
GROUP BY device_type
ORDER BY transaction_count DESC;

SELECT *
FROM bronze_transactions
WHERE amount <= 0;

SELECT *
FROM bronze_transactions
WHERE transaction_id IS NULL;
