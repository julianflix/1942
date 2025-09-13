# Repository Structure: https://github.com/julianflix/1942.git (main)

## Tree (filtered)

```
├── build/
│   └── version.txt
├── levels/
│   ├── level1.txt
│   ├── level10.txt
│   ├── level2.txt
│   ├── level3.txt
│   ├── level4.txt
│   ├── level5.txt
│   ├── level6.txt
│   ├── level7.txt
│   ├── level8.txt
│   └── level9.txt
├── README.md
├── main.py
└── requirements.txt
```

## Files

### FILE: `build/version.txt`

#### Description

# `build/version.txt` Documentation

---

## Overview

The `build/version.txt` file is a **version control file** that stores the current version number of the application. This file is typically used during the build process to embed version information into the application, enabling users and developers to identify the exact release version.

---

## File Location

```
build/version.txt
```

This file is located in the `build/` directory of the project, which is commonly used to store build artifacts and configuration files.

---

## File Content

```
0.9.2
```

The file contains a single line with a **semantic version number** in the format `MAJOR.MINOR.PATCH`. 

- **MAJOR**: 0 (indicating the project is in early development)
- **MINOR**: 9 (feature updates)
- **PATCH**: 2 (bug fixes)

This follows [Semantic Versioning (SemVer)](https://semver.org/), a standard for versioning software.

---

## Usage

### Purpose
- **Version Identification**: The version number is used to track the state of the application, helping users and developers understand what features or fixes are included in a release.
- **Build Process**: During the build, this file may be read to inject the version into the application (e.g., in logs, UI, or metadata).
- **Release Management**: Updating this file is part of the release process to indicate new versions.

### Example Use Cases
- **Displaying Version**: The application may read this file at runtime to show the version in the UI or logs.
- **CI/CD Pipelines**: Continuous integration systems may use this file to automate versioning and deployment.

---

## Implications of Modification

- **Incrementing the Version**: Update the version number according to SemVer rules when:
  - Adding new features (increment `MINOR`),
  - Fixing bugs (increment `PATCH`),
  - Making breaking changes (increment `MAJOR`).
- **Build Artifacts**: Changing this file may require rebuilding the application to reflect the new version in outputs.

---

## Example

To update the version to `1.0.0` (a major release):

1. Modify `build/version.txt`:
   ```
   1.0.0
   ```

2. Rebuild the application to embed the new version.

---

## Related Files

- **`requirements.txt`**: Specifies dependencies like `pygame>=2.5.2` and `pygbag`, which are required for the application to run.
- **`main.py`**: The entry point of the application, which may read the version during initialization.
- **`README.md`**: Contains project documentation, including setup and usage instructions.

---

## Best Practices

- **Automate Version Updates**: Use scripts or tools (e.g., `bumpversion`, `git tags`) to manage version increments.
- **Consistency**: Ensure the version in `version.txt` matches the version in other project metadata (e.g., `setup.py`, `package.json` if applicable).
- **Documentation**: Update release notes or changelogs when the version changes.

#### Source

```
0.9.2
```

### FILE: `README.md`

#### Description

# 1942-lite Shooter Game

A lightweight 2D shooter game inspired by classic arcade titles, featuring player mechanics, enemy AI, power-ups, and level progression.

---

## 📌 Overview

This project is a 2D shooter game built using Python's [Pygame](https://www.pygame.org/) library. It includes:
- Player movement and shooting
- Enemy AI and wave-based combat
- Power-up mechanics (e.g., enhanced fire, diagonal shooting)
- Level progression system
- Safe zone victory condition

The game supports multiple levels, configurable difficulty, and includes a simple HUD for tracking lives, ammo, and power-up timers.

---

## 🧰 Prerequisites

- Python 3.7+
- [Pygame](https://www.pygame.org/) (`pygame>=2.5.2`)
- [Pygbag](https://pygbag.readthedocs.io/) (for web deployment)

---

## 📦 Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🕹️ Usage

### Run the Game
```bash
python main.py
```

### Specify a Level
```bash
python main.py --level 3
```

---

## 📁 Project Structure

```
/levels/               # Level files (level1.txt, level2.txt, etc.)
/main.py               # Main game logic
/README.md             # This file
/requirements.txt      # Python dependencies
/build/version.txt     # Version number (0.9.2)
```

---

## 🎮 Key Features

- **Player Controls**: Arrow keys or touch controls (mobile/web)
- **Shooting**: Normal and enhanced fire modes
- **Power-Ups**:
  - `health`: Restore 1 life
  - `ammo`: Add 50 bullets
  - `enhanced`: Temporary rapid-fire mode
  - `fan`: Diagonal shooting for 3 seconds
- **Enemies**: Various types with different behaviors
- **Level System**: Progress through multiple levels
- **Safe Zone**: Victory condition when reaching the bottom of the screen

---

## 🧠 Configuration

### Level Files
- Located in `/levels/`
- Format: `levelX.txt` (e.g., `level1.txt`)
- Define enemy waves, bullet patterns, and level geometry

### Environment Variables
- `LEVELS_DIR`: Directory containing level files (default: `./levels`)

---

## 🧩 Development

### Adding New Levels
1. Create a new `levelX.txt` file in `/levels/`
2. Define enemy spawn patterns and level boundaries

### Contributing
1. Fork the repository
2. Create a new branch for your feature
3. Submit a pull request

---

## 📦 Version
Current version: `0.9.2` (from `build/version.txt`)

---

## 📄 License
This project is open-source and distributed under the MIT License. See the [LICENSE](LICENSE) file for details.

#### Source

```md


```

### FILE: `main.py`

#### Description

# Game Documentation

## Overview
This is a 2D shooter game inspired by classic arcade titles like 1942. The game features a player ship, enemies, bullets, power-ups, and a scrolling background. The code uses Pygame for rendering and input handling, with an async game loop for smooth animations and transitions.

## Key Components

### 1. **Main Game Class: `Game`**
The central class that manages the game state, rendering, and interactions.

#### Key Methods:
- `__init__`: Initializes game components (player, enemies, bullets, background, etc.).
- `update`: Async method that handles game logic (movement, collisions, power-ups).
- `render`: Draws all game elements to the screen.
- `handle_input`: Processes keyboard, mouse, and touch inputs.
- `next_level_or_win`: Transitions to the next level or ends the game.

#### Key Attributes:
- `player_sprite`: The player's ship object.
- `enemies`: List of enemy sprites.
- `player_bullets`: List of bullets fired by the player.
- `enemy_bullets`: List of bullets fired by enemies.
- `drops`: Power-up items that appear after defeating enemies.
- `fx`: Explosion effects.
- `bg`: Background object (scrolling or static).

---

### 2. **Player Sprite: `PlayerSprite`**
Controls the player's ship, including movement, shooting, and power-ups.

#### Key Methods:
- `update`: Handles movement and shooting.
- `shoot`: Fires bullets based on player input.
- `damage`: Reduces player health and triggers invincibility.
- `grant_enhanced`: Grants a temporary bullet spread power-up.
- `grant_fan`: Grants diagonal shooting for a limited time.

#### Power-Ups:
- `enhanced`: Wider bullet spread for 5 seconds.
- `fan`: Diagonal shooting for 5 seconds.
- `health`: Increases player lives.
- `ammo`: Increases bullet capacity.

---

### 3. **Enemy Classes**
Various enemy types with different behaviors.

#### Example:
- `ShooterEnemy`: Fires bullets periodically.
- `Enemy`: Base class for all enemies, handling movement and collision.

#### Key Features:
- Enemies spawn from level files.
- Collisions with bullets or the player trigger damage.
- Defeated enemies drop power-ups.

---

### 4. **Bullet System**
Handles both player and enemy bullets.

#### Key Features:
- **Player Bullets**: Fired on key press or auto-fire.
- **Enemy Bullets**: Fired by `ShooterEnemy` at intervals.
- **Collision Detection**: Checks for hits against enemies and the player.

---

### 5. **Power-Ups (Drops)**
Collectible items that appear after defeating enemies.

#### Types:
- `health`: +1 life.
- `ammo`: +50 bullets.
- `enhanced`: Temporary bullet spread.
- `fan`: Temporary diagonal shooting.

---

### 6. **Background System**
Manages scrolling or static backgrounds.

#### Key Methods:
- `update`: Updates background position.
- `draw`: Renders the background to the screen.

---

### 7. **Game Loop**
The async `update` method handles:
- Input processing
- Movement and collision checks
- Power-up collection
- Level transitions
- Rendering

---

## Configuration and Constants

### Game Settings
```python
PLAYER_SPEED = 300  # Pixels per second
BULLET_SPEED = 500
ENEMY_SPEED = 100
ENEMY_SPAWN_INTERVAL = 2.0  # Seconds
DROP_CHANCE = 0.3  # 30% chance for power-ups
```

### Colors
```python
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)
```

### Power-Up Weights
```python
DROP_WEIGHTS = {
    "health": 1,
    "ammo": 2,
    "enhanced": 1,
    "fan": 1
}
```

---

## Level System
- **Level Files**: Text files in `./levels/` (e.g., `level1.txt`).
- **Loading**: `discover_level_files()` finds and sorts level files.
- **Progression**: `next_level_or_win()` transitions to the next level or ends the game.

---

## Input Handling
Supports multiple input types:
- **Keyboard**: WASD or arrow keys for movement, SPACE for shooting.
- **Mouse**: Click to shoot (optional).
- **Touch**: Mobile-friendly controls via `TouchControls`.

---

## Usage Examples

### Starting the Game
```bash
python game.py --level 1
```

### Level File Format
Each `levelX.txt` defines enemy positions and patterns. Example:
```
enemy1,100,200
enemy2,300,150
```

### Power-Up Collection
When the player collides with a power-up:
```python
# Example: Collecting a "health" drop
self.player_sprite.lives = min(9, self.player_sprite.lives + 1)
```

---

## Key Functions

### `shoot(time, bullets_group)`
Fires bullets from the player. Handles cooldown and ammo limits.

### `damage(damage_amount)`
Reduces player/enemy health. Returns `True` if the entity is destroyed.

### `grant_enhanced(now)`
Activates the enhanced bullet spread for 5 seconds.

### `grant_fan(now)`
Activates diagonal shooting for 5 seconds.

---

## Environment Variables
- `LEVELS_DIR`: Directory containing level files (default: `./levels/`).

---

## Dependencies
- `pygame`: For rendering and input handling.
- `asyncio`: For async game loop.
- `glob`: For discovering level files.
- `random`: For power-up spawning.

---

## File Structure (Repository Context)
```
game.py
levels/
  level1.txt
  level2.txt
  ...
utils.py  # (Assumed helper functions)
```

---

## Future Improvements
- Add sound effects and music.
- Implement more enemy types and boss battles.
- Add a pause menu and settings screen.
- Optimize power-up spawning logic.

---

This documentation provides a high-level overview of the game's architecture, key components, and configuration. For deeper insights, explore the source code for specific implementations.

#### Source

```python
#!/usr/bin/env python3
from __future__ import annotations
import os, sys, time, math, random, glob, asyncio
import pygame

WIDTH, HEIGHT = 800, 600
FPS = 60
PLAYER_SPEED = 300.0
PLAYER_BULLET_SPEED = 600.0
PLAYER_BULLET_COOLDOWN = 0.15
PLAYER_START_LIVES = 5
INVULN_AFTER_DEATH = 2.0
ENHANCED_WEAPON_DURATION = 10.0

# ---- On-screen controls (thumbstick + fire button) ----
JOY_BASE_POS = (120, HEIGHT - 120)   # left-bottom
JOY_BASE_R   = 35
JOY_KNOB_R   = 16
JOY_DEADZONE = 0.12                  # ignore tiny jitters

FIRE_POS     = (WIDTH - 120, HEIGHT - 120)  # right-bottom
FIRE_R       = 56
FIRE_COLOR   = (255, 200, 80)
UI_ALPHA     = 140                   # transparency for UI widgets
_UI_BOTTOM_MARGIN = 60            # distance from bottom edge
_UI_SIDE_MARGIN   = 90            # distance from left/right edge

JOY_BASE_POS = ( _UI_SIDE_MARGIN, HEIGHT - _UI_BOTTOM_MARGIN )
FIRE_POS     = ( WIDTH - _UI_SIDE_MARGIN, HEIGHT - _UI_BOTTOM_MARGIN )
FIRE_R       = 28                 # was 56
FIRE_COLOR   = (255, 200, 80)

# Big enemy sizing (relative guarantees)
BIG_MIN_SCALE_VS_SHOOTER = 1.8
BIG_PADDING = 0.92
# --- BigEnemy safety caps (add near other BIG_* constants) ---
BIG_MIN_ABS_W = 80
BIG_MIN_ABS_H = 60
BIG_MAX_ABS_W = int(WIDTH * 0.70)   # prevent skyscraper-wide bosses
BIG_MAX_ABS_H = int(HEIGHT * 0.55)  # prevent skyscraper-tall bosses

# Only allow big enemies when the letter is explicitly 'B'
ONLY_EXPLICIT_BOSS = True

# Optional spawn debug
DEBUG_SPAWN = False

ENEMY_BASE_SPEED = 120.0

# Kamikaze config
KAMIKAZE_SPEED = 200.0
KAMIKAZE_BOOST = 200.0
KAMIKAZE_LOCK_DX = 100
KAMIKAZE_LOCK_DY = 600

ENEMY_BULLET_SPEED = 300.0
ENEMY_FIRE_COOLDOWN = (0.5, 1.0)

# Shooter tracking
SHOOTER_HMOVE_SPEED = 160.0
SHOOTER_TRACK_GAIN  = 1.0

SPAWN_ROW_MS = 800
DROP_CHANCE = 0.35
DROP_TYPES = ["health", "ammo", "enhanced", "fan"]
DROP_WEIGHTS = {"health": 1, "ammo": 1, "enhanced": 2, "fan": 2}

SAFE_ZONE_TAIL_MS = 5000
WHITE=(255,255,255); BLACK=(0,0,0); GREEN=(0,220,0); RED=(220,40,40); YELLOW=(250,220,80); BLUE=(60,160,255); GRAY=(100,100,100)

# Web vs desktop
IS_WEB = (sys.platform == "emscripten")

# Paths: absolute on desktop, relative on web
if IS_WEB:
    BASE_DIR   = ""
    ASSETS_DIR = "assets"
    LEVELS_DIR = "levels"
else:
    BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
    ASSETS_DIR = os.path.join(BASE_DIR, "assets")
    LEVELS_DIR = os.path.join(BASE_DIR, "levels")

async def sleep_ms(ms: int):
    if IS_WEB:
        await asyncio.sleep(ms / 1000.0)
    else:
        pygame.time.delay(ms)

def load_image(path: str, fallback_size=(24,24), color=(200,200,200)):
    if os.path.exists(path):
        try:
            img = pygame.image.load(path).convert_alpha()
            return img
        except Exception:
            pass
    s = pygame.Surface(fallback_size, pygame.SRCALPHA)
    pygame.draw.rect(s, color, (0,0,*fallback_size), border_radius=4)
    return s

def load_explosion_frames(folder="assets", prefix="explosion_", count=6):
    frames = []
    for i in range(count):
        p = os.path.join(folder, f"{prefix}{i}.png")
        if os.path.exists(p):
            try:
                frames.append(pygame.image.load(p).convert_alpha())
            except Exception:
                pass
    if not frames:
        for i in range(count):
            r = 10 + i*3
            s = pygame.Surface((r*2, r*2), pygame.SRCALPHA)
            pygame.draw.circle(s, (255,200,50), (r,r), r-1)
            pygame.draw.circle(s, (255,120,20), (r,r), max(1,r-4), 3)
            if i%2==0:
                pygame.draw.circle(s, (255,255,255), (r,r), max(1,r-8), 2)
            frames.append(s)
    return frames

def load_level_grid(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\\n") for line in f]
    maxw = max((len(l) for l in lines), default=0)
    norm = [(l + " " * max(0, maxw - len(l)))[:maxw] for l in lines]
    return norm

def connected_components(grid: list[str]) -> list[dict]:
    if not grid: return []
    R, C = len(grid), len(grid[0])
    visited = [[False]*C for _ in range(R)]
    comps = []
    for r in range(R):
        for c in range(C):
            ch = grid[r][c]
            if ch not in (" ", ".", "\\t") and not visited[r][c]:
                stack=[(r,c)]; visited[r][c]=True; cells=[]
                while stack:
                    rr,cc=stack.pop(); cells.append((rr,cc))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr,nc=rr+dr,cc+dc
                        if 0<=nr<R and 0<=nc<C and not visited[nr][nc] and grid[nr][nc]==ch:
                            visited[nr][nc]=True; stack.append((nr,nc))
                rows=[rr for rr,_ in cells]; cols=[cc for _,cc in cells]
                comps.append({"letter":ch,"cells":cells,"min_r":min(rows),"max_r":max(rows),
                              "min_c":min(cols),"max_c":max(cols),"area":len(cells)})
    comps.sort(key=lambda d:d["min_r"])
    return comps

# ------------ Scrolling background --------------
def _ui_positions():
    # recompute every draw in case of resize (pygbag can rescale canvas)
    joy_pos = (_UI_SIDE_MARGIN, HEIGHT - _UI_BOTTOM_MARGIN)
    fire_pos = (WIDTH - _UI_SIDE_MARGIN, HEIGHT - _UI_BOTTOM_MARGIN)
    return joy_pos, fire_pos

class TouchControls:
    """
    Dual-input (mouse + multitouch) virtual joystick + fire button.
    Works on desktop and pygbag. Keeps separate pointer IDs so two-finger
    control is reliable on mobile.
    """
    def __init__(self):
        # pointer_id -> where it started and what it's controlling
        self.active = {}  # {id: {"kind":"joy"/"fire", "start":(x,y)}}
        self.joy_vec = (0.0, 0.0)
        self.fire_held = False

        # prebuild UI surfaces
        self._joy_base = pygame.Surface((JOY_BASE_R*2, JOY_BASE_R*2), pygame.SRCALPHA)
        self._joy_knob = pygame.Surface((JOY_KNOB_R*2, JOY_KNOB_R*2), pygame.SRCALPHA)
        self._fire_surf = None  # built in draw()
        pygame.draw.circle(self._joy_base, (255,255,255,UI_ALPHA), (JOY_BASE_R, JOY_BASE_R), JOY_BASE_R, 2)
        pygame.draw.circle(self._joy_knob, (255,255,255,UI_ALPHA), (JOY_KNOB_R, JOY_KNOB_R), JOY_KNOB_R)

    # ------- helpers -------
    @staticmethod
    def _dist(ax, ay, bx, by):
        dx, dy = ax-bx, ay-by
        return math.hypot(dx, dy)

    def _which_zone(self, x, y):
        joy_pos, fire_pos = _ui_positions()
        # fire first so taps near RH side don't grab stick
        if self._dist(x, y, *fire_pos) <= 28:  # FIRE_R
            return "fire"
        if self._dist(x, y, *joy_pos) <= JOY_BASE_R:
            return "joy"
        return None

    def _update_joy_from(self, x, y):
        joy_pos, _ = _ui_positions()
        dx = x - joy_pos[0]
        dy = y - joy_pos[1]
        # clamp to circle
        mag = math.hypot(dx, dy)
        if mag > 0:
            nx = dx / max(1e-6, JOY_BASE_R)
            ny = dy / max(1e-6, JOY_BASE_R)
            # stick vector normalized to [-1,1] within base radius
            l = math.hypot(nx, ny)
            if l > 1.0:
                nx /= l; ny /= l
        else:
            nx = ny = 0.0
        # deadzone
        if math.hypot(nx, ny) < JOY_DEADZONE:
            nx = ny = 0.0
        self.joy_vec = (max(-1.0, min(1.0, nx)), max(-1.0, min(1.0, ny)))
        # Convenience: single-entry dispatcher so Game can just forward events
    def handle_event(self, e):
        if e.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION):
            self.handle_mouse_event(e)
        elif e.type in (pygame.FINGERDOWN, pygame.FINGERMOTION, pygame.FINGERUP):
            self.handle_finger_event(e)

    # Back-compat with your Game.update() calls
    def get_vector(self):
        jx, jy = self.joy_vec
        return pygame.Vector2(jx, jy)

    def is_firing(self):
        return self.fire_held
    # ------- public API for events -------
    def handle_mouse_event(self, e):
        # Treat mouse as pointer id = -1
        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            x, y = e.pos
            k = self._which_zone(x, y)
            if k:
                self.active[-1] = {"kind": k}
                if k == "joy":
                    self._update_joy_from(x, y)
                elif k == "fire":
                    self.fire_held = True

        elif e.type == pygame.MOUSEMOTION:
            if -1 in self.active and self.active[-1]["kind"] == "joy":
                self._update_joy_from(*e.pos)

        elif e.type == pygame.MOUSEBUTTONUP and e.button == 1:
            if -1 in self.active:
                kind = self.active[-1]["kind"]
                del self.active[-1]
                if kind == "joy":
                    self.joy_vec = (0.0, 0.0)
                elif kind == "fire":
                    self.fire_held = False

    def handle_finger_event(self, e):
        # e.x, e.y are normalized [0..1] in pygbag
        pid = int(e.finger_id) if hasattr(e, "finger_id") else int(e.touch_id)
        x = int(e.x * WIDTH)
        y = int(e.y * HEIGHT)

        if e.type == pygame.FINGERDOWN:
            k = self._which_zone(x, y)
            if k:
                self.active[pid] = {"kind": k}
                if k == "joy":
                    self._update_joy_from(x, y)
                elif k == "fire":
                    self.fire_held = True

        elif e.type == pygame.FINGERMOTION:
            if pid in self.active and self.active[pid]["kind"] == "joy":
                self._update_joy_from(x, y)

        elif e.type == pygame.FINGERUP:
            if pid in self.active:
                kind = self.active[pid]["kind"]
                del self.active[pid]
                if kind == "joy":
                    self.joy_vec = (0.0, 0.0)
                elif kind == "fire":
                    self.fire_held = False

    # ------- polling -------
    def get_axis(self):
        # returns (x, y) in [-1..1]
        return self.joy_vec

    def is_fire(self):
        return self.fire_held

    # ------- draw -------
    def draw(self, surf):
        joy_pos, fire_pos = _ui_positions()
        # draw fire button (build once at scale)
        if self._fire_surf is None:
            r = 28
            s = pygame.Surface((r*2, r*2), pygame.SRCALPHA)
            pygame.draw.circle(s, (255, 200, 80, UI_ALPHA), (r, r), r)
            pygame.draw.circle(s, (255, 255, 255, UI_ALPHA), (r, r), r, 2)
            self._fire_surf = s
        # stick base
        surf.blit(self._joy_base, (joy_pos[0] - JOY_BASE_R, joy_pos[1] - JOY_BASE_R))
        # knob at current vector position, scaled within base radius
        jx, jy = self.joy_vec
        knob_x = int(joy_pos[0] + jx * (JOY_BASE_R - JOY_KNOB_R))
        knob_y = int(joy_pos[1] + jy * (JOY_BASE_R - JOY_KNOB_R))
        surf.blit(self._joy_knob, (knob_x - JOY_KNOB_R, knob_y - JOY_KNOB_R))
        # fire
        surf.blit(self._fire_surf, (fire_pos[0] - self._fire_surf.get_width()//2,
                                    fire_pos[1] - self._fire_surf.get_height()//2))

class ScrollingBackground:
    def __init__(self, segments, speed=50, loop=True):
        self.segs = segments[:] if segments else [pygame.Surface((WIDTH, HEIGHT))]
        self.speed = float(speed)
        self.loop = loop
        self.offset = 0.0  # float for sub-pixel scroll
        self.heights = [s.get_height() for s in self.segs]
        self.total_h = sum(self.heights)

    def update(self, dt):
        if not self.segs or self.total_h <= 0:
            return
        # Move terrain DOWN the screen
        self.offset -= self.speed * dt
        if self.loop:
            self.offset %= self.total_h
        else:
            self.offset = max(0.0, min(self.offset, float(max(0, self.total_h - HEIGHT))))

    def draw(self, surf):
        if not self.segs:
            surf.fill((20, 20, 20))
            return

        # Normalize offset
        off = (self.offset % self.total_h) if self.loop else max(0.0, min(self.offset, float(max(0, self.total_h - HEIGHT))))

        # Find starting segment index and y inside it
        idx = 0
        remaining = off
        while remaining >= self.heights[idx]:
            remaining -= self.heights[idx]
            idx = (idx + 1) % len(self.segs) if self.loop else min(idx + 1, len(self.segs) - 1)

        # Start drawing so that the first segment begins at y = -remaining
        y = -int(remaining)
        i = idx
        # Blit until the screen is filled
        while y < HEIGHT:
            seg = self.segs[i % len(self.segs)] if self.loop else self.segs[min(i, len(self.segs) - 1)]
            surf.blit(seg, (0, y))
            y += seg.get_height()
            i += 1
            if not self.loop and (i >= len(self.segs) and y >= HEIGHT):
                break

def _extract_level_number_from_path(path: str) -> int:
    base = os.path.basename(path)
    digits = ''.join(ch for ch in base if ch.isdigit())
    try:
        return int(digits) if digits else 1
    except ValueError:
        return 1

def load_level_background(level_number: int) -> ScrollingBackground:
    segs = []
    seg_paths = []
    idx = 1
    while True:
        p = os.path.join(ASSETS_DIR, f"background{level_number}_{idx}.png")
        if not os.path.exists(p):
            break
        seg_paths.append(p)
        idx += 1

    if not seg_paths:
        p = os.path.join(ASSETS_DIR, f"background{level_number}.png")
        if os.path.exists(p):
            seg_paths.append(p)

    # Load + rescale each segment to exactly WIDTH, keeping aspect ratio
    for p in seg_paths:
        img = load_image(p)
        if img.get_width() != WIDTH:
            new_h = max(1, int(img.get_height() * (WIDTH / img.get_width())))
            img = pygame.transform.smoothscale(img, (WIDTH, new_h))
        segs.append(img)

    # Visible fallback tile (green land, lakes, forest blobs)
    if not segs:
        tile = pygame.Surface((WIDTH, HEIGHT))
        tile.fill((26, 46, 26))
        for _ in range(10):
            rx = random.randint(0, WIDTH-180)
            ry = random.randint(0, HEIGHT-120)
            pygame.draw.ellipse(tile, (40, 80, 140), (rx, ry, 180, 90))
        for _ in range(16):
            rx = random.randint(0, WIDTH-80)
            ry = random.randint(0, HEIGHT-50)
            pygame.draw.rect(tile, (34, 90, 34), (rx, ry, 70, 36), border_radius=10)
        segs.append(tile)
        print(f"[BG] Level {level_number}: no PNGs found, using fallback tile")

    base_speed = 50  # tweak speed here
    bg = ScrollingBackground(segs, speed=base_speed, loop=True)
    # Start with the last part visible to avoid black at boot
    if bg.total_h > 0:
        bg.offset = (bg.total_h - HEIGHT) % bg.total_h
    print(f"[BG] Level {level_number}: loaded {len(segs)} segment(s) total_h={bg.total_h}px speed={base_speed}px/s")
    return bg

# ------------ Entities --------------
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, vy, color=YELLOW, friendly=True, vx=0.0):
        super().__init__()
        self.image = pygame.Surface((4, 10), pygame.SRCALPHA)
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        self.vx = vx
        self.vy = vy
        self.friendly = friendly

    def update(self, dt):
        self.rect.x += int(self.vx * dt)
        self.rect.y += int(self.vy * dt)
        if (self.rect.bottom < 0 or self.rect.top > HEIGHT
                or self.rect.right < 0 or self.rect.left > WIDTH):
            self.kill()

class Drop(pygame.sprite.Sprite):
    def __init__(self, x, y, kind: str):
        super().__init__(); self.kind = kind
        self.image = pygame.Surface((16, 16), pygame.SRCALPHA)
        if kind == "health":
            pygame.draw.rect(self.image, GREEN, (0,0,16,16), border_radius=3)
            pygame.draw.line(self.image, WHITE, (8,2),(8,14), 2)
            pygame.draw.line(self.image, WHITE, (2,8),(14,8), 2)
        elif kind == "ammo":
            pygame.draw.rect(self.image, BLUE, (0,0,16,16), border_radius=3)
            pygame.draw.rect(self.image, WHITE, (6,3,4,10))
        elif kind == "enhanced":
            pygame.draw.rect(self.image, YELLOW, (0,0,16,16), border_radius=3)
            pygame.draw.circle(self.image, WHITE, (8,8), 5, 2)
        elif kind == "fan":
            pygame.draw.rect(self.image, YELLOW, (0,0,16,16), border_radius=3)
            pygame.draw.line(self.image, WHITE, (3,13), (13,3), 2)
            pygame.draw.line(self.image, WHITE, (3,3), (13,13), 1)
        else:
            pygame.draw.rect(self.image, YELLOW, (0,0,16,16), border_radius=3)
        self.rect = self.image.get_rect(center=(x,y))
        self.vy = 60

    def update(self, dt):
        self.rect.y += int(self.vy * dt)
        if self.rect.top > HEIGHT: self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, frames, fps=24):
        super().__init__()
        self.frames = frames; self.index = 0; self.time_per = 1.0 / fps; self.t = 0.0
        self.image = self.frames[0]; self.rect = self.image.get_rect(center=(x,y))
    def update(self, dt):
        self.t += dt
        while self.t >= self.time_per:
            self.t -= self.time_per; self.index += 1
            if self.index >= len(self.frames): self.kill(); return
            center = self.rect.center; self.image = self.frames[self.index]
            self.rect = self.image.get_rect(center=center)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, img: pygame.Surface, hp=2):
        super().__init__(); self.base_image = img; self.image = img.copy()
        self.rect = self.image.get_rect(center=(x,y))
        self.hp = hp; self.vy = ENEMY_BASE_SPEED; self.fire_t = random.uniform(*ENEMY_FIRE_COOLDOWN); self.time = 0.0
    def update(self, dt):
        self.time += dt; self.rect.y += int(self.vy * dt)
        if self.rect.top > HEIGHT: self.kill()
    def damage(self, dmg=1):
        self.hp -= dmg
        if self.hp <= 0: self.kill(); return True
        return False
    def maybe_drop(self, drops_group):
        if random.random() < DROP_CHANCE:
            pool = []
            for k, w in DROP_WEIGHTS.items():
                pool.extend([k] * int(max(1, w)))
            kind = random.choice(pool)
            drops_group.add(Drop(self.rect.centerx, self.rect.centery, kind))

class ShooterEnemy(Enemy):
    def __init__(self, x, y, img, hp=3):
        super().__init__(x, y, img, hp)
        self.target_ref = None

    def update(self, dt, bullets_group=None):
        if self.target_ref is not None:
            dx = self.target_ref.rect.centerx - self.rect.centerx
            vx = max(-SHOOTER_HMOVE_SPEED, min(SHOOTER_HMOVE_SPEED, dx * SHOOTER_TRACK_GAIN))
            self.rect.x += int(vx * dt)
            if self.rect.left < 0: self.rect.left = 0
            if self.rect.right > WIDTH: self.rect.right = WIDTH
        super().update(dt)
        self.fire_t -= dt
        if bullets_group is not None and self.fire_t <= 0:
            self.fire_t = random.uniform(*ENEMY_FIRE_COOLDOWN)
            bullets_group.add(Bullet(self.rect.centerx, self.rect.bottom, ENEMY_BULLET_SPEED, color=WHITE, friendly=False))

class KamikazeEnemy(Enemy):
    def __init__(self, x, y, img, hp=2):
        super().__init__(x, y, img, hp)
        self.vy = KAMIKAZE_SPEED
        self.target_ref = None
        self.locked = False

    def update(self, dt):
        if self.target_ref is not None:
            px, py = self.target_ref.rect.center
            dx = px - self.rect.centerx
            dy = py - self.rect.centery
            if abs(dx) < KAMIKAZE_LOCK_DX and 0 < dy < KAMIKAZE_LOCK_DY:
                self.locked = True
            fwd = self.vy + (KAMIKAZE_BOOST if self.locked else 0.0)
            d = max(1.0, math.hypot(dx, dy))
            vx = (dx / d) * 100.0
            vy = (dy / d) * fwd / (KAMIKAZE_SPEED / 100.0)
            self.rect.x += int(vx * dt)
            self.rect.y += int(vy * dt)
        else:
            self.rect.y += int(self.vy * dt)
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.kill()

class BigEnemy(Enemy):
    def __init__(self, x, y, base_img, w_cells, h_cells, cell_w, cell_h, shooter_img):
        # Desired bbox from component
        bbox_w = max(int(w_cells * cell_w * BIG_PADDING), BIG_MIN_ABS_W)
        bbox_h = max(int(h_cells * cell_h * BIG_PADDING), BIG_MIN_ABS_H)

        # Enforce caps
        bbox_w = min(bbox_w, BIG_MAX_ABS_W)
        bbox_h = min(bbox_h, BIG_MAX_ABS_H)

        # Ensure bigger than a shooter, still within caps
        sw, sh = shooter_img.get_width(), shooter_img.get_height()
        bbox_w = max(bbox_w, int(sw * BIG_MIN_SCALE_VS_SHOOTER))
        bbox_h = max(bbox_h, int(sh * BIG_MIN_SCALE_VS_SHOOTER))
        bbox_w = min(bbox_w, BIG_MAX_ABS_W)
        bbox_h = min(bbox_h, BIG_MAX_ABS_H)

        # Preserve aspect ratio of the base image
        bw, bh = base_img.get_width(), base_img.get_height()
        if bw <= 0 or bh <= 0:
            target_w, target_h = bbox_w, bbox_h
        else:
            scale = min(bbox_w / bw, bbox_h / bh)
            target_w = max(1, int(bw * scale))
            target_h = max(1, int(bh * scale))

        img2 = pygame.transform.smoothscale(base_img, (target_w, target_h))

        # HP scaled to component area, with a floor
        hp = max(6, 4 + (w_cells * h_cells) // 2)
        super().__init__(x, y, img2, hp=hp)
        self.vy = ENEMY_BASE_SPEED * 0.75

        # keep inside screen horizontally
        if self.rect.left < 0: self.rect.left = 0
        if self.rect.right > WIDTH: self.rect.right = WIDTH


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        super().__init__(); self.base_image = img; self.image = self.base_image.copy()
        self.rect = self.image.get_rect(center=(x,y)); self.speed = PLAYER_SPEED; self.lives = PLAYER_START_LIVES
        self.invuln_t = 0.0; self.shoot_t = 0.0; self.ammo = 9999; self.enhanced_until = 0.0
        self.fan_until = 0.0 
    def has_enhanced(self, now: float) -> bool: return now < self.enhanced_until
    def grant_enhanced(self, now: float): self.enhanced_until = max(self.enhanced_until, now + ENHANCED_WEAPON_DURATION)
    def has_fan(self, now: float) -> bool: return now < self.fan_until
    def grant_fan(self, now: float): self.fan_until = max(self.fan_until, now + ENHANCED_WEAPON_DURATION)
    def update(self, dt, keys):
        vx = vy = 0.0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]: vx -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]: vx += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]: vy -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]: vy += self.speed
        self.rect.x += int(vx * dt); self.rect.y += int(vy * dt)
        self.rect.clamp_ip(pygame.Rect(0,0,WIDTH,HEIGHT))
        if self.invuln_t > 0: self.invuln_t -= dt
    def shoot(self, now: float, bullets_group):
        if self.shoot_t > now: return
        self.shoot_t = now + PLAYER_BULLET_COOLDOWN
        cx, cy = self.rect.centerx, self.rect.top
        if self.has_enhanced(now):
            bullets_group.add(Bullet(cx,     cy, -PLAYER_BULLET_SPEED, color=YELLOW, friendly=True))
            bullets_group.add(Bullet(cx - 10, cy, -PLAYER_BULLET_SPEED, color=YELLOW, friendly=True))
            bullets_group.add(Bullet(cx + 10, cy, -PLAYER_BULLET_SPEED, color=YELLOW, friendly=True))
        else:
            bullets_group.add(Bullet(cx, cy, -PLAYER_BULLET_SPEED, color=YELLOW, friendly=True))
        if self.has_fan(now):
            diag = PLAYER_BULLET_SPEED / math.sqrt(2)
            bullets_group.add(Bullet(cx, cy, -diag, color=YELLOW, friendly=True, vx=-diag))
            bullets_group.add(Bullet(cx, cy, -diag, color=YELLOW, friendly=True, vx= diag))
    def damage(self):
        if self.invuln_t > 0: return False
        self.lives -= 1; self.invuln_t = INVULN_AFTER_DEATH
        return self.lives >= 0

class SpawnEvent:
    def __init__(self, min_row, cx, cy, w_cells, h_cells, letter):
        self.min_row = min_row; self.cx = cx; self.cy = cy
        self.w_cells = w_cells; self.h_cells = h_cells; self.letter = letter; self.spawned = False

class LevelTimeline:
    def __init__(self, grid, assets):
        self.grid = grid; self.R = len(grid); self.C = len(grid[0]) if self.R else 0
        self.cell_w = WIDTH / max(1, self.C); self.cell_h = 28
        self.events = []
        comps = connected_components(grid)
        for comp in comps:
            cminr,cmaxr=comp["min_r"],comp["max_r"]; cminc,cmaxc=comp["min_c"],comp["max_c"]
            center_c = (cminc + cmaxc + 1) / 2.0; w_cells = cmaxc - cminc + 1; h_cells = cmaxr - cminr + 1
            cx = int(center_c * self.cell_w); cy = -int(h_cells * self.cell_h) - 20
            self.events.append(SpawnEvent(cminr, cx, cy, w_cells, h_cells, comp["letter"]))
        self.events.sort(key=lambda e:e.min_row)
        self.row_timer = 0.0; self.row_index = 0; self.done_spawning = False; self.all_spawned_time = None
        self.img_shooter = assets["enemy_shooter"]; self.img_kamikaze = assets["enemy_kamikaze"]; self.img_big = assets["enemy_big"]
    def update(self, dt_ms, enemies_group, player_ref, enemy_bullets):
        self.row_timer += dt_ms
        while not self.done_spawning and self.row_timer >= SPAWN_ROW_MS * (self.row_index + 1):
            self.row_index += 1; target_row = self.row_index - 1
            for ev in self.events:
                if not ev.spawned and ev.min_row == target_row:
                    ev.spawned = True; self._spawn_event(ev, enemies_group, player_ref, enemy_bullets)
        if not self.done_spawning and self.row_index >= self.R:
            self.done_spawning = True; self.all_spawned_time = pygame.time.get_ticks()
    def _spawn_event(self, ev, enemies_group, player_ref, enemy_bullets):
        letter = ev.letter.upper()

        # Safety: optionally *only* spawn BigEnemy when the map letter is 'B'
        if ONLY_EXPLICIT_BOSS and letter != "B":
            # Not a boss; fall through to regular types below
            pass
        elif letter == "B":
            # Guard against absurd components (just in case)
            if ev.w_cells > 12 or ev.h_cells > 12:
                if DEBUG_SPAWN:
                    print(f"[SPAWN] Suppressing giant BigEnemy {ev.w_cells}x{ev.h_cells} at row {ev.min_row}")
                e = Enemy(ev.cx, ev.cy, self.img_shooter, hp=2)
            else:
                e = BigEnemy(
                    ev.cx, ev.cy,
                    self.img_big,
                    ev.w_cells, ev.h_cells,
                    self.cell_w, self.cell_h,
                    shooter_img=self.img_shooter,
                )
                enemies_group.add(e)
                if DEBUG_SPAWN:
                    print(f"[SPAWN] BigEnemy {ev.w_cells}x{ev.h_cells} at row {ev.min_row}, center=({ev.cx},{ev.cy})")
                return  # done

        # Normal spawns
        if letter == "S":
            e = ShooterEnemy(ev.cx, ev.cy, self.img_shooter); e.target_ref = player_ref
        elif letter == "K":
            e = KamikazeEnemy(ev.cx, ev.cy, self.img_kamikaze); e.target_ref = player_ref
        else:
            e = Enemy(ev.cx, ev.cy, self.img_shooter, hp=2)

        enemies_group.add(e)


class Game:
    def __init__(self, level_paths: list[str]):
        pygame.init()
        # Use default font (works on web)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)); pygame.display.set_caption("1942-lite")
        self.clock = pygame.time.Clock(); self.font    = pygame.font.Font(None, 18); self.bigfont = pygame.font.Font(None, 28)
        self.running = True; self.paused = False; self.debug = False
        self.controls = TouchControls()
        self.assets = {
            "player":         load_image(os.path.join(ASSETS_DIR, "player.png"),         (28,28), (70,160,255)),
            "enemy_shooter":  load_image(os.path.join(ASSETS_DIR, "enemy_shooter.png"),  (36,28), (210,60,60)),
            "enemy_kamikaze": load_image(os.path.join(ASSETS_DIR, "enemy_kamikaze.png"), (30,26), (255,140,30)),
            "enemy_big":      load_image(os.path.join(ASSETS_DIR, "enemy_big.png"),      (54,42), (180,60,200)),
            "explosion_frames": load_explosion_frames(ASSETS_DIR, "explosion_", 6),
        }

        self.all_sprites = pygame.sprite.Group(); self.enemies = pygame.sprite.Group()
        self.player_bullets = pygame.sprite.Group(); self.enemy_bullets = pygame.sprite.Group(); self.drops = pygame.sprite.Group(); self.fx = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle(Player(WIDTH//2, HEIGHT-70, self.assets["player"]))
        self.level_paths = level_paths; self.level_index = 0; 
        self.bg = None
        self.load_level(self.level_paths[self.level_index])
        self.safe_zone_active = False; self.safe_zone_y = HEIGHT - 80

    @property
    def player_sprite(self): return self.player.sprite

    def load_level(self, path):
        grid = load_level_grid(path)
        self.timeline = LevelTimeline(grid, self.assets)
        self.safe_zone_active = False
        self.enemy_bullets.empty(); self.enemies.empty(); self.drops.empty(); self.fx.empty()

        lvl_num = _extract_level_number_from_path(path)
        self.bg = load_level_background(lvl_num)

        # Start with the last part of the stack on-screen (no initial black)
        if self.bg and self.bg.total_h > 0:
            self.bg.offset = (self.bg.total_h - HEIGHT) % self.bg.total_h

        print(f"[BG] Level {lvl_num}: segments={len(self.bg.segs)} total_h={self.bg.total_h}")

    def spawn_safe_zone_if_ready(self):
        if not self.timeline.done_spawning: return
        if self.timeline.all_spawned_time is not None:
            if pygame.time.get_ticks() - self.timeline.all_spawned_time >= SAFE_ZONE_TAIL_MS: self.safe_zone_active = True

    async def run(self):
        while self.running:
            dt = self.clock.tick(FPS)/1000.0; dt_ms = dt*1000.0
            self.handle_events()
            if not self.paused:
                await self.update(dt, dt_ms)
            self.render()

            # Important for pygbag: let the browser breathe
            if IS_WEB:
                await asyncio.sleep(0)

        # On desktop, quit pygame at the end
        if not IS_WEB:
            pygame.quit()

    def handle_events(self):
        for e in pygame.event.get():
            self.controls.handle_event(e)

            if e.type == pygame.QUIT: self.running=False
            elif e.type == pygame.KEYDOWN:
                if e.key in (pygame.K_ESCAPE, pygame.K_q): self.running=False
                elif e.key == pygame.K_p: self.paused = not self.paused
                elif e.key == pygame.K_F1: self.debug = not self.debug
                elif e.key == pygame.K_f:
                    px, py = self.player_sprite.rect.center
                    self.drops.add(Drop(px, py - 20, "fan"))
            
            elif e.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION):
                self.controls.handle_mouse_event(e)

            # --- finger -> touch controls (pygbag/mobile) ---
            elif e.type in (pygame.FINGERDOWN, pygame.FINGERMOTION, pygame.FINGERUP):
                self.controls.handle_finger_event(e)

        keys = pygame.key.get_pressed()
        if not self.paused:
            self.player_sprite.update(0, keys)
            if keys[pygame.K_SPACE]: self.player_sprite.shoot(time.perf_counter(), self.player_bullets)

    async def update(self, dt, dt_ms):
        keys = pygame.key.get_pressed(); self.player_sprite.update(dt, keys)
        ax, ay = self.controls.get_axis()   # [-1..1]
        if ax or ay:
            self.player_sprite.rect.x += int(ax * PLAYER_SPEED * dt)
            self.player_sprite.rect.y += int(ay * PLAYER_SPEED * dt)
            self.player_sprite.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

        # Virtual fire (hold to auto-fire at your normal cooldown)
        if self.controls.is_fire():
            self.player_sprite.shoot(time.perf_counter(), self.player_bullets)

        move = self.controls.get_vector() * PLAYER_SPEED
        if move.length_squared() > 0:
            self.player_sprite.rect.x += int(move.x * dt)
            self.player_sprite.rect.y += int(move.y * dt)
            self.player_sprite.rect.clamp_ip(pygame.Rect(0,0,WIDTH,HEIGHT))

        # --- Touch fire button ---
        if self.controls.is_firing():
            self.player_sprite.shoot(time.perf_counter(), self.player_bullets)

        self.timeline.update(dt_ms, self.enemies, self.player_sprite, self.enemy_bullets); self.spawn_safe_zone_if_ready()
        for e in list(self.enemies):
            if isinstance(e, ShooterEnemy): e.update(dt, bullets_group=self.enemy_bullets)
            else: e.update(dt)
        self.player_bullets.update(dt); self.enemy_bullets.update(dt); self.drops.update(dt); self.fx.update(dt)
        if self.bg: self.bg.update(dt)

        for bullet in list(self.player_bullets):
            hits = [sp for sp in self.enemies if sp.rect.colliderect(bullet.rect)]
            if hits:
                bullet.kill()
                for enemy in hits:
                    dead = enemy.damage(1)
                    if dead:
                        self.fx.add(Explosion(enemy.rect.centerx, enemy.rect.centery, self.assets["explosion_frames"]))
                        enemy.kill()
                        cx, cy = enemy.rect.center
                        if random.random() < DROP_CHANCE:
                            pool = []
                            for k, w in DROP_WEIGHTS.items():
                                pool.extend([k] * int(max(1, w)))
                            kind = random.choice(pool)
                            self.drops.add(Drop(cx, cy, kind))

        if self.player_sprite.invuln_t <= 0:
            if pygame.sprite.spritecollideany(self.player_sprite, self.enemy_bullets) or pygame.sprite.spritecollideany(self.player_sprite, self.enemies):
                px, py = self.player_sprite.rect.center; alive = self.player_sprite.damage()
                for b in list(self.enemy_bullets):
                    if self.player_sprite.rect.colliderect(b.rect): b.kill()
                self.fx.add(Explosion(px, py, self.assets["explosion_frames"]))
                if not alive: await self.game_over()
                else: self.player_sprite.rect.center = (px, py)
        got = pygame.sprite.spritecollide(self.player_sprite, self.drops, dokill=True)
        now = time.perf_counter()
        for d in got:
            if d.kind == "health":
                self.player_sprite.lives = min(9, self.player_sprite.lives + 1)
            elif d.kind == "ammo":
                self.player_sprite.ammo = min(9999, self.player_sprite.ammo + 50)
            elif d.kind == "enhanced":
                self.player_sprite.grant_enhanced(now)
            elif d.kind == "fan":
                self.player_sprite.grant_fan(now)

        if self.safe_zone_active and self.player_sprite.rect.top <= self.safe_zone_y: await self.next_level_or_win()

    async def next_level_or_win(self):
        self.level_index += 1
        if self.level_index < len(self.level_paths):
            await self.banner("LEVEL CLEARED!", (80,220,80), delay=1200)
            self.load_level(self.level_paths[self.level_index])
            self.player_sprite.rect.center = (WIDTH//2, HEIGHT-70); self.player_sprite.invuln_t = 1.0
        else:
            await self.win_and_exit()

    async def game_over(self):
        surf = self.screen; surf.fill(BLACK)
        txt = self.bigfont.render("GAME OVER", True, RED); surf.blit(txt, txt.get_rect(center=(WIDTH//2, HEIGHT//2)))
        pygame.display.flip()
        await sleep_ms(2200)
        self.running = False

    async def win_and_exit(self):
        surf = self.screen; surf.fill(BLACK)
        txt = self.bigfont.render("SAFE ZONE REACHED! YOU WIN!", True, GREEN); surf.blit(txt, txt.get_rect(center=(WIDTH//2, HEIGHT//2)))
        pygame.display.flip()
        await sleep_ms(2200)
        self.running = False

    async def banner(self, text, color, delay=1000):
        surf = self.screen; surf.fill(BLACK)
        b = self.bigfont.render(text, True, color); surf.blit(b, b.get_rect(center=(WIDTH//2, HEIGHT//2)))
        pygame.display.flip()
        await sleep_ms(delay)

    def render(self):
        self.screen.fill(BLACK)
        if self.bg: self.bg.draw(self.screen)
        if self.safe_zone_active:
            pygame.draw.rect(self.screen, (40,120,40), (0, self.safe_zone_y, WIDTH, HEIGHT - self.safe_zone_y))
        self.enemies.draw(self.screen); self.player_bullets.draw(self.screen); self.enemy_bullets.draw(self.screen); self.fx.draw(self.screen)
        if int(self.player_sprite.invuln_t * 10) % 2 == 0 or self.player_sprite.invuln_t <= 0: self.screen.blit(self.player_sprite.image, self.player_sprite.rect)
        self.drops.draw(self.screen); self.draw_hud(self.screen); 
        
        self.controls.draw(self.screen)
        pygame.display.flip()

    def draw_hud(self, surf):
        lives_s = self.font.render(f"Lives: {max(0,self.player_sprite.lives)}", True, WHITE); surf.blit(lives_s, (8, 8))
        now = time.perf_counter()
        if self.player_sprite.has_enhanced(now):
            rem = max(0.0, self.player_sprite.enhanced_until - now); enh_s = self.font.render(f"Enhanced: {rem:0.1f}s", True, YELLOW); surf.blit(enh_s, (8, 30))
        if self.player_sprite.has_fan(now):
            rem2 = max(0.0, self.player_sprite.fan_until - now)
            fan_s = self.font.render(f"Diagonal: {rem2:0.1f}s", True, YELLOW)
            surf.blit(fan_s, (8, 52))
        if self.paused:
            p = self.bigfont.render("PAUSED - P to resume, Q/Esc to quit", True, WHITE); surf.blit(p, p.get_rect(center=(WIDTH//2, HEIGHT//2)))
        if self.debug:
            dbg = self.font.render(f"Enemies:{len(self.enemies)} PB:{len(self.player_bullets)} EB:{len(self.enemy_bullets)} FX:{len(self.fx)}", True, GRAY); surf.blit(dbg, (8, HEIGHT-22))

def discover_level_files(level_dir=LEVELS_DIR):  # default now absolute
    files = []
    for p in glob.glob(os.path.join(level_dir, "level*.txt")):
        base = os.path.basename(p)
        try: num = int(''.join(ch for ch in base if ch.isdigit()))
        except ValueError: num = 9999
        files.append((num, p))
    files.sort(key=lambda x: (x[0], x[1]))
    return [p for _,p in files]

async def main_async():
    import argparse
    parser = argparse.ArgumentParser(description="1942-lite shooter")
    parser.add_argument("--level", type=int, default=1, help="Level number to start from (default: 1)")
    args = parser.parse_args()

    level_files = discover_level_files()
    if not level_files:
        print("No levels found in ./levels (expected level1.txt).")
        sys.exit(1)

    start_index = max(0, args.level - 1)
    if start_index >= len(level_files):
        print(f"Level {args.level} not found. Available: 1–{len(level_files)}")
        sys.exit(1)

    game = Game(level_files[start_index:])
    await game.run()

if __name__ == "__main__":
    asyncio.run(main_async())

```

### FILE: `requirements.txt`

#### Description

# `requirements.txt` Documentation

The `requirements.txt` file specifies the Python package dependencies required to run the project. It is used by `pip` to install all necessary libraries for development and execution.

---

## Overview

This file lists the external Python packages required by the game application. It ensures consistency across environments by pinning specific versions of dependencies.

---

## Key Dependencies

### 1. `pygame>=2.5.2`
- **Purpose**: Core library for game development in Python.
- **Features**:
  - Graphics rendering
  - Sound and music handling
  - Input device support (keyboard, mouse, etc.)
  - Collision detection
- **Version**: Minimum version `2.5.2` (latest stable recommended).

### 2. `pygbag`
- **Purpose**: Enables running Pygame applications in web browsers via WebAssembly (WASM).
- **Features**:
  - WebAssembly compilation for browser compatibility
  - Integration with Pygame's API for web deployment
- **Usage**: Required for building or running the game in a web environment.

---

## Usage Examples

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Verify Installation
```bash
pip show pygame pygbag
```

---

## Configuration Implications

- **Environment Setup**: Ensure Python 3.x is installed. The project uses `asyncio`, so a modern Python version (3.7+) is required.
- **Web Deployment**: `pygbag` is necessary for packaging the game as a web application. Without it, browser-based execution will fail.
- **Version Compatibility**: The pinned version of `pygame` ensures stability. Upgrading may require testing for compatibility.

---

## Relationship with Other Files

- **`main_async.py`**: Uses `pygbag` for async game loops and web deployment.
- **`build/version.txt`**: Tracks the project version (0.9.2), separate from dependency versions.
- **Game Logic**: Relies on `pygame` for all core mechanics (e.g., `PlayerSprite`, `Enemy`, bullet physics).

---

## Best Practices

- **Lock Versions**: Always use pinned versions in `requirements.txt` to avoid unexpected behavior from updates.
- **Environment Isolation**: Use virtual environments (`venv`) to manage dependencies per project.
- **Web Builds**: For web deployment, ensure `pygbag` is installed and configured correctly.

#### Source

```
pygame>=2.5.2
pygbag

```