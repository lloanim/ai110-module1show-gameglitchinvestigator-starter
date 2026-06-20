# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
    When I first ran the game it told me that my guess of 40 should be higher. My next input was 50 telling me to guess higher when it should have been lower. The next input was 80 again telling me to guess higher. When I inputed 100 it told me to guess higher again. On my last attempt I guessed 135 and thats when it told me to go guess lower and revealed that the number was actually 38. Giving me a score of -5 on easy mode.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
    -- The hints kept telling me to guess higher when at my second attempt should have said for me to guess lower. 
    -- The score is negative after not being able to guess the number
    -- Does not allow for you to actually start the game over
    -- As the level changes from easy to hard the instructions of range stays the same when it changed from 
       one to the other 
    -- The attempts are not the same from the settings to the instruction like the range
    -- The input does not register immediately only until you click the screen again. Leading you to 
       believe you have more tries left when you have one less before you guess again. 


**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input           | Expected Behavior   |      Actual Behavior     | Console Output / Error |
|-----------------|---------------------|--------------------------|------------------------|
| guess of 40 but |  "Go LOWER" hint    |   "Go HIGHER" hint shown |         none           |
| answer is 38    |                     |                          |                        |
|-----------------|---------------------|--------------------------|------------------------|
| Did not guess   |                     |                          |                        |
| the number in   |   Total score of    |      Total score of      |          none          |
| available       |        zero         |            -5            |                        |
|  attempts       |                     |                          |                        |
|-----------------|---------------------|--------------------------|------------------------|
| last guess of   |  Not accept number  |   "Go LOWER" hint shown  | "Out of attempts!" The |
| 135 on easy mode| not in range of 1-20|                          | secret was 38. Score -5|
|-----------------|---------------------|--------------------------|------------------------|
| Clicked on      |   Game resets       |    Nothing happens       |        none            |
| Play Again      |                     |  stuck on last game      |                        |
|-----------------|---------------------|--------------------------|------------------------|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
    -- I used Claude AI

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
    -- A correct suggestion was that the logic of the hint was correct it was just the text that had it backwards. It mentioned that "Too High" had been paired with "Go HIGHER" when it should be "Go LOWER" and the same with the "Too Low" paired wrongly with "Go HIGHER" instead of "Go LOWER". In the same prompt it noticed that on even outputs the secret would be typecasted as a string. Which caused an underlying error of comparision of string numbers (lexicographically) instead of numerically causing false comparsion / output of hints.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
    -- I had commented a FIXME for if new_game where I was confused as to what exactly the rerun does. It was able to explain to me well and answer my concern of the guesses not clearing for a new game. There it explained that the rerun does not deal with this but rather missing code that makes the game actually start the game over again. Here it suggested to put "st.session_state.attempts = 1". I tried it by playing the game and noticed that attempts had 1 instead of 0 at the beggining. So I asked it again why it had suggested 1 instead of the original form of 0. It stated because of this line "points = 100 - 10 * (attempt_number + 1)" where it was adding 1. On asking to see the suggested changes I realized another bug where "if "attempts" not in st.session_state:" had attempts at 1. This was causing the main issue so I changed it to 0 and fixed the points formula. I played the game again and the results looked better. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
