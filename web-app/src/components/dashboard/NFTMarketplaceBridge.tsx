import React, { useState } from "react";
import { Badge, Button, Card } from "@/components/ui";

export interface NftListing {
  id: string;
  name: string;
  priceEth: number;
  rarity: "Common" | "Rare" | "Epic" | "Legendary";
}

const MOCK_LISTINGS: NftListing[] = [
  { id: "SS-001", name: "Star Seed #001", priceEth: 0.42, rarity: "Rare" },
  { id: "SS-002", name: "Star Seed #002", priceEth: 1.2, rarity: "Epic" },
  { id: "SS-003", name: "Star Seed #003", priceEth: 0.18, rarity: "Common" },
  { id: "SS-004", name: "Star Seed #004", priceEth: 3.4, rarity: "Legendary" },
];

const RARITY_TONE: Record<NftListing["rarity"], "slate" | "cyan" | "emerald" | "amber"> = {
  Common: "slate",
  Rare: "cyan",
  Epic: "emerald",
  Legendary: "amber",
};

/**
 * NFTMarketplaceBridge — Star Seed NFT marketplace & wallet bridge panel
 * (spec parity component; uses mock listings, wallet bridge stub).
 */
export function NFTMarketplaceBridge() {
  const [walletConnected, setWalletConnected] = useState(false);
  const [selected, setSelected] = useState<NftListing | null>(null);

  return (
    <Card className="flex flex-col gap-4">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-sm font-bold uppercase tracking-widest text-slate-200">
            Star Seed Marketplace
          </h2>
          <p className="text-xs text-slate-500">NFT marketplace & wallet bridge</p>
        </div>
        <Badge tone={walletConnected ? "emerald" : "slate"}>
          {walletConnected ? "● Wallet Linked" : "○ Bridge Idle"}
        </Badge>
      </div>

      <div className="grid grid-cols-2 gap-3">
        {MOCK_LISTINGS.map((listing) => (
          <button
            key={listing.id}
            onClick={() => setSelected(listing)}
            className={`rounded-xl border p-3 text-left transition-all ${
              selected?.id === listing.id
                ? "border-cyan-500 bg-cyan-950/30"
                : "border-slate-800 bg-slate-950/50 hover:border-slate-600"
            }`}
          >
            <div className="flex items-center justify-between">
              <span className="text-xs font-semibold text-slate-200">{listing.name}</span>
              <Badge tone={RARITY_TONE[listing.rarity]}>{listing.rarity}</Badge>
            </div>
            <div className="mt-2 font-mono text-sm font-bold text-cyan-400">
              {listing.priceEth.toFixed(2)} Ξ
            </div>
          </button>
        ))}
      </div>

      <div className="flex gap-2 border-t border-slate-800 pt-3">
        <Button
          variant={walletConnected ? "ghost" : "accent"}
          className="flex-1"
          onClick={() => setWalletConnected(!walletConnected)}
        >
          {walletConnected ? "Disconnect Wallet" : "Connect Wallet"}
        </Button>
        <Button
          variant="default"
          className="flex-1"
          disabled={!walletConnected || !selected}
          onClick={() => {
            if (selected) {
              // Bridge stub — would route through the Star Seed contract
              window.alert(`Bridged purchase intent for ${selected.name} (${selected.priceEth} Ξ)`);
            }
          }}
        >
          Bridge Purchase
        </Button>
      </div>
    </Card>
  );
}
