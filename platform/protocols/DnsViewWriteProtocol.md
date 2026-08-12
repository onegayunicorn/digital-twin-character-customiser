# Protocol: DnsViewWriteProtocol

> Capability #32 — **DNS View Write** · Domain: Domain, DNS & Networking · Access: `write`

## Purpose
Split DNS, views, and geography-based resolution.

## Interface contract
```typescript
// protocol: DnsViewWriteProtocol
interface DnsViewWriteProtocol extends BaseOperation {
  id: string;
  name: 'DNS View Write';
  accessLevel: 'write';
  category: 'Domain, DNS & Networking';
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
| Trigger(s) | [`DNSViewConfigTrigger`](../triggers/DnsViewWriteTrigger.md) |
| Task(s) | [`ConfigureDNSViewTask`](../tasks/DnsViewWriteTask.md) |
| Workflow | [`DnsViewWriteWorkflow`](../workflows/DnsViewWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Define view -> Assign zones -> Set match -> Deploy
