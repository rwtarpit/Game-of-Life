# Conway's Game of Life 

An interactive, visually sleek Python implementation of John Conway's famous cellular automaton, built using the `pygame` library.

---

## Github Repository

https://github.com/rwtarpit/Game-of-Life

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

## Demo

![Demo Video](assets/demo.mp4)

---

## What This Code Does

This Python implementation provides a fully interactive sandbox to explore Conway's Game of Life. Instead of generating a completely random or static board, it boots into a paused state allowing user to initiate starting configurations. By means of pygame, state of all cells are atomically updated over the iterations with variable defined rendering speed. 


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
python life_game.py