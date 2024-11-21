# tic-tac-toe

This repository serves to verify our digital electronic implementation of the [tic-tac-toe](https://arxiv.org/abs/2406.16801) game.

 Our electronic device consists of a 3x3 grid of three-way switches, and a 3x3 grid of LEDs. The switches are used to indicate the occupation of each tile (player 1, player 2, empty), and the LEDs are used to display the game state. When a win condition is met, the respective row, column, or diagonal is lit up with green lights, and all other lights are turned off. 

We define the input and output signals as follows:

* Inputs:
 * `iRij`: Boolean signal indicating whether player 1 (Red) has placed their mark at position (i,j)
 * `iBij`: Boolean signal indicating whether player 2 (Blue) has placed their mark at position (i,j)
 * where i represents the column {0,1,2} and j represents the row {0,1,2}:
   ```
   0,0 | 1,0 | 2,0
   ---------------
   0,1 | 1,1 | 2,1
   ---------------
   0,2 | 1,2 | 2,2
   ```

* Outputs:
 * `Rij`: Red LED at position (i,j)
 * `Bij`: Blue LED at position (i,j)
 * `Gij`: Green LED at position (i,j)
 * where i,j follow the same grid positions as inputs

We verify the following properties of our input and output signals:

1. If there is a winning configuration (three marks in a row, column, or diagonal) for either player, then all green LEDs in that line must be lit.

  Formally: For any winning line $L$ (row, column, or diagonal), let $iR_L$ and $iB_L$ be the inputs along that line and $G_L$ be the green LEDs along that line:
  $$
  \forall L: (iR_L[0] \land iR_L[1] \land iR_L[2]) \rightarrow (G_L[0] \land G_L[1] \land G_L[2])
  $$
  $$
  \forall L: (iB_L[0] \land iB_L[1] \land iB_L[2]) \rightarrow (G_L[0] \land G_L[1] \land G_L[2])
  $$

2. If all green LEDs in a line are lit and no other green LEDs are lit, then there must be a winning configuration (either all red or all blue) in that line.

  Formally: For any line $L$ and its complement $\bar{L}$ (all positions not in $L$):
  $$
  \forall L: (G_L[0] \land G_L[1] \land G_L[2] \land \lnot(\bigvee G_{\bar{L}})) \rightarrow 
      ((iR_L[0] \land iR_L[1] \land iR_L[2]) \lor (iB_L[0] \land iB_L[1] \land iB_L[2]))
  $$

3. When any green LED is on (indicating a win), all red and blue LEDs must be off.

  Formally: 
  $$
  (\bigvee_{i,j} G_{ij}) \rightarrow \lnot((\bigvee_{i,j} R_{ij}) \lor (\bigvee_{i,j} B_{ij}))
  $$

> **Note**  
> Our hardware implementation prevents a given tile from being occupied by more than one player, so we do not verify this property.