import math

import numpy as np
import pytest

from medgen.dmd_mutations import (NONSENSE_TABLE, STOP_CODONS,
                                  all_classified, classify_mutation,
                                  premature_stop_position, stop_codon_for)
from medgen.repair_sim import cohort_summary, repair_strategies
from medgen.cancer_dynamics import gompertz_growth, therapy_response


def test_stop_codon_mapping():
    assert stop_codon_for("c.702C>A") == "TAG"
    assert stop_codon_for("c.7912C>T") == "TGA"
    assert stop_codon_for("c.3340A>T") == "TAG"


def test_classify_mutation_hotspot():
    cls = classify_mutation(44, "c.7912C>T", "p.Arg2638*")
    assert cls["is_nonsense"] is True
    assert cls["exon_skipping_eligible"] is True
    cls2 = classify_mutation(3, "c.94C>T", "p.Gln32*")
    assert cls2["exon_skipping_eligible"] is False


def test_table_structure_and_all_nonsense():
    rows = all_classified()
    assert len(rows) == len(NONSENSE_TABLE)
    assert all(r["is_nonsense"] for r in rows)
    assert all(r["stop_codon"] in STOP_CODONS for r in rows)


def test_premature_stop():
    r = premature_stop_position(3685, 1085)
    assert r["is_premature"] is True
    assert r["truncation_frac"] > 0.7
    assert premature_stop_position(1000, 1200)["is_premature"] is False


def test_repair_strategies_contract():
    res = repair_strategies(44, "c.7912C>T", "p.Arg2638*")
    assert res["clinical_claim_level"] == "none"
    assert "disclaimer" in res
    mechanisms = [s["mechanism"] for s in res["strategies"]]
    assert "exon_skipping" in mechanisms
    assert "prime_editing" in mechanisms


def test_repair_no_skipping_for_non_hotspot():
    res = repair_strategies(3, "c.94C>T", "p.Gln32*")
    mechanisms = [s["mechanism"] for s in res["strategies"]]
    assert "exon_skipping" not in mechanisms


def test_cohort_summary_fraction():
    s = cohort_summary(NONSENSE_TABLE)
    assert s["cohort_size"] == len(NONSENSE_TABLE)
    assert 0.1 < s["skipping_fraction"] < 0.5  # ~25% hotspot band
    assert s["clinical_claim_level"] == "none"


def test_gompertz_growth_monotonic():
    t = np.linspace(0, 100, 200)
    n = gompertz_growth(t, 1e4, 0.3, 0.02)
    assert np.all(np.diff(n) > 0)


def test_therapy_response_nadir_and_rebound():
    t = np.linspace(0, 150, 300)
    res = therapy_response(t, 1e6, 0.3, 0.02, kill_rate=0.05, resistance_rate=0.01)
    assert res["clinical_claim_level"] == "none"
    assert res["nadir"] < res["end_tumor"]  # rebound after resistance
    assert res["rebound_detected"] is True


def test_therapy_response_no_rebound_without_resistance():
    t = np.linspace(0, 150, 300)
    res = therapy_response(t, 1e6, 0.3, 0.02, kill_rate=0.05, resistance_rate=0.0)
    assert res["rebound_detected"] is False
