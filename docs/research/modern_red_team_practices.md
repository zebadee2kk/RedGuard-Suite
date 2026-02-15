# What Modern Red Teams & Security Firms Actually Do

> Research synthesis of professional red team practices, tool patterns, and operational disciplines.

## Key Reality

Professional red teams rarely rely on a single tool. Instead they use toolchains, automation pipelines, custom scripting, threat intelligence, business-context modelling, and detection engineering feedback loops.

## 1. Inspiration from Leading Red-Team Platforms

### Cobalt Strike
- Reliable C2, malleable traffic profiles, lateral movement tooling
- **Lesson**: Stealth and evasion matter more than exploitation; post-compromise actions create real risk; modular payload and comms design

### Bishop Fox Sliver (Open-source C2)
- Modern implant design, cross-platform, encrypted comms, operator UX
- **Lesson**: Operational reliability and operator visibility are critical

### SpecterOps & BloodHound Ecosystem
- Identity attack path mapping — most breaches involve identity abuse, not exploits
- Reveals: privilege escalation chains, shadow admin accounts, unintended trust relationships
- **Critical insight**: Identity is the new perimeter

### Red Canary Atomic Red Team
- Validate detection coverage continuously, test behaviors not tools, map to MITRE ATT&CK
- **Lesson**: Detection validation is as important as attack simulation

### AttackIQ / SafeBreach (Breach & Attack Simulation)
- Continuous adversary simulation, automated scenario testing, risk scoring
- **Lesson**: Continuous testing beats annual pentests

## 2. Tools Used by Penetration Testers

### Recon & Attack Surface Mapping
- OWASP Amass and OSINT tools map infrastructure, discover forgotten assets, enumerate trust relationships
- **Insight**: The biggest risks are often unknown assets

### Nuclei (ProjectDiscovery)
- Template-driven scanning, rapid vulnerability coverage, automation friendly
- **Takeaway**: Templated automation scales expertise

### Burp Suite
- Workflow efficiency matters; manual + automated testing combination; human insight still critical

## 3. Methods Used by Elite Red Teams

### Threat Emulation (not random testing)
- Simulate real adversaries: ransomware groups, insider threats, supply chain attackers, nation-state tradecraft
- Inspired by MITRE ATT&CK

### Identity & Privilege Escalation Focus
- Credential theft, token abuse, Kerberos delegation flaws, OAuth abuse, MFA bypass
- These techniques work because identity is the primary attack surface

### Living-Off-The-Land Techniques (LOLBins)
- PowerShell, WMI, built-in admin tools, scheduled tasks, cloud CLI tools
- Harder to detect than traditional malware

### Cloud & SaaS Attack Paths
- Azure/Entra ID privilege paths, AWS IAM misconfigurations, API exposure, OAuth consent abuse, SSO trust relationships

### Persistence & Stealth
- Hidden admin roles, long-lived tokens, conditional access bypass, mailbox forwarding rules, backdoor service principals

## 4. How AI is Changing Red Teaming

- **AI-assisted recon analysis**: LLMs summarize findings and highlight risks
- **AI-generated phishing pretexts**: Realistic lures from OSINT
- **Attack chain analysis**: AI identifies highest-risk paths
- **Defensive evasion research**: AI generates technique variants

## 5. How Security Consultancies Deliver Value

What clients pay for:
- **Attack path narratives** — not vulnerability lists
- **Business risk translation** — "This misconfiguration enables ransomware deployment in under 2 hours"
- **Detection gap identification** — what wasn't seen by SOC tools
- **Process failures** — joiner/mover/leaver failures, vendor onboarding weaknesses, weak MFA policy

## 6. Common Engagement Workflow

1. **Recon & Intelligence**: Asset discovery, employee OSINT, supply chain mapping
2. **Initial Access**: Phishing, password spraying, exposed service exploitation
3. **Privilege Escalation**: Identity abuse, misconfiguration exploitation
4. **Lateral Movement**: Trust path exploitation, token reuse
5. **Persistence & Impact**: Data exfiltration simulation, ransomware deployment simulation
6. **Detection & Response Review**: SOC visibility gaps, response time, containment effectiveness

## 7. What Tools Don't Teach (But Pros Know)

- Tools are not breaches — misconfigurations + identity flaws cause most compromises
- CVSS scores don't equal risk — context matters
- Attack paths matter more than individual vulnerabilities
- Human processes are often the weakest link

## 8. Design Principles for RedGuard Suite

These principles directly inform the project architecture:

- Identity-first security testing
- Attack path modelling
- Continuous validation
- Detection engineering feedback loop
- AI-assisted analysis and prioritization
- Business risk storytelling
- Automation + human insight hybrid
- Cloud and SaaS focus
- Stealth and persistence testing
