export default function Home() {
  return (
    <div className="mx-auto flex w-full max-w-5xl flex-1 flex-col gap-8 px-4 py-10 sm:px-6">
      <section className="flex flex-col gap-2">
        <h1 className="text-3xl font-semibold tracking-tight text-zinc-950 dark:text-zinc-50">
          Welcome to StyleForge
        </h1>
        <p className="max-w-2xl text-zinc-600 dark:text-zinc-400">
          Build your wardrobe, compare looks online, and complete quests to
          level up your style.
        </p>
      </section>

      {/* 3D Customizer placeholder */}
      <section className="flex aspect-video w-full items-center justify-center rounded-2xl border border-dashed border-zinc-300 bg-zinc-100 dark:border-zinc-700 dark:bg-zinc-900">
        <div className="flex flex-col items-center gap-2 text-center">
          <span className="text-4xl" aria-hidden>
            🧥
          </span>
          <p className="text-lg font-medium text-zinc-800 dark:text-zinc-200">
            3D Customizer
          </p>
          <p className="max-w-sm text-sm text-zinc-500 dark:text-zinc-400">
            Coming soon — try on outfits in real time with the interactive 3D
            avatar and garment customizer.
          </p>
        </div>
      </section>
    </div>
  );
}
