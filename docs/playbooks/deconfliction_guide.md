# Deconfliction Guide

> Procedures for coordinating between red team and blue team during engagements to prevent confusion with real incidents.

## 1. Purpose

Deconfliction ensures that:
- Blue team doesn't waste resources investigating known red team activity
- Red team activity is distinguishable from real attacks in logs and alerts
- Real threats discovered during testing are properly escalated
- Both teams maintain operational effectiveness

## 2. Pre-Engagement Setup

### Deconfliction Channel
- Establish a **dedicated, encrypted deconfliction channel** before the engagement starts
- Both Red Team Lead and Blue Team Lead (or designated SOC analyst) must have access
- Channel must support real-time communication (not email-only)
- Backup contact method agreed (phone numbers for Red Team Lead and Blue Team Lead)

### Deconfliction Model

Choose the appropriate model based on engagement type:

| Model | Description | Use When |
|-------|-------------|----------|
| **Full knowledge** | Blue team knows scope, timing, and techniques | Purple team exercises, initial engagements |
| **Partial knowledge** | Blue team knows engagement is happening, but not specifics | Standard red team assessments |
| **Minimal knowledge** | Only Blue Team Lead knows; SOC analysts are unaware | Advanced adversary simulations |
| **No knowledge** | Only CISO and engagement sponsor know | Assumed-breach / stealth assessments |

### Deconfliction Identifiers
- Assign a unique **Engagement ID** (e.g., `RT-2026-003`)
- Red team provides a list of **source IPs/ranges** used for testing
- Red team provides approximate **testing windows** (even if broad)
- Store these in a sealed envelope or encrypted file accessible to the Blue Team Lead only

## 3. During Engagement

### When Blue Team Detects Activity

**Blue team suspects red team activity:**
1. Blue Team Lead contacts Red Team Lead on the deconfliction channel
2. Provides: timestamp, source IP, alert details, affected system
3. Red Team Lead confirms or denies within **15 minutes**
4. If confirmed: Blue team logs as "red team exercise" and continues normal monitoring
5. If denied: **Treat as a real incident** and escalate per IR procedures

**Red Team Lead initiates deconfliction:**
1. Red Team Lead contacts Blue Team Lead before high-impact actions
2. Provides: approximate timing, general technique category (not specifics)
3. Blue Team Lead acknowledges
4. This prevents unnecessary incident response escalation

### Deconfliction Log Entry

Every deconfliction event must be recorded:

```
Engagement ID: [RT-YYYY-NNN]
Timestamp:     [UTC]
Initiated by:  [Red Team / Blue Team]
Reason:        [Alert triggered / Pre-notification / Incident query]
Red Team Action: [Confirmed as red team / Not red team / Pending]
Resolution:    [Logged as exercise / Escalated as real incident]
Participants:  [Names]
```

## 4. Scenario Playbooks

### Scenario A: SOC Alert on Red Team Activity
1. SOC analyst escalates alert to Blue Team Lead
2. Blue Team Lead checks deconfliction channel and source IPs
3. If match → confirm with Red Team Lead → log as exercise
4. If no match → treat as real incident → full IR response

### Scenario B: Red Team Discovers Real Threat
1. Red Team **halts all activity immediately**
2. Red Team Lead notifies Blue Team Lead: "Real threat discovered, not our activity"
3. Red team preserves evidence without touching attacker artefacts
4. Hand off to IR team; red team engagement paused
5. See [incident_response.md](incident_response.md) for full procedure

### Scenario C: Red Team Plans High-Impact Action
1. Red Team Lead sends pre-notification: "Expect activity against [system category] in [time window]"
2. Blue Team Lead acknowledges and adjusts SOC priority if needed
3. Red team proceeds within the agreed window
4. Post-action: Red Team Lead confirms completion

### Scenario D: Engagement Overlaps with Real Incident
1. If a real incident occurs during the engagement:
2. Red team **immediately halts** all testing
3. Red Team Lead contacts Blue Team Lead to confirm halt
4. Engagement resumes only after the CISO clears it
5. Timeline and scope may be adjusted

## 5. Post-Engagement

- Include all deconfliction events in the final engagement report
- Review deconfliction effectiveness in the retrospective
- Update the deconfliction model and procedures based on lessons learned
- Blue team provides feedback on detection quality and response times
