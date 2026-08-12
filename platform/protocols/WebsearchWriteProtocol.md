# Protocol: WebsearchWriteProtocol

> Capability #6 — **Websearch Write** · Domain: Agents & AI / Automation · Access: `write`

## Purpose
Search scope, allowed domains, rate limits, and result filtering for web search.

## Interface contract
```typescript
// protocol: WebsearchWriteProtocol
interface WebsearchWriteProtocol extends BaseOperation {
  id: string;
  name: 'Websearch Write';
  accessLevel: 'write';
  category: 'Agents & AI / Automation';
  serviceDomain: string;
  enabled: boolean;
  auditLogging: boolean;
  rateLimit?: RateLimit;
  // capability-specific contract fields
}
```

## Related artifacts
| Type | File |
|---|---|
| Trigger(s) | [`SearchConfigUpdatedTrigger`](../triggers/WebsearchWriteTrigger.md) |
| Task(s) | [`UpdateWebsearchConfigTask`](../tasks/WebsearchWriteTask.md) |
| Workflow | [`WebsearchWriteWorkflow`](../workflows/WebsearchWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Validate -> Apply -> Test -> Audit
