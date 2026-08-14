export default function ComparisonsPage() {
  return (
    <div className="mx-auto w-full max-w-5xl flex-1 px-4 py-10 sm:px-6">
      <h1 className="text-3xl font-semibold tracking-tight text-zinc-950 dark:text-zinc-50">
        Online Comparisons
      </h1>
      <p className="mt-2 max-w-2xl text-zinc-600 dark:text-zinc-400">
        Compare prices and product details across online stores to find the
        best deal.
      </p>
      <div className="mt-8 space-y-4">
        {[
          {
            item: "Classic Denim Jacket",
            stores: [
              { name: "Store A", price: "$89.99" },
              { name: "Store B", price: "$74.50" },
              { name: "Store C", price: "$95.00" },
            ],
          },
          {
            item: "Leather Chelsea Boots",
            stores: [
              { name: "Store A", price: "$129.99" },
              { name: "Store B", price: "$118.00" },
            ],
          },
        ].map((comparison) => (
          <div
            key={comparison.item}
            className="rounded-2xl border border-zinc-200 bg-white p-6 dark:border-zinc-800 dark:bg-zinc-900"
          >
            <h2 className="text-lg font-medium text-zinc-900 dark:text-zinc-100">
              {comparison.item}
            </h2>
            <ul className="mt-4 divide-y divide-zinc-100 dark:divide-zinc-800">
              {comparison.stores.map((store) => (
                <li
                  key={store.name}
                  className="flex items-center justify-between py-2 text-sm"
                >
                  <span className="text-zinc-600 dark:text-zinc-400">
                    {store.name}
                  </span>
                  <span className="font-semibold text-zinc-900 dark:text-zinc-100">
                    {store.price}
                  </span>
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    </div>
  );
}
