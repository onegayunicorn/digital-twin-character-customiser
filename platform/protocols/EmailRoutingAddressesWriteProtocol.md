# Protocol: EmailRoutingAddressesWriteProtocol

> Capability #76 — **Email Routing Addresses Write** · Domain: Account, Auth, Email & Billing · Access: `write`

## Purpose
Aliases, destinations, and forwarding addresses for email routing.

## Interface contract
```typescript
// protocol: EmailRoutingAddressesWriteProtocol
interface EmailRoutingAddressesWriteProtocol extends BaseOperation {
  id: string;
  name: 'Email Routing Addresses Write';
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
| Trigger(s) | [`EmailAddressCreatedTrigger`](../triggers/EmailRoutingAddressesWriteTrigger.md) |
| Task(s) | [`ManageEmailRoutingAddressTask`](../tasks/EmailRoutingAddressesWriteTask.md) |
| Workflow | [`EmailRoutingAddressesWriteWorkflow`](../workflows/EmailRoutingAddressesWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Create -> Verify DNS -> Activate -> Test
