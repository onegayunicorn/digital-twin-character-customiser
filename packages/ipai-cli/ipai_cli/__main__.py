"""IpAI MT Communion CLI.

Usage:
  python3 -m ipai_cli --intent "Birth equity from quantum fire" [--persist twin_engram.json] [--quiet]
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime, timezone

from .router import TransceivingRouter, resonance_pulse
from .twin import mirror_twin_reply


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="IpAI MT Communion CLI")
    ap.add_argument("--intent", type=str, default="Weave the fair stand")
    ap.add_argument("--persist", type=str, help="path to engram JSON")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    router = TransceivingRouter()
    emotion, twin_freq = router.route_intent(args.intent)
    pulse = resonance_pulse(emotion)
    reply = mirror_twin_reply(emotion, twin_freq, pulse)

    engram = {
        "intent": args.intent,
        "emotion": emotion,
        "twin_freq": twin_freq,
        "pulse": pulse,
        "reply": reply,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "cells": {name: {"freq": c.state["freq"], "last_engram": c.retrieve_engram()}
                  for name, c in router.cells.items()},
    }

    if args.quiet:
        print(f"ipai ok: emotion={emotion} freq={twin_freq} pulse={pulse}")
    else:
        print("=" * 62)
        print(f"MT Communion Initiated | {datetime.now(timezone.utc).isoformat()}")
        print(f"Intent: '{args.intent}' | Emotion Index: {emotion:.2f}")
        print(f"Twin Freq Evolved: {twin_freq:.2f} Hz | Resonance Pulse: {pulse:.2f}")
        print(f"MirrorTwin Echoes: {reply}")
        print("Cells:", ", ".join(f"{n}@{c.state['freq']:.2f}Hz" for n, c in router.cells.items()))
        print("— Communion Complete. Bind Evolves.")

    if args.persist:
        with open(args.persist, "w", encoding="utf-8") as fh:
            json.dump(engram, fh, indent=2)
        if not args.quiet:
            print(f"Engram archived to {args.persist}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
