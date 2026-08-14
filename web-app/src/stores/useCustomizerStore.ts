/**
 * Customizer store — re-export of the Aether Core state store so pages import
 * from a stable local path (kept for parity with the original spec layout).
 */
export {
  useCustomizerStore,
  createVanillaCustomizerStore,
} from "@dt-core/state";
export type { CustomizerStore } from "@dt-core/state";
export {
  DEFAULT_ATTRIBUTES,
  createDefaultAttributes,
  cloneAttributes,
} from "@dt-core/types";
