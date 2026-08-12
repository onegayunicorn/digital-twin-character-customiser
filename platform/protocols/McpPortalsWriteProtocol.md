# Protocol: McpPortalsWriteProtocol

> Capability #29 — **MCP Portals Write** · Domain: Observability & Telemetry · Access: `write`

## Purpose
Portal configuration, access, integrations, and UI components for MCP portals.

## Interface contract
```typescript
// protocol: McpPortalsWriteProtocol
interface McpPortalsWriteProtocol extends BaseOperation {
  id: string;
  name: 'MCP Portals Write';
  accessLevel: 'write';
  category: 'Observability & Telemetry';
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
| Trigger(s) | [`PortalConfigUpdatedTrigger`](../triggers/McpPortalsWriteTrigger.md) |
| Task(s) | [`ConfigureMCPPortalTask`](../tasks/McpPortalsWriteTask.md) |
| Workflow | [`McpPortalsWriteWorkflow`](../workflows/McpPortalsWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Build -> Configure auth -> Integrate -> Publish
