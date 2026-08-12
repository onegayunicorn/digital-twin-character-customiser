# IPS — Invisible Pressure Sensor: Engineering Specification

**Source:** "Invisible Pressure Sensor (IPS) — Nanophotonic Detection" manuscript (2026)
**Status:** Engineering spec — prototype phase 0 (see [`../hardware/sourcing-plan.md`](../hardware/sourcing-plan.md))
**Claim status:** Detection principles are HYPOTHESIS until prototype validation.

## 1. Concept

A transparent nanophotonic lattice that detects ionic-potential pressure via laser
interferometry — "invisible" because lattice features are smaller than visible-light
wavelengths (no Mie scattering). Integrated with **Dynamic Electrostatic Containment
(DEC)**, an energy sphere that concentrates ambient ionic/entropy waste into a usable
potential, plus an emergency graphene/CNT supercapacitor for instantaneous dump.

## 2. Target specifications

| Feature | Specification | Status |
|---|---|---|
| Sensor transparency | > 99.9 % (nanophotonic lattice) | HYPOTHESIS (fabrication pending) |
| Detection threshold | 10⁻¹⁸ Pa (attopascal) | HYPOTHESIS — lab-grade atom interferometry territory; aggressive |
| Detection method | Laser interferometry, phase shift Δφ = 2πnL/λ | SIMULATED (model in `packages/sensor`) |
| Containment | Dynamic Electrostatic Containment (DEC) | SIMULATED |
| Recovery efficiency | ~40–60 % of thermal waste | SIMULATED (design target) |
| Capacitor response | < 5 ns (R_ESR·C) | SIMULATED (material-dependent) |
| UI | Twin-State dashboard (phase-synced, zero-chrome) | DESIGN |

## 3. Architecture

```
┌─────────────────────── IPS stack ───────────────────────┐
│ 1. SENSOR ARRAY   graphene-doped glass + nanophotonic   │
│    lattice, vacuum-sealed micro-gap, cold-photon laser   │
│ 2. DEC CORE       potential well V(r), Lorentz coils,    │
│    inward spiral collection, saturation hold            │
│ 3. STORAGE        graphene/CNT supercapacitor, hot       │
│    standby, <5 ns dump path                             │
│ 4. DASHBOARD      Twin-State UI: sphere opacity = charge │
│    density; Psi-Sync line; entropy reclaim shadow fill;  │
│    capacitor tension border; physical-tap dump trigger   │
└──────────────────────────────────────────────────────────┘
```

## 4. Detection physics

- **Phase shift** `Δφ = 2π·n·L/λ` — an ion passing the micro-gap shifts the fringe;
  sensitivity scales with path length and index change.
- **Invisibility** — sub-wavelength lattice features avoid Mie scattering.
- **DEC collection** — `F = q(E + v×B)`, reshaped dynamically to pull stray charge to the
  sphere centre; saturation follows the energy density `u = ½ε₀E² + B²/2μ₀`.
- **Reclaim** — `η_S = E_recovered/E_waste`; design band 40–60 % of hardware thermal waste.
- **Emergency dump** — `U_C = ½CV²`, `τ = R_ESR·C < 5 ns`.

## 5. Dashboard (Twin-State UI)

- Sphere visual is a **phase-synced projection** of the physical charge state (design
  concept: entanglement-twin mapping; implementation: event-sourced state sync — see
  [`../platform/ar-vr-digital-twin.md`](../platform/ar-vr-digital-twin.md)).
- Metrics: Ψ-sync, Entropy Reclaim Rate, Void Capacity, Capacitor Tension.
- Interaction: physical tap on sensor frame triggers dump (haptic); zero-chrome design.

## 6. Test strategy

- Unit: model verification in `tests/unit/test_ips_model.py` (23 tests green).
- HIL: bench harness with calibrated pressure sources; validation protocol in
  [`../testing/test-plan.md`](../testing/test-plan.md).
- Fabrication milestones in [`../hardware/sourcing-plan.md`](../hardware/sourcing-plan.md).
