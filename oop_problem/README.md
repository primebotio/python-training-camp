# Object Oriented Programming
The goal of this repo is to help new programmers get familiar with the concepts of Object Oriented Programming (**OOP**). In that direction, you are asked to solve the following problem in an OOP fashion.

### Problem Definition
Write a program that enables two players to have a game of Tic Tac Toe ( [like this](https://playtictactoe.org/) ) in a terminal session. Take care of the following:

 - enable two players to play the game and **do not** provide the option of playing against the computer
 - both players will be playing from **the same terminal session**.
 - use **python 3** to code your solution.
 - use **OOP** techniques to design the structure of your program.
 - provide the interface described in the following paragraph.

#### Interface
When the game starts, your program shall print a welcoming message and an empty board:
```
./tic_tac_toe.py
Hello! Welcome to ASCII Tic Tac Toe! 
Let the games begiiin!
   a     b     c
      |     |     
1  -  |  -  |  -  
 _____|_____|_____
      |     |     
2  -  |  -  |  -  
 _____|_____|_____
      |     |     
3  -  |  -  |  -  
      |     |     

#### Player 1 > 
```
The players then, provide in turns their movements using the following notation `<line><column>`. After each movement, the program should ask the next player to play:
```
   a     b     c
      |     |     
1  -  |  -  |  -  
 _____|_____|_____
      |     |     
2  -  |  -  |  -  
 _____|_____|_____
      |     |     
3  -  |  -  |  -  
      |     |     

#### Player 1 > 2b

   a     b     c
      |     |     
1  -  |  -  |  -  
 _____|_____|_____
      |     |     
2  -  |  x  |  -  
 _____|_____|_____
      |     |     
3  -  |  -  |  -  
      |     |     

#### Player 2 > 1a

   a     b     c
      |     |     
1  o  |  -  |  -  
 _____|_____|_____
      |     |     
2  -  |  x  |  -  
 _____|_____|_____
      |     |     
3  -  |  -  |  -  
      |     |     

#### Player 1 > 1c
     ...
```
You program must be able to **detect illegal movements** as well as **check if there is a winner**, and print a message accordingly: 
```
   a     b     c
      |     |     
1  o  |  -  |  x  
 _____|_____|_____
      |     |     
2  -  |  x  |  -  
 _____|_____|_____
      |     |     
3  -  |  -  |  o  
      |     |     

#### Player 1 > 1a

   a     b     c
      |     |     
1  o  |  -  |  x  
 _____|_____|_____
      |     |     
2  -  |  x  |  -  
 _____|_____|_____
      |     |     
3  -  |  -  |  o  
      |     |  
      
#### Player 1 ( illegal movement! ) > 4a

   a     b     c
      |     |     
1  o  |  -  |  x  
 _____|_____|_____
      |     |     
2  -  |  x  |  -  
 _____|_____|_____
      |     |     
3  -  |  -  |  o  
      |     |  
      
#### Player 1 ( illegal movement! ) > 3a

   a     b     c
      |     |     
1  o  |  -  |  x  
 _____|_____|_____
      |     |     
2  -  |  x  |  -  
 _____|_____|_____
      |     |     
3  x  |  -  |  o  
      |     |  

******** We have a winner!! Player 1 wins ********
      
```
Finally, When there is a winner, or the user enters `exit_game`, your **program should terminate**.

#### Bonus Features

##### 1) Better movement validator

Inform the user why his movement was illegal,as seen below:
```
   a     b     c
      |     |     
1  o  |  -  |  x  
 _____|_____|_____
      |     |     
2  -  |  x  |  -  
 _____|_____|_____
      |     |     
3  -  |  -  |  o  
      |     |     

#### Player 1 > 1a

   a     b     c
      |     |     
1  o  |  -  |  x  
 _____|_____|_____
      |     |     
2  -  |  x  |  -  
 _____|_____|_____
      |     |     
3  -  |  -  |  o  
      |     |  
      
#### Player 1 ( 1a is occupied )> 4a

   a     b     c
      |     |     
1  o  |  -  |  x  
 _____|_____|_____
      |     |     
2  -  |  x  |  -  
 _____|_____|_____
      |     |     
3  -  |  -  |  o  
      |     |  
      
#### Player 1 ( 4a is outside of board )>
```

##### 2) Support player names
In the beginning of each game, ask both users about their names and use them instead of `Player 1` and `Player 2`, and then decide **randomly** who plays first. In case there are no names provided, keep the names `Player 1` and `Player 2`.
```
./tic_tac_toe.py
Hello! Let the games begiiin!
Player 1, Name [o] > Jim
Player 2, Name [x] > George

   a     b     c
      |     |     
1  -  |  -  |  -  
 _____|_____|_____
      |     |     
2  -  |  -  |  -  
 _____|_____|_____
      |     |     
3  -  |  -  |  -  
      |     |     

#### George > 

```
##### 3) Don't rerun the program every time
After a win or a tie, give players the option to play the game again, as seen below:
```
#### Jim > 3a

   a     b     c
      |     |     
1  o  |  -  |  x  
 _____|_____|_____
      |     |     
2  -  |  x  |  -  
 _____|_____|_____
      |     |     
3  x  |  -  |  o  
      |     |  

******** We have a winner!! Jim wins ********
Play another one? [Y/n] > Y

Let the games begiiin!

   a     b     c
3      |     |     
1  -  |  -  |  -  
 _____|_____|_____
      |     |     
2  -  |  -  |  -  
 _____|_____|_____
      |     |     
3  -  |  -  |  -  
      |     |     

#### George > 

```

##### 4) Remember the players and their score:
Store and update each session's score, and give players the option to load their old score, like seen below:
```
./tic_tac_toe.py
Hello! Welcome to ASCII Tic Tac Toe!
1. Start a new game
2. Load an existing game
3. Exit
> 2
######### Stored Sessions #########
0. Session not in here
1. George vs Jim
2. Maria  vs Pascal
3. Anna   vs Eduard
> 2
====== Scoreboard ======
Maria                 4
Pascal                2
Ties                  7

Let the games begiiin!

   a     b     c
      |     |     
1  -  |  -  |  -  
 _____|_____|_____
      |     |     
2  -  |  -  |  -  
 _____|_____|_____
      |     |     
3  -  |  -  |  -  
      |     |     

#### Pascal > 
```

##### 5) Use your imagination
Feel free to implement additional features of your own :)


#### Enjoy !

