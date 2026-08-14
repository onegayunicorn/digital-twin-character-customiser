import React from "react";
import { Redirect } from "wouter";

/**
 * CustomizerPage — default customizer route redirects into the builder.
 */
export function CustomizerPage() {
  return <Redirect to="/customizer/builder" />;
}
