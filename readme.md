# Conway's Game of Life with Pygame

An interactive, visually sleek Python implementation of John Conway's famous cellular automaton, built using the `pygame` library.

---

## What is Conway's Game of Life?

Created by British mathematician John Horton Conway in 1970, the **Game of Life** is a zero-player game. This means that its evolution is determined entirely by its initial state, requiring no further human interaction. 

The "game" takes place on an infinite two-dimensional grid of orthogonal square cells. Each cell can be in one of two possible states:
* **Alive** (populated)
* **Dead** (unpopulated)

Every cell interacts with its eight neighbors (the cells that are horizontally, vertically, or diagonally adjacent). At each step in time (called a generation), the following transitions occur based on four simple rules:

1.  **Underpopulation:** Any live cell with fewer than two live neighbors dies.
2.  **Survival:** Any live cell with two or three live neighbors lives on to the next generation.
3.  **Overpopulation:** Any live cell with more than three live neighbors dies.
4.  **Reproduction:** Any dead cell with exactly three live neighbors becomes a live cell.

Despite having only four foundational rules, the Game of Life is **Turing complete**—it is capable of complex emergent behaviors, local patterns that move like organisms (gliders), stable structures (still lifes), and oscillating engines.

---

## What This Code Does

This specific Python implementation provides a fully interactive sandbox to explore Conway's Game of Life. Instead of generating a completely random or static board, it boots into a paused state allowing you to paint your own starting configurations.

### Key Technical Features

* **Interactive Grid Sandbox:** Using raw mouse event handling, you can left-click and drag to paint living cells, or right-click and drag to erase them dynamically.
* **Toroidal Grid (Edge Wrapping):** The edges of the screen are structurally connected. If a pattern wanders off the right side of the screen, it loops back seamlessly onto the left side, allowing for infinite-feeling simulations on a finite display.
* **Simultaneous Generation Updating:** To obey Conway's strict mathematics, the entire state of the board updates atomically. The script reads from a snapshot of the current frame and writes to a separate, blank buffer array before drawing to prevent calculation cascades.
* **Framerate Pacing:** The game uses `pygame.time.Clock` capped at a smooth but readable speed, allowing you to observe the generations changing without the simulation flashing by too quickly.

---

## Simulation Controls

Run the script and use these keyboard/mouse inputs to manage the window:

| Control | Action |
| :--- | :--- |
| **`Spacebar`** | Toggle Pause / Resume the simulation |
| **`Left-Click + Drag`** | Draw / Spawn living cells |
| **`Right-Click + Drag`** | Erase living cells |
| **`C` Key** | Instantly clear the entire grid (wipes board dead) |

---

## Requirements & Running

Ensure you have Python 3 and `pygame` installed:

```bash
pip install pygame
python conway_life.py