#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate the platform contract from the 131-item Cloudflare Permissions &
Capabilities specification.

Outputs (under platform/):
  protocols/<Name>Protocol.md   - interface contract per capability
  triggers/<Name>Trigger.md     - event source per capability
  workflows/<Name>Workflow.md   - end-to-end process per capability
  tasks/<Name>Task.md           - atomic unit per capability
  schemas/base-types.md         - BaseOperation/TriggerContract/WorkflowDefinition/TaskSpecification
  README.md                     - capability -> file mapping index

Usage:
  python3 scripts/generate_platform_spec.py [--dry-run]
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLATFORM = os.path.join(ROOT, "platform")

sys.path.insert(0, os.path.join(ROOT, "scripts"))
from spec_data_a import ENTRIES_A  # noqa: E402
from spec_data_b import ENTRIES_B  # noqa: E402

ENTRIES = ENTRIES_A + ENTRIES_B

ACCESS_LEVELS = ["read", "write", "admin"]


def slugify(title: str) -> str:
    """'Access: Organizations, Identity Providers, and Groups Write' ->
    'AccessOrganizationsIdentityProvidersAndGroupsWrite'"""
    s = re.sub(r"[^0-9A-Za-z ]+", "", title)
    return "".join(part.capitalize() for part in s.split())


def access_level(entry_num: int, title: str) -> str:
    t = title.lower()
    if "read" in t:
        return "read"
    if "admin" in t:
        return "admin"
    return "write"


def category(num: int) -> str:
    # Domain grouping mirroring the source document's section headers
    if num <= 7:
        return "Agents & AI / Automation"
    if num <= 14:
        return "Workers, Compute & Code"
    if num <= 20:
        return "Storage & Data"
    if num <= 23:
        return "Messaging, PubSub & Queues"
    if num <= 29:
        return "Observability & Telemetry"
    if num <= 34:
        return "Domain, DNS & Networking"
    if num <= 62:
        return "Security & Edge"
    if num <= 78:
        return "Account, Auth, Email & Billing"
    if num <= 82:
        return "Media & Streaming"
    if num <= 89:
        return "Load Balancing & Traffic"
    return "Access & Zero Trust"


def split_items(s: str):
    return [x.strip() for x in s.split("|") if x.strip()]


def protocol_md(num, title, purpose, triggers, tasks, workflow):
    slug = slugify(title)
    trig = split_items(triggers)
    task_list = split_items(tasks)
    return f"""# Protocol: {slug}Protocol

> Capability #{num} — **{title}** · Domain: {category(num)} · Access: `{access_level(num, title)}`

## Purpose
{purpose}

## Interface contract
```typescript
// protocol: {slug}Protocol
interface {slug}Protocol extends BaseOperation {{
  id: string;
  name: '{title}';
  accessLevel: '{access_level(num, title)}';
  category: '{category(num)}';
  serviceDomain: string;
  enabled: boolean;
  auditLogging: boolean;
  rateLimit?: RateLimit;
  // capability-specific contract fields
}}
```

## Related artifacts
| Type | File |
|---|---|
| Trigger(s) | {', '.join(f'[`{t}`](../triggers/{slug}Trigger.md)' for t in trig)} |
| Task(s) | {', '.join(f'[`{t}`](../tasks/{slug}Task.md)' for t in task_list)} |
| Workflow | [`{slug}Workflow`](../workflows/{slug}Workflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
{workflow}
"""


def trigger_md(num, title, triggers, tasks):
    slug = slugify(title)
    trig = split_items(triggers)
    task_list = split_items(tasks)
    lines = []
    for i, t in enumerate(trig):
        name = t.split(" (")[0]
        cond = t.split(" (")[1][:-1] if " (" in t else f"condition for {name}"
        lines.append(f"""### Trigger: {name}

```typescript
// trigger: {name}
const {name}Contract: TriggerContract = {{
  triggerId: '{name}',
  triggerType: 'event',
  condition: {{ matchExpression: '{cond}' }},
  actionTarget: '{task_list[0] if task_list else 'N/A'}',
  enabled: true,
  retryPolicy: {{ maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 }},
  timeoutMs: 30000
}};
```
""")
    return f"""# Trigger: {slug}Trigger

> Capability #{num} — **{title}**

Event source(s) that initiate execution for this capability.

{chr(10).join(lines)}
## Related artifacts
- [Protocol](../protocols/{slug}Protocol.md) · [Tasks](../tasks/{slug}Task.md) · [Workflow](../workflows/{slug}Workflow.md)
"""


def workflow_md(num, title, workflow, triggers):
    slug = slugify(title)
    steps = [s.strip() for s in workflow.split("->")]
    step_list = "".join(
        f"""  - stepId: 'step{i + 1}'
    name: '{s}'
    taskRef: 'Task'
    continueOnError: false
""" for i, s in enumerate(steps)
    )
    return f"""# Workflow: {slug}Workflow

> Capability #{num} — **{title}**

## Definition
```typescript
// workflow: {slug}Workflow
const {slug}Workflow: WorkflowDefinition = {{
  workflowId: '{slug}Workflow',
  version: '1.0.0',
  description: '{title} — {workflow}',
  trigger: {{ triggerId: '{split_items(triggers)[0]}' }},
  steps: [
{step_list}  ],
  errorHandling: {{ onFailure: 'retry', notifyOnError: true }},
  executionMode: 'sequential',
  timeoutTotalMs: 120000
}};
```

## Pipeline
{workflow}

## Related artifacts
- [Protocol](../protocols/{slug}Protocol.md) · [Trigger(s)](../triggers/{slug}Trigger.md) · [Tasks](../tasks/{slug}Task.md)
"""


def task_md(num, title, tasks):
    slug = slugify(title)
    task_list = split_items(tasks)
    blocks = []
    for i, t in enumerate(task_list):
        tname = t.split(" (")[0]
        tdesc = t.split(" (")[1][:-1] if " (" in t else f"Execute {tname}"
        blocks.append(f"""### Task: {tname}

```typescript
// task: {tname}
const {tname}Spec: TaskSpecification = {{
  taskId: '{tname}',
  operationRef: '{slug}Protocol',
  inputSchema: {{ capability: '{title}' }},
  outputSchema: {{ status: 'ok' }},
  implementation: 'api_call',
  dependencies: []
}};
```
**Description:** {tdesc}
""")
    return f"""# Task: {slug}Task

> Capability #{num} — **{title}**

Atomic executable unit(s) for this capability.

{chr(10).join(blocks)}
## Related artifacts
- [Protocol](../protocols/{slug}Protocol.md) · [Trigger(s)](../triggers/{slug}Trigger.md) · [Workflow](../workflows/{slug}Workflow.md)
"""


BASE_TYPES = """# Base Types & Contracts

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
"""


def main():
    dry = "--dry-run" in sys.argv
    counts = {"protocols": 0, "triggers": 0, "workflows": 0, "tasks": 0}
    index_rows = []

    if dry:
        print(f"[DRY-RUN] would generate {len(ENTRIES)} capabilities x 4 artifact types")
        print(f"[DRY-RUN] capability count check: {len(ENTRIES)} (expect 131)")
        assert len(ENTRIES) == 131, f"expected 131 entries, got {len(ENTRIES)}"
        return

    for num, title, purpose, triggers, tasks, workflow in ENTRIES:
        slug = slugify(title)
        for sub, writer in (
            ("protocols", protocol_md),
            ("triggers", trigger_md),
            ("workflows", workflow_md),
            ("tasks", task_md),
        ):
            path = os.path.join(PLATFORM, sub, f"{slug}{sub.capitalize()[:-1]}.md")
            if sub == "protocols":
                content = writer(num, title, purpose, triggers, tasks, workflow)
            elif sub == "triggers":
                content = writer(num, title, triggers, tasks)
            elif sub == "workflows":
                content = writer(num, title, workflow, triggers)
            else:
                content = writer(num, title, tasks)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(content)
            counts[sub] += 1
        index_rows.append(
            f"| {num} | {title} | [`{slug}Protocol`](protocols/{slug}Protocol.md) | "
            f"[`{slug}Trigger`](triggers/{slug}Trigger.md) | [`{slug}Workflow`](workflows/{slug}Workflow.md) | "
            f"[`{slug}Task`](tasks/{slug}Task.md) |"
        )

    os.makedirs(os.path.join(PLATFORM, "schemas"), exist_ok=True)
    with open(os.path.join(PLATFORM, "schemas", "base-types.md"), "w", encoding="utf-8") as fh:
        fh.write(BASE_TYPES)

    index = f"""# Platform Contract — Protocol / Trigger / Workflow / Task Specification

Formalization of the Cloudflare Permissions & Capabilities list: **{len(ENTRIES)} capabilities**,
each mapped to a Protocol (interface contract), Trigger(s) (event sources), Workflow(s)
(end-to-end process), and Task(s) (atomic units).

- Base types: [`schemas/base-types.md`](schemas/base-types.md)
- Storage layout: [`manifests/buckets.yaml`](../manifests/buckets.yaml)
- Regenerate: `python3 scripts/generate_platform_spec.py`

## Capability index

| # | Capability | Protocol | Trigger | Workflow | Task |
|---|---|---|---|---|---|
{chr(10).join(index_rows)}

---
*Generated by `scripts/generate_platform_spec.py` — do not hand-edit.*
"""
    with open(os.path.join(PLATFORM, "README.md"), "w", encoding="utf-8") as fh:
        fh.write(index)

    print(f"Generated: protocols={counts['protocols']} triggers={counts['triggers']} "
          f"workflows={counts['workflows']} tasks={counts['tasks']} + schemas/base-types.md + README.md")
    print("Total artifact files:", sum(counts.values()))


if __name__ == "__main__":
    main()
