-- ====================================
-- Dashboard 1
-- Fraud by Category
-- ====================================

SELECT
fraud_category,
COUNT(*) transaction_count
FROM gold_transactions
GROUP BY fraud_category;

-- ====================================
-- Dashboard 2
-- Top Risk Customers
-- ====================================

SELECT
customer_id,
avg_fraud_score,
txn_count
FROM customer_risk
ORDER BY avg_fraud_score DESC
LIMIT 20;

-- ====================================
-- Dashboard 3
-- Fraud By Country
-- ====================================

SELECT
country,
COUNT(*) fraud_count
FROM gold_transactions
WHERE fraud_score >= 2
GROUP BY country
ORDER BY fraud_count DESC;

-- ====================================
-- Dashboard 4
-- Fraud By Device
-- ====================================

SELECT
device_type,
COUNT(*) fraud_count
FROM gold_transactions
WHERE fraud_score >= 2
GROUP BY device_type
ORDER BY fraud_count DESC;

-- ====================================
-- Dashboard 5
-- High Value Fraud
-- ====================================

SELECT
transaction_id,
customer_id,
amount
FROM gold_transactions
WHERE amount > 50000
ORDER BY amount DESC;

-- ====================================
-- Dashboard 6
-- Late Arriving Events
-- ====================================

SELECT
COUNT(*) total_late_events
FROM silver_transactions
WHERE late_event = TRUE;

-- ====================================
-- Dashboard 7
-- Daily Fraud Trend
-- ====================================

SELECT
DATE(event_time) txn_date,
COUNT(*) fraud_transactions
FROM gold_transactions
WHERE fraud_score >= 2
GROUP BY DATE(event_time)
ORDER BY txn_date;

-- ====================================
-- Dashboard 8
-- Fraud Rate
-- ====================================

SELECT

ROUND(
100.0 *
SUM(
CASE
WHEN fraud_score >= 2
THEN 1
ELSE 0
END
)
/
COUNT(*),
2
) fraud_percentage

FROM gold_transactions;

-- ====================================
-- Dashboard 9
-- Top 10 Largest Transactions
-- ====================================

SELECT
transaction_id,
customer_id,
amount
FROM gold_transactions
ORDER BY amount DESC
LIMIT 10;

-- ====================================
-- Dashboard 10
-- Customer Risk Distribution
-- ====================================

SELECT

CASE

WHEN avg_fraud_score >= 3
THEN 'HIGH'

WHEN avg_fraud_score >= 2
THEN 'MEDIUM'

ELSE 'LOW'

END risk_level,

COUNT(*) customers

FROM customer_risk

GROUP BY

CASE

WHEN avg_fraud_score >= 3
THEN 'HIGH'

WHEN avg_fraud_score >= 2
THEN 'MEDIUM'

ELSE 'LOW'

END;
