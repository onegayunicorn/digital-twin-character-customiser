# Base Types & Contracts

Canonical interfaces referenced by every protocol/trigger/workflow/task definition
in this platform contract. All capabilities in `protocols/`, `triggers/`,
`workflows/`, and `tasks/` conform to these base types.

## 1. BaseOperation (protocol base)

```typescript
// protocol: BaseOperation
interface BaseOperation {
  id: string;
  name: string;
  description: string;
  accessLevel: 'read' | 'write' | 'admin';
  category: string;
  serviceDomain: string;
  enabled: boolean;
  rateLimit?: RateLimit;
  auditLogging: boolean;
}

interface RateLimit {
  requestsPerSecond: number;
  requestsPerMinute: number;
  burstLimit: number;
}
```

## 2. TriggerContract (trigger base)

```typescript
// protocol: TriggerContract
interface TriggerContract {
  triggerId: string;
  triggerType: 'event' | 'schedule' | 'api' | 'webhook' | 'metric' | 'log';
  condition: TriggerCondition;
  actionTarget: string;
  enabled: boolean;
  retryPolicy?: RetryPolicy;
  timeoutMs: number;
}

interface TriggerCondition {
  eventSource?: string;
  matchExpression?: string;
  threshold?: number;
  cronSchedule?: string;
  httpMethod?: string;
  pathPattern?: string;
}

interface RetryPolicy {
  maxAttempts: number;
  backoffStrategy: 'linear' | 'exponential';
  delayMs: number;
}
```

## 3. WorkflowDefinition (workflow base)

```typescript
// protocol: WorkflowDefinition
interface WorkflowDefinition {
  workflowId: string;
  version: string;
  description: string;
  trigger: TriggerContract;
  steps: WorkflowStep[];
  errorHandling: ErrorHandlingStrategy;
  executionMode: 'sequential' | 'parallel';
  timeoutTotalMs: number;
}

interface WorkflowStep {
  stepId: string;
  name: string;
  taskRef: string;
  dependsOn?: string[];
  inputMapping: Record<string, string>;
  outputMapping: Record<string, string>;
  continueOnError: boolean;
}

interface ErrorHandlingStrategy {
  onFailure: 'abort' | 'retry' | 'fallback' | 'ignore';
  fallbackTask?: string;
  notifyOnError: boolean;
}
```

## 4. TaskSpecification (task base)

```typescript
// protocol: TaskSpecification
interface TaskSpecification {
  taskId: string;
  operationRef: string;
  inputSchema: Record<string, any>;
  outputSchema: Record<string, any>;
  implementation: 'api_call' | 'script' | 'function' | 'pipeline';
  endpoint?: string;
  code?: string;
  dependencies?: string[];
}
```
