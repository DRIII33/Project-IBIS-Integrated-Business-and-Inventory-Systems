CREATE OR REPLACE VIEW `driiiportfolio.logistics_gold.vw_inventory_health` AS
SELECT
  sku,
  description,
  current_qty,
  min_stock,
  CASE 
    WHEN current_qty < min_stock THEN 'REORDER REQUIRED'
    WHEN current_qty > max_stock THEN 'OVERSTOCKED'
    ELSE 'HEALTHY'
  END AS stock_status,
  -- Identifying discrepancies from Cycle Counts
  (SELECT SUM(variance_detected) 
   FROM `driiiportfolio.raw_logistics.warehouse_transactions` t 
   WHERE t.sku = i.sku AND transaction_type = 'CYCLE_COUNT') AS net_shrinkage
FROM `driiiportfolio.logistics_silver.stg_inventory` i;
