CREATE OR REPLACE VIEW `driiiportfolio.logistics_gold.vw_shipment_spotlight` AS
SELECT
  shipment_id,
  vendor_oem,
  status,
  created_at,
  TIMESTAMP_DIFF(CURRENT_TIMESTAMP(), created_at, DAY) AS days_aging,
  CASE
    WHEN TIMESTAMP_DIFF(CURRENT_TIMESTAMP(), created_at, DAY) >= 90 THEN '90+ Days: ABANDONED / CSA ESCALATION'
    WHEN TIMESTAMP_DIFF(CURRENT_TIMESTAMP(), created_at, DAY) >= 30 THEN '30-89 Days: CRITICAL AGING'
    WHEN TIMESTAMP_DIFF(CURRENT_TIMESTAMP(), created_at, DAY) >= 14 THEN '14-29 Days: WARNING'
    WHEN TIMESTAMP_DIFF(CURRENT_TIMESTAMP(), created_at, DAY) >= 5  THEN '5-13 Days: ACTIVE MONITORING'
    ELSE '0-4 Days: NEW'
  END AS aging_priority_level
FROM `driiiportfolio.logistics_silver.stg_shipments`
WHERE status NOT IN ('DELIVERED', 'DISPATCHED');
