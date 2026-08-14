export default function WardrobePage() {
  return (
    <div className="mx-auto w-full max-w-5xl flex-1 px-4 py-10 sm:px-6">
      <h1 className="text-3xl font-semibold tracking-tight text-zinc-950 dark:text-zinc-50">
        Wardrobe
      </h1>
      <p className="mt-2 max-w-2xl text-zinc-600 dark:text-zinc-400">
        Manage your collection of clothing items — tops, bottoms, shoes, and
        accessories.
      </p>
      <div className="mt-8 grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {[
          { name: "Oversized Hoodie", category: "Tops" },
          { name: "Slim-Fit Jeans", category: "Bottoms" },
          { name: "Canvas Sneakers", category: "Shoes" },
          { name: "Denim Jacket", category: "Outerwear" },
          { name: "Crew Socks", category: "Accessories" },
          { name: "White Tee", category: "Tops" },
        ].map((item) => (
          <div
            key={item.name}
            className="flex aspect-square flex-col items-center justify-center gap-2 rounded-2xl border border-zinc-200 bg-white text-center dark:border-zinc-800 dark:bg-zinc-900"
          >
            <span className="text-3xl" aria-hidden>
              👕
            </span>
            <p className="font-medium text-zinc-900 dark:text-zinc-100">
              {item.name}
            </p>
            <p className="text-sm text-zinc-500 dark:text-zinc-400">
              {item.category}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}
