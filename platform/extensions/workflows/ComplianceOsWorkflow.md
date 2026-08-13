# Workflow: ComplianceOsWorkflow

> Capability #156 — **Compliance OS**

## Definition
```typescript
// workflow: ComplianceOsWorkflow
const ComplianceOsWorkflow: WorkflowDefinition = {
  workflowId: 'ComplianceOsWorkflow',
  version: '1.0.0',
  description: 'Compliance OS — Gate chain -> Evidence -> Allow/Block -> Audit',
  trigger: { triggerId: 'FeatureEnableRequestTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Gate chain'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Evidence'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Allow/Block'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Audit'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Gate chain -> Evidence -> Allow/Block -> Audit

## Related artifacts
- [Protocol](../protocols/ComplianceOsProtocol.md) · [Trigger(s)](../triggers/ComplianceOsTrigger.md) · [Tasks](../tasks/ComplianceOsTask.md)
