# Red Team Learning Roadmap & Resources

> Self-directed learning path from intermediate security testing to modern red team operations, with curated OSINT, exploit intelligence, and training resources.

## 1. What Modern Red Teaming Actually Is

Modern red teaming is less about "find as many vulns as possible" and more about **emulating real adversaries end-to-end**:

- Uses MITRE ATT&CK to plan campaigns by tactics/techniques rather than just CVEs
- Focuses on **adversary emulation**: picking a threat group or breach pattern and recreating its TTPs
- Leverages **breach and attack simulation (BAS)** platforms to continuously test controls
- Integrates with defenders (purple teaming) to improve detection engineering and incident response
- Includes **cloud, SaaS, identity, supply-chain and social engineering** paths — reflecting how real breaches happen

## 2. Core Skill Map

1. **Offensive fundamentals (web, infra, AD)** — Web app vulns, auth flows, deserialization, SSRF, IDOR; AD abuse, Kerberos, delegation, pivoting, tunnelling
2. **Cloud & SaaS** — Common misconfigs and abuse paths in AWS/Azure/GCP, M365/Entra, OAuth/OIDC
3. **OSINT & social engineering** — People, infrastructure, supply-chain mapping; phishing, vishing, pretext development, OPSEC
4. **Adversary emulation & tooling** — ATT&CK-driven planning, C2 frameworks, EDR evasion, BAS platforms
5. **Automation & scripting** — Python/PowerShell/Bash for tooling, data parsing, engagement automation
6. **Reporting & consultancy** — Executive narratives, clear attack paths, remediation-oriented recommendations

## 3. Learning Phases

### Phase 1 — Sharpen Offensive Fundamentals (6-12 months)

**Hands-on practice:**
- TryHackMe "Jr Penetration Tester" and "Pentest+" paths for structured fundamentals
- TCM Security "Certified Practical Penetration Tester" as a practical starting point
- OSCP / CRTP (AD-focused) as stretch goals for exam-style validation

**Key skills to emphasise:**
- Windows/AD attack chains (initial access → privesc → DC compromise → persistence)
- Pivoting and C2 basics (redirectors, OPSEC, traffic blending)
- Internal phishing / help-desk style social engineering

### Phase 2 — Red Teaming & Adversary Emulation (6-12 months)

**Framework & methodology:**
- Study MITRE ATT&CK deeply; learn to design scenarios from it
- Model known threat groups relevant to target sectors
- Select technique chains to emulate; map findings back to ATT&CK

**Tools and platforms:**
- Open-source BAS: Caldera, Infection Monkey, Metta, Atomic Red Team
- Commercial awareness: SCYTHE, SafeBreach, Picus, Pentera

**Target capability:** Take a real-world breach pattern → decompose into ATT&CK techniques → recreate in lab → demonstrate impact.

### Phase 3 — OSINT and Human-Centric Operations

**OSINT frameworks and tools:**
- OSINT Framework (lockfale) — classic index of free OSINT tools
- doctorfree/osint — curated list (SpiderFoot, Maltego, Shodan, Recon-ng, IntelOwl)
- OSIF — Metasploit-style CLI for OSINT tasks

**Training resources:**
- SANS SEC497: Practical Open-Source Intelligence
- IMSL (UK) OSINT courses — Ofqual-approved Level 1 and 3
- Seiber OSINT Practitioner (UK) — 5-day course on legalities and tradecraft
- My OSINT Training (MOT) — practical, exercise-driven

**Staying current on OSINT tradecraft:**
- The OSINT Newsletter — tools, techniques, investigations
- Monthly OSINT Roundup — curated tips and tool updates

### Phase 4 — Business, Compliance, and Service Delivery

**Legal & compliance:**
- Understand and operate within Computer Misuse Act (UK) and related legislation
- Draft standard engagement documents: RoE, scope of work, NDAs, data handling
- Consider professional indemnity insurance and ISO-aligned processes

**Service packaging examples:**
- Web/app pentest packages (small/medium/large)
- Internal & AD assessment / assumed-breach exercise
- Red team engagement: threat-informed campaign mapped to ATT&CK
- OSINT-driven attack surface review

## 4. Vulnerability & Exploit Intelligence Feeds

Build a **weekly feed routine** around:

| Source | Focus |
|--------|-------|
| [Exploit-DB](https://www.exploit-db.com) | Public exploit PoCs; learning how exploits are built and chained |
| [Zero Day Initiative (ZDI)](https://www.zerodayinitiative.com/advisories/) | Regular vulnerability advisories including active 0-days |
| [Zero-day.cz](https://www.zero-day.cz/database/) | 0-day tracking database |
| [Google Project Zero](https://projectzero.google/0day.html) | Analysis and stats on real-world exploited vulnerabilities |
| [Rapid7 zero-day blog](https://www.rapid7.com/blog/tag/zero-day/) | Ongoing analysis and response guidance |
| [Red Canary](https://redcanary.com/blog/) | Annual threat detection reports for TTP-level trends |

## 5. Keeping Methods Modern

Two key shifts:

1. **AI-powered red teaming and continuous testing** — AI-driven platforms simulate attacks 24/7 across cloud and API surfaces
2. **2025 breach lessons** — major incidents involved compromised third-party helpdesks, supply-chain/OAuth token theft, and internet-exposed industrial systems with default credentials

When designing services and lab practice, deliberately target:
- Third-party and help-desk processes
- OAuth/OIDC and SSO misconfigurations in SaaS
- Default/exposed management interfaces in cloud and OT/IoT

## 6. Realistic Weekly Routine

**Daily (30-60 minutes)**
- 1 lab box (TryHackMe/HTB/own infra)
- 10-15 minutes reading: one exploit write-up or red teaming article

**Weekly**
- 1-2 hours of structured course material
- Design or extend one mini-attack chain in lab
- Review new 0-day / exploit summaries from feeds

**Monthly**
- Write a short, client-style report for one lab engagement
- Update personal playbooks: initial access techniques, common misconfigs, OSINT sources
