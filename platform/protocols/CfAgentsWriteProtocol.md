# Protocol: CfAgentsWriteProtocol

> Capability #2 — **CF Agents Write** · Domain: Agents & AI / Automation · Access: `write`

## Purpose
Agent lifecycle, configuration, deployment, and permissions management.

## Interface contract
```typescript
// protocol: CfAgentsWriteProtocol
interface CfAgentsWriteProtocol extends BaseOperation {
  id: string;
  name: 'CF Agents Write';
  accessLevel: 'write';
  category: 'Agents & AI / Automation';
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
| Trigger(s) | [`AgentDeploymentTrigger`](../triggers/CfAgentsWriteTrigger.md), [`AgentConfigChangeTrigger`](../triggers/CfAgentsWriteTrigger.md) |
| Task(s) | [`ProvisionUpdateAgentTask`](../tasks/CfAgentsWriteTask.md) |
| Workflow | [`CfAgentsWriteWorkflow`](../workflows/CfAgentsWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Validate spec -> Deploy -> Health check -> Activate
