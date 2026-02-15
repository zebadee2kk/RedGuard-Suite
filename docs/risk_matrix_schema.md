# Risk Matrix Schema

RedGuard Suite uses a standardized **Impact x Likelihood x Exploitability** risk matrix for scoring findings, aligned to NIST SP 800-30 and ISO 27005.

## Risk Score Formula

```
Risk Score = Impact x Likelihood x Exploitability
Rating = map_to_tier(Risk Score)
```

## Impact Levels

| Level    | Score | Description                                                    | Examples                                       |
|----------|-------|----------------------------------------------------------------|------------------------------------------------|
| Low      | 1     | Negligible operational impact; no data exposure                | Information disclosure of public data          |
| Medium   | 2     | Localized impact with quick recovery; limited data exposure    | Non-sensitive config leak; service degradation |
| High     | 3     | Major service disruption or sensitive data exposure            | PII exposure; production outage; credential leak |
| Critical | 4     | Severe business impact, safety risk, or regulatory violation   | Full domain compromise; OT/ICS impact; mass data breach |

## Likelihood Levels

| Level          | Score | Description                                              |
|----------------|-------|----------------------------------------------------------|
| Rare           | 1     | Requires highly specialized skills and insider knowledge |
| Possible       | 2     | Requires moderate skill; known attack patterns exist     |
| Likely         | 3     | Exploitable with publicly available tools; low barrier   |
| Almost Certain | 4     | Trivially exploitable; actively exploited in the wild    |

## Exploitability Levels

| Level    | Score | Description                                                  |
|----------|-------|--------------------------------------------------------------|
| Theoretical | 1  | Proof of concept only; no reliable exploit available         |
| Difficult   | 2  | Requires chaining multiple vulnerabilities or custom tooling |
| Moderate    | 3  | Public exploit exists; some configuration required           |
| Easy        | 4  | Weaponized exploit available; script-kiddie level            |

## Risk Rating Tiers

| Score Range | Rating   | Color  | SLA for Remediation |
|-------------|----------|--------|---------------------|
| 1-8         | Low      | Green  | 90 days             |
| 9-24        | Medium   | Yellow | 30 days             |
| 25-48       | High     | Orange | 7 days              |
| 49-64       | Critical | Red    | 24 hours            |

## JSON Schema

Findings in reports use this structure:

```json
{
  "finding_id": "RG-2026-001",
  "title": "Unauthenticated API Endpoint",
  "description": "The /api/v1/users endpoint returns user data without authentication.",
  "attack_technique": "T1190",
  "impact": 3,
  "likelihood": 4,
  "exploitability": 3,
  "risk_score": 36,
  "risk_rating": "High",
  "affected_assets": ["api-gateway-prod"],
  "evidence": "screenshots/rg-2026-001.png",
  "remediation": "Implement OAuth2 bearer token validation on all API endpoints.",
  "references": [
    "https://attack.mitre.org/techniques/T1190/",
    "https://owasp.org/API-Security/"
  ]
}
```

## MITRE ATT&CK Integration

Each finding maps to one or more ATT&CK techniques. The report engine automatically:
1. Links to the ATT&CK navigator visualization
2. Calculates coverage percentage across the kill chain
3. Highlights gaps in detection for blue team handoff
