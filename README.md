# Operation - Gold Finger

A standalone RimWorld 1.6 mod with four naturally generated veins, four mined resources, and two wearable jewelry shapes: rings and pendants.

| Vein | Yield per tile | Relative commonality | Resource |
| --- | ---: | ---: | --- |
| Compacted copper | 25 | 0.85 | Copper (metallic stuff) |
| Compacted platinum | 8 | 0.12 | Platinum (metallic stuff) |
| Amethyst deposit | 6 | 0.20 | Amethyst |
| Emerald deposit | 5 | 0.10 | Emerald |

## Jewelry

At a **machining table** after researching **Machining**, make either shape with **6 units of one metal** and **1 gemstone**. The metal selector accepts `Metallic` stuff, including steel, copper and platinum. Pick one gem by selecting its bill:

| Shape | Gem choices | Apparel slot |
| --- | --- | --- |
| Ring | Amethyst or emerald | Left hand, Belt layer |
| Pendant | Amethyst or emerald | Neck, Belt layer |

The two gem choices per shape appear as four crafting bills. This is how the gem is recorded in the resulting item using RimWorld's normal XML recipes; every ring and pendant can still choose its metal independently.

### Color masks and replacing art

Ground icons and worn textures use RimWorld's `CutoutComplex` shader. Each texture has a corresponding mask PNG: **red** marks metal, **green** marks gem, and transparent pixels are unused. The metal gets its color from the selected `Metallic` stuff. The gem variant provides the second color in the ground graphic's XML. Worn graphics include a gem-tinted base as a fallback because RimWorld's apparel renderer may not pass the second color through in every rendering path. No custom shader or DLL is needed for these four combinations.

- Ground art: `Textures/Things/Item/Jewelry/<Gem><Shape>.png` and its `<Gem><Shape>_m.png` mask.
- Worn art: `Textures/Things/Pawn/Humanlike/Apparel/<Gem><Shape>/`. Edit the four master directional files ending in `_north`, `_east`, `_south`, `_west` and their masks, which append `m` (for example, `AmethystRing_southm.png`). Run `python Tools/rebuild_worn_variants.py` from this folder to copy them to the body-type names RimWorld expects for Belt-layer apparel. The generated files are included in the mod for immediate use.
- Mineable veins use RimWorld's `Things/Building/Linked/RockFlecked_Atlas` with XML colors. They need no ore texture files.
- Mined resource icons are separate PNGs under `Textures/Things/Item/Resource/`.

Adding a new gem choice means adding a resource, a gem-specific bill/product `ThingDef`, and corresponding masked textures. The metal remains selectable through `stuffCategories` and `costStuffCount` on that product.

## Install

Copy the **Operation - Gold Finger** folder into `RimWorld/Mods/` and enable it in the game's Mods menu. Newly generated maps will contain the veins. Existing colony maps do not retroactively gain them; use developer mode to spawn test veins if needed.

The original amethyst-ring and emerald-pendant Def names are preserved. Jewelry crafted in an earlier version had no material set; loading those existing items after the change may assign the game's default metal to them.
