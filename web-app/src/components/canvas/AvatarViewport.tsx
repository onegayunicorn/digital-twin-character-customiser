import React from "react";
import { Canvas } from "@react-three/fiber";
import { OrbitControls, ContactShadows } from "@react-three/drei";
import { AvatarMesh } from "./AvatarMesh";

/**
 * AvatarViewport — isolated R3F Canvas mounting rig with studio lighting,
 * contact shadows, and constrained orbit controls (per the Digital Twin spec).
 */
export function AvatarViewport({ modelId = "standing" }: { modelId?: string }) {
  return (
    <div className="h-full w-full select-none bg-gradient-to-b from-slate-950 to-slate-900 outline-none">
      <Canvas
        shadows
        gl={{ antialias: true, preserveDrawingBuffer: true, powerPreference: "high-performance" }}
        camera={{ position: [0, 0.2, 2.6], fov: 40 }}
      >
        <ambientLight intensity={0.45} />
        <pointLight position={[5, 5, 5]} intensity={0.8} castShadow />
        <directionalLight position={[-5, 3, 2]} intensity={0.55} castShadow />
        <AvatarMesh modelId={modelId} />
        <ContactShadows position={[0, -1.45, 0]} opacity={0.6} blur={2.4} scale={6} />
        <OrbitControls
          enablePan={false}
          enableZoom
          minDistance={1.2}
          maxDistance={4.0}
          minPolarAngle={Math.PI / 2.6}
          maxPolarAngle={Math.PI / 1.9}
          target={[0, 0.35, 0]}
        />
      </Canvas>
    </div>
  );
}
