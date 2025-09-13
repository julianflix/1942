# 1942-lite — Top-Down Warplane Shooter (Pygame)

**What is new (v2):**
- PNG **sprites** supported for enemies and player (drop images into `assets/`).
- **Explosion animations** on kills (uses `assets/explosion_0..5.png` if available, otherwise procedural).
- **Multi-level** flow: `levels/level1.txt` → `levels/level2.txt` → ... (auto-discovery).

## Features
- **Top-down shooter** with warplane controls
- **Customizable sprites** for player and enemies
- **Animated explosions** on enemy elimination
- **Multi-level progression** with auto-discovered level files
- **Pause/Resume** and **debug mode** support
- **Safe Zone** mechanic for level completion
- **Cross-platform** with Pygame (Windows, macOS, Linux)

## API Calls
### Command-line Interface
```bash
python main.py --level 2
```
- `--level`: Start at a specific level (e.g., `--level 3`)

### Key Game Functions (Internal API)
- `Game.run()`: Starts the game loop
- `Game.next_level()`: Loads the next level file
- `Game.game_over()`: Handles game-over state
- `Game.win_and_exit()`: Handles win state and exits

## Components Overview
```
/project-root
  ├── main.py              # Entry point
  ├── requirements.txt   # Dependencies
  ├── assets/              # Sprite/animation files
  │   ├── player.png
  │   ├── enemy_shooter.png
  │   └── explosion_0.png...explosion_5.png
  ├── levels/              # Level configuration files
  │   ├── level1.txt
  │   └── level2.txt
  └── README.md          # This file
```

## Prerequisites
- Python 3.7+
- `pygame>=2.5.2` (installed via `pip install -r requirements.txt`)

## Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/1942-lite.git
cd 1942-lite

# Install dependencies
pip install -r requirements.txt
```

## Configuration
- **Level files**: Add `levels/levelX.txt` files following the ASCII format:
  - `S` = shooter enemy
  - `K` = kamikaze enemy
  - `B` = big enemy (or clustered letters)
  - `.` or space = empty cell
- **Assets**: Place PNGs in `assets/` for custom visuals. Missing assets use default shapes.

## How to Run
### Development
```bash
python main.py
```
### Production
```bash
python main.py --level 3
```

## Testing
- Run the game and verify:
  - Controls (arrow keys/WASD)
  - Bullet firing (space)
  - Level progression
  - Explosion animations
  - Safe zone detection

## Project Structure
```
├── main.py              # Game entry point
├── game.py              # Core game logic (Game class)
├── level_parser.py      # Level file parsing
├── assets/              # Sprite/animation assets
├── levels/              # Level configuration files
└── requirements.txt     # Dependency definitions
```

## Contribution Guidelines
1. Fork the repository
2. Create a new branch for features/fixes
3. Add new levels to `levels/` following the ASCII format
4. Submit a pull request with clear description
5. Follow PEP8 style guide for code

## License
**GNU General Public License v3.0**  
See `LICENSE` for full terms.  
This project is free software: you can redistribute it and/or modify it under the terms of the GNU GPL.