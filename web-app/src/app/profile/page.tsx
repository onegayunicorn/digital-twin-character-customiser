export default function ProfilePage() {
  return (
    <div className="mx-auto w-full max-w-5xl flex-1 px-4 py-10 sm:px-6">
      <h1 className="text-3xl font-semibold tracking-tight text-zinc-950 dark:text-zinc-50">
        Profile
      </h1>
      <p className="mt-2 max-w-2xl text-zinc-600 dark:text-zinc-400">
        Your personal style profile, stats, and settings.
      </p>

      <div className="mt-8 flex flex-col gap-6 sm:flex-row">
        <div className="flex w-full flex-col items-center gap-4 rounded-2xl border border-zinc-200 bg-white p-6 text-center dark:border-zinc-800 dark:bg-zinc-900 sm:w-64">
          <div className="flex h-20 w-20 items-center justify-center rounded-full bg-zinc-900 text-3xl text-white dark:bg-zinc-100 dark:text-black">
            A
          </div>
          <div>
            <p className="font-semibold text-zinc-900 dark:text-zinc-100">
              Alex Chen
            </p>
            <p className="text-sm text-zinc-500 dark:text-zinc-400">
              @alexchen
            </p>
          </div>
          <div className="flex w-full justify-around border-t border-zinc-100 pt-4 dark:border-zinc-800">
            <div className="text-center">
              <p className="text-lg font-semibold text-zinc-900 dark:text-zinc-100">
                42
              </p>
              <p className="text-xs text-zinc-500 dark:text-zinc-400">Items</p>
            </div>
            <div className="text-center">
              <p className="text-lg font-semibold text-zinc-900 dark:text-zinc-100">
                7
              </p>
              <p className="text-xs text-zinc-500 dark:text-zinc-400">
                Outfits
              </p>
            </div>
            <div className="text-center">
              <p className="text-lg font-semibold text-zinc-900 dark:text-zinc-100">
                320
              </p>
              <p className="text-xs text-zinc-500 dark:text-zinc-400">XP</p>
            </div>
          </div>
        </div>

        <div className="flex-1 rounded-2xl border border-zinc-200 bg-white p-6 dark:border-zinc-800 dark:bg-zinc-900">
          <h2 className="text-lg font-medium text-zinc-900 dark:text-zinc-100">
            Settings
          </h2>
          <ul className="mt-4 divide-y divide-zinc-100 text-sm dark:divide-zinc-800">
            {["Account details", "Notifications", "Privacy", "Appearance"].map(
              (setting) => (
                <li
                  key={setting}
                  className="flex items-center justify-between py-3 text-zinc-600 dark:text-zinc-400"
                >
                  {setting}
                  <span className="text-zinc-400 dark:text-zinc-600">›</span>
                </li>
              )
            )}
          </ul>
        </div>
      </div>
    </div>
  );
}
