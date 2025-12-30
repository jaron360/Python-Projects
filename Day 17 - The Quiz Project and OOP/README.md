# True/False Quiz Game

A Python-based interactive quiz game that tests your knowledge with interesting true/false questions. The game presents a series of fascinating facts and tracks your score as you progress through the quiz.

## Overview

This quiz game features 27 carefully curated true/false questions covering topics like:
- Animal facts and biology
- Historical events and figures
- Science and nature
- Geography and culture
- Fun and unusual trivia

The game provides immediate feedback after each question and displays your running score throughout the quiz.

## Features

- **Interactive Gameplay**: Answer true/false questions in the terminal
- **Score Tracking**: Real-time score updates after each question
- **Immediate Feedback**: Learn the correct answer after each question
- **Progress Tracking**: See how many questions you've completed
- **Final Results**: Get your total score at the end

## How to Play

1. Run the program
2. Read each question carefully
3. Type "True" or "False" (case insensitive)
4. See if you got it right and learn the correct answer
5. Continue until all questions are completed
6. View your final score

## Project Structure

```
quiz-game/
├── main.py           # Main game loop and program entry point
├── quiz_brain.py     # QuizBrain class - handles game logic
├── question_model.py # Question class - models individual questions
├── data.py          # Question database with all quiz questions
└── README.md        # This file
```

## Classes and Components

### Question Class (`question_model.py`)
- Models individual quiz questions
- Stores question text and correct answer

### QuizBrain Class (`quiz_brain.py`)
- Manages the quiz flow and game state
- Tracks current question number and score
- Handles user input and answer checking
- Provides feedback and scoring

### Question Data (`data.py`)
- Contains 27 true/false questions
- Each question includes text and correct answer
- Covers diverse topics for engaging gameplay

## Sample Questions

- "A slug's blood is green." (True)
- "The Great Wall of China is visible from space with the naked eye." (False)
- "Octopuses have three hearts." (True)
- "Honey never spoils." (True)

## Example Gameplay

```
Q.1: A slug's blood is green. (True or False?) True
You got the correct answer
Current score: 1/1
The correct answer was True

Q.2: The loudest animal is the African Elephant. (True or False?) True
You got wrong answer
Current score: 1/2
The correct answer was False

...

You have completed the quiz
Your final score is 18/27
```

## Requirements

- Python 3.x
- No external libraries required

## How to Run

1. Ensure all four Python files are in the same directory
2. Run the main program:
   ```bash
   python main.py
   ```
3. Follow the prompts to answer each question
4. Complete all questions to see your final score

## Learning Objectives

This project demonstrates:
- Object-oriented programming with multiple classes
- Class interaction and method calls
- List iteration and data management
- User input handling and validation
- Game state management
- Modular code organization

## Educational Value

Perfect for:
- Learning Python OOP concepts
- Understanding class design and interaction
- Practicing with lists and loops
- Building interactive console applications
- Exploring modular programming structure
