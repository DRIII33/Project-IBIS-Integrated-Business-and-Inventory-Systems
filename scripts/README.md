## Agining Shipments and Inventory shrinkage

To replicate the high-precision environment of an Equinix data center, I implemented a SQL architecture that separates raw ingestion from business-ready analytics.
These views automate the identification of Aging Shipments and Inventory Shrinkage, allowing the Logistics Lead to pivot from manual data entry to proactive problem-solving and independent action.
---

'/* STEP 0: ARCHITECTURE SETUP
Objective: Create the empty containers for the Silver (Cleaned) and Gold (Analytics) layers.
*/

CREATE SCHEMA IF NOT EXISTS `driiiportfolio.logistics_silver`
OPTIONS(location="US");

CREATE SCHEMA IF NOT EXISTS `driiiportfolio.logistics_gold`
OPTIONS(location="US");
'
