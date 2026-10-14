# Return Fraud and Abuse Prevention Standard

# KARTWAY OPERATIONAL POLICY MANUAL
**Document Ref:** POL-REV-442  
**Effective Date:** 14 October 2024  
**Subject:** Return Abuse, Account Flagging, and Fraud Escalation  
**Applies To:** All Tier 1, Tier 2, and Specialist Support Agents  

---

## 1. PURPOSE AND SCOPE

1.1 This policy defines the operational thresholds, agent restrictions, and mandatory escalation pathways regarding customer return abuse, serial refund requests, and suspected fraudulent activity within the Kartway marketplace.

1.2 Compliance with this document is mandatory for all customer operations personnel. Deviation from these procedures without documented managerial authorization will result in a formal performance review.

---

## 2. RETURN-RATE THRESHOLD AND AUTOMATED FLAGGING

2.1 An account shall be automatically flagged for internal review by the Kartway Risk Engine when it meets the following quantitative criteria over a rolling 90-day window:
*   **Item Return Rate:** Exceeds 45% of total units ordered.
*   **Total Order Volume:** Minimum of 6 completed orders within the 90-day evaluation period.
*   **Monetary Return Value:** Cumulative refunded value exceeding \$1,200.00 USD.

2.2 When an account reaches the threshold defined in Section 2.1, the system applies the internal tag `RISK-RET-04`. Agents viewing a profile bearing this tag shall see a restricted banner stating: *"Account under operational review. Standard return policies suspended pending verification."*

2.3 Accounts flagged with `RISK-RET-04` are restricted from using instant automated refund labels. All return requests for these accounts must be manually processed by a Tier 2 specialist.

---

## 3. SERIAL REFUND REQUESTERS

3.1 A customer is classified as a "Serial Refund Requester" (tag `SRR-09`) when they submit three (3) or more refund claims without an accompanying physical return tracking scan within any 30-day period.

3.2 For customers classified under `SRR-09`, agents are strictly prohibited from issuing goodwill refunds, appeasement credits, or reshipments without prior approval from a Fraud Operations Team Lead.

3.3 **Mandatory Holding Period:** Return processing for customers with the `SRR-09` designation shall be subjected to a mandatory 14-day holding period commencing upon the date the warehouse scans the returned parcel, superseding standard 3-day SLA guidelines.

---

## 4. PROHIBITION OF DISCLOSURE TO CUSTOMERS

4.1 **Strict Confidentiality:** Support agents, regardless of tier or tenure, are strictly prohibited from disclosing to any customer, third-party representative, or legal counsel that their account is flagged, monitored, under review, or restricted due to high return rates or suspected abuse.

4.2 If a customer inquires directly about why their return privileges have been restricted or why automated labels are unavailable, agents must use the following mandatory script without deviation:
> *"Due to recent updates in our logistics processing system, automated return generation is temporarily unavailable for this transaction. I have manually generated a standard return workflow for you."*

4.3 Under no circumstances shall an agent utter phrases including, but not limited to: *"your account is flagged," "you return too many items," "our risk system,"* or *"fraud department."* Violation of this clause results in immediate referral to Employee Relations.

---

## 5. ESCALATION ROUTE FOR SUSPECTED FRAUD

5.1 Agents must immediately suspend standard customer interaction and initiate the Fraud Escalation Route when encountering any of the following triggers:
*   Return of empty boxes, counterfeit goods, or items materially different from the original shipment (Item Substitution).
*   Admission by the customer of exploiting loopholes in the return policy.
*   Discrepancies exceeding \$500.00 USD between declared return contents and warehouse intake inspection logs.

5.2 **Escalation Procedure:**
1.  **Immediate Halt:** Cease all communication with the customer. Do not issue any refunds, replacements, or promises of resolution.
2.  **Internal Ticket Tagging:** Update the support ticket tag to `FRD-ESC-99` and assign the ticket directly to the queue `Fraud-Operations-Central`.
3.  **Mandatory Form:** Complete the Internal Fraud Incident Report (Form FIR-8) within 2 hours of ticket identification, detailing tracking numbers, order IDs, and warehouse inspection photos.
4.  **Customer Notification:** Apply macro template `MAC-HOLD-12` to the customer-facing ticket, which states: *"Your inquiry requires additional review by our specialized logistics team. You will be contacted via email within 3 to 5 business days."*

5.3 The Fraud Operations Team shall assume full ownership of the ticket upon assignment. Support agents are barred from reopening or responding to the ticket unless explicitly instructed via written directive from a Fraud Operations Manager.
