# Protocol: RepoSandboxProtocol

> Capability #152 — **Repo Sandbox** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Per-repository agent + sandbox workspace generation from the 420-repo inventory (manifest, sim stub, README).

## Interface contract
```typescript
// protocol: RepoSandboxProtocol
interface RepoSandboxProtocol extends BaseOperation {
  id: string;
  name: 'Repo Sandbox';
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
| Trigger(s) | [`RepoInventoriedTrigger`](../triggers/RepoSandboxTrigger.md) |
| Task(s) | [`GenerateSandboxTask`](../tasks/RepoSandboxTask.md), [`InstantiateRepoAgentTask`](../tasks/RepoSandboxTask.md) |
| Workflow | [`RepoSandboxWorkflow`](../workflows/RepoSandboxWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Load repo -> Generate sandbox -> Agent -> Verify -> Report
