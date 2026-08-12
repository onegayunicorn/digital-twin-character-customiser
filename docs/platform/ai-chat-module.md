# AI LLM Chat Module

**Spec refs:** `AIGatewayWrite` (routing/policies), `AutoRagWrite` (RAG),
`VectorizeWrite` (embeddings), `WorkersAIWrite` (model bindings), `AgentMemoryWrite`
(memory), `MessagingRead`/`QueuesWrite` (delivery).

## 1. Architecture

```
Client (web/mobile/desktop) ──► Workers ai-chat
                                  ├─ AI Gateway: model routing + rate limits + auth
                                  ├─ Vectorize: RAG over theory docs + VR memory index
                                  ├─ D1/KV: session memory + user profile + consent flags
                                  └─ Queues: async jobs (summaries, embeddings refresh)

IpAI / other agents ──► same gateway (agent runtime integration)
```

## 2. Capabilities

| Feature | Implementation |
|---|---|
| Multi-model chat | AI Gateway routing (Workers AI + external providers); per-plan rate limits |
| RAG on theory | Vectorize index of `docs/theory/*` + claims register → grounded answers |
| Claims-aware answering | Chat output checker tags claims by register status; refuses to state UNVERIFIED claims as fact |
| Session memory | KV session store + D1 profile; TTL + consent controls (AgentMemoryWrite) |
| Agent runtime | IpAI, Business, Sensor-Design agents registered as AI Gateway routes (CFAgentsWrite) |
| Safety | Turnstile on public chat; content moderation via TrustSafetyWrite; DLP on PII |

## 3. RAG pipeline

1. `docs/theory/*` → chunk → embed (Workers AI embeddings) → Vectorize index
   (`AutoRAGWrite` workflow: Connect source → Chunk → Embed → Store → Test query).
2. Chat query → embed → top-k retrieval → context assembly → generation with
   grounding constraints.
3. Index refresh on doc change via `DocumentIngestedTrigger` / `IndexUpdatedTrigger`.

## 4. Memory & consent

- Chat memory is per-user, encrypted at rest, deletable (VRmemories-grade consent UX).
- Agent memory follows `AgentMemoryWriteProtocol` (CRUD, scope, TTL, access controls).

## 5. Observability & cost

- Per-route tokens/cost via AI Gateway metrics → `WorkersObservabilityWrite` alerts.
- Model fallback chain (primary → fallback) via `AIGatewaySetupWorkflow`.

## 6. Sample flow (user asks about the theory)

```
1. POST /chat {message}            (Turnstile token required)
2. ai-chat: embed query → Vectorize top-k=5
3. AI Gateway: route to primary model with grounded context + claims tags
4. Output checker: verify claim tags present; strip unverified claims
5. Store session memory; emit usage metrics; return streamed response
```
