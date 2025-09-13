# 1942-lite — Top‑Down Warplane Shooter (Pygame)

A small, **1942-inspired** top‑down shooter built with **Pygame**.

- Player is a warplane that can move in all 4 directions.
- Enemies enter from the top and exit at the bottom.
- Multiple enemy types (shooters, kamikaze, and bigger clustered enemies).
- Destroyed enemies may drop **health packs**, **ammo**, or **enhanced weapons**.
- **Enhanced weapons** activate on pickup and last **10 seconds** (triple-shot).
- Player has **5 lives**; on explosion, player **respawns at the same spot** with brief invulnerability.
- **Level layout** is defined in a **text file** where **letters = enemy types**.
  - **Clusters** of the same letter form **oversized/big enemies** (connected components across the grid).

## Controls
- **Move**: Arrow Keys or **W/A/S/D**
- **Shoot**: **Space**
- **Pause**: **P**
- **Quit**: **Esc** or **Q** (from pause or running)
- **Toggle Debug overlay**: **F1**

## Requirements
```
pip install -r requirements.txt
```

## Run
```
python main.py
```

## Level Design (Text File)
Open `levels/level1.txt`. It is an ASCII grid processed as **connected components**:

- Each **row** represents a slice of time (top → bottom). As the level progresses, entries from higher rows spawn first.
- Each **column** maps horizontally across the screen.
- **Letters** spawn enemies:
  - `S` = **Shooter** (fires bullets downward in bursts)
  - `K` = **Kamikaze** (home-in movement; attempts to ram player)
  - `B` = **Big enemy** (any clustered letter area > 1 cell makes a larger enemy with more health)
  - `.` or space = empty

**Clustering rule:** Adjacent (4-neighbour) identical letters are grouped into a single **component**. If a component's area is 1 cell → a normal enemy; if bigger than 1 cell → a **big enemy** with proportional size/HP. The **spawn time** of the component is based on the **top-most row index** of that component.

### Tuning Spawn Pace
Inside `main.py`, `SPAWN_ROW_MS` controls how quickly the next "row" of the level is considered (default 800 ms). Larger = slower level; smaller = faster.

## Safe Zone (End of Level)
When the last spawns are processed and a brief tail time passes, a **Safe Zone** line appears near the bottom. Reach it to **win the level**.

## Assets
No external assets are required (all graphics are procedural). If you drop images into `assets/` (e.g. `assets/player.png`), the game will attempt to use them, but that is optional for this build.

## Notes
- The game window defaults to **800×600**.
- The code is contained in a **single file** (`main.py`) for simplicity.
- Intended as a learning/demo project and starter template for further expansion.
