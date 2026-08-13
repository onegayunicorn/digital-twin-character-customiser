"""Procurement engine: RFQ/RFP/tender, bid evaluation, three-way matching.

Three-way matching is the core integrity check: a supplier invoice is payable
only when PO, goods-received note (GRN), and invoice quantities/prices agree.
"""
from __future__ import annotations

import time
import uuid


class ProcurementEngine:
    def __init__(self):
        self._tenders: dict[str, dict] = {}
        self._pos: dict[str, dict] = {}
        self._grns: dict[str, dict] = {}
        self._invoices: dict[str, dict] = {}

    def create_tender(self, title: str, buyer: str, items: list[dict],
                      value_for_money_weight: float = 0.5) -> str:
        tid = f"tender_{uuid.uuid4().hex[:8]}"
        self._tenders[tid] = {"id": tid, "title": title, "buyer": buyer,
                              "items": items, "bids": [],
                              "vf_weight": value_for_money_weight,
                              "created": time.time()}
        return tid

    def submit_bid(self, tender_id: str, supplier: str, price: float,
                   quality_score: float = 0.5) -> str:
        bid = {"id": f"bid_{uuid.uuid4().hex[:8]}", "supplier": supplier,
               "price": price, "quality": quality_score}
        self._tenders[tender_id]["bids"].append(bid)
        return bid["id"]

    def evaluate(self, tender_id: str) -> list[dict]:
        """Score bids: combined = w*vf + (1-w)*quality, vf = lowest/price."""
        t = self._tenders[tender_id]
        lowest = min((b["price"] for b in t["bids"]), default=0.0)
        scored = []
        for b in t["bids"]:
            vf = lowest / b["price"] if lowest else 0.0
            score = t["vf_weight"] * vf + (1 - t["vf_weight"]) * b["quality"]
            scored.append({**b, "value_for_money": round(vf, 3),
                           "combined_score": round(score, 3)})
        scored.sort(key=lambda b: -b["combined_score"])
        return scored

    def create_po(self, supplier: str, buyer: str, lines: list[dict]) -> str:
        po = {"id": f"po_{uuid.uuid4().hex[:8]}", "supplier": supplier,
              "buyer": buyer, "lines": lines}
        self._pos[po["id"]] = po
        return po["id"]

    def create_grn(self, po_id: str, received: list[dict]) -> str:
        grn = {"id": f"grn_{uuid.uuid4().hex[:8]}", "po": po_id, "received": received}
        self._grns[grn["id"]] = grn
        return grn["id"]

    def create_invoice(self, po_id: str, supplier: str, lines: list[dict]) -> str:
        inv = {"id": f"inv_{uuid.uuid4().hex[:8]}", "po": po_id,
               "supplier": supplier, "lines": lines}
        self._invoices[inv["id"]] = inv
        return inv["id"]

    def three_way_match(self, po_id: str, grn_id: str, invoice_id: str) -> dict:
        """PO vs GRN vs invoice: quantities and unit prices must agree per line
        (within 1e-6). Returns match verdict + discrepancies."""
        po = self._pos[po_id]
        grn = self._grns[grn_id]
        inv = self._invoices[invoice_id]
        po_map = {l["sku"]: l for l in po["lines"]}
        grn_map = {l["sku"]: l for l in grn["received"]}
        inv_map = {l["sku"]: l for l in inv["lines"]}
        issues = []
        for sku, pl in po_map.items():
            gl = grn_map.get(sku)
            il = inv_map.get(sku)
            if not gl:
                issues.append(f"{sku}: no GRN line")
            if not il:
                issues.append(f"{sku}: no invoice line")
            if gl and il:
                if abs(gl["qty"] - pl["qty"]) > 1e-6:
                    issues.append(f"{sku}: GRN qty {gl['qty']} != PO qty {pl['qty']}")
                if abs(il["qty"] - pl["qty"]) > 1e-6:
                    issues.append(f"{sku}: invoice qty {il['qty']} != PO qty {pl['qty']}")
                if abs(il["unit_price"] - pl["unit_price"]) > 1e-6:
                    issues.append(f"{sku}: invoice price {il['unit_price']} != PO {pl['unit_price']}")
        return {"po": po_id, "grn": grn_id, "invoice": invoice_id,
                "match": len(issues) == 0, "issues": issues,
                "payable": len(issues) == 0}
