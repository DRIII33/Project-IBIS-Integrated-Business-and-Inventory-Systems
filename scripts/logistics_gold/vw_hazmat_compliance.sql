CREATE OR REPLACE VIEW `driiiportfolio.logistics_gold.vw_hazmat_compliance` AS
SELECT
  i.sku,
  i.hazmat_class,
  i.msds_link,
  a.vendor_partner,
  a.inspection_date,
  a.safety_status,
  CASE 
    WHEN i.msds_link = 'PENDING_UPLOAD' THEN 'NON-COMPLIANT: MISSING MSDS'
    WHEN a.safety_status = 'NON-COMPLIANT' THEN 'NON-COMPLIANT: VENDOR EXCEPTION'
    WHEN DATE_DIFF(CURRENT_DATE(), CAST(a.inspection_date AS DATE), DAY) > 90 THEN 'WARNING: AUDIT OVERDUE'
    ELSE 'COMPLIANT'
  END AS compliance_verdict
FROM `driiiportfolio.logistics_silver.stg_inventory` i
LEFT JOIN `driiiportfolio.raw_logistics.hazmat_compliance_log` a ON i.sku = a.sku
WHERE i.is_hazmat = TRUE;
