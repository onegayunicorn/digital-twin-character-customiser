# Protocol: WebhookValidatorProtocol

> Capability #166 — **Webhook Validator** · Domain: Access & Zero Trust · Access: `write`

## Purpose
HMAC-SHA256 webhook signature validation with per-tenant secrets.

## Interface contract
```typescript
// protocol: WebhookValidatorProtocol
interface WebhookValidatorProtocol extends BaseOperation {
  id: string;
  name: 'Webhook Validator';
  accessLevel: 'write';
  category: 'Access & Zero Trust';
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
| Trigger(s) | [`WebhookReceivedTrigger`](../triggers/WebhookValidatorTrigger.md) |
| Task(s) | [`ValidateSignatureTask`](../tasks/WebhookValidatorTask.md), [`LogWebhookTask`](../tasks/WebhookValidatorTask.md) |
| Workflow | [`WebhookValidatorWorkflow`](../workflows/WebhookValidatorWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Receive -> Validate HMAC -> Accept/Reject -> Log
