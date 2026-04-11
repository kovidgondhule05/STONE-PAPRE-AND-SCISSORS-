---

This program is a **console-based Stone–Paper–Scissors game** where the user can choose to play either with a **bot (computer)** or with a **friend**.

---

### 🔹 Game Start

* The program begins by printing a **welcome message** and the **rules of the game**.
* It then waits for the user to press **ENTER** to begin.

---

### 🔹 Mode Selection

* The user is asked to choose how they want to play:

  * With a **friend**
  * With a **bot**
* Based on the user’s choice, the program moves into the selected mode.

---

### 🔹 Bot Mode 🤖

* The computer randomly selects one option from:

  * stone
  * paper
  * scissors
* The user also enters their choice.
* Both choices are displayed.

#### Result Decision:

* If both choices are the same → **It’s a tie**
* Otherwise:

  * stone beats scissors
  * paper beats stone
  * scissors beats paper
* The winner is displayed accordingly.

---

### 🔹 Friend Mode 👥

* Two players take turns entering their choices.
* The program compares both inputs.

#### Result Decision:

* If both players choose the same → **Tie**
* Otherwise:

  * stone beats scissors
  * paper beats stone
  * scissors beats paper
* The program announces whether **Player 1** or **Player 2** wins.

---

### 🔹 Game End

* After showing the result, the program displays a **thank you message** and ends the game.

---

### ✅ Overall Description

This program:

* Simulates the classic **Stone–Paper–Scissors game**
* Supports both **single-player (bot)** and **two-player modes**
* Uses conditional logic to determine the winner
* Uses random selection for the bot’s move

