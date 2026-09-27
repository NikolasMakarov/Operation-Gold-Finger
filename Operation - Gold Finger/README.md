# Gems, Ores & Jewelry

A standalone XML mod for RimWorld 1.6. No DLC or other mods required.

| Mineable vein | Yield per tile | Relative vein commonality | Resource |
| --- | ---: | ---: | --- |
| Compacted copper | 25 | 0.85 | Copper, a metallic building and crafting material |
| Compacted platinum | 8 | 0.12 | Platinum, a rare metallic building and crafting material |
| Amethyst deposit | 6 | 0.20 | Amethyst gemstone |
| Emerald deposit | 5 | 0.10 | Emerald gemstone |

The two wearable pieces are **amethyst ring** (6 copper + 1 amethyst, left hand) and **emerald pendant** (6 platinum + 1 emerald, neck). Both use the Belt apparel layer to avoid most ordinary clothing conflicts. Add a bill at a **machining table** after researching Machining. Quality comes from the inherited apparel quality component; a small PawnBeauty bonus applies while worn.

## Install

Extract the ZIP to `RimWorld/Mods/` so the resulting directory is `RimWorld/Mods/GemsOresJewelry/`, containing `About`, `Defs`, `Textures`, and this README. Enable **Gems, Ores & Jewelry** in the game's Mods menu. The veins are included by ordinary map generation, so newly generated maps will contain them. They do not retroactively appear in already generated colony maps; resources on an existing map can still be spawned with developer mode for testing.

## Replace art

All PNGs under `Textures` are deliberately simple placeholders. Replace each PNG in place without changing its filename. Each mined resource has one ground icon. Each wearable has a ground icon and four directional worn graphics (`_north`, `_east`, `_south`, `_west`). Mineable veins reuse RimWorld's own `Things/Building/Linked/RockFlecked_Atlas` texture with different XML colors, so they need no new textures.

## Extend

- Add a new resource `ThingDef` in `Defs/ThingDefs/Resources.xml` with a unique `GOJ_` defName and matching texture.
- Add a `ThingDef ParentName="RockBase"` in `Defs/ThingDefs/Mineables.xml`; point `building.mineableThing` at the resource, then tune `mineableYield`, `mineableScatterCommonality` and `mineableScatterLumpSizeRange`.
- Copy a jewelry `ThingDef` in `Defs/ThingDefs/Jewelry.xml`, give it a unique defName, update its `costList`, texture paths, and apparel body part group.

Compatibility note: This mod does not modify the linked Jewelry mod and does not require it. Its gemstones are standalone resources for these two recipes; existing Jewelry mod recipes may not automatically accept them as generic gemstone stuff.
