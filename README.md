# Conway's Game of Life

## Description
Implementation of John Conway's classic cellular automaton "Game of Life".

## Rules
- A live cell with 2-3 neighbors survives
- A live cell with <2 or >3 neighbors dies
- A dead cell with exactly 3 neighbors becomes alive

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python main.py
```

## Technologies
- Python
- Matplotlib for visualization
- Toroidal world topology