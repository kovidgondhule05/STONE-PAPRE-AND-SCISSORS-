## 🔹 1. Welcome & Rules

```python
print("WELCOME TO THE GAME...")
```

* Displays the game title and rules
* Tells the user:

  * Don’t use CAPS
  * Press ENTER to confirm choice
  * No changing input
  * Spell correctly

```python
input()
```

* Waits for user to press ENTER before starting

---

## 🔹 2. Mode Selection

```python
p = input("with whom do you want to play...")
```

User chooses:

* `"bot"` → play with computer 🤖
* `"freind"` (or anything else) → play with another player 👥

---

## 🔹 3. Bot Mode 🤖

```python
if(p == 'bot'):
```

### 📦 Setup

```python
import random
list = ['stone', 'paper', 'scissors']
```

* Uses `random` module
* Stores possible choices

---

### 🎮 Player & Bot Moves

```python
you = input(...)
bot = random.choice(list)
```

* Player enters their move
* Bot randomly selects one

---

### ⚖️ Result Logic

```python
if(you == bot):
```

* Same choice → **Tie**

Winning conditions:

* stone beats scissors
* paper beats stone
* scissors beats paper

If none match → bot wins

---

## 🔹 4. Friend Mode 👥

```python
else:
```

### 🎮 Inputs

```python
player1 = input(...)
player2 = input(...)
```

* Two players enter choices

---

### ⚖️ Result Logic

* Same choice → Tie
* Player 1 wins if:

  * stone > scissors
  * paper > stone
  * scissors > paper
* Otherwise → Player 2 wins

---

## 🔹 5. Ending

```python
print("!!!THANKS FOR PLAYING!!!")
```

* Shows game over message

---

## ✅ What’s Good in Your Code

✔ Correct game logic
✔ Bot using `random`
✔ Clean if-elif conditions
✔ Supports both modes

---

3. **Using `list` as variable name**

   * `list` is a built-in Python keyword

   ✅ Better:

   ```python
   choices = ['stone', 'paper', 'scissors']
   ```

---

## 💡 Suggested Improved Version (Short Fix)

```python
choices = ['stone', 'paper', 'scissors']
you = input("YOUR TURN ---> ").lower()
```
