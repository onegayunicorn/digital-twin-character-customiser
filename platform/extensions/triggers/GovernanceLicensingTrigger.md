# Trigger: GovernanceLicensingTrigger

> Capability #165 — **Governance & Licensing**

Event source(s) that initiate execution for this capability.

### Trigger: ProposalSubmittedTrigger

```typescript
// trigger: ProposalSubmittedTrigger
const ProposalSubmittedTriggerContract: TriggerContract = {
  triggerId: 'ProposalSubmittedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for ProposalSubmittedTrigger' },
  actionTarget: 'RunCouncilVoteTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

### Trigger: MarketplaceListedTrigger

```typescript
// trigger: MarketplaceListedTrigger
const MarketplaceListedTriggerContract: TriggerContract = {
  triggerId: 'MarketplaceListedTrigger',
  triggerType: 'event',
  condition: { matchExpression: 'condition for MarketplaceListedTrigger' },
  actionTarget: 'RunCouncilVoteTask',
  enabled: true,
  retryPolicy: { maxAttempts: 3, backoffStrategy: 'exponential', delayMs: 1000 },
  timeoutMs: 30000
};
```

## Related artifacts
- [Protocol](../protocols/GovernanceLicensingProtocol.md) · [Tasks](../tasks/GovernanceLicensingTask.md) · [Workflow](../workflows/GovernanceLicensingWorkflow.md)
