# Workflow: McpPortalsWriteWorkflow

> Capability #29 — **MCP Portals Write**

## Definition
```typescript
// workflow: McpPortalsWriteWorkflow
const McpPortalsWriteWorkflow: WorkflowDefinition = {
  workflowId: 'McpPortalsWriteWorkflow',
  version: '1.0.0',
  description: 'MCP Portals Write — Build -> Configure auth -> Integrate -> Publish',
  trigger: { triggerId: 'PortalConfigUpdatedTrigger' },
  steps: [
  - stepId: 'step1'
    name: 'Build'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step2'
    name: 'Configure auth'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step3'
    name: 'Integrate'
    taskRef: 'Task'
    continueOnError: false
  - stepId: 'step4'
    name: 'Publish'
    taskRef: 'Task'
    continueOnError: false
  ],
  errorHandling: { onFailure: 'retry', notifyOnError: true },
  executionMode: 'sequential',
  timeoutTotalMs: 120000
};
```

## Pipeline
Build -> Configure auth -> Integrate -> Publish

## Related artifacts
- [Protocol](../protocols/McpPortalsWriteProtocol.md) · [Trigger(s)](../triggers/McpPortalsWriteTrigger.md) · [Tasks](../tasks/McpPortalsWriteTask.md)
