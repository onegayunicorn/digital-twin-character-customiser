# Protocol: AccessPoliciesWriteProtocol

> Capability #110 — **Access: Policies Write** · Domain: Access & Zero Trust · Access: `write`

## Purpose
Rules, precedence, actions, include/exclude, and conditions for policies.

## Interface contract
```typescript
// protocol: AccessPoliciesWriteProtocol
interface AccessPoliciesWriteProtocol extends BaseOperation {
  id: string;
  name: 'Access: Policies Write';
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
| Trigger(s) | [`AccessPolicyTrigger`](../triggers/AccessPoliciesWriteTrigger.md) |
| Task(s) | [`CreateAccessPolicyTask`](../tasks/AccessPoliciesWriteTask.md) |
| Workflow | [`AccessPoliciesWriteWorkflow`](../workflows/AccessPoliciesWriteWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Define -> Order -> Test -> Enable -> Audit
