export default function QuestsPage() {
  return (
    <div className="mx-auto w-full max-w-5xl flex-1 px-4 py-10 sm:px-6">
      <h1 className="text-3xl font-semibold tracking-tight text-zinc-950 dark:text-zinc-50">
        Quests
      </h1>
      <p className="mt-2 max-w-2xl text-zinc-600 dark:text-zinc-400">
        Complete styling challenges to earn XP and unlock exclusive rewards.
      </p>
      <div className="mt-8 grid grid-cols-1 gap-4 sm:grid-cols-2">
        {[
          {
            title: "Monochrome Master",
            description: "Build an all-black outfit from your wardrobe.",
            xp: "+50 XP",
            status: "In progress",
          },
          {
            title: "Streetwear Starter",
            description: "Add 5 streetwear items to your collection.",
            xp: "+100 XP",
            status: "Not started",
          },
          {
            title: "Price Hunter",
            description: "Compare 3 items across different online stores.",
            xp: "+75 XP",
            status: "Not started",
          },
          {
            title: "Mix & Match",
            description: "Create 3 new outfit combinations.",
            xp: "+150 XP",
            status: "Completed",
          },
        ].map((quest) => (
          <div
            key={quest.title}
            className="flex flex-col gap-2 rounded-2xl border border-zinc-200 bg-white p-6 dark:border-zinc-800 dark:bg-zinc-900"
          >
            <div className="flex items-start justify-between gap-4">
              <h2 className="text-lg font-medium text-zinc-900 dark:text-zinc-100">
                {quest.title}
              </h2>
              <span className="shrink-0 rounded-full bg-zinc-100 px-2.5 py-1 text-xs font-semibold text-zinc-700 dark:bg-zinc-800 dark:text-zinc-300">
                {quest.xp}
              </span>
            </div>
            <p className="text-sm text-zinc-600 dark:text-zinc-400">
              {quest.description}
            </p>
            <span className="mt-2 text-xs font-medium uppercase tracking-wide text-zinc-500 dark:text-zinc-400">
              {quest.status}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
}
