# Warranty and Replacement Policy

# KARTWAY OPERATING PROCEDURE: WP-402
**SUBJECT:** WARRANTY, DEFECT, AND REPAIR POLICY  
**EFFECTIVE DATE:** OCTOBER 1, 2026  
**APPLIES TO:** ALL TIER 1, TIER 2, AND SPECIALIST SUPPORT AGENTS  
**AUTHOR:** BEATRICE THORNE, DIRECTOR OF CUSTOMER OPERATIONS POLICY  

---

### 1.0 PURPOSE AND SCOPE
1.1 This document establishes the binding operational rules for handling product warranty claims, defect reporting, and resolution pathways for merchandise sold through the Kartway platform.  
1.2 Agents are strictly bound by the thresholds, deadlines, and decision rules contained herein. Discretionary deviations outside these parameters require prior written approval from a Tier 3 Escalations Manager.  

---

### 2.0 MANUFACTURER VERSUS KARTWAY WARRANTY DIVISION
2.1 **Manufacturer Warranty Period (Days 1 through 365):** For all items carrying a manufacturer warranty, the primary warranty obligation rests with the Original Equipment Manufacturer (OEM) for the first 365 calendar days from the date of delivery, subject to Section 3.0.  
2.2 **Kartway Direct Warranty Period (Days 1 through 30):** For all marketplace transactions, Kartway acts as the primary warranty guarantor for the first 30 calendar days post-delivery. During this window, the customer may elect to bypass the OEM and process a warranty claim directly through Kartway Support.  
2.3 **Marketplace Fulfillment Obligation:** For items sold by Third-Party Merchants via Kartway Fulfilled Services (KFS), Kartway manages the Tier 1 claim intake, but financial liability transfers to the merchant's escrow account on Day 31. For merchant-fulfilled items (FBM), Kartway enforces compliance with the Kartway Merchant Service Agreement (MSA) SLA of 48 hours for merchant-led warranty communication.  
2.4 **Out-of-Box Failures (DOA):** Any defect reported within 72 hours of confirmed carrier delivery is classified as Dead on Arrival (DOA). DOA claims are exclusively handled by Kartway operations, overriding standard OEM routing.  

---

### 3.0 COVERAGE PERIODS BY MERCHANDISE CATEGORY
3.1 Warranty coverage periods and Kartway direct support windows are strictly bound by the following product classifications:

| Category ID | Category Description | Kartway Direct Window | Standard Warranty Period | Extended Coverage Available |
| :--- | :--- | :--- | :--- | :--- |
| **CAT-01** | Consumer Electronics & Computing | 30 Days | 365 Days (OEM) | Yes (KartwayCare 2-Yr) |
| **CAT-02** | Large Home Appliances | 14 Days | 730 Days (2 Years OEM) | Yes (KartwayCare 3-Yr) |
| **CAT-03** | Apparel, Footwear, & Soft Goods | 30 Days | 90 Days (Kartway Direct) | No |
| **CAT-04** | Power Tools & Outdoor Equipment | 30 Days | 365 Days (OEM) | Yes (KartwayCare 2-Yr) |
| **CAT-05** | Home Goods & Non-Power Furnishings | 30 Days | 180 Days (Kartway Direct) | No |
| **CAT-06** | Certified Refurbished (All Types) | 15 Days | 180 Days (Kartway/Merchant) | No |

3.2 Claims submitted outside the applicable window defined in Section 3.1 shall be rejected by the agent using macro `MAC-WRN-EXPIRED`, unless covered by an active KartwayCare Service Plan registered under policy KP-881.

---

### 4.0 WARRANTY VOIDANCE CONDITIONS
4.1 A warranty claim shall be unconditionally denied if the item exhibits any of the following voidance conditions, verified via photographic evidence or physical inspection at the Kartway Returns Processing Center (RPC):
* **4.1.1 Liquid Ingestion:** Presence of internal corrosion, mineral deposits, or activation of any internal Liquid Contact Indicator (LCI) turning pink or red.
* **4.1.2 Unauthorized Modification:** Evidence of aftermarket repair, uncertified component swapping, or tampering with internal circuitry.
* **4.1.3 Physical Trauma:** Cracked screens, bent frames, or structural fractures resulting from drops, excessive force, or animal damage, excepting manufacturing metallurgical defects reported within the DOA window (Section 2.4).
* **4.1.4 Environmental Abuse:** Damage caused by operation outside manufacturer-specified thermal ranges (below -10°C or above 50°C for electronics) or heavy particulate/saline exposure.
* **4.1.5 Serial Number Alteration:** Missing, defaced, or illegible serial numbers or IMEI labels that prevent verification against the Kartway inventory database.

4.2 Normal wear and tear, cosmetic scratching under 2 millimeters in length that does not impede core functionality, and consumable component degradation (e.g., battery capacity retention above 80% of original factory specification after 365 days) do not constitute valid warranty defects.

---

### 5.0 REPLACE-VERSUS-REPAIR DECISION RULE
5.1 Agents and RPC technicians shall apply the following financial and categorical decision rule to determine whether a defective item is repaired or replaced:
* **5.1.1 The 60% Threshold:** If the estimated cost of repair (parts plus localized labor) equals or exceeds 60% of the current Kartway Buy Box price for an identical replacement item, the item must be replaced.
* **5.1.2 Category Mandates:** 
  * *CAT-01 (Electronics) & CAT-03 (Apparel):* Mandatory replacement upon verification of defect. No repair path permitted.
  * *CAT-02 (Large Appliances) & CAT-04 (Power Tools):* Mandatory repair path via certified local depot if repair cost is under the 60% threshold. Replacement is authorized only if the same unit fails repair twice within a 90-day window.
* **5.1.3 Refurbished Items:** CAT-06 items are ineligible for repair; all valid claims within the warranty period result in a like-for-like replacement or a full original-tender refund if stock is depleted.

---

### 6.0 TURNAROUND COMMITMENTS AND SERVICE LEVEL AGREEMENTS (SLAs)
6.1 **Intake and Assessment SLA:** Support agents must review submitted warranty claim forms and photographic evidence within 24 operational hours of customer submission.  
6.2 **Replacement Path Turnaround:** 
* For items processed under the replacement path, the replacement unit must be dispatched from a Kartway fulfillment center within 48 hours of claim approval. 
* Standard delivery of the replacement item shall not exceed 5 business days from dispatch.
6.3 **Repair Path Turnaround:** 
* For items routed to a certified repair depot (CAT-02, CAT-04), the total turnaround time from the date the item is received at the depot to the date it is handed back to the outbound carrier shall not exceed 14 calendar days.
* If a repair depot fails to complete the repair within the 14-day window, the case must be escalated to a Tier 2 Supervisor for an immediate forced replacement override.
6.4 **Customer Compensation for Delay:** If a replacement or repair exceeds the stated SLAs in sections 6.2 or 6.3 by more than 5 business days due to internal Kartway or partner delay, the agent is authorized to issue a $25.00 Kartway Promotional Credit using code `CRED-DELAY-WRN`.
