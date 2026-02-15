# Tooling Reference & Operational Standards

> Centralized reference of external tools, standards, and operational maturity guidance for RedGuard Suite.

## GitHub Repos (By Capability)

### Recon and Discovery
- six2dez/reconftw
- OWASP/Amass
- projectdiscovery/httpx
- projectdiscovery/nuclei
- nmap/nmap

### Web and App Testing
- zaproxy/zaproxy
- rapid7/metasploit-framework

### Identity and Attack Paths
- SpecterOps/BloodHound
- mitre/caldera

### C2 and Emulation
- BishopFox/sliver
- its-a-feature/Mythic

### BAS and Detection Validation
- redcanaryco/atomic-red-team
- facebookincubator/TTPForge

### Social Engineering (Authorized Only)
- gophish/gophish
- trustedsec/social-engineer-toolkit

### LLM and AI Security
- NVIDIA/garak
- Azure/PyRIT
- promptfoo/promptfoo

## Kali Linux Influence

- Kali is the reference operator environment for many teams and toolchains.
- Keep automation portable and OS-agnostic; avoid hardcoding Kali paths.
- Prefer containerized tools so Windows or macOS operators can run the same workflows.
- Enforce lab hygiene: isolated networks, snapshots, and explicit scope controls.

## Standards and Frameworks

- MITRE ATT&CK and ATLAS for TTP mapping and scenario design.
- OWASP guidance for web application testing.
- NIST and ISO 27001 for governance alignment and audit readiness.

## Operational Maturity Notes

- Attack path narratives and time-to-impact metrics outperform CVE-only reporting.
- Detection feedback loops are core to sustained value (simulate, validate, tune).
- Identity abuse and cloud/SaaS paths are the dominant real-world risk areas.

## Supply Chain and Safety Controls

- Pin dependencies, generate SBOMs, and sign releases for public artifacts.
- Encrypt internal configurations (SOPS or vault) and add classification headers.
- Use dry-run defaults, rate limits, and kill switches to prevent outages.
