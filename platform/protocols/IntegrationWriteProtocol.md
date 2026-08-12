# Protocol: IntegrationWriteProtocol

> Capability #68 — **Integration Write** · Domain: Account, Auth, Email & Billing · Access: `write`

## Purpose
Third-party connectors, OAuth, webhooks, and credentials for integrations.

## Interface contract
```typescript
// protocol: IntegrationWriteProtocol
interface IntegrationWriteProtocol extends BaseOperation {
  id: string;
  name: 'Integration Write';
  accessLevel: 'write';
  category: 'Account, Auth, Email & Billing';
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
| Trigger(s) | [`IntegrationConnectedTrigger`](../triggers/IntegrationWriteTrigger.md) |
| Task(s) | [`ConfigureIntegrationTask`](../tasks/IntegrationWriteTask.md) |
| Workflow | [`IntegrationWriteWorkflow`](../workflows/IntegrationWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Select -> Auth -> Configure -> Test -> Activate
