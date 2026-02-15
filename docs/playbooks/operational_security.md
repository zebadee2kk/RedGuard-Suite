# Operational Security (OPSEC) Playbook

> Guidelines for maintaining operational security during red team engagements.

## 1. Pre-Engagement OPSEC

### Infrastructure Preparation
- Use dedicated VMs or containers for each engagement — never reuse attack infrastructure across clients
- Rotate VPN endpoints and DNS resolvers between engagements
- Verify all tools are from trusted sources; validate checksums before deployment
- Clear browser history, cached credentials, and clipboard before starting

### Identity Separation
- Use engagement-specific accounts and SSH keys — never personal credentials
- Register any required cloud resources under engagement-specific billing accounts
- Ensure no personal metadata (email signatures, Git usernames) leaks into payloads or logs

### Communication Security
- All engagement communications via encrypted channels (Signal, encrypted email, or approved platform)
- Never discuss active engagement details on unencrypted channels
- Use code names for sensitive targets in team communications

## 2. During Engagement

### Network OPSEC
- Route all traffic through engagement-approved infrastructure
- Use encrypted tunnels (WireGuard, SSH tunnels) for C2 traffic
- Monitor your own traffic for inadvertent data leakage
- Rate-limit scanning and enumeration to avoid triggering DoS conditions

### Payload and Tool OPSEC
- Strip metadata from all documents and payloads before deployment
- Use unique payloads per target — avoid signature reuse
- Test payloads in isolated lab before deploying to target environment
- Clean up payloads, shells, and persistence mechanisms at engagement end

### Data Handling
- Never store target data on personal devices
- Encrypt all evidence and findings at rest (AES-256 minimum)
- Follow the evidence handling procedures in [evidence_handling.md](evidence_handling.md)
- If PII/PHI is encountered, follow the stop condition in the RoE

### Logging
- Log all actions with timestamps and operator ID
- Maintain an immutable audit trail (append-only log)
- Sync logs to encrypted storage daily
- Logs must be available for deconfliction (see [deconfliction_guide.md](deconfliction_guide.md))

## 3. Post-Engagement OPSEC

### Cleanup Checklist
- [ ] Remove all persistence mechanisms from target environment
- [ ] Delete or disable all engagement-specific accounts
- [ ] Wipe and decommission attack infrastructure
- [ ] Clear engagement data from local machines
- [ ] Verify no target data remains on personal/shared storage
- [ ] Archive encrypted logs per retention policy (90 days default)

### Reporting OPSEC
- Reports transmitted via encrypted channel only
- Password-protect report PDFs with separate password delivery
- Strip metadata from report files before delivery
- Never include cleartext credentials in reports — use redacted hashes

## 4. OPSEC Failure Response

If operational security is compromised during an engagement:

1. **Immediately halt** the affected activity
2. **Notify** the Red Team Lead within 15 minutes
3. **Assess** whether the blue team or external parties may have been alerted
4. **Document** the failure, root cause, and any exposed information
5. **Coordinate** with the engagement sponsor on whether to continue, pause, or abort
6. **Update** the RoE and OPSEC controls before resuming
