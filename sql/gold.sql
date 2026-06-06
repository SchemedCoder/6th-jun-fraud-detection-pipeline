-- ====================================
-- Fraud Summary
-- ====================================

SELECT fraud_category,
       COUNT(*) total
FROM gold_transactions
GROUP BY fraud_category;

-- ====================================
-- High Risk Customers
-- ====================================

SELECT *
FROM customer_risk
ORDER BY avg_fraud_score DESC
LIMIT 20;

-- ====================================
-- High Value Transactions
-- ====================================

SELECT *
FROM gold_transactions
WHERE high_value_flag = 1
ORDER BY amount DESC;

-- ====================================
-- Country Risk Analysis
-- ====================================

SELECT country,
       COUNT(*) risky_transactions
FROM gold_transactions
WHERE country_risk_flag = 1
GROUP BY country
ORDER BY risky_transactions DESC;

-- ====================================
-- Device Risk Analysis
-- ====================================

SELECT device_type,
       COUNT(*) risky_transactions
FROM gold_transactions
WHERE device_risk_flag = 1
GROUP BY device_type;
