# Domain Strategy

**Owner:** Business Agent · Platform: Cloudflare Registrar + DNS (per the 131-item spec:
`RegistrarDomainsAdmin`, `AccountDNSSettingsWrite`, `AccountSSLandCertificatesWrite`).

## 1. Naming candidates (verify availability before use)

| Candidate | Suitability | Notes |
|---|---|---|
| `invisiblepressure.com` | High — descriptive | Primary contender |
| `invisiblepressure.ai` | High — tech positioning | If available via .ai registry |
| `duptheory.com` / `dup.space` | Medium | Theory brand |
| `vrmemories.app` / `vrmemories.io` | High for VR line | Product brand |
| `ipssensor.com` / `ipstech.io` | Medium | Hardware line |

**Recommendation:** acquire a **brand master domain** (e.g. `invisiblepressure.com`) for
the company + product subdomains, and one product domain per line (VRmemories, IPS) when
budget allows. Do not squat; register only what will be used.

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
