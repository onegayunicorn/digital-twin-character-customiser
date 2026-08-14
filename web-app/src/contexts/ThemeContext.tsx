import React, {
  createContext,
  useContext,
  useEffect,
  useState,
  type ReactNode,
} from "react";

type ThemeMode = "chiaroscuro" | "cyber" | "noir";

interface ThemeContextValue {
  mode: ThemeMode;
  setMode: (mode: ThemeMode) => void;
}

const ThemeContext = createContext<ThemeContextValue>({
  mode: "chiaroscuro",
  setMode: () => undefined,
});

export function ThemeProvider({ children }: { children: ReactNode }) {
  const [mode, setMode] = useState<ThemeMode>("chiaroscuro");

  useEffect(() => {
    const root = document.documentElement;
    root.dataset.theme = mode;
    if (mode === "cyber") {
      root.style.setProperty("--color-accent", "#22d3ee");
    } else if (mode === "noir") {
      root.style.setProperty("--color-accent", "#94a3b8");
    } else {
      root.style.setProperty("--color-accent", "#06b6d4");
    }
  }, [mode]);

  return (
    <ThemeContext.Provider value={{ mode, setMode }}>
      {children}
    </ThemeContext.Provider>
  );
}

export function useTheme(): ThemeContextValue {
  return useContext(ThemeContext);
}
