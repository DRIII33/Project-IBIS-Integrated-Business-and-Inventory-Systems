#INSTALL PACKAGES
!pip install pandas numpy
---------

import pandas as pd
import numpy as np
import uuid
import random
from datetime import datetime, timedelta

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)

class EquinixDataGenerator:
    def __init__(self, num_records=1000):
        self.num_records = num_records
        self.base_date = datetime.now() - timedelta(days=120)
        self.skus = [f"SKU-{random.randint(1000, 9999)}" for _ in range(50)]
        self.bins = [f"ZONE-{r}-{c}" for r in ['A', 'B', 'C'] for c in range(1, 20)]

    def generate_inventory_master(self):
        """Creates the 'System of Record' for inventory levels."""
        data = []
        for sku in self.skus:
            is_hazmat = random.random() < 0.15
            data.append({
                "sku": sku,
                "description": random.choice(["Fiber Transceiver", "Server Rail Kit", "Power Cord C13", "Line Card", "Cleaning Solvent"]),
                "min_stock": random.randint(10, 20),
                "max_stock": random.randint(50, 100),
                "current_qty": random.randint(5, 110),
                "bin_location": random.choice(self.bins),
                "is_hazmat": is_hazmat,
                "hazmat_class": random.choice(["Flammable", "Corrosive", "None"]) if is_hazmat else "None",
                "msds_link": f"https://docs.equinix.com/msds/{sku}.pdf" if (is_hazmat and random.random() > 0.1) else None # 10% missing link exception
            })
        return pd.DataFrame(data)

    def generate_shipments(self):
        """Generates inbound/outbound shipments with aging logic."""
        data = []
        statuses = ["DELIVERED", "IN-TRANSIT", "PENDING", "ABANDONED"]
        for i in range(self.num_records // 2):
            # Simulate aging: some shipments created 95 days ago and never updated
            created_at = self.base_date + timedelta(days=random.randint(0, 115))
            status = random.choices(statuses, weights=[0.7, 0.1, 0.15, 0.05])[0]

            data.append({
                "shipment_id": str(uuid.uuid4())[:8].upper(),
                "type": random.choice(["INBOUND", "OUTBOUND"]),
                "vendor_oem": random.choice(["Cisco", "Juniper", "Dell", "Panduit"]),
                "created_at": created_at,
                "status": status,
                "tracking_number": f"1Z{random.randint(100000, 999999)}",
                "priority": random.choice(["Standard", "Expedited", "Next Day Air"])
            })
        return pd.DataFrame(data)

    def generate_transactions(self, inventory_df):
        """Records granular warehouse movements and physical count variances."""
        data = []
        types = ["RECEIVE", "PICK", "TRANSFER", "CYCLE_COUNT"]
        for _ in range(self.num_records):
            sku_row = inventory_df.sample(1).iloc[0]
            qty = random.randint(1, 10)

            # Simulate Shrinkage during CYCLE_COUNT
            trans_type = random.choice(types)
            variance = 0
            if trans_type == "CYCLE_COUNT" and random.random() < 0.08:
                variance = -random.randint(1, 3) # System shows more than physical

            data.append({
                "transaction_id": str(uuid.uuid4()),
                "timestamp": self.base_date + timedelta(days=random.randint(0, 110)),
                "sku": sku_row['sku'],
                "transaction_type": trans_type,
                "quantity": qty,
                "variance_detected": variance,
                "operator_id": f"EMP-{random.randint(100, 999)}",
                "bin_id": sku_row['bin_location']
            })
        return pd.DataFrame(data)

    def generate_software_licenses(self):
        """Tracks critical software assets as per JD requirements."""
        data = []
        softwares = ["VMWare ESXi", "RedHat Enterprise", "Windows Server 2022", "Cisco IOS-XE"]
        for sw in softwares:
            total = random.randint(50, 200)
            in_use = int(total * random.uniform(0.7, 1.1)) # Potential over-utilization
            data.append({
                "software_name": sw,
                "total_licenses": total,
                "licenses_in_use": in_use,
                "renewal_date": datetime.now() + timedelta(days=random.randint(-30, 365)),
                "compliance_status": "PASS" if in_use <= total else "FAIL"
            })
        return pd.DataFrame(data)

    def generate_hazmat_compliance_log(self, inventory_df):
        """Generates a regulatory audit log for HAZMAT storage safety."""
        hazmat_items = inventory_df[inventory_df['is_hazmat'] == True]
        data = []
        vendors = ["SafetyFirst Inc.", "CleanHarbors", "Global-Spec Logistics"]

        for _, item in hazmat_items.iterrows():
            # Generate 2-3 inspections per hazardous SKU
            for _ in range(random.randint(1, 3)):
                data.append({
                    "audit_id": f"AUD-{random.randint(1000, 9999)}",
                    "sku": item['sku'],
                    "vendor_partner": random.choice(vendors),
                    "inspection_date": self.base_date + timedelta(days=random.randint(0, 110)),
                    "safety_status": random.choices(["COMPLIANT", "NON-COMPLIANT"], weights=[0.9, 0.1])[0],
                    "inspector_notes": "All labels legible and storage temperature within range."
                })
        return pd.DataFrame(data)

# Execution
if __name__ == "__main__":
    generator = EquinixDataGenerator(num_records=2000)

    # 1. Generate Primary Datasets
    inventory = generator.generate_inventory_master()
    shipments = generator.generate_shipments()
    transactions = generator.generate_transactions(inventory)
    software = generator.generate_software_licenses()

    # 2. Generate the 5th File: HAZMAT Compliance Audit
    hazmat_audit = generator.generate_hazmat_compliance_log(inventory)

    # 3. Save all 5 files for BigQuery Ingestion
    inventory.to_csv("inventory_master.csv", index=False)
    shipments.to_csv("shipments_aging.csv", index=False)
    transactions.to_csv("warehouse_transactions.csv", index=False)
    software.to_csv("software_compliance.csv", index=False)
    hazmat_audit.to_csv("hazmat_compliance_log.csv", index=False) # The 5th File

    print("Project IBIS: 5 Operational Datasets Generated Successfully.")
    print("Files created: inventory_master.csv, shipments_aging.csv, warehouse_transactions.csv, software_compliance.csv, hazmat_compliance_log.csv")
