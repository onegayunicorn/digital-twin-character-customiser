# Medtech Hardware Procurement & Global Deployment

**Owner:** Sensor-Design / Business Agents · **Status:** planning
**Reality rule:** procurement is limited to real, purchasable equipment (sequencing, PCR,
EEG, microfluidics, compute). The document's "DNA-origami nanobots", "petal dispersal
carriers", and "SiC nanosensors at $1K" are NOT procurable commodities — they are excluded
(claims H5, N5) until a credible supplier exists.

## 1. Research-laboratory hardware (procurable now)

| Item | Spec | Source | Est. cost |
|---|---|---|---|
| OpenBCI Cyton + Daisy (EEG/EMG, 16ch) | 250 Hz, 24-bit | OpenBCI | $1,000-2,000 |
| qPCR cycler (DMD exon analysis) | 96-well, 4-channel | Bio-Rad / Thermo | $8-15K |
| Benchtop sequencer (targeted NGS) | MiSeq-class | Illumina / Element | $30-100K |
| Electrophoresis + gel imager | fragment analysis | Bio-Rad / Azure | $3-6K |
| Microfluidics kit (droplet PCR) | — | Dolomite / Elveflow | $5-15K |
| HPC workstation (sims, GA) | 64-core, 128 GB | Dell/HP | $5-10K |
| Optics bench (sonar-5d visualization rig) | — | Thorlabs | $3-8K |

**Phase budget:** $60-140K for a full research bench; $5-8K for the simulation-only path.

## 2. Supplier & MOQ rules

- Single units / low MOQ: OpenBCI, Bio-Rad, Thermo, Thorlabs, Digi-Key.
- Volume consumables (PCR kits, sequencing reagents): Alibaba-class wholesale only for
  non-GMP consumables; **clinical-grade consumables from authorized distributors only**.
- Two-source critical reagents; cold-chain logistics for sequencing kits.

## 3. Global deployment regulatory map (software + hardware)

| Region | Software (research) | Clinical device path |
|---|---|---|
| US | Research-use labeling; no FDA clearance for RUO tools | FDA 510(k)/De Novo (SaMD); IND for therapeutics |
| EU | General software; GDPR for health data | EU MDR Class I-IIa; AI Act high-risk for clinical BCI |
| UK | MHRA guidance | UKCA/MHRA registration |
| Australia (AU) | TGA: software as medical device if diagnostic claims | TGA ARTG |
| Japan | PMDA consultation | PMDA approval |

**Data compliance:** patient data (if any pilot) — GDPR/CCPA/HIPAA; our platform's
client-side encryption + audit chain (manifests/buckets.yaml) is the design baseline.

## 4. Deployment architecture (global)

- Edge: Workers (Cloudflare) per region → latency <100 ms; R2 buckets per-region
  (data residency); Zero-Trust access for hospital tenants (ZeroTrustWrite spec).
- On-prem option for hospitals: sovereign orchestrator (stdlib-only) runs air-gapped with
  local-first storage — the "sovereign" positioning is the compliance moat.

## 5. Procurement guardrails

1. No supplier whose product claims "cure" or unverified efficacy (register G1/H1 checks).
2. Certifications: CE/FCC/RoHS for hardware; IVD-grade where applicable (IVDR).
3. Budgets include freight, duties, cold chain, and calibration.
4. Nanobot/BCI-implant lines: only after regulatory engagement + credible supplier audit.
