# Protocol: PhotonicAnalysisProtocol

> Capability #136 — **Photonic Analysis** · Domain: Access & Zero Trust · Access: `write`

## Purpose
PERO photonic toolkit: splitting efficiency, spatial coherence, spectral decomposition, FFT, Bell S-parameter, SPDC coincidence.

## Interface contract
```typescript
// protocol: PhotonicAnalysisProtocol
interface PhotonicAnalysisProtocol extends BaseOperation {
  id: string;
  name: 'Photonic Analysis';
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
| Trigger(s) | [`MeasurementIngestedTrigger`](../triggers/PhotonicAnalysisTrigger.md) |
| Task(s) | [`AnalyzeClassicalTask`](../tasks/PhotonicAnalysisTask.md), [`VerifyQuantumTask`](../tasks/PhotonicAnalysisTask.md) |
| Workflow | [`PhotonicAnalysisWorkflow`](../workflows/PhotonicAnalysisWorkflow.md) |

## Operations
- Configure / manage the capability through the workflow below.
- All mutations are audited; destructive operations require `admin` access.
- See [`../schemas/base-types.md`](../schemas/base-types.md) for base contracts.

## Workflow
Ingest -> Classical metrics -> Quantum verify -> Verdict -> Report
