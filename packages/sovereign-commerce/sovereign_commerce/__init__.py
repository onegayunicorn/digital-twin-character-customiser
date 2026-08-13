"""Sovereign Commerce Platform — working kernel.

Modules:
  kernel        - 12 shared primitives registry
  domains       - 14-domain master scope
  jurisdiction  - 6-dimension jurisdiction engine
  compliance    - compliance OS with regulatory capability gates
  entities      - legal entity registry (person..DAO)
  ledger        - double-entry ledger + escrow settlement
  payments      - Stripe-style payment orchestration (test-mode)
  procurement   - tender/bid evaluation + three-way matching
  supplychain   - SKU/serialisation/provenance/custody
  offgrid       - offline queue, store-and-forward, sync, disaster mode
  nfc_escrow    - NFC-tap conditional settlement bridge
  twins         - digital twins for platform entities
  api           - HTTP API

Honest notice: this is an architecture/compliance map implemented as working
software, NOT legal advice. Regulatory gates enforce documented policy; they
do not substitute for licensed legal/regulatory advice.
"""
from .kernel import SovereignKernel, PRIMITIVES
from .domains import DOMAINS, domain_by_name
from .jurisdiction import JurisdictionEngine
from .compliance import ComplianceOS, GATE_ORDER
from .entities import EntityRegistry, ENTITY_TYPES
from .ledger import Ledger, LedgerError
from .payments import StripeClient, PaymentOrchestrator
from .procurement import ProcurementEngine
from .supplychain import SupplyChain
from .offgrid import OffGridNode
from .nfc_escrow import NfcEscrowBridge
from .twins import CommerceTwinHub

__all__ = ["SovereignKernel", "PRIMITIVES", "DOMAINS", "domain_by_name",
           "JurisdictionEngine", "ComplianceOS", "GATE_ORDER", "EntityRegistry",
           "ENTITY_TYPES", "Ledger", "LedgerError", "StripeClient",
           "PaymentOrchestrator", "ProcurementEngine", "SupplyChain",
           "OffGridNode", "NfcEscrowBridge", "CommerceTwinHub"]
