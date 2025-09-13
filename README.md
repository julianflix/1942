# 1942-lite — Top-Down Warplane Shooter (Pygame)

**What is new (v2):**
- PNG **sprites** supported for enemies and player (drop images into `assets/`).
- **Explosion animations** on kills (uses `assets/explosion_0..5.png` if available, otherwise procedural).
- **Multi-level** flow: `levels/level1.txt` → `levels/level2.txt` → ... (auto-discovery).

## Controls
- Move: Arrow keys / W A S D
- Shoot: Space
- Pause: P
- Toggle debug: F1
- Quit: Esc / Q

## Run
```bash
pip install pygame>=2.5.2
python main.py
```

## Assets (PNG sprites)
Put any of these optional files in `assets/`:
- `player.png`
- `enemy_shooter.png`
- `enemy_kamikaze.png`
- `enemy_big.png`
- `explosion_0.png` ... `explosion_5.png`

If any file is missing, the game draws a clean fallback shape.

## Level files
Add `levels/level2.txt`, `levels/level3.txt`, ... using the ASCII-letter scheme:
- `S` shooter, `K` kamikaze, `B` big (or any clustered letter → big)
- `.` or space = empty

The engine loads all matching `levels/level*.txt` in ascending order and advances when you reach the **Safe Zone**.
