# Task: IpPrefixesBgpOnDemandWriteTask

> Capability #89 — **IP Prefixes: BGP On Demand Write**

Atomic executable unit(s) for this capability.

### Task: ControlBGPAnnouncementTask

```typescript
// task: ControlBGPAnnouncementTask
const ControlBGPAnnouncementTaskSpec: TaskSpecification = {
  taskId: 'ControlBGPAnnouncementTask',
  operationRef: 'IpPrefixesBgpOnDemandWriteProtocol',
  inputSchema: { capability: 'IP Prefixes: BGP On Demand Write' },
  outputSchema: { status: 'ok' },
  implementation: 'api_call',
  dependencies: []
};
```
**Description:** Execute ControlBGPAnnouncementTask

## Related artifacts
- [Protocol](../protocols/IpPrefixesBgpOnDemandWriteProtocol.md) · [Trigger(s)](../triggers/IpPrefixesBgpOnDemandWriteTrigger.md) · [Workflow](../workflows/IpPrefixesBgpOnDemandWriteWorkflow.md)
