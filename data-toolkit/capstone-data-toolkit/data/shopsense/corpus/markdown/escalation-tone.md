# Escalation Triggers and Customer Communication Standard

# SOP-CX-412: Mandatory Escalation to Human Support

**Effective Date:** 14 January 2025  
**Applies To:** All Tier 1 Automated and Human Support Agents  
**Owner:** Customer Operations Policy Directorate, Kartway Inc.

---

## 1. PURPOSE AND SCOPE

1.1 This Standard defines the mandatory operational thresholds and behavioral triggers that require the immediate transfer of an active customer support interaction from automated systems or Tier 1 agents to a human specialist within the Kartway Escalated Operations Group.

1.2 Compliance with this Standard is mandatory. Failure to escalate in accordance with these clauses constitutes a Tier 2 operational policy breach.

---

## 2. ESCALATION TRIGGERS

An interaction must be escalated to a human agent immediately upon the occurrence of any of the following events:

### 2.1 Explicit Request for a Human
* **2.1.1** If a customer explicitly requests human intervention using phrases including, but not limited to, "speak to a person," "human agent," "real person," or "manager," the automated system or Tier 1 agent must initiate the transfer protocol within two (2) message turns.
* **2.1.2** Under no circumstances shall an automated system attempt to dissuade the customer from speaking to a human after an explicit request has been logged.

### 2.2 Abusive Language and Harassment
* **2.2.1** If a customer uses profane, sexually explicit, or overtly threatening language directed at the AI agent or support staff, the interaction must be flagged for human review.
* **2.2.2** Agents and systems are authorized to issue a single automated warning advising the customer that abusive language violates the Kartway User Terms of Service. If abuse continues after the warning, the chat session shall be transferred to a Tier 2 human supervisor with chat termination rights enabled after an additional sixty (60) seconds of non-compliant messaging.

### 2.3 Repeated Contact Threshold
* **2.3.1** Any support interaction where the customer is contacting Kartway for the third (3rd) time regarding the same underlying Order ID or ticket reference within a fourteen (14) day window must be routed directly to a human agent.
* **2.3.2** The CRM routing engine (System Identifier: *K-Route-v4*) is configured to automatically lock out automated resolution paths upon the creation of a third contact thread.

### 2.4 Legal Action and Regulatory Complaints
* **2.4.1** Any mention, allusion, or explicit threat of legal action, litigation, small claims court filing, or retention of legal counsel requires immediate escalation to the Kartway Legal Liaison Unit.
* **2.4.2** Any mention of regulatory bodies, including but not limited to the Federal Trade Commission (FTC), Consumer Product Safety Commission (CPSC), state Attorney General offices, or local trading standards authorities, must be escalated to a human agent within five (5) minutes of receipt.

### 2.5 Physical Harm and Product Safety
* **2.5.1** Any reference to personal injury, property damage, chemical burns, choking hazards, electrical failure, fire, or product-related illness must bypass automated triage entirely.
* **2.5.2** The receiving human agent must immediately apply the *Critical Safety Tag (CST-01)* and notify the Product Safety Directorate within fifteen (15) minutes of transfer.

### 2.6 Financial Thresholds and Refunds
* **2.6.1** Automated systems are strictly prohibited from issuing refunds, store credits, or promotional compensation exceeding the automated cap of fifty dollars ($50.00 USD).
* **2.6.2** Any claim, compensation request, or disputed charge exceeding fifty dollars ($50.00 USD) must be escalated to a human agent for manual review and authorization pursuant to *SOP-FIN-109 (Discretionary Financial Adjustments)*.

---

## 3. TONE GUIDANCE FOR ESCALATIONS

3.1 During the escalation handoff, both automated transition messages and human agent responses must adhere to the Kartway Neutral Operational Tone (NOT).

3.2 **Required Tone Attributes:**
* **Concise:** Messages must be under forty (40) words where possible.
* **Objective:** Focus exclusively on the mechanics of the transfer.
* **Calm:** Avoid emotional intensification, exclamation marks, or colloquialisms.

3.3 **Mandatory Handoff Template (Automated System):**
> "Your request has been routed to a Kartway human support specialist. Please remain in the chat. Current estimated wait time is three (3) minutes."

---

## 4. LIABILITY AND APOLOGY PROHIBITION

4.1 **Strict Liability Limitation:** Under no circumstances shall an automated system, Tier 1 agent, or escalating representative issue an apology that admits legal fault, contractual breach, negligence, or regulatory non-compliance on behalf of Kartway Inc. or its merchant partners.

4.2 **Permitted Expressions:** Expressions of empathy are restricted strictly to operational inconvenience. Permitted formulations are limited to:
* "I understand this situation has caused disruption to your schedule."
* "We regret the delay you have experienced with this order."

4.3 **Prohibited Formulations:** The use of phrases including, but not limited to, "It is our fault," "We were negligent," "We take full legal responsibility," or "We breached our service agreement" is strictly prohibited and subject to internal compliance auditing.
