# Security Playbooks & Operational Protocols

This directory contains the operational playbooks and security protocols for conducting red team engagements using RedGuard Suite. These are **essential reading** for all operators before any engagement.

## Playbooks

| Document | Purpose | When to Use |
|----------|---------|-------------|
| [operational_security.md](operational_security.md) | OPSEC guidelines for red team operators | Before, during, and after every engagement |
| [incident_response.md](incident_response.md) | Response to unintended impact or active threat discovery | When something goes wrong during testing |
| [evidence_handling.md](evidence_handling.md) | Chain of custody, encryption, retention, destruction | Whenever collecting, storing, or transferring evidence |
| [deconfliction_guide.md](deconfliction_guide.md) | Red team / blue team coordination procedures | Before and during every engagement |
| [legal_compliance_checklist.md](legal_compliance_checklist.md) | Pre-engagement legal and regulatory checklist | Before every engagement — all boxes must be checked |

## Related Documents

- [Rules of Engagement Template](../roe_template.md) — Engagement-specific authorization and scope
- [Risk Matrix Schema](../risk_matrix_schema.md) — Finding severity scoring methodology
- [Architecture Overview](../architecture.md) — System design and safety controls

## Usage

1. **Before an engagement**: Complete the [legal compliance checklist](legal_compliance_checklist.md) and establish [deconfliction](deconfliction_guide.md) procedures
2. **During an engagement**: Follow [OPSEC](operational_security.md) and [evidence handling](evidence_handling.md) procedures
3. **If something goes wrong**: Follow the [incident response](incident_response.md) playbook immediately
4. **After an engagement**: Complete the OPSEC cleanup checklist and evidence destruction schedule
