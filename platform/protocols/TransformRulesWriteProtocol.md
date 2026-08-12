# Protocol: TransformRulesWriteProtocol

> Capability #59 — **Transform Rules Write** · Domain: Security & Edge · Access: `write`

## Purpose
Header modification, URI rewrite, host, path, and query string transforms.

## Interface contract
```typescript
// protocol: TransformRulesWriteProtocol
interface TransformRulesWriteProtocol extends BaseOperation {
  id: string;
  name: 'Transform Rules Write';
  accessLevel: 'write';
  category: 'Security & Edge';
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
| Trigger(s) | [`TransformRuleUpdatedTrigger`](../triggers/TransformRulesWriteTrigger.md) |
| Task(s) | [`CreateTransformRuleTask`](../tasks/TransformRulesWriteTask.md) |
| Workflow | [`TransformRulesWriteWorkflow`](../workflows/TransformRulesWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Define match -> Set action -> Order -> Test -> Apply
