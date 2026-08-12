# IPS Prototype — Hardware Sourcing Plan

**Owner:** Sensor-Design Agent · **Status:** Phase 0 planning
**Claims note:** detection performance targets are HYPOTHESIS (register E2-E5) until
bench validation. Cost ranges are planning estimates — verify with live quotes.

## 1. Sourcing strategy

- **Precision optics & lab instrumentation** → Digi-Key / Mouser / Thorlabs / Newport
  (verifiable datasheets, fast shipping, small MOQ).
- **Bulk/commodity electronics, enclosures, PCBs, cable, power** → Alibaba.com /
  PCBWay / JLCPCB (cost-driven, larger MOQs). PCB fabrication + assembly via
  JLCPCB/PCBWay is standard practice for prototypes.
- **Exotic materials (graphene-doped glass, CNT supercaps)** → specialty vendors +
  university fabrication labs; treat as R&D line items, not commodity buys.
- **BCI line (generepair-adjacent)** → OpenBCI (EEG/EMG, ~$500 class), evaluation boards
  from TI/ADI for signal chains.

## 2. BOM — Phase 0 bench rig (monitoring + detection proof)

| # | Component | Spec target | Source channel | Unit cost (est.) | MOQ |
|---|---|---|---|---|---|
| 1 | Laser diode (green 532 nm, stabilized) | 532 nm, <1 MHz linewidth | Thorlabs/Newport | $400-1,200 | 1 |
| 2 | Beam splitter + mirrors (interferometer) | broadband, λ/10 | Thorlabs | $150-400 | 1 |
| 3 | Photodiode array (balanced detection) | 200 MHz BW, low noise | Thorlabs/Digi-Key | $200-600 | 1 |
| 4 | Vacuum micro-gap cell (custom glass) | sealed, 10-100 µm gap | JLCPCB/PCBWay (glass fab) | $50-200 | 10 |
| 5 | Graphene-doped glass coupon | >90% transparency, conductive | Specialty vendor / lab | $500-2,000 | 1-5 |
| 6 | High-speed ADC + FPGA (DAQ) | 100 MS/s+, 16-bit | Digi-Key (Xilinx/Intel/Altera) | $500-1,500 | 1 |
| 7 | DEC coil array (micro-magnetic) | 1-10 mT controllable | Custom PCB coils (JLCPCB) | $100-300 | 10 |
| 8 | High-voltage driver (DEC potential well) | 0-5 kV, current-limited | Digi-Key (EMCO/XPPower) | $300-800 | 1 |
| 9 | Graphene/CNT supercapacitor (emergency dump) | ≥1 F, ESR ≤5 mΩ target | Specialty (Skeleton/CAP-XX) | $200-800 | 1-10 |
| 10 | MCU (ESP32/RP2040 class) | telemetry + safety interlock | Digi-Key/Alibaba | $5-15 | 10+ |
| 11 | Enclosure + EMI shielding | Faraday-class | Alibaba / custom | $50-150 | 10 |
| 12 | Bench PSU + measurement gear | — | Digi-Key/Keysight | $500-2,000 | 1 |

**Phase 0 budget estimate: $4-10K.** Phase 1 (monitoring product prototype) $15-30K.
Phase 2 (reclamation module) — separate engineering program.

## 3. Prototype phases

| Phase | Goal | Duration | Budget |
|---|---|---|---|
| 0 | Bench validation: interferometry sensitivity (µPa → nPa), data pipeline | 3-4 mo | $4-10K |
| 1 | Monitoring product: HPC pilot nodes, telemetry SaaS | 6 mo | $15-30K |
| 2 | Reclamation module: DEC + supercap integration | 12 mo | $50-150K |

## 4. Compliance & certification

| Market | Requirement | Trigger |
|---|---|---|
| EU | CE (EMC/LVD), RoHS | Phase 1 |
| US | FCC Part 15 (intentional radiator), UL if mains | Phase 1 |
| Global | Battery/transport regs if supercap packs ship | Phase 2 |
| Health-adjacent (BCI) | FDA Class II (2025 Neural Interface + AI SaMD guidance) | Only if BCI line advances |

Include compliance cost (est. $3-8K per certification) in phase budgets.

## 5. Procurement rules

1. **Verify before commit:** request datasheets + sample testing before MOQ orders;
   use Trade Assurance / escrow-protected payment on Alibaba.
2. **Two-source critical components** (laser, ADC, supercap).
3. **Import duties** (AU → local): include 5-10% buffer + freight.
4. **IP protection:** fabrication details as trade secrets; NDAs for specialty vendors.

## 6. Live search results (2026-08-12, Alibaba.com)

| Component | Query | Results | Match quality | Outcome |
|---|---|---|---|---|
| Laser diode module | "532nm green laser diode module" | 80 products | 24 perfect (verified suppliers among them) | Sufficient — no pivot; low-cost modules from $1.40-7.50/unit available |
| Supercapacitor | "graphene supercapacitor 1F" | 70 products | 5 direct 1F matches; 16% attribute match (< 25%) | Pivoted to suppliers: 115 suppliers, 40% capacitance-customization capability — strong pool |

Key findings for BOM: 532 nm modules are commodity-priced (sub-$10 at MOQ 1-10, ~$2-5
at MOQ 100); graphene supercapacitors with exact 1F/5.5V-3V specs are available from
several Shenzhen manufacturers (~$0.09-0.75/unit at MOQ 100), and large capacitor OEMs
offer capacitance customization for the <5 ns dump path. **Phase-0 budget impact: BOM
rows 1 and 9 are cheaper than the original estimates; update budget at next review.**

## 7. Next actions

- Request datasheets + samples before MOQ orders (verify ESR for the 1F cells — the
  <5 ns dump requirement needs low-ESR parts, not generic 1F cells).
- Further live searches available on request: ESP32 dev boards, photodiode arrays,
  beam splitters, graphene coupons, DEC coil PCB fab.
