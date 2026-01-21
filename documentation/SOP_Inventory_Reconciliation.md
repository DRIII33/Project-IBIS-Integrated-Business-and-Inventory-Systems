# SOP: Inventory Reconciliation & Variance Analysis
**Document ID:** LOG-SOP-003
**Effective Date:** 2025-10-27
**Owner:** Daniel Rodriguez III - Data Center Logistics Lead

## 1. Objective
To maintain 99.9% inventory accuracy through systematic cycle counts and rigorous Root Cause Analysis (RCA) of discrepancies. This ensures that digital records match physical reality, preventing stock-outs and project delays.

## 2. Procedure
### Step 1: Cycle Count Execution
* **Frequency:** Top 20% high-value SKUs counted weekly; remaining SKUs counted monthly (ABC Analysis).
* **Blind Counts:** Operators count physical items *without* seeing the expected system quantity to prevent bias.

### Step 2: Variance Identification
* Compare Physical Count vs. System Record.
* **Tolerance:**
    * High-Value (>$1000): 0% Variance allowed.
    * Consumables (<$10): ±2% Variance allowed.

### Step 3: Root Cause Analysis (RCA)
If a variance exceeds tolerance, the Logistics Lead must investigate:
1.  **Transaction History:** Check for unposted receipts or transfers in the last 24 hours.
2.  **Adjacent Bins:** check neighboring locations for misplaced items.
3.  **Packaging Issues:** Verify if "Unit of Measure" (Pack vs. Each) caused the error.

### Step 4: Adjustment & Reporting
1.  **System Adjustment:** If the item is confirmed missing, process a "Shrinkage Adjustment" in the WMS.
2.  **RCA Tagging:** Categorize the loss (e.g., "Theft," "Vendor Error," "Data Entry Error") for trend analysis.
3.  **Executive Report:** Submit monthly "Net Inventory Variance" report to Operations Management.

## 3. JD Alignment & Process Improvement
### Job Description Mapping
* *"Leads periodic stock checks to ensure accuracy and proactively makes adjustments."*
* *"Controls stock inventory... and uses a high degree of initiative to resolve issues."*

### Before & After Impact (Project IBIS Case Study)
* **Before:** Reactive annual counts resulted in significant "Phantom Inventory" and project delays.
* **After:** Implemented weekly "Blind Cycle Counts" and RCA workflows, reducing annual shrinkage by 65% and improving project delivery timelines.
