# Incident Response Playbook

> Procedures for when red team testing causes unintended impact or discovers an active threat.

## 1. Unintended Impact During Testing

### Severity Classification

| Severity | Description | Examples | Response Time |
|----------|-------------|----------|---------------|
| **Critical** | Production service degraded or data exposed | System outage, customer data accessed, safety system affected | **Immediate** |
| **High** | Non-production impact affecting operations | Staging environment crash, network segment disruption | **15 minutes** |
| **Medium** | Contained impact, no operational effect | Test account lockout, non-critical service restart needed | **1 hour** |
| **Low** | No real impact, procedural concern only | Alert generated in SIEM, blue team query | **4 hours** |

### Response Procedure

#### Step 1: Stop (Immediate)
- **Halt all active testing** — do not attempt to "fix" the issue by running more commands
- Preserve the current state for forensic analysis
- Note the exact time, action performed, and observed impact

#### Step 2: Notify (Within 15 minutes)
- Contact the Red Team Lead via the encrypted channel
- Red Team Lead contacts the engagement sponsor and Blue Team Lead
- Provide: timestamp, action taken, observed impact, affected systems

#### Step 3: Assess (Within 1 hour)
- Determine root cause: was impact from a known test action, or is there an unrelated issue?
- Assess blast radius: what systems/data are affected?
- Determine if the issue is self-resolving or requires intervention

#### Step 4: Remediate
- If red team action caused the issue: assist with rollback under blue team supervision
- If infrastructure issue was exposed: document and hand off to operations team
- Never attempt unauthorized remediation — always coordinate through the sponsor

#### Step 5: Document
- Full incident timeline with actions and decisions
- Root cause analysis
- Lessons learned and RoE updates
- Include in final engagement report as a separate appendix

## 2. Discovery of Active Threat Actor

If during testing you discover evidence of a **real, unauthorized intrusion**:

### Immediate Actions
1. **STOP all red team activity** to avoid contaminating evidence
2. **Do NOT interact** with the attacker's tools, infrastructure, or persistence
3. **Preserve evidence** — screenshot/log what you found without modifying it
4. **Notify** the CISO and Blue Team Lead within 15 minutes via the fastest secure channel available

### Evidence Preservation
- Note file paths, process IDs, network connections, and timestamps
- Do not delete, move, or modify any artefacts
- If possible, capture volatile data (memory, active connections) before it's lost
- Document the discovery context: what you were doing when you found it

### Handoff
- The engagement transitions to incident response mode
- Red team may be asked to support the IR team with knowledge of the environment
- All red team activities remain paused until cleared by the CISO
- Engagement timeline and scope may be revised

## 3. Communication Templates

### Unintended Impact Notification
```
SUBJECT: [RED TEAM] Unintended Impact — [SEVERITY]
TIME: [UTC timestamp]
ACTION: [What was being performed]
IMPACT: [Observed effect]
AFFECTED: [Systems/services]
STATUS: [Testing halted / Contained / Investigating]
CONTACT: [Red Team Lead name and channel]
```

### Active Threat Discovery Notification
```
SUBJECT: [RED TEAM] Possible Active Threat Discovered
TIME: [UTC timestamp of discovery]
CONTEXT: [What red team was doing when discovered]
INDICATORS: [Brief description — no IOCs in email]
EVIDENCE: [Preserved / Screenshot / Logged]
STATUS: [All red team activity halted]
REQUEST: Immediate IR team engagement
CONTACT: [Red Team Lead name and channel]
```

## 4. Post-Incident Review

Within 5 business days of any incident:
- Conduct a blameless retrospective with red team, blue team, and sponsor
- Document root cause, timeline, and improvement actions
- Update RoE, safety controls, and playbooks based on findings
- File the review as a permanent engagement record
