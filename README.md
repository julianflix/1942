# 1942-lite Shooter Game

A 2D shooter game inspired by classic arcade titles, featuring multiple levels, power-ups, and web compatibility.

---

## What is This Project?

This is a 2D shooter game developed using Python's `pygame` library, with support for web deployment via `pygbag`. The game features scrolling levels, enemy waves, player upgrades, and a "safe zone" mechanic. It is designed to be simple, fast-paced, and compatible with both desktop and web environments.

---

## Key Features

- **2D Shooter Gameplay**: Classic side-scrolling action with player movement, shooting, and collision detection.
- **Multiple Levels**: Progress through a series of levels, each with unique enemy patterns and challenges.
- **Power-Ups**: Collect items like health, ammo, enhanced abilities, and diagonal movement.
- **Safe Zone**: Reach the bottom of the screen to progress to the next level or win.
- **Web Compatibility**: Run the game in a browser using `pygbag` (WebAssembly).
- **Modular Design**: Clean separation of game logic, rendering, and input handling.

---

## API Calls (if applicable)

This project does not expose public API endpoints. It is a self-contained game application with internal functions for game mechanics, level loading, and rendering.

---

## How Components Fit Together

- **Main Loop**: `main_async.py` orchestrates the game loop, handling async operations and event processing.
- **Game Logic**: The `Game` class manages levels, player state, enemies, bullets, and power-ups.
- **Rendering**: `pygame` handles graphics, with the `render` method drawing all game elements.
- **Level System**: `discover_level_files` loads level data from text files, enabling easy expansion.
- **Web Support**: `pygbag` allows the game to run in web browsers via WebAssembly.

---

## Prerequisites

- Python 3.7+
- `pygame>=2.5.2` (for game mechanics)
- `pygbag` (for web deployment)
- `asyncio` (for asynchronous operations)

---

## Installation

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Prepare Level Files**:
   - Place level files (e.g., `level1.txt`) in the `levels/` directory.

---

## Configuration

- **Level Files**: Add new levels as `levelX.txt` files in the `levels/` directory.
- **Command-Line Arguments**:
  - Start at a specific level:  
    ```bash
    python main_async.py --level 3
    ```

---

## How to Run

### Development Mode
```bash
python main_async.py
```

### Web Deployment
Ensure `pygbag` is installed, then build and run the game in a browser.

---

## Testing

- **Manual Testing**: Run the game and verify gameplay mechanics (movement, shooting, collisions).
- **Unit Tests**: Add test cases for game logic (e.g., level loading, power-up effects).

---

## Project Structure

```
/levels/              # Level data files (level1.txt, etc.)
/main_async.py        # Entry point and game loop
/requirements.txt      # Dependency list
/LICENSE              # License file
README.md              # This file
```

---

## Contribution Guidelines

- **Add Levels**: Create new `levelX.txt` files for additional content.
- **Enhance Mechanics**: Improve gameplay features like enemy AI or power-ups.
- **Submit PRs**: Follow the project structure and add tests for new features.

---

## License

**GNU General Public License v3.0**  
See the [LICENSE](LICENSE) file for details.