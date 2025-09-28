# snake_game_cli

A command-line implementation of the classic Snake game written in Python.

## Features

- Play the classic Snake game directly in your terminal.
- Simple, lightweight, and easy to run.
- No external dependencies required except Python and modules listed in `requirements.txt`.

## Technologies Used

- **Python** (3.x recommended)
- **asyncio** (for asynchronous game loop)
- **random** (for food placement)
- **pynput** (for keyboard input handling)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ramimK0bir/snake_game_cli.git
   cd snake_game_cli
   ```

2. **Install the requirements:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the game:**
   ```bash
   python snake_game.py
   ```

   You can optionally set the snake's speed using the `--speed` argument (default is 2):
   ```bash
   python snake_game.py --speed 5
   ```

## Gameplay

- Use arrow keys to control the direction of the snake.
- Eat food to grow longer.
- Avoid hitting the walls or the snake's own body.

## License

This project is licensed under a custom Non-Commercial License based on the MIT License. See [LICENSE](./LICENSE.txt)
 for details.

---

Enjoy playing Snake in your CLI!
