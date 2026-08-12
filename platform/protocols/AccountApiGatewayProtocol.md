# Protocol: AccountApiGatewayProtocol

> Capability #63 — **Account API Gateway** · Domain: Account, Auth, Email & Billing · Access: `write`

## Purpose
API definitions, auth, quotas, transforms, and CORS for the API gateway.

## Interface contract
```typescript
// protocol: AccountApiGatewayProtocol
interface AccountApiGatewayProtocol extends BaseOperation {
  id: string;
  name: 'Account API Gateway';
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
| Trigger(s) | [`APIRequestTrigger`](../triggers/AccountApiGatewayTrigger.md), [`GatewayConfigTrigger`](../triggers/AccountApiGatewayTrigger.md) |
| Task(s) | [`ConfigureAPIGatewayTask`](../tasks/AccountApiGatewayTask.md) |
| Workflow | [`AccountApiGatewayWorkflow`](../workflows/AccountApiGatewayWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Define API -> Set auth -> Attach policies -> Deploy -> Test
