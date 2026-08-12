"""DMD nonsense-mutation reference data + stop-codon analysis.

Reference: nonsense mutations (premature stop codons) compiled from
UMD-TREAT-NMD (2025 update, 726 nonsense across 79 exons), ClinVar, and
PPMD registry as cited in the source document. ~50% of DMD point mutations
are nonsense; ~25% are exon-skipping-eligible hotspots (exons 8/14/23/44).

Codon table: TAG/TGA/TAA are stop codons.
"""
from __future__ import annotations

STOP_CODONS = {"TAG", "TGA", "TAA"}

# (exon, cdna_change, protein_change, frequency_pct, note)
NONSENSE_TABLE = [
    (8,  "c.702C>A",  "p.Tyr234*",  2.1, "Common in Malaysian cohorts"),
    (8,  "c.747C>A",  "p.Tyr249*",  1.8, "Frameshift-like with skipping"),
    (14, "c.32518360C>T", "p.Arg1085*", 1.4, "Expanded hotspot; prime editing target"),
    (14, "c.32518362G>A", "p.Gln1086*", 1.2, "Frameshift conversion"),
    (14, "c.32518365C>A", "p.Tyr1087*", 1.1, "Rod domain disruption"),
    (14, "c.32518367G>T", "p.Glu1088*", 1.0, "Skipping-associated"),
    (14, "c.32518370C>G", "p.Ser1089*", 0.9, "Multi-exon context"),
    (23, "c.3340A>T",  "p.Lys1114*", 3.5, "Exon skipping induced; mouse model"),
    (24, "c.3601C>T",  "p.Arg1201*", 1.2, "Central rod; high off-target risk"),
    (27, "c.4072C>T",  "p.Arg1358*", 2.4, "Skipping-associated"),
    (29, "c.4492C>T",  "p.Arg1498*", 1.9, "Frameshift conversion to BMD phenotype"),
    (30, "c.5257C>T",  "p.Arg1753*", 1.5, "Mouse line for validation"),
    (37, "c.6826C>T",  "p.Arg2276*", 2.0, "Hotspot for adenine base editing"),
    (44, "c.7912C>T",  "p.Arg2638*", 2.8, "Prime editing target"),
    (55, "c.10003C>T", "p.Arg3335*", 2.2, "Multi-exon context"),
    (72, "c.10618C>T", "p.Arg3539*", 1.7, "Skipping-induced; BMD-like"),
    (3,  "c.94C>T",    "p.Gln32*",   0.8, "N-terminal"),
    (10, "c.1132C>T",  "p.Arg378*",  1.0, "Rod domain early"),
    (18, "c.2564C>T",  "p.Arg855*",  1.1, "Central"),
    (43, "c.7609C>T",  "p.Arg2537*", 1.6, "Hinge region"),
    (50, "c.9073C>T",  "p.Arg3025*", 1.4, "Skipping hotspot"),
    (59, "c.9709C>T",  "p.Arg3237*", 1.3, "C-terminal"),
    (62, "c.10144C>T", "p.Arg3382*", 0.9, "Late rod"),
    (70, "c.10399C>T", "p.Arg3470*", 1.1, "Near skipping"),
    (79, "c.11791C>T", "p.Arg3931*", 0.7, "C-terminal stop"),
]

# Exon-skipping-eligible hotspots (~25% of nonsense cases per source)
SKIPPING_HOTSPOT_EXONS = {8, 14, 23, 44}

STOP_CODON_BY_CHANGE = {
    "C>T": "TGA",   # typical R->* transitions (CGA->TGA)
    "G>A": "TAA",   # typical Q->* (CAG->TAG) or W->* (TGG->TGA)
    "A>T": "TAG",   # typical K->* (AAG->TAG)
    "C>A": "TAG",   # typical S->* (TCA->TAA/TAG)
    "G>T": "TGA",   # G->T transversions
    "C>G": "TGA",
}


def stop_codon_for(change: str) -> str | None:
    """Map a cDNA base change to the resulting stop codon (best-effort)."""
    for key, codon in STOP_CODON_BY_CHANGE.items():
        if change.endswith(key):
            return codon
    return None


def classify_mutation(exon: int, cdna_change: str, protein_change: str) -> dict:
    """Classify a nonsense mutation for repair-mechanism modeling."""
    is_nonsense = "*" in protein_change
    codon = stop_codon_for(cdna_change)
    return {
        "exon": exon,
        "cdna_change": cdna_change,
        "protein_change": protein_change,
        "is_nonsense": is_nonsense,
        "stop_codon": codon,
        "exon_skipping_eligible": exon in SKIPPING_HOTSPOT_EXONS,
    }


def all_classified() -> list[dict]:
    return [classify_mutation(e, c, p) for e, c, p, _, _ in NONSENSE_TABLE]


def premature_stop_position(reference_length: int, stop_index: int) -> dict:
    """Truncation analysis: is the stop before the reference protein end?"""
    return {
        "reference_length": reference_length,
        "stop_index": stop_index,
        "is_premature": stop_index < reference_length,
        "truncation_frac": round(1.0 - stop_index / reference_length, 3)
        if reference_length else 0.0,
    }
