# 1942-lite

A WWII top-down shooter built with Python and portable to the web using **pygbag**.

## What is 1942-lite?

**1942-lite** is a modern, lightweight arcade shooter inspired by classic vertical scrollers. Pilot your plane through waves of enemy fighters, dodge bullets, collect power-ups, and reach the **Safe Zone** to clear each level. The game runs on desktop via **Pygame** and can be exported to the browser via **pygbag** (WASM), so it can be played without local installation.

---

## Features

- **Classic vertical-scrolling gameplay** with waves of enemies
- **Power-ups**: Health, Ammo, Enhanced (spread/rapid fire), Fan (diagonal movement)
- **Level progression** via text-based maps in `levels/`
- **Cross-platform support**:
  - **Desktop**: Keyboard (WASD/Arrow Keys) + Space for shooting
  - **Web/Mobile**: Virtual joystick + fire button
- **Web deployment** via `pygbag` (WASM)
- **Modular architecture** for easy expansion

---

## API Calls

### Command-line Arguments
- `--level N`: Start from a specific level (e.g., `--level 3`)
  ```bash
  python main.py --level 3
  ```

### Game Class Methods
- `Game.run()`: Starts the game loop
- `Game.load_level(level_path)`: Loads a level from a file

---

## Project Components

1. **`main.py`**: Entry point for the game. Handles CLI args and initializes the `Game` class.
2. **`Game` class**: Manages game state, rendering, input, and level progression.
3. **`requirements.txt`**: Lists dependencies for desktop and web builds.
4. **`assets/`**: Contains sprites, backgrounds, and sound effects.
5. **`levels/`**: Text-based level maps (e.g., `level1.txt`).

---

## Prerequisites

- Python 3.x (tested with 3.8+)
- Basic knowledge of Python and virtual environments

---

## Installation

1. **Create a virtual environment**:
   ```bash
   python -m venv venv_1942
   ```

2. **Activate the environment**:
   - Windows:
     ```bash
     venv_1942\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv_1942/bin/activate
     ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Configuration

- **Levels**: Autodiscovered from `levels/` directory. Use `--level N` to select a specific level.
- **Assets**: Place PNGs in `assets/` for custom visuals. Missing assets use simple fallbacks.
- **Web Deployment**: Ensure `assets/` and `levels/` are hosted alongside the `build/web/` directory. Demo: https://julianflix.com/1942/index.html

---

## How to Run

### Desktop (Development)
```bash
python main.py
```
Start from a specific level:
```bash
python main.py --level 3
```

### Web (Production)
1. **Build the web version**:
   ```bash
   python -m pygbag .
   ```
2. **Host the output**:
   - Place `build/web/`, `assets/`, and `levels/` in the same directory.
   - Open `build/web/index.html` in a browser.

---

## Project Structure

```
assets/              # Sprite/background images
  background1.png
  player.png
levels/              # Level map files (e.g., level1.txt)
README.md            # This file
main.py              # Game entry point
requirements.txt     # Dependencies
```

---

## Testing

- **Unit tests**: Not included in the current release. Contributions welcome!
- **Manual testing**: Play the game locally or in a browser to verify functionality.

---

## Contribution Guidelines

- **Open issues** for bugs or feature requests.
- **Submit pull requests** for improvements.
- Follow the **GNU GPL v3.0** license for all contributions.

---

## License

**GNU General Public License v3.0**  

See the [LICENSE](LICENSE) file for details.
