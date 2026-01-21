CREATE OR REPLACE TABLE `driiiportfolio.logistics_silver.stg_shipments` AS
SELECT
  shipment_id,
  type,
  vendor_oem,
  CAST(created_at AS TIMESTAMP) AS created_at,
  status,
  tracking_number,
  priority
FROM `driiiportfolio.raw_logistics.shipments_aging`;
