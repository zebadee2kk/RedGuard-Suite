# Research & Design References

This directory contains research materials and design rationale gathered during the planning phase of RedGuard Suite. These documents capture industry best practices, tool evaluations, and architectural decisions that informed the project design.

## Documents

| File | Topic | Source |
|------|-------|--------|
| [initial_design.md](initial_design.md) | Original repo architecture, tool integrations, and transition to local deployment | Planning phase |
| [modern_red_team_practices.md](modern_red_team_practices.md) | What modern red teams and security firms actually do — toolchains, methods, and design principles | Industry research |
| [executive_validation.md](executive_validation.md) | Security model validation, toolchain assessment, legal/compliance, maturity roadmap | Architecture review |
| [garak_integration_plan.md](garak_integration_plan.md) | Garak (LLM red teaming) integration design, probe categories, and automation patterns | AI security research |

## How These Inform the Project

- **Architecture**: The modular pipeline design and config-driven approach came from studying how enterprise red teams chain tools
- **Safety**: The multi-layer safety architecture (dry_run, allowed_networks, stop_on_prod) was informed by operational risk analysis
- **ATT&CK Mapping**: The technique coverage plan draws from real engagement workflows documented here
- **AI/LLM Testing**: The Garak integration approach follows the patterns validated in the executive review
- **Governance**: Data classification, encryption requirements, and legal considerations shaped the public/internal repo split
