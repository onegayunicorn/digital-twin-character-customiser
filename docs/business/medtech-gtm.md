# Medtech Go-to-Market — Hospitals, Doctors, Researchers

**Owner:** Business Agent · **Claims envelope:** [`../theory/04-claims-register.md`](../theory/04-claims-register.md) §G
**Non-negotiable:** decision-support positioning only; zero cure/efficacy claims until trial data (claims H1/H4/H6 quarantined).

## 1. Product lines (medtech)

| Line | Offer | Buyer | Status |
|---|---|---|---|
| **DMD Decision Support** | mutation classification + repair-mechanism modeling (medgen) | researchers, clinical genetics units | SIMULATED tool — pilot-ready as research software |
| **Cancer Dynamics Studio** | Gompertz therapy-response modeling | oncology researchers | SIMULATED tool |
| **Healthcare Agency** | triage scoring + case review + literature match (medagents) | hospitals (ops), doctors (decision support) | pilot software — NOT a device, no autonomous decisions |
| **Sonar-5D / crystal mesh** | geometry + visualization | research/visualization | SIMULATED tool |

## 2. Segments & messaging

| Segment | Message | Channel |
|---|---|---|
| **Researchers** | "Open, reproducible mechanism-modeling toolkit — data + code + claims register" | arXiv-adjacent bioinformatics communities, GitHub, conferences |
| **Doctors** | "Decision-support dashboard: mutation context, mechanism options, literature — your judgment stays final" | Medical societies, CME webinars, EHR-adjacent integrations (advisory) |
| **Hospitals** | "Ops triage analytics + audit-logged decision support" | Health-system innovation offices, pilots |

**Messaging guardrails:** no "cure", "treat", "diagnose", "therapy" language in product copy; every interface shows the decision-support disclaimer; efficacy claims appear only after IRB-approved studies.

## 3. Funding path (from cancer-killer process doc)

1. **NIH SBIR (Phase I)** — Project Summary, Specific Aims, Commercialization Strategy (templates in the source doc, adopted). Position: *software tools for mechanism modeling* (SBIR-friendly, lower regulatory bar than therapeutics).
2. **VC pitch** — deck structure from the source doc; **exclude** all quarantined claims (H1/H4/H6); lead with verifiable sims + claims discipline as the differentiator.
3. **Tax strategy** — R&D credits; document software-dev + simulation expenses.

## 4. Regulatory posture

- **Software tools for research:** general-purpose research software — lower regulatory burden; clearly labeled "for research use only" where appropriate.
- **Clinical deployment (future):** FDA SaMD guidance (AI/ML-enabled device software), EU MDR; the platform's audit chain + decision-support-only design are built to satisfy those requirements later.
- **DMD therapeutic path (future, not claimed):** IND → trials; see `medtech-procurement.md` for hardware; "100% sim cure" claims stay quarantined permanently.

## 5. 90-day plan

1. Publish medgen/genesis/medagents + data as research software (repo public).
2. Two researcher pilot partnerships (DMD/oncology labs).
3. NIH SBIR Phase I draft (grant templates).
4. One hospital ops pilot for triage analytics (IRB-lite, anonymized data).
