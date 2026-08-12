# Protocol: AddressMapsWriteProtocol

> Capability #84 — **Address Maps Write** · Domain: Load Balancing & Traffic · Access: `write`

## Purpose
IP/region-to-pool mapping, weighted routing, and geo-steering.

## Interface contract
```typescript
// protocol: AddressMapsWriteProtocol
interface AddressMapsWriteProtocol extends BaseOperation {
  id: string;
  name: 'Address Maps Write';
  accessLevel: 'write';
  category: 'Load Balancing & Traffic';
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
| Trigger(s) | [`AddressMapUpdatedTrigger`](../triggers/AddressMapsWriteTrigger.md) |
| Task(s) | [`ManageAddressMapTask`](../tasks/AddressMapsWriteTask.md) |
| Workflow | [`AddressMapsWriteWorkflow`](../workflows/AddressMapsWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Define mappings -> Assign priority -> Validate -> Deploy
