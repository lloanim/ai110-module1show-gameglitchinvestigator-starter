# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
      - In this game you can guess a number from a certain range and certain number attempts depending on the difficulty chosen. There is a secret number that you need to guess and can have the option to have hints that direct you to guess lower or higher than your current guess. You lose 10 points as you use more attempts. If you guess in lower attempts you get a higher score.  

- [x] Detail which bugs you found.
      - I found four bugs where the hints gave opposite direction on where to guess. If you guessed high, it would tell you to guess even higher. If you guessed lower than the actual number, it would tell you to guess even lower. Another bug was where the score did not update correctly after each attempt and would give a negative score if in available attempts the secret number is not guessed. The third bug was that the range is not restricted to the different modes of easy, normal, and hard. The description is not changed on the different modes either. The last bug I found was that clicking on the Play Again button did not actually restart the game.  

- [x] Explain what fixes you applied.
      - I fixed the first bug by switching the text of "Go HIGHER" for lower and "Go Lower" for higher. The logic for this was generally correct except for when every even attempt it would make the guess a string rather an int causing an error in comparison between the guess and the secret. The second bug, I changed the part of the code where attempts was inizialized to 1 rather than 0 and fixed the formula for calculating points. A wrong guess of either "Too High" or "Too Low" are treated the same with a small penalty, but never letting the score go negative. The third bug I fixed by addding the difficulty to be set to certain difficulty when the secret number is generated. As well as changed the description to the difficulty range in each mode. For last bug I added blank states to secret, score, status, and history to effectively enter the restart of the game. 

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters 21 the output says "Guess must be between 1 to 20" (This depends on difficulty)
2. User enters 20 the output hint says "Go LOWER"
3. User enters 1 the output hint says "Go HIGHER"
4. User enters 10 the output says "You won! The secret was 10. Final score: 60"
5. The score works by updating after each attempt. (In example was 6 attempts on easy mode)
6. Click on "New Game" button restarts the game.

**Screenshot** *(optional)*: <img src="./assests/Screenshot 2026-06-20 at 4.46.41 PM.png/" /> <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

tests/test_game_logic.py ................                                                                [100%]

============================================== 16 passed in 0.09s ==============================================

## 🚀 Stretch Features

- [x] Challenge 1: Where the AI had provided seven tests to verify the function parse_guess functionality after fixing a bug. The range restictions based on difficulty did not work. I asked it to create pytests to verify its functionalty which correlated to tests for challenge 1. It added a test for inclusive bounds, a test for below range, a test above range, a test non-numerical, an empty guess, and a float guess. I then asked to added another test to verify negative numbers work as well. 
