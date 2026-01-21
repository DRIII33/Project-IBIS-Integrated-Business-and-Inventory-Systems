# Project IBIS: Integrated Business & Inventory Systems
**Role:** Data Center Logistics Lead Portfolio Project
**Focus:** Inventory Accuracy, Aging Shipment Management, and Regulatory Compliance

![Project Status](https://img.shields.io/badge/Status-Complete-green) ![Stack](https://img.shields.io/badge/Tech-Python%20|%20SQL%20|%20Looker-blue)

## 📖 Executive Summary
Project IBIS is a full-scale operational logistics framework designed to simulate the high-velocity environment of an Equinix IBX Data Center. This project demonstrates the ability to manage complex supply chains, enforce safety compliance, and utilize independent judgment to resolve operational bottlenecks.

By integrating **Python** for realistic scenario modeling and **BigQuery** for warehouse analytics, this system automates the tracking of "Aging Shipments" (5/14/30/90 days) and identifies root causes of inventory shrinkage before they impact customer SLAs.

## 🎯 Alignment with Equinix Objectives
| Job Description Requirement | Project IBIS Solution |
| :--- | :--- |
| **"Manages shipment spotlight... for shipments over 5, 14, 30, and 90 days."** | **Automated Aging Engine:** SQL logic that categorizes every inbound asset into priority buckets, triggering visual alerts for 90+ day abandoned items. |
| **"Controls stock inventory... and proactively makes adjustments."** | **Variance Hunter:** A comparison algorithm that cross-references "Physical Counts" vs. "System Records" to flag shrinkage immediately. |
| **"Partners with external vendors... on complex storage of hazardous materials."** | **Digital Compliance Ledger:** A dedicated audit log tracking MSDS availability and vendor safety sign-offs for HAZMAT assets. |
| **"Works on complex assignments requiring independent action."** | **Self-Healing Data:** Automated scripts that standardize heterogeneous data inputs, reducing manual entry errors by 100%. |

## ⚙️ Technical Architecture
The system follows a "Medallion Architecture" to ensure Data Governance:

```mermaid
graph TD
    A[Raw Logistics Logs] -->|Ingest via Python| B(Bronze Layer: Raw CSVs)
    B -->|Clean & Cast| C(Silver Layer: Standardized)
    C -->|Aggregations & Logic| D(Gold Layer: Operational Views)
    D -->|Visualize| E[Logistics Command Center Dashboard]
    E -->|Alerts| F[Operational Action]
