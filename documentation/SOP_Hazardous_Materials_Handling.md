# SOP: Hazardous Materials (HAZMAT) Handling & Storage
**Document ID:** LOG-SOP-002
**Effective Date:** 2025-10-27
**Owner:** Daniel Rodriguez III - Data Center Logistics Lead
**Compliance Standard:** OSHA / Regional Environmental Safety

## 1. Objective
To ensure the safe handling, compliant storage, and accurate documentation of all Hazardous Materials entering the Equinix IBX facility. This SOP mitigates risk to personnel and infrastructure while ensuring audit readiness.

## 2. Scope
Applies to all flammable, corrosive, toxic, or reactive materials, including but not limited to: industrial cleaners, backup battery electrolytes, and thermal compounds.

## 3. Receiving Protocol
**WARNING:** *Do not accept damaged or leaking HAZMAT packages.*

1.  **Visual Inspection:** Check for leakages, odors, or packaging damage upon arrival.
2.  **MSDS Verification:**
    * Locate the Material Safety Data Sheet (MSDS) included with the shipment.
    * Scan/Upload the MSDS to the *Project IBIS* Compliance Ledger.
    * **STOP:** If MSDS is missing, quarantine the item and contact the vendor immediately.
3.  **Labeling:** Apply an internal "HAZMAT-Active" tracking tag with the date of receipt and expiration.

## 4. Storage Compatibility Rules
* **Flammables (Class 3):** Must be stored in approved yellow safety cabinets with self-closing doors.
* **Corrosives (Class 8):** Store on low shelves in corrosion-resistant trays. **NEVER** store with flammables.
* **Batteries:** Store in cool, dry, ventilated areas away from conductive materials.

## 5. Vendor Partnership & Audits
* **Vendor Handoff:** Coordinate with approved waste disposal partners (e.g., CleanHarbors) for the removal of expired chemicals.
* **Audit Cadence:**
    * **Weekly:** Internal visual inspection of storage cabinets (Lead).
    * **Quarterly:** Third-party vendor safety audit.
* **Record Keeping:** All disposal manifests must be retained for 3 years in the *Project IBIS* database.

## 6. JD Alignment & Process Improvement
### Job Description Mapping
* *"Partners with external vendors as needed to ensure proper delivery, handling, and complex storage of hazardous materials."*
* *"Ensures compliance with hazardous materials protocols as described by regional regulatory bodies."*

### Before & After Impact (Project IBIS Case Study)
* **Before:** Inconsistent MSDS filing led to "Audit Warnings" during safety inspections.
* **After:** Implemented digital MSDS linking in the Inventory System (SQL Join), achieving 100% Audit Readiness and zero safety violations.
