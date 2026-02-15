# Evidence Handling Procedures

> Chain of custody, encryption, retention, and destruction requirements for red team engagement data.

## 1. Evidence Classification

| Classification | Description | Examples | Handling |
|---------------|-------------|----------|----------|
| **Critical** | Data that could cause harm if leaked | Credentials, PII, exploit code targeting live systems | Encrypted at rest + in transit; need-to-know access |
| **Sensitive** | Engagement-specific operational data | Attack paths, findings, vulnerability details | Encrypted at rest; team access only |
| **Standard** | General engagement artefacts | Screenshots, tool output, scan results | Encrypted at rest; standard access |
| **Public** | Sanitized, shareable data | Anonymized metrics, generic technique descriptions | No special handling required |

## 2. Collection Standards

### What to Collect
- Screenshots of successful exploitation with timestamps
- Tool output logs (scan results, C2 session logs, Garak probe results)
- Network packet captures where relevant (targeted, not bulk)
- Configuration files that demonstrate vulnerabilities
- Timeline of all actions performed

### What NOT to Collect
- Real customer PII/PHI — if encountered, log the path but not the data
- Cleartext passwords — hash or redact immediately
- Bulk data exports — collect only enough to prove the finding
- Any data outside the engagement scope

### Collection Integrity
- Use UTC timestamps on all evidence
- Record the operator name and tool version for each artefact
- Calculate SHA-256 hashes of all evidence files at collection time
- Store hashes in a separate manifest file

## 3. Storage Requirements

### Encryption
- All evidence encrypted at rest using AES-256 (GPG, LUKS, or VeraCrypt)
- Encryption keys stored separately from the evidence (password manager or hardware token)
- In-transit encryption required for any evidence transfer (SFTP, SCP, or encrypted email)

### Access Control
- Evidence accessible only to named engagement team members
- No evidence on personal devices, cloud drives, or unencrypted media
- Access log maintained for all evidence retrieval

### Directory Structure
```
engagement-<ID>/
  evidence/
    findings/          # Organized by finding ID
      FINDING-001/
        screenshots/
        logs/
        manifest.sha256
    timeline/          # Chronological action logs
    raw/               # Unprocessed tool output
  reports/
    draft/
    final/
  manifest.sha256      # Master hash manifest
```

## 4. Chain of Custody

Every evidence transfer must be logged:

| Field | Description |
|-------|-------------|
| Evidence ID | Unique identifier for the item |
| Description | Brief description of the evidence |
| Collected by | Operator name |
| Collection time | UTC timestamp |
| Collection method | Tool/technique used |
| SHA-256 hash | Hash at time of collection |
| Transferred to | Recipient name (if applicable) |
| Transfer time | UTC timestamp (if applicable) |
| Transfer method | Encrypted channel used |
| Verification | Hash verified by recipient (yes/no) |

## 5. Retention and Destruction

### Retention Schedule

| Data Type | Retention Period | Start Date |
|-----------|-----------------|------------|
| Final report | 3 years | Report acceptance date |
| Evidence (Critical) | 90 days | Report acceptance date |
| Evidence (Sensitive) | 90 days | Report acceptance date |
| Evidence (Standard) | 90 days | Report acceptance date |
| Engagement logs | 1 year | Engagement end date |
| Chain of custody records | 3 years | Engagement end date |

### Destruction Procedure
1. Verify retention period has expired
2. Confirm with engagement sponsor that evidence can be destroyed
3. Use secure deletion: `shred -vfz -n 5` for files; LUKS header wipe for encrypted volumes
4. For cloud storage: delete + verify object is gone (no soft-delete retention)
5. Record destruction in the chain of custody log
6. Two team members must witness and sign off on destruction

### Early Destruction
If the engagement sponsor requests early destruction:
- Obtain written authorization
- Follow the standard destruction procedure
- Archive the destruction authorization with the chain of custody records
