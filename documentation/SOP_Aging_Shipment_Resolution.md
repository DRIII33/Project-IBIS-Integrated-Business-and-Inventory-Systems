# SOP: Aging Shipment Resolution & Escalation Protocol
**Document ID:** LOG-SOP-001
**Effective Date:** 2025-10-27
**Owner:** Daniel Rodriguez III - Data Center Logistics Lead
**Review Cycle:** Quarterly

## 1. Objective
To establish a standardized workflow for identifying, tracking, and resolving inbound shipments that have exceeded standard dwell times. This protocol directly supports the "Shipment Spotlight" initiative to prevent asset stagnation and ensure SLA compliance.

## 2. Scope
Applies to all inbound shipments (OEM Hardware, Cabling, Consumables) remaining in "Received" or "Pending" status for more than 5 days.

## 3. Aging Thresholds & Action Matrix
The Logistics Lead must execute the following actions based on the "Days Aging" metric calculated in the *Project IBIS* dashboard.

| Aging Category | Threshold | Responsible Party | Required Action |
| :--- | :--- | :--- | :--- |
| **Active Monitoring** | 5-13 Days | Logistics Coordinator | Verify bin location accuracy and check for "Partial Receipt" flags. |
| **Warning** | 14-29 Days | Logistics Lead | Contact Internal Customer (Engineer/PM) to confirm project readiness. |
| **Critical Aging** | 30-89 Days | Logistics Lead | Initiate "Stagnant Asset" ticket. Escalate to Customer Service Associate (CSA) for client outreach. |
| **Abandoned** | 90+ Days | Ops Manager | Execute "Return to Vendor" (RTV) or Disposal Protocol per abandoned equipment policy. |

## 4. Resolution Procedure
### Phase 1: Verification (Days 5-13)
1.  **Physical Audit:** Locate the physical asset in the staging area.
2.  **System Check:** Ensure the shipping manifest matches the digital entry in the Warehouse Management System (WMS).
3.  **Gap Analysis:** If the item is physically present but digitally "In-Transit," update status to "Received" immediately.

### Phase 2: Escalation (Days 14-89)
1.  **Stakeholder Outreach:** Send a formal notification to the recipient listed on the purchase order.
2.  **Blocker Identification:** Determine if the delay is due to:
    * Missing Licensing/Software
    * Project Cancellation
    * Lack of Rack Space
3.  **Documentation:** Log all communications in the shipment record notes.

### Phase 3: Disposition (Days 90+)
1.  **Abandonment Notice:** Issue final warning to the asset owner.
2.  **Removal:** If no response within 48 hours, move asset to "Disposal/RTV" staging zone.
3.  **System Closeout:** Mark shipment as "Closed - Abandoned" to remove it from the active inventory valuation.

## 5. JD Alignment & Process Improvement
### Job Description Mapping
* *"Manages shipment spotlight and shipment dashboard for customers inbound/outbound shipments."*
* *"Use the aging shipment business processes/tools for shipments over 5, 14, 30, and 90 days."*

### Before & After Impact (Project IBIS Case Study)
* **Before:** Manual spreadsheet tracking led to $200k+ in "Ghost Inventory" (assets lost in staging for >6 months).
* **After:** Automated SQL alerts for 30-day thresholds reduced dwell time by 40% and reclaimed 15% of warehouse floor space.
