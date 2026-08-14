import React, { useEffect, useMemo, useRef, useState } from "react";
import { useFrame } from "@react-three/fiber";
import * as THREE from "three";
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader.js";
import { gltfRegistry } from "@dt-engine/gltf-registry";
import { writeMorphInfluences } from "@dt-engine/mesh-pipeline";
import { useAvatarMesh } from "@/hooks/useAvatarMesh";
import { createHeritageMaterial, syncHeritageUniforms } from "./shaders/HeritageShaderMaterial";

/**
 * AvatarMesh — drives a character rig from the customizer store.
 *
 * Resilience model:
 *   1. If the archive GLB is present under /assets/models it is loaded and the
 *      morph target dictionary is driven every frame via writeMorphInfluences.
 *   2. If the asset is missing (dev/CI without assets), a procedural rig is
 *      rendered with the heritage shader so the pipeline stays visible.
 */
export function AvatarMesh({ modelId = "standing" }: { modelId?: string }) {
  const { influences, skinTone, resemblance, motherId, fatherId } = useAvatarMesh();
  const [gltfFailed, setGltfFailed] = useState(false);
  const [gltfReady, setGltfReady] = useState(false);

  const material = useMemo(
    () => createHeritageMaterial(skinTone, resemblance),
    // eslint-disable-next-line react-hooks/exhaustive-deps
    [],
  );

  useEffect(() => {
    syncHeritageUniforms(material, { skinTone, resemblance });
  }, [material, skinTone, resemblance]);

  const modelPath = gltfRegistry.resolvePath(modelId) ?? "/assets/models/wo-standing-v17.glb";

  return (
    <group dispose={null}>
      {!gltfFailed ? (
        <GltfCharacter
          path={modelPath}
          onReady={() => setGltfReady(true)}
          onError={() => setGltfFailed(true)}
          frameInfluences={influences}
        />
      ) : null}
      {(!gltfReady || gltfFailed) ? (
        <ProceduralRig material={material} influences={influences} motherId={motherId} fatherId={fatherId} />
      ) : null}
    </group>
  );
}

/** GLTF loader child — suspends while loading; errors are caught by onError. */
function GltfCharacter({
  path,
  onReady,
  onError,
  frameInfluences,
}: {
  path: string;
  onReady: () => void;
  onError: () => void;
  frameInfluences: Record<string, number>;
}) {
  const ref = useRef<THREE.Group>(null);

  useEffect(() => {
    let cancelled = false;
    const loader = new GLTFLoader();
    loader.load(
      path,
      (gltf) => {
        if (cancelled) return;
        if (ref.current) {
          ref.current.add(gltf.scene);
          onReady();
        }
      },
      undefined,
      () => {
        if (!cancelled) onError();
      },
    );
    return () => {
      cancelled = true;
    };
  }, [path, onReady, onError]);

  useFrame(() => {
    // Drive morph targets once the mesh exists
    const mesh = ref.current?.getObjectByName("Character_Mesh") as
      | (THREE.SkinnedMesh & {
          morphTargetDictionary?: Record<string, number>;
          morphTargetInfluences?: number[];
        })
      | undefined;
    if (mesh) {
      writeMorphInfluences(
        mesh.morphTargetDictionary,
        mesh.morphTargetInfluences,
        frameInfluences,
      );
    }
  });

  return <group ref={ref} position={[0, -1, 0]} />;
}

/** Procedural fallback rig — head/body sculpt driven by morph influences. */
function ProceduralRig({
  material,
  influences,
  motherId,
  fatherId,
}: {
  material: THREE.ShaderMaterial;
  influences: Record<string, number>;
  motherId: number;
  fatherId: number;
}) {
  const groupRef = useRef<THREE.Group>(null);
  const headRef = useRef<THREE.Mesh>(null);

  useFrame(() => {
    if (!headRef.current) return;
    const s = headRef.current.scale;
    s.x = 1 + (influences.Nose_Wide ?? 0) * 0.08 - (influences.Nose_Narrow ?? 0) * 0.08;
    s.y = 1 + (influences.Jaw_Square ?? 0) * 0.06 - (influences.Jaw_Round ?? 0) * 0.04;
    s.z = 1 + (influences.Nose_Long ?? 0) * 0.05;
  });

  return (
    <group ref={groupRef} position={[0, -1.1, 0]}>
      {/* Head — heritage blend shader */}
      <mesh ref={headRef} position={[0, 1.62, 0]} castShadow>
        <sphereGeometry args={[0.32, 48, 48]} />
        <primitive object={material} attach="material" />
      </mesh>
      {/* Torso */}
      <mesh position={[0, 0.85, 0]} castShadow>
        <capsuleGeometry args={[0.32, 0.9, 8, 24]} />
        <meshStandardMaterial color="#3b4252" roughness={0.7} metalness={0.15} />
      </mesh>
      {/* Hair overlay hint */}
      <mesh position={[0, 1.9, -0.02]} castShadow>
        <sphereGeometry args={[0.335, 32, 32, 0, Math.PI * 2, 0, Math.PI * 0.62]} />
        <meshStandardMaterial color="#b8860b" roughness={0.65} />
      </mesh>
      {/* Heritage chip display */}
      <group position={[0.62, 1.55, 0]}>
        <mesh>
          <boxGeometry args={[0.14, 0.1, 0.02]} />
          <meshStandardMaterial
            color={motherId === fatherId ? "#06b6d4" : "#f59e0b"}
            emissive={motherId === fatherId ? "#06b6d4" : "#f59e0b"}
            emissiveIntensity={0.6}
          />
        </mesh>
      </group>
    </group>
  );
}
