# Snake Game - README

## Project Overview
The **Snake Game** is a Python project with a graphical user interface (GUI) developed using the **Turtle** library. In this game, the player controls a snake that moves around the screen, eating randomly spawning food and growing longer. The objective is to eat as much food as possible without hitting the borders or the snake's own tail.

## Features
- **Food Class**:  
  - Creates a circle-shaped food item that spawns at random coordinates on the screen.
  - When the snake eats the food, it randomly spawns at a new location.
  
- **Snake Class**:  
  - Controls the snake's movement and growth. 
  - Each time the snake eats food, a segment is added, and the speed increases.
  - Movement is controlled using the `onkey` method for smooth keyboard input.
  
- **Scoreboard Class**:  
  - Tracks and displays the player's current score as they eat the food.
  - If the snake hits the border or its own tail, the score resets and starts from zero.
  
- **Highscore Persistence**:  
  - A file is used to save and load the **highscore**. The highscore remains stored across multiple sessions using Python's `file open/close` method.

## How It Works
1. **Movement**: Control the snake using the keyboard to navigate the screen.
2. **Eating Food**: The snake grows longer and faster each time it eats food.
3. **Score Tracking**: The current score is updated as the snake eats food, and a separate highscore is maintained.
4. **Game Over**: The game resets if the snake hits the wall or collides with its tail, but the highscore remains intact.

## Dependencies
- **Python 3.x**
- **Turtle** (Standard with Python)

## Installation
1. Clone the repository or download the project files.
2. Ensure Python 3.x is installed on your system.
3. Run the main Python script to start the game:

```bash
python main.py
```

## Usage
- Use arrow keys to control the snake’s movement.
- The game will keep track of your score and highscore, which is saved in a file for future game sessions.

## Future Enhancements
- Add different difficulty levels (speed variations).
- Implement different snake skins and food types for variety.
- Introduce sound effects and background music.

---
