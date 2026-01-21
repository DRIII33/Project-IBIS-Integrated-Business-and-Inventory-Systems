/* FILE: silver_layer_standardization.sql
PURPOSE: Cast data types and handle missing metadata in the inventory system.
MAPPING: JD Section 'Documentation & System Updates'
*/

CREATE OR REPLACE TABLE `driiiportfolio.logistics_silver.stg_inventory` AS
SELECT
  sku,
  UPPER(description) AS description,
  CAST(min_stock AS INT64) AS min_stock,
  CAST(max_stock AS INT64) AS max_stock,
  CAST(current_qty AS INT64) AS current_qty,
  bin_location,
  CAST(is_hazmat AS BOOL) AS is_hazmat,
  IFNULL(hazmat_class, 'NON-HAZARDOUS') AS hazmat_class,
  IFNULL(msds_link, 'PENDING_UPLOAD') AS msds_link
FROM `driiiportfolio.raw_logistics.inventory_master`;
