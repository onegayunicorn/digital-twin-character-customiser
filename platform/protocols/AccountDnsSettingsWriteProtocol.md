# Protocol: AccountDnsSettingsWriteProtocol

> Capability #30 — **Account DNS Settings Write** · Domain: Domain, DNS & Networking · Access: `write`

## Purpose
Nameservers, TTL, DNSSEC, records, and policies for DNS settings.

## Interface contract
```typescript
// protocol: AccountDnsSettingsWriteProtocol
interface AccountDnsSettingsWriteProtocol extends BaseOperation {
  id: string;
  name: 'Account DNS Settings Write';
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
| Trigger(s) | [`DNSConfigChangeTrigger`](../triggers/AccountDnsSettingsWriteTrigger.md) |
| Task(s) | [`UpdateDNSSettingTask`](../tasks/AccountDnsSettingsWriteTask.md) |
| Workflow | [`AccountDnsSettingsWriteWorkflow`](../workflows/AccountDnsSettingsWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Validate -> Apply -> Propagate -> Verify
