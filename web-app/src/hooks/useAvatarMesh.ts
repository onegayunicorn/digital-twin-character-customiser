import { useEffect, useMemo, useRef } from "react";
import { useCustomizerStore } from "@dt-core/state";
import { applyMorphTargets } from "@dt-engine/mesh-pipeline";

export interface MorphInfluence {
  [key: string]: number;
}

/**
 * useAvatarMesh — bridges the store's feature matrix into morph influences
 * that the R3F AvatarMesh applies to the SkinnedMesh every frame.
 */
export function useAvatarMesh() {
  const activeCharacter = useCustomizerStore((s) => s.activeCharacter);
  const frameRef = useRef<MorphInfluence>({});

  const influences = useMemo<MorphInfluence>(() => {
    const map = applyMorphTargets(activeCharacter.features);
    frameRef.current = { ...map };
    return map;
  }, [activeCharacter.features]);

  useEffect(() => {
    // Refresh frame cache whenever features change
    frameRef.current = { ...influences };
  }, [influences]);

  return {
    influences,
    frameRef,
    skinTone: activeCharacter.skinTone,
    resemblance: activeCharacter.resemblance,
    motherId: activeCharacter.motherId,
    fatherId: activeCharacter.fatherId,
  };
}
