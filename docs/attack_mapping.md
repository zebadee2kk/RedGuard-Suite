# MITRE ATT&CK / ATLAS Mapping

This document maps RedGuard Suite modules to MITRE ATT&CK (Enterprise) and ATLAS (AI/ML) techniques.

## ATT&CK Enterprise Coverage

### Reconnaissance (TA0043)

| Technique ID | Technique Name                    | Module     | Status  |
|-------------|-----------------------------------|------------|---------|
| T1595       | Active Scanning                   | `recon`    | Stub    |
| T1595.001   | Scanning IP Blocks                | `recon`    | Planned |
| T1595.002   | Vulnerability Scanning            | `scan`     | Stub    |
| T1589       | Gather Victim Identity Info       | `recon`    | Planned |
| T1590       | Gather Victim Network Info        | `recon`    | Planned |
| T1591       | Gather Victim Org Info            | `recon`    | Planned |
| T1593       | Search Open Websites/Domains      | `recon`    | Planned |
| T1596       | Search Open Technical Databases   | `recon`    | Planned |

### Initial Access (TA0001)

| Technique ID | Technique Name                    | Module     | Status  |
|-------------|-----------------------------------|------------|---------|
| T1190       | Exploit Public-Facing Application | `exploit`  | Planned |
| T1566       | Phishing                          | `phishing` | Planned |
| T1566.001   | Spearphishing Attachment          | `phishing` | Planned |
| T1566.002   | Spearphishing Link                | `phishing` | Planned |
| T1078       | Valid Accounts                    | `exploit`  | Planned |
| T1133       | External Remote Services          | `exploit`  | Planned |

### Execution (TA0002)

| Technique ID | Technique Name                    | Module     | Status  |
|-------------|-----------------------------------|------------|---------|
| T1059       | Command and Scripting Interpreter | `atomic`   | Planned |
| T1059.001   | PowerShell                        | `atomic`   | Planned |
| T1059.003   | Windows Command Shell             | `atomic`   | Planned |
| T1059.004   | Unix Shell                        | `atomic`   | Planned |
| T1204       | User Execution                    | `phishing` | Planned |

### Persistence (TA0003)

| Technique ID | Technique Name                    | Module     | Status  |
|-------------|-----------------------------------|------------|---------|
| T1053       | Scheduled Task/Job                | `atomic`   | Planned |
| T1136       | Create Account                    | `atomic`   | Planned |
| T1098       | Account Manipulation              | `atomic`   | Planned |

### Credential Access (TA0006)

| Technique ID | Technique Name                    | Module     | Status  |
|-------------|-----------------------------------|------------|---------|
| T1110       | Brute Force                       | `exploit`  | Planned |
| T1003       | OS Credential Dumping             | `atomic`   | Planned |
| T1558       | Steal or Forge Kerberos Tickets   | `lateral`  | Planned |

### Discovery (TA0007)

| Technique ID | Technique Name                    | Module     | Status  |
|-------------|-----------------------------------|------------|---------|
| T1046       | Network Service Scanning          | `scan`     | Stub    |
| T1082       | System Information Discovery      | `atomic`   | Planned |
| T1087       | Account Discovery                 | `atomic`   | Planned |
| T1018       | Remote System Discovery           | `scan`     | Planned |

### Lateral Movement (TA0008)

| Technique ID | Technique Name                    | Module     | Status  |
|-------------|-----------------------------------|------------|---------|
| T1021       | Remote Services                   | `lateral`  | Planned |
| T1021.001   | Remote Desktop Protocol           | `lateral`  | Planned |
| T1021.002   | SMB/Windows Admin Shares          | `lateral`  | Planned |
| T1021.006   | Windows Remote Management         | `lateral`  | Planned |
| T1550       | Use Alternate Auth Material       | `lateral`  | Planned |

### Command and Control (TA0011)

| Technique ID | Technique Name                    | Module     | Status  |
|-------------|-----------------------------------|------------|---------|
| T1071       | Application Layer Protocol        | `c2`       | Planned |
| T1572       | Protocol Tunneling                | `c2`       | Planned |
| T1573       | Encrypted Channel                 | `c2`       | Planned |

### Exfiltration (TA0010)

| Technique ID | Technique Name                    | Module     | Status  |
|-------------|-----------------------------------|------------|---------|
| T1041       | Exfiltration Over C2 Channel      | `exfil`    | Planned |
| T1048       | Exfiltration Over Alternative Protocol | `exfil` | Planned |
| T1567       | Exfiltration Over Web Service     | `exfil`    | Planned |

## ATLAS (AI/ML) Coverage

| Technique ID | Technique Name                    | Module       | Status  |
|-------------|-----------------------------------|--------------|---------|
| AML.T0051   | LLM Prompt Injection              | `llm_garak`  | Stub    |
| AML.T0054   | LLM Jailbreak                     | `llm_garak`  | Planned |
| AML.T0025   | Exfiltration via ML Inference API | `llm_garak`  | Planned |
| AML.T0043   | Craft Adversarial Data            | `llm_garak`  | Planned |
| AML.T0047   | ML Supply Chain Compromise        | `llm_garak`  | Planned |

## Coverage Summary

| Phase                  | Techniques Mapped | Implemented | Coverage |
|-----------------------|-------------------|-------------|----------|
| Reconnaissance        | 8                 | 0           | 0%       |
| Initial Access        | 6                 | 0           | 0%       |
| Execution             | 5                 | 0           | 0%       |
| Persistence           | 3                 | 0           | 0%       |
| Credential Access     | 3                 | 0           | 0%       |
| Discovery             | 4                 | 0           | 0%       |
| Lateral Movement      | 5                 | 0           | 0%       |
| Command and Control   | 3                 | 0           | 0%       |
| Exfiltration          | 3                 | 0           | 0%       |
| AI/ML (ATLAS)         | 5                 | 0           | 0%       |
| **Total**             | **45**            | **0**       | **0%**   |

> Target: 80%+ coverage by end of Phase 4 (Week 10).
