# 1942-lite

A WWII top-down shooter built with Python and portable to the web using **pygbag**.

## Description

**1942-lite** is a modern, lightweight arcade shooter inspired by classic vertical scrollers. Pilot your plane through waves of enemy fighters, dodge bullets, collect power-ups, and reach the **Safe Zone** to clear each level. The game runs on desktop via **Pygame** and can be exported to the browser via **pygbag** (WASM), so it can be played without local installation.

## Features

- Classic vertical-scrolling shooter gameplay with waves and simple AI
- Power-ups: **health**, **ammo**, **enhanced** (spread/rapid), **fan** (diagonal)
- Level progression from text-based maps in `levels/`
- Desktop (keyboard) and mobile/web (virtual joystick + fire button) support
- Portable to web using **pygbag**

## Getting Started

### Prerequisites

- Python 3.x installed on your system
- Basic familiarity with Python and virtual environments

### Installation

1. Create a Python virtual environment:
   ```bash
   python -m venv venv_1942
   ```

2. Activate the virtual environment:
   - On Windows:
     ```bash
     venv_1942\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv_1942/bin/activate
     ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Playing the Game

### Local Play (Desktop)

Run the game locally after installing dependencies:

```bash
python main.py
```

Start from a specific level (e.g. level 3):

```bash
python main.py --level 3
```

### Controls (Desktop)

- **Move**: Arrow Keys or **W/A/S/D**
- **Shoot**: **Space**
- **Pause / Resume**: **P**
- **Quit**: **Esc** or **Q**
- **Debug overlay**: **F1** (toggles)

### Controls (Web/Mobile)

- **Left thumb**: Virtual joystick (bottom-left)
- **Right thumb**: Fire button (bottom-right)

## Web Play (Browser via pygbag)

To build and run the game in a web browser:

1. **Install pygbag** (inside your virtual environment, if not already installed):
   ```bash
   pip install pygbag
   ```

2. **Build the web bundle** from the project root:
   ```bash
   python -m pygbag .
   ```
   This generates a `build/web/` folder containing `index.html`, the WASM runtime, and compiled assets.

3. **Publish static files**. For the browser build to find game data, place the following **side-by-side** on your web host or static server:
   ```
   /your-host-root/
     ├─ build/
     │  └─ web/          <-- web bundle (contains index.html)
     ├─ assets/          <-- image/sprite PNGs used by the game
     └─ levels/          <-- levelX.txt files used by the game
   ```
   The game expects `assets/` and `levels/` at the same level as `build/web/` (relative paths are used on the web).

4. **Open `build/web/index.html`** in your browser (or deploy the folders to a static host and visit the deployed URL).

> Tip: When testing locally in a browser, serve the directory with a simple HTTP server to avoid cross-origin issues (e.g., `python -m http.server` from the host root shown above).

## Project Structure

```
build/
  version.txt          # current game version (e.g., 0.9.2)
levels/
  level1.txt …         # text-based level layouts
README.md
main.py                # game entry point
requirements.txt
```

## Configuration

- **Levels Directory**: `levels/`  
  Level files are autodiscovered (e.g., `level1.txt`, `level2.txt`, …).  
  Use `--level N` to start from a specific level.

- **Assets Directory**: `assets/`  
  Contains optional PNGs for player/enemies/backgrounds. If missing, the game draws simple fallbacks so it still runs.

## Version

The current version is tracked in **`build/version.txt`** (e.g., `0.9.2`).

## Deployment

For a complete web deployment, upload **both**:
- The contents of `build/web/` (including `index.html`)
- The `assets/` and `levels/` folders (kept as siblings of `build/web/`)

Maintaining these relative paths ensures the browser build can load images and level files.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is released under the **GNU GPL v3.0**. See the `LICENSE` file for details.

## Acknowledgments

- Inspired by classic 1942-style vertical shooters  
- Built with Python’s **Pygame** and the **pygbag** framework for web portability
