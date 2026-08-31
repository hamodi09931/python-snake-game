# 🐍 Python Snake Game

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success.svg)](https://github.com/hamodi09931/python-snake-game)
[![Turtle Graphics](https://img.shields.io/badge/Graphics-Turtle-orange.svg)](https://docs.python.org/3/library/turtle.html)

A classic Snake game built with Python's Turtle graphics module. Control the snake with arrow keys, eat food to grow, and avoid hitting walls or your own tail!

## ✨ Features

- 🎮 **Arrow key controls** - Smooth and responsive gameplay
- 🍎 **Random food generation** - Unpredictable food placement
- 📊 **Score tracking** - Keep track of your progress
- 🧱 **Wall collision detection** - Game ends when hitting boundaries
- 🐍 **Self-collision detection** - Game ends when snake hits itself
- 🎯 **Simple and clean game loop** - Easy to understand and modify
- 🎨 **Enhanced UI** - Beautiful colors and smooth animations

## 📋 Requirements

- Python 3.8 or newer
- Turtle module (included with Python)

## 🚀 How to run

```bash
python main.py
```

## 🎮 Controls

| Key | Action |
|-----|--------|
| ⬆️ Up Arrow | Move Up |
| ⬇️ Down Arrow | Move Down |
| ⬅️ Left Arrow | Move Left |
| ➡️ Right Arrow | Move Right |

## 📁 Project Structure

```
snake-game/
├── main.py           # Main game loop and initialization
├── snake.py          # Snake class and movement logic
├── food.py           # Food spawning and positioning
├── score.py          # Score tracking and game over display
├── rong.py           # Collision detection logic
├── .gitignore        # Git ignore rules
└── README.md         # This file
```

## 🎨 Game Features

- **Snake**: Starts with 3 segments, grows when eating food
- **Food**: Randomly spawned on the game grid
- **Scoring**: +1 point for each food eaten
- **Game Over**: Triggered by wall collision or self-collision
- **Colors**: Dark theme with contrasting UI elements

## 🛠️ Customization

You can easily customize the game by editing:
- Screen size in `main.py` (default: 600x600)
- Game speed by adjusting `time.sleep()` value
- Colors in `snake.py`, `food.py`, and `score.py`
- Game grid boundaries

## 📝 License

This project is for educational purposes.
MIT License - Feel free to use and modify!

## 👨‍💻 Author

Created as a Python learning project.

---

**Enjoy the game! 🎮**
