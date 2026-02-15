# Legal & Compliance Checklist

> Pre-engagement checklist ensuring all legal, regulatory, and organizational requirements are satisfied before testing begins.

## 1. Authorization

- [ ] **Written authorization** obtained from an authorized executive (CTO, CISO, or equivalent)
- [ ] Authorization letter explicitly names the red team operators
- [ ] Authorization covers the specific scope, timeframe, and techniques
- [ ] Authorization is stored securely and accessible to all team members
- [ ] Legal counsel has reviewed the authorization document

## 2. Scope Agreement

- [ ] **Rules of Engagement (RoE)** document completed and signed by all parties
- [ ] In-scope assets clearly defined (IPs, domains, applications, accounts)
- [ ] Out-of-scope assets explicitly listed (production data, payment systems, third parties)
- [ ] Testing windows agreed (dates, hours, blackout periods)
- [ ] Stop conditions defined and communicated
- [ ] Deconfliction procedures established

## 3. Legal Compliance

### General
- [ ] Activities comply with **Computer Misuse Act 1990** (UK) or equivalent local legislation
- [ ] Activities comply with **Computer Fraud and Abuse Act** (US) if US systems are in scope
- [ ] No testing of systems or networks not explicitly authorized
- [ ] No interception of communications without explicit authorization (RIPA/Wiretap considerations)

### Data Protection
- [ ] **GDPR** compliance confirmed if EU/UK personal data may be encountered
- [ ] Data Processing Agreement (DPA) in place if personal data will be handled
- [ ] Data Protection Impact Assessment (DPIA) completed if high-risk processing
- [ ] Data minimization principle applied — collect only what's needed to demonstrate findings
- [ ] Data subject rights considered — plan for if data subjects request information
- [ ] **Data Protection Officer (DPO)** notified of the engagement

### Industry-Specific
- [ ] **PCI DSS** scope identified and excluded (or separate authorization for PCI testing)
- [ ] **HIPAA** considerations if health data may be encountered
- [ ] **SOX** compliance if financial systems are in scope
- [ ] **NIS2** directive compliance if critical infrastructure is in scope
- [ ] Industry regulator notification requirements checked (if applicable)

## 4. Contractual

- [ ] **Non-Disclosure Agreement (NDA)** signed by all team members
- [ ] **Statement of Work (SoW)** or contract specifying deliverables and timelines
- [ ] **Professional Indemnity Insurance** coverage confirmed for the engagement
- [ ] **Liability limitations** agreed in writing
- [ ] **Third-party access**: if cloud providers or SaaS platforms are in scope, their terms of service permit security testing (or separate authorization obtained)
- [ ] **Subcontractor agreements**: if using external operators, they are bound by the same terms

## 5. Ethical Requirements

- [ ] Engagement purpose is defensive (improving security posture)
- [ ] No targeting of individuals for harassment or retaliation
- [ ] Findings will be reported responsibly to the client
- [ ] Any discovered criminal activity will be handled per the agreed escalation path
- [ ] Team members have read and agree to the project [Code of Conduct](../../CODE_OF_CONDUCT.md)

## 6. Operational Readiness

- [ ] **Insurance** coverage active for the engagement period
- [ ] **Communication plan** established (encrypted channels, escalation contacts)
- [ ] **Evidence handling** procedures agreed (see [evidence_handling.md](evidence_handling.md))
- [ ] **OPSEC** measures in place (see [operational_security.md](operational_security.md))
- [ ] **Deconfliction** with blue team/SOC established (see [deconfliction_guide.md](deconfliction_guide.md))
- [ ] **Incident response** plan agreed for unintended impact (see [incident_response.md](incident_response.md))
- [ ] **Backup and rollback** plan for any configuration changes

## 7. Sign-Off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Engagement Sponsor | | | |
| Red Team Lead | | | |
| Legal Counsel | | | |
| CISO / Security Lead | | | |
| Data Protection Officer | | | |

## 8. Post-Engagement Compliance

- [ ] All evidence handled per retention and destruction schedule
- [ ] Final report delivered securely
- [ ] Engagement data destroyed per agreed timeline
- [ ] Lessons learned documented and filed
- [ ] Any regulatory notifications completed (if applicable)
