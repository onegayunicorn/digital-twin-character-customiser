# Protocol: SelectConfigurationWriteProtocol

> Capability #61 — **Select Configuration Write** · Domain: Security & Edge · Access: `write`

## Purpose
Conditional selection, feature targeting, and environment routing.

## Interface contract
```typescript
// protocol: SelectConfigurationWriteProtocol
interface SelectConfigurationWriteProtocol extends BaseOperation {
  id: string;
  name: 'Select Configuration Write';
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
| Trigger(s) | [`SelectConfigUpdatedTrigger`](../triggers/SelectConfigurationWriteTrigger.md) |
| Task(s) | [`UpdateSelectConfigurationTask`](../tasks/SelectConfigurationWriteTask.md) |
| Workflow | [`SelectConfigurationWriteWorkflow`](../workflows/SelectConfigurationWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Define criteria -> Assign targets -> Validate -> Deploy
