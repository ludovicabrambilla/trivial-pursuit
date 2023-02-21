# Trivia quiz game

Trivia like Python quiz game (2 to 6 players) built for Codecademy "Computer Science - Career Path".
The project is an application of the concepts learnt through the first module of the course, which covers basic elements of Python, from the introduction to programming to the first elements of OOP.
________

## Table of contents
1. [Acknowledgements](#acknowledgements)
2. [Disclaimer](#disclaimer-this-is-a-learning-project)
3. [How to play](#how-to-play)

    a. [General rules](#general-rules)

    b. [Initialize the game](#initialize-the-game)

    c. [Play](#play)
4. [Project structure and features](#project-structure-and-features)

    a. [Course prompt](#course-prompt)

    b. [Built to be enhanced](#built-to-be-enhanced)

    c. [Elements of the game](#elements-of-the-game)

5. [Upcoming](#upcoming)
_________
## Acknowledgements
### Code structure and development
- [Codecademy](https://join.codecademy.com/learn/paths/computer-science/)
- [Real Python](https://realpython.com/python-quiz-application/#step-3-organize-your-code-with-functions)
### Trivia questions
 - [All categories trivia questions](https://www.opinionstage.com/blog/trivia-questions/)
 - [Geography trivia questions](https://parade.com/1246355/marynliles/geography-trivia/)
 - [History trivia questions](https://www.rd.com/list/history-questions/)
 - [Sports trivia questions](https://triviahat.com/sports-trivia-questions/#:~:text=Sports%20Trivia%20Questions%201%201.%20What%20sport%20features,used%20in%20which%20team%20sport%3F%20...%20Altri%20elementi)


## Disclaimer: this is a learning project!
This project does not have any distribution purposes. It is just a learning project, created to practice concepts learnt through the First module of [Codecademy's Computer Science Career Path](https://join.codecademy.com/learn/paths/computer-science/).

The Module covers the basics of Programming in Python, such as:
- variables
- functions
- data types
- modules and pip
- Object Oriented Programming (classes and methods)

The course also gives an overview of some tools the programmer might need in the development process, such as:
- [Git](https://git-scm.com/)
- [GitHub](https://github.com/) 

To further learn about these tools, I took [Codecademy's course](https://www.codecademy.com/learn/learn-git) on the topic.

Based on these premises, the project may evolve according to the new competences I progressively acquire in my software development journey.

Check out any upcoming feature or update in the [Upcoming](#upcoming) section of this file.

## How to play

### General rules
If you are not familiar with the Trivia board game, here are some basic rules.

There are **from 2 to 6 players** (or teams). Each player **rolls a die and gets on a square**. Each square of the board has an **assigned color**, which corresponds to a **category**. There are *6 colors in total*, which means 6 categories of questions.

Once the player is on the square, he/she gets **asked a question of the square category**. If the player gives the wrong answer, the turn passes to the following player. However, if the player gives the right answer he/she keeps on playing (meaning, roll the die, answer the question). 

To **earn a point**, the player must go on one of the **special squares** of the board and **answer the question correctly**. Each special square belongs to a category.

Once the player has collected **all the six points** from the special squares, the player **can to try to win**, by going on the start square (rolling the die) and answering a **final question**. If the player gets it right, he/she wins the game. Otherwise, the game continues until one player wins.

### Initialize the game
Go to the [main](./main.py) file and run it. 

The game will ask you how many players you want to create (from 2 to 6, included) and will ask you to choose a name and a token color for each of them.

Then, the order of the players will be determined automatically by the game.

The game has a board. Each square in the board has a color. Each color represents a category. The default categories are:
- *Geography* - **blue**
- *History* - **yellow**
- *Sports & Leisure* - **orange**
- *Entertainment* - **pink**
- *Arts & Literature* - **brown**
- *Science & Nature* - **green**

The board has also a **start** square and **roll again** squares. 

The **start square and other 6 squares** around the board are *special squares* (they can assign points to the player).

### Play
After the initialization is complete, you can start playing.

The game will **automatically roll the die** for the player and **ask a question of the corresponding category**.
The player can input an asnwer from the options provided.

If the **answer is correct**, the game will **keep rolling the die and ansking questions** to the player until he/she gets an answer **wrong**. When this happens, the **turn is passed** to the following player.

If by rolling the die, the player **gets on a special square**, the game will **notify the player** that he/she is playing to get a point (with the message *"You play for a token!"*). Therefore, if the player answers that question correctly, he/she **gets a point** for the question category.

Once a player has **collected all 6 points** (one in each category), he/she can **try to win**. To do so, the player must try to go on the start square, choose a category and answer correctly.

The game **goes on until one player wins**.


## Project structure and features

### Course prompt
The course asked to build a basic terminal game to play with friends and family, written in Python.

### Built to be enhanced
The project has been written considering not just the actual features, but also the potential new features coming in the future.

### Elements of the game
The game recalls the famous Trivial Pursuit board game. In this version, I tried to reproduce the standard version of the game.

The classes are:
- [Player](#player) (check the code [here](./player.py))
- [Board](#board) (check the code [here](./board.py))
- [Game](#game) (check the code [here](./game.py))

Other files you see in the project are:
- [Questions](./questions.py) , where the questions and answers asked through the game are stored
- [Main](./main) , which is the file to run to play the game

#### Player
Check the player implementation [here](./player.py)!

You can create **from 2 to 6 players**. When the game starts, the user is asked how many players he/she wants to create within this range.

Each player must then **choose a name and a token** (by color).

The player has some instance features that mark its position (eg: on a special square or on the start square) that are necessary for the points assignment throughout the game.

#### Board
Check the board implementation [here](./board.py)!

The board stores the colors of the squares, a dictionary mapping the squares and the respective colors and a list of the "special squares" (meaning the squares where the Player can obtain a point).

In this implementation, the board is not visually represented. Check the [Upcoming](#upcoming) features for future developments.

#### Game
Check the game implementation [here](./game.py)!

The Game class controls the development of the game. It keeps track of:
- the players and their movements
- the board
- the questions and their categories

As for the methods, the Game:
- asks the questions to the assigned player
- gets his/her answer
- checks if the answer is correct or incorrect
- assigns a point to the player, checks if he/she won the game or passes the turn to the other player.

### Questions
Check the questions file [here](./questions.py)!

The file holds the categories and the questions for each of them.

The categories are provided in a separated list.

The questions are stored as nested dictionaries. The first level maps the categories (keys) to a dictionary of questions (values). The second level maps each question (keys) to a list of possible answers (values).

### Main
Check the code [here](./main.py)!

As you can see, in this implementation, the main file holds very few lines of code, which instantiate a Game object. 

However, you can customize it! For example, you can create a tournament of different matches, each represented by a Game object.


## Upcoming

### User interface
Once detached the project from the course purposes, I plan on building a more appealing graphic interface for the player, with a visual representation of the board. 

This will allow me to replicate the movement of the player across the board and the rolling of the die.

### Customization
I would like to give the opportunity to the user to build its own game. The colors will be constants, but the associated categories and questions can be written by the player.

### Limited editions
Among the various versions of the game, there are several which are addressed to a younger audience (eg: Disney version, Easy version, etc.). I woul like to replicate these, in order to offer a wider choice to the player, and maybe use it in family gatherings!

### Data Structures and DB
This is a more technical aspect, but I plan on enhancing the structure of my code, making it progressively more clean and efficient as long as I learn new programming concepts. 

I would also like to create an underlying database system, in order to manage mutiple users, questions, games, etc.

