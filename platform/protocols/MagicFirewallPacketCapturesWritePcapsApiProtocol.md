# Protocol: MagicFirewallPacketCapturesWritePcapsApiProtocol

> Capability #94 — **Magic Firewall Packet Captures - Write PCAPs API** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Filter, duration, sampling, storage, and export of PCAP captures.

## Interface contract
```typescript
// protocol: MagicFirewallPacketCapturesWritePcapsApiProtocol
interface MagicFirewallPacketCapturesWritePcapsApiProtocol extends BaseOperation {
  id: string;
  name: 'Magic Firewall Packet Captures - Write PCAPs API';
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
| Trigger(s) | [`PacketCaptureTrigger`](../triggers/MagicFirewallPacketCapturesWritePcapsApiTrigger.md), [`SecurityEventTrigger`](../triggers/MagicFirewallPacketCapturesWritePcapsApiTrigger.md) |
| Task(s) | [`CapturePacketsTask`](../tasks/MagicFirewallPacketCapturesWritePcapsApiTask.md) |
| Workflow | [`MagicFirewallPacketCapturesWritePcapsApiWorkflow`](../workflows/MagicFirewallPacketCapturesWritePcapsApiWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Define filter -> Start -> Capture -> Stop -> Export -> Analyze
