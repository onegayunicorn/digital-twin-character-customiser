"""Sovereign Commerce CLI.

Usage:
  python3 -m sovereign_commerce --mode health
  python3 -m sovereign_commerce --mode gate --feature digital-asset-exchange --context '{"classification":"VASP","registered":true,"aml_program":true,"kyc":true,"transaction_monitoring":true,"sanctions_ok":true,"record_keeping":true,"jurisdiction":"AU"}'
  python3 -m sovereign_commerce --mode pay --payer buyer --payee seller --amount 100
  python3 -m sovereign_commerce --mode proc  (demo tender + three-way match)
  python3 -m sovereign_commerce --mode offgrid --node n1
  python3 -m sovereign_commerce --mode serve --port 8788
"""
from __future__ import annotations

import argparse
import json
import sys


def _build():
    from .kernel import SovereignKernel
    from .jurisdiction import JurisdictionEngine
    from .compliance import ComplianceOS
    from .entities import EntityRegistry
    from .ledger import Ledger
    from .payments import PaymentOrchestrator
    from .procurement import ProcurementEngine
    from .offgrid import OffGridNode
    from .nfc_escrow import NfcEscrowBridge
    from .twins import CommerceTwinHub
    return {
        "kernel": SovereignKernel(),
        "jurisdiction": JurisdictionEngine(),
        "compliance": ComplianceOS(),
        "entities": EntityRegistry(),
        "ledger": Ledger(),
        "procurement": ProcurementEngine(),
        "escrow": NfcEscrowBridge(),
        "twins": CommerceTwinHub(),
        "payments": PaymentOrchestrator(ledger=Ledger()),
        "offgrid": OffGridNode("edge-1"),
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="sovereign_commerce")
    ap.add_argument("--mode", choices=["health", "gate", "pay", "proc",
                                       "offgrid", "serve"], default="health")
    ap.add_argument("--feature", default="digital-asset-exchange")
    ap.add_argument("--context", type=json.loads, default=None)
    ap.add_argument("--payer", default="buyer")
    ap.add_argument("--payee", default="seller")
    ap.add_argument("--amount", type=float, default=100.0)
    ap.add_argument("--node", default="edge-1")
    ap.add_argument("--port", type=int, default=8788)
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)
    ctx = _build()

    if args.mode == "health":
        print(json.dumps({"status": "ok",
                          "primitives": ctx["kernel"].primitives(),
                          "domains": 14}, indent=2 if not args.quiet else None))
        return 0
    if args.mode == "gate":
        res = ctx["compliance"].run_gates(args.feature, args.context or {})
        print(json.dumps(res, indent=2))
        return 0
    if args.mode == "pay":
        ledger = ctx["payments"].ledger
        if ledger.balance(args.payer) < args.amount:
            ledger.post(args.payer, args.amount * 5, "demo opening balance")
        res = ctx["payments"].pay(args.payer, args.payee, args.amount)
        print(json.dumps(res, indent=2))
        return 0
    if args.mode == "proc":
        p = ctx["procurement"]
        tid = p.create_tender("IT Hardware", "gov-dept", [{"sku": "LAP", "qty": 10}])
        p.submit_bid(tid, "supplier-a", 9500.0, 0.8)
        p.submit_bid(tid, "supplier-b", 8800.0, 0.6)
        ev = p.evaluate(tid)
        po = p.create_po("supplier-b", "gov-dept", [{"sku": "LAP", "qty": 10, "unit_price": 880.0}])
        grn = p.create_grn(po, [{"sku": "LAP", "qty": 10}])
        inv = p.create_invoice(po, "supplier-b", [{"sku": "LAP", "qty": 10, "unit_price": 880.0}])
        m = p.three_way_match(po, grn, inv)
        print(json.dumps({"evaluation": ev, "three_way_match": m}, indent=2))
        return 0
    if args.mode == "offgrid":
        n = ctx["offgrid"]
        n.local_transaction("edge-buyer", -50.0, "offline purchase")
        n.enter_disaster_mode()
        print(json.dumps(n.status(), indent=2))
        return 0
    if args.mode == "serve":
        from .api import CommerceAPI, make_server
        api = CommerceAPI(kernel=ctx["kernel"], jurisdiction=ctx["jurisdiction"],
                          compliance=ctx["compliance"], entities=ctx["entities"],
                          ledger=ctx["ledger"], payments=ctx["payments"],
                          procurement=ctx["procurement"], offgrid=ctx["offgrid"],
                          escrow=ctx["escrow"], twins=ctx["twins"])
        server = make_server(api, port=args.port)
        print(f"Sovereign Commerce API on http://127.0.0.1:{server.server_address[1]}")
        server.serve_forever()
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
