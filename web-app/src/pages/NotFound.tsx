import React from "react";
import { Link } from "wouter";
import { Button } from "@/components/ui";

/** 422/404 fallback page. */
export function NotFound() {
  return (
    <main className="flex min-h-[60vh] flex-col items-center justify-center gap-4 px-6 text-center">
      <p className="font-mono text-7xl font-black text-slate-800">422</p>
      <h1 className="text-2xl font-black uppercase tracking-widest text-slate-300">
        Coordinate Out of Range
      </h1>
      <p className="max-w-sm text-sm text-slate-500">
        This feature vector sits outside the matrix bounds [-1.0, 1.0]. Return to the forge.
      </p>
      <Link href="/">
        <Button variant="accent">Return Home</Button>
      </Link>
    </main>
  );
}
