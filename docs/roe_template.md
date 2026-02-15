# Rules of Engagement (RoE) Template

> **Classification**: This template is for the public/generic repo. Replace all `[PLACEHOLDER]` values with actual data in the internal repo only.

## 1. Authorization

| Field                  | Value                                      |
|------------------------|--------------------------------------------|
| Engagement Name        | [PLACEHOLDER]                              |
| Authorization Date     | [YYYY-MM-DD]                               |
| Authorizing Executive  | [Name, Title]                              |
| Red Team Lead          | [Name]                                     |
| Document Version       | 1.0                                        |
| Classification         | [Internal / Confidential]                  |

**Legal Basis**: This engagement is authorized under [company policy / contract reference]. All activities comply with applicable laws including the Computer Fraud and Abuse Act (CFAA) and equivalent local legislation.

## 2. Scope

### 2.1 In-Scope Assets

| Asset Type       | Identifier             | Environment  | Notes                |
|-----------------|------------------------|--------------|----------------------|
| Domain          | [example.com]          | [Prod/Stage] |                      |
| IP Range        | [10.0.0.0/24]          | [Lab]        |                      |
| Application     | [App Name]             | [Stage]      |                      |
| Cloud Account   | [AWS Account ID]       | [Dev]        |                      |
| OT/ICS Segment  | [Segment ID]           | [Lab Only]   | Read-only probing    |

### 2.2 Out-of-Scope (Do NOT Touch)

- Production databases containing customer data
- Payment processing systems (PCI DSS scope)
- Third-party SaaS platforms unless explicitly listed
- Physical security systems
- [Additional exclusions]

### 2.3 Time Window

| Parameter        | Value                                       |
|-----------------|---------------------------------------------|
| Start Date      | [YYYY-MM-DD HH:MM UTC]                     |
| End Date        | [YYYY-MM-DD HH:MM UTC]                     |
| Testing Hours   | [e.g., 08:00-22:00 UTC weekdays only]      |
| Blackout Dates  | [e.g., Black Friday, system maintenance]    |

## 3. Authorized Techniques

### 3.1 Allowed (Green)

| MITRE ATT&CK ID | Technique                        | Constraints                        |
|------------------|----------------------------------|------------------------------------|
| T1595            | Active Scanning                  | Rate-limited; no DoS              |
| T1589            | Gather Victim Identity Info      | OSINT only; no social engineering of real employees |
| T1190            | Exploit Public-Facing App        | Staging/lab environments only     |
| T1078            | Valid Accounts                   | Test accounts only                |
| T1021            | Remote Services                  | Lab network only                  |
| T1059            | Command and Scripting            | Non-destructive payloads only     |

### 3.2 Restricted (Yellow) — Requires Approval Per Instance

| Technique                        | Approval Required From     |
|----------------------------------|---------------------------|
| Phishing simulation              | HR + Legal                |
| Credential dumping               | Red Team Lead + CISO      |
| Lateral movement to OT segment   | OT Manager + CISO         |
| Data exfiltration simulation     | Legal + Data Protection   |

### 3.3 Prohibited (Red)

- Denial of Service (DoS/DDoS) attacks
- Destruction or modification of production data
- Accessing real customer PII/PHI
- Social engineering of real employees (unless explicitly authorized)
- Physical intrusion
- Supply chain attacks against real vendors
- Any action that could impact product safety

## 4. Data Handling

| Data Type                    | Handling Rule                                        |
|-----------------------------|------------------------------------------------------|
| Credentials discovered      | Log hash only; do not store cleartext; report immediately |
| PII/PHI encountered         | Stop; do not exfiltrate; report to DPO within 1 hour |
| Proprietary formulas/IP     | Do not access; report path that led to discovery     |
| Screenshots/evidence        | Store in encrypted vault; destroy after report acceptance |
| Tool output/logs            | Retain for 90 days post-engagement; then destroy     |

## 5. Safety Controls

### 5.1 Stop Conditions (Immediate Halt)

- Unintended access to production customer data
- Impact to production system availability
- Discovery of active threat actor (real breach in progress)
- Request from any authorized contact below
- Any uncertainty about whether an action is in scope

### 5.2 Communication Protocol

| Role                | Contact           | Channel              | Response SLA |
|--------------------|-------------------|----------------------|-------------|
| Red Team Lead      | [Name]            | [Encrypted channel]  | Immediate   |
| Blue Team Lead     | [Name]            | [Encrypted channel]  | 15 min      |
| CISO               | [Name]            | [Phone + encrypted]  | 30 min      |
| Legal Counsel      | [Name]            | [Email + phone]      | 1 hour      |
| Incident Response  | [Team]            | [IR channel]         | 15 min      |

### 5.3 Deconfliction

If the blue team detects red team activity:
1. Red team lead contacts blue team lead on the deconfliction channel
2. Provide engagement ID and timeframe
3. Blue team confirms and continues normal operations
4. All deconfliction events are logged for the final report

## 6. Reporting

| Deliverable              | Due Date                    | Audience           |
|--------------------------|-----------------------------|--------------------|
| Daily status update      | End of each testing day     | Red Team Lead      |
| Finding alerts (Critical)| Within 1 hour of discovery  | CISO + Blue Team   |
| Draft report             | [Date: End + 5 business days]| Red Team + CISO   |
| Final report             | [Date: End + 10 business days]| Executive team   |
| Remediation retest       | [Date: End + 30 days]       | Red Team + Blue Team|

## 7. Signatures

| Role                     | Name | Signature | Date |
|--------------------------|------|-----------|------|
| Authorizing Executive    |      |           |      |
| CISO                     |      |           |      |
| Red Team Lead            |      |           |      |
| Legal Counsel            |      |           |      |
