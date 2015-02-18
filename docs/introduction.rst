===========
Tic-Tac-Toe
===========

Tic-Tac-Toe is a classic, simple two-person strategy game.
On a square 3 × 3 squares wide playing field, the two players take turns placing their character (a player crosses the other circles) in an open field. 
The player who can put the first three characters in a row, column or diagonal wins. 
If both players play optimally, no one can win, and it comes to a draw. That is, all nine fields are filled without any player could set the required characters in a row, column or diagonal.

Steps
-----

First we create some global variables.
Then we define a function, that show witch player's turn and read the Input from the Player.
The next step is to define a function, that set the field which has the player selected and to check, if the field is already occupied or not.
At some point in time, the game should be ended, so we need to define a function that can stop the game or can return the winner.
To check, if there are three same symbols in a row, column or diagonal we need three functions to find it out.
The first function for the horizontal check.
The second function for the vertical check and the last for the diagonal check.
At the end we define who starts first.