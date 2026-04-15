# Wordle-Command-Line
wordle played in the terminal, you need the 5 letter word folder
I built this to practice logic-based coloring and real-time input handling without using the standard input() function.

how it works
non-blocking input: I used the keyboard library to capture keystrokes instantly. This makes the game feel like a real app instead of a basic script where you have to hit 'Enter' after every single letter.

the algorithm: every time you submit a word, the game runs a comparison against the secret target word. It checks for exact matches (Green), character-only matches (Yellow), and misses (Grey).

dynamic keyboard: I built a "virtual keyboard" at the bottom of the screen that updates its colors as you play, so you can track which letters you've already burned.

technical wins
the backspace fix: handling the backspace key in a terminal is surprisingly annoying. I used the ANSI sequence \b \b to manually move the cursor back, delete the character, and reset the position so the UI doesn't break.

ansi color states: I used specific escape codes to handle the background colors for the tiles. I had to make sure the "Keyboard" state and the "Grid" state updated independently so the colors didn't bleed into each other.

coordinate mapping: used \033[H to ensure the game board always stays at the top of the terminal, even if the user resizes the window or scrolls.

what's next
I’m going back to refactor this Wordle game into classes to make the state management less messy.

