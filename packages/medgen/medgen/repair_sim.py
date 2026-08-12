"""Repair-mechanism simulation for DMD nonsense mutations.

Models *mechanisms only*:
  - Exon skipping (ASO): feasible on hotspot exons; effect = in-frame restoration
    of downstream reading frame (models the established dystrophin-bypass concept)
  - Base editing (ABE/CBE): feasible when the stop codon type matches the editor
    (ABE: T->C; CBE: C->T)
  - Prime editing: feasible for any substitution (no PAM-blocked modelling here)

OUTPUT CONTRACT: every result carries clinical_claim_level="none" and a
disclaimer. This module does NOT assert efficacy, safety, or clinical benefit.
"""
from __future__ import annotations

from .dmd_mutations import classify_mutation


def repair_strategies(exon: int, cdna_change: str, protein_change: str) -> dict:
    cls = classify_mutation(exon, cdna_change, protein_change)
    stop = cls["stop_codon"]
    strategies = []
    if cls["exon_skipping_eligible"]:
        strategies.append({
            "mechanism": "exon_skipping",
            "rationale": "hotspot exon; in-frame skipping concept",
            "model_status": "feasible_in_model",
        })
    if stop in ("TAG", "TAA", "TGA"):
        # CBE converts C->T (e.g., CAG->TAG is a CBE *off* switch; here we model
        # the reverse concept: base editors can convert a stop codon back to a
        # sense codon only for specific contexts — modeled as a feasibility flag)
        strategies.append({
            "mechanism": "base_editing",
            "rationale": f"stop codon {stop} present; editor feasibility is context-dependent",
            "model_status": "context_dependent",
        })
    strategies.append({
        "mechanism": "prime_editing",
        "rationale": "prime editing templates can restore any substitution",
        "model_status": "feasible_in_model",
    })
    return {
        "mutation": {"exon": exon, "cdna_change": cdna_change,
                     "protein_change": protein_change, "stop_codon": stop},
        "strategies": strategies,
        "clinical_claim_level": "none",
        "disclaimer": ("Simulated mechanism analysis only. No efficacy, safety, or "
                       "clinical benefit is claimed. Wet-lab and trial validation required."),
    }


def cohort_summary(rows: list[tuple]) -> dict:
    """Aggregate strategy feasibility across a mutation cohort."""
    n = len(rows)
    skipping = sum(1 for e, c, p, *_ in rows
                   if classify_mutation(e, c, p)["exon_skipping_eligible"])
    return {
        "cohort_size": n,
        "exon_skipping_eligible": skipping,
        "skipping_fraction": round(skipping / n, 3) if n else 0.0,
        "clinical_claim_level": "none",
        "disclaimer": "Mechanism feasibility only; not efficacy.",
    }
