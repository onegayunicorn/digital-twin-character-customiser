import React, { type ComponentType } from "react";
import { Route, Switch } from "wouter";
import { Navbar } from "./components/Navbar";
import { Home } from "./pages/Home";
import { JourneyPage } from "./pages/JourneyPage";
import { TelemetryPage } from "./pages/TelemetryPage";
import { GlobalModePage } from "./pages/GlobalModePage";
import { CustomizerPage } from "./pages/CustomizerPage";
import { OperationsDashboardPage } from "./pages/OperationsDashboardPage";
import { NotFound } from "./pages/NotFound";
import { CustomizerLayout } from "./app/customizer/layout";
import { CharacterBuilderPage } from "./app/customizer/builder/page";
import { AIChatCustomizerPage } from "./app/customizer/ai-chat/page";
import { AvatarShowcasePage } from "./app/customizer/showcase/page";
import { SavedCharactersPage } from "./app/customizer/saved/page";

/** Wrap a page in the customizer sidebar layout. */
const withCustomizer =
  (Comp: ComponentType): ComponentType =>
  () => (
    <CustomizerLayout>
      <Comp />
    </CustomizerLayout>
  );

export function App() {
  return (
    <div className="min-h-screen bg-abyss text-script">
      <Navbar />
      <Switch>
        <Route path="/" component={Home} />
        <Route path="/journey" component={JourneyPage} />
        <Route path="/telemetry" component={TelemetryPage} />
        <Route path="/global-mode" component={GlobalModePage} />
        <Route path="/dashboard" component={OperationsDashboardPage} />
        <Route path="/customizer" component={CustomizerPage} />
        <Route
          path="/customizer/builder"
          component={withCustomizer(CharacterBuilderPage)}
        />
        <Route
          path="/customizer/ai-chat"
          component={withCustomizer(AIChatCustomizerPage)}
        />
        <Route
          path="/customizer/showcase"
          component={withCustomizer(AvatarShowcasePage)}
        />
        <Route
          path="/customizer/saved"
          component={withCustomizer(SavedCharactersPage)}
        />
        <Route component={NotFound} />
      </Switch>
    </div>
  );
}
