# Task: MagicFirewallPacketCapturesWritePcapsApiTask

> Capability #94 — **Magic Firewall Packet Captures - Write PCAPs API**

Atomic executable unit(s) for this capability.

### Task: CapturePacketsTask

```typescript
// task: CapturePacketsTask
const CapturePacketsTaskSpec: TaskSpecification = {
  taskId: 'CapturePacketsTask',
  operationRef: 'MagicFirewallPacketCapturesWritePcapsApiProtocol',
  inputSchema: { capability: 'Magic Firewall Packet Captures - Write PCAPs API' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute CapturePacketsTask

## Related artifacts
- [Protocol](../protocols/MagicFirewallPacketCapturesWritePcapsApiProtocol.md) · [Trigger(s)](../triggers/MagicFirewallPacketCapturesWritePcapsApiTrigger.md) · [Workflow](../workflows/MagicFirewallPacketCapturesWritePcapsApiWorkflow.md)
