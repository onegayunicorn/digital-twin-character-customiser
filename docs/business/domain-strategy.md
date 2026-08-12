# Domain Strategy

**Owner:** Business Agent · Platform: Cloudflare Registrar + DNS (per the 131-item spec:
`RegistrarDomainsAdmin`, `AccountDNSSettingsWrite`, `AccountSSLandCertificatesWrite`).

## 1. Naming candidates (availability verified 2026-08-12 via ICANN RDAP)

| Candidate | Suitability | Availability | Notes |
|---|---|---|---|
| `invisiblepressure.com` | High — descriptive | **REGISTERED** | NameCheap, registered 2022-02-04, expires 2027-02-04, status "client transfer prohibited" (parked) — not available without a buy-out negotiation |
| `invisiblepressure.ai` | High — tech positioning | **AVAILABLE** (registry RDAP 404) | Verify at registrar at purchase time |
| `duptheory.com` | Medium | **AVAILABLE** (RDAP 404) | Theory brand |
| `dup.space` / `vrmemories.app` / `vrmemories.io` / `ipssensor.com` | Medium-high | not yet checked | Check before use |
| `ipstech.io` | Medium | not yet checked | Hardware line |

**Recommendation:** with `invisiblepressure.com` taken, the acquisition priority is
**`invisiblepressure.ai`** (brand master) or **`duptheory.com`** (theory brand) — register
one of them soon; do not squat; register only what will be used.

## 2. DNS & infrastructure layout (Cloudflare)

| Host | Service | Purpose |
|---|---|---|
| `app.invisiblepressure.com` | Workers (web) | Main web app |
| `api.invisiblepressure.com` | Workers (api) | REST/WebSocket API |
| `chat.invisiblepressure.com` | Workers (ai-chat) | AI chat module |
| `sim.invisiblepressure.com` | Workers + R2 (public) | Simulation outputs/figures |
| `vrmemories.app` | Workers (ar-vr) | VRmemories product |
| `mail.*` | Email routing | Routing to Gmail |

## 3. Setup sequence (Cloudflare)

1. **Register domain** via Cloudflare Registrar (RegistrarDomainProtocol) with
   auto-renew + transfer lock.
2. **DNS:** add records via AccountDNSSettingsWrite; enable DNSSEC (TLD support);
   proxy all A/AAAA through Cloudflare.
3. **TLS:** Universal SSL → Advanced Certificate (SAN covering all hosts); auto-renew.
4. **WAF/Turnstile:** enable managed ruleset; Turnstile on signup/chat endpoints.
5. **Email:** Cloud Email Security + Email Routing addresses (info@, support@, tpower@).
6. **Ownership:** personal account (tpower86@live.com) as owner; add team members with
   scoped API tokens (`AccountAPITokensWrite`).

## 4. Brand safety

- Claims register compliance: no domain/branding copy that asserts unverified claims.
- Trademark search + registration for chosen brand before heavy spend.
- Redirect strategy: old project names (e.g., legacy engine names) → master domain
  canonical paths to consolidate SEO.
