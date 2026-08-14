import React, { useState } from "react";
import { useCustomizerStore } from "@/stores/useCustomizerStore";
import { parseAIPrompt } from "@/utils/aiPromptRouter";
import { AvatarR3FCanvas } from "@/components/canvas/AvatarR3FCanvas";

interface ChatMessage {
  role: "assistant" | "user";
  content: string;
}

/**
 * AI Customizer Chat — Procedural Matrix Assistant. Natural-language prompts
 * are compiled by the AI prompt router into store mutations, with the live
 * store snapshot shown in the 3D viewport panel.
 */
export function AIChatCustomizerPage() {
  const { activeCharacter, updateAttributes } = useCustomizerStore();
  const [inputPrompt, setInputPrompt] = useState("");
  const [messages, setMessages] = useState<ChatMessage[]>([
    {
      role: "assistant",
      content:
        "Design engine ready. Prompt adjustments like: 'Make skin paler, hair neon green, and increase physical strength attributes.'",
    },
  ]);

  const handlePromptInjection = (e: React.FormEvent) => {
    e.preventDefault();
    if (!inputPrompt.trim()) return;
    const userMessage: ChatMessage = { role: "user", content: inputPrompt };
    setMessages((prev) => [...prev, userMessage]);

    const { mutator, logs } = parseAIPrompt(inputPrompt);
    updateAttributes(mutator);

    const assistantResponse: ChatMessage = {
      role: "assistant",
      content: `Injected operations into active configuration:\n\n${logs.join("\n")}`,
    };
    setMessages((prev) => [...prev, assistantResponse]);
    setInputPrompt("");
  };

  return (
    <div className="flex h-full w-full">
      {/* 3D Model Rendering Container Viewport */}
      <div className="relative flex-1 border-r border-slate-800 bg-slate-950 p-6">
        <AvatarR3FCanvas modelId="standing" label="Live Morph Preview" />
        <div className="pointer-events-none absolute left-9 top-9 z-10 mt-14 rounded-xl border border-slate-800 bg-slate-900/60 p-4 font-mono text-[11px] text-slate-400 backdrop-blur">
          <p className="mb-2 font-bold text-cyan-400">Live Store Snapshot Data:</p>
          <p>Resemblance: {activeCharacter.resemblance.toFixed(2)}</p>
          <p>
            Nose Grid X/Y: [{activeCharacter.features.nose.x.toFixed(2)},{" "}
            {activeCharacter.features.nose.y.toFixed(2)}]
          </p>
          <p>
            Jaw Matrix: [{activeCharacter.features.jaw.x.toFixed(2)},{" "}
            {activeCharacter.features.jaw.y.toFixed(2)}]
          </p>
          <p>Illegal Activity Hours: {activeCharacter.lifestyle.illegalWork}h</p>
        </div>
      </div>

      {/* Procedural AI Prompter Interface Workspace */}
      <div className="z-10 flex h-full w-[450px] flex-col bg-slate-900/30 shadow-2xl backdrop-blur-md">
        <div className="border-b border-slate-800 bg-slate-950/50 p-4">
          <h1 className="text-sm font-bold uppercase tracking-widest text-slate-300">
            Procedural Matrix Assistant
          </h1>
          <p className="text-xs text-slate-500">
            Natural language adjustments binding straight to your character array parameters.
          </p>
        </div>

        {/* Conversation Logs */}
        <div className="flex-1 space-y-4 overflow-y-auto p-4">
          {messages.map((msg, idx) => (
            <div
              key={idx}
              className={`flex ${msg.role === "user" ? "justify-end" : "justify-start"}`}
            >
              <div
                className={`max-w-[85%] whitespace-pre-line rounded-2xl px-4 py-3 text-xs leading-relaxed ${
                  msg.role === "user"
                    ? "bg-cyan-600 font-medium text-slate-950"
                    : "border border-slate-800 bg-slate-900 font-mono text-slate-300"
                }`}
              >
                {msg.content}
              </div>
            </div>
          ))}
        </div>

        {/* Chat Entry Console */}
        <div className="border-t border-slate-800 bg-slate-950/60 p-4">
          <form
            onSubmit={handlePromptInjection}
            className="flex items-center gap-2 rounded-xl border border-slate-800 bg-slate-900 p-1.5 transition-colors focus-within:border-cyan-500"
          >
            <input
              type="text"
              value={inputPrompt}
              onChange={(e) => setInputPrompt(e.target.value)}
              placeholder="Try 'make character an alpha criminal with a square jaw'..."
              className="flex-1 bg-transparent px-2 text-xs text-slate-200 outline-none placeholder-slate-600"
            />
            <button
              type="submit"
              className="rounded-lg bg-cyan-600 px-4 py-2 text-xs font-bold uppercase tracking-wider text-slate-950 transition-colors hover:bg-cyan-500"
            >
              Inject
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}
