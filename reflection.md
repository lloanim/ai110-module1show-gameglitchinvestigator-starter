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
    -- A correct suggestion was that the logic of the hint was correct, it was just the text that had it backwards. It mentioned that "Too High" had been paired with "Go HIGHER" when it should be "Go LOWER" and the same with the "Too Low" paired wrongly with "Go LOWER" instead of "Go HIGHER". In the same prompt it noticed that on even outputs the secret would be typecasted as a string. Which caused an underlying error of comparision of string numbers (lexicographically) instead of numerically causing false comparsion / output of hints. I verified this after I took out the parts of the code that typecasted the guess to string on even attempts and the worked well. The tests pass as well after I changed it to accept the int rather than the string. 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
    -- I had commented a FIXME for if new_game where I was confused as to what exactly the rerun does. It was able to explain to me well and answer my concern of the guesses not clearing for a new game. There it explained that the rerun does not deal with this but rather missing code that makes the game actually start the game over again. Here it suggested to put "st.session_state.attempts = 1". I tried it by playing the game and noticed that attempts had 1 instead of 0 at the beginning. So I asked it again why it had suggested 1 instead of the original form of 0. It stated because of this line "points = 100 - 10 * (attempt_number + 1)" where it was adding 1. On asking to see the suggested changes, I realized another bug where "if "attempts" not in st.session_state:" had attempts at 1. This was causing the main issue so I changed it to 0 and fixed the points formula. I played the game again and the results looked better, it also passes the tests.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
    -- I decided a bug was really fixed when it passes the tests but also testing it out myself the game. I tried it on the three different modes.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
    -- One test I ran using pytest was test_hint_direction_matches_guess() where it tested to see if the guess is higher than secret then the output is "Go LOWER". Using the guess of 60 and secret of 50 it passed. It also checks if the guess is lower than the secret then the output is "Go HIGHER". Using the guess of 40 and secret of 50, it also passed. 

- Did AI help you design or understand any tests? How?
    -- Yes AI helped me gain a deeper understanding of tests because it reminded me about boundary testing and testing just below and above the accepted range. I had previously learned about this in my uni class but was not sure how it would actually be implement which I can see how with this example where I had to test within range. As well with the points tests where I test in first win (test_update_score_win_awards_points()), in no wins (test_update_score_never_goes_negative()), and in late wins not going below 10 points (test_update_score_win_has_minimum_floor()).

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
    --- I would explain Streamlit "reruns" as stopping the file from continuing its execution and restarting back to the top of the file. Reading the file over again. A session state is where information is active and used throughout the file to update changes through events that occur to the state as it reads through the file. The information is saved even after the script reruns again.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
    --- One habit I used from this project was commenting the possible bugs I see myself and asking questions on parts I did not understand. Then using AI to look at my comments and explain what I did not understand but as well help fix the bugs. When I did not understand a suggestion I would ask follow up questions to better understand its suggestions. 

- What is one thing you would do differently next time you work with AI on a coding task?
    --- One thing I would do differently next time is fully reading what the AI gives as comments because at the end it, it would give other possible errors with the one I am looking at. 

- In one or two sentences, describe how this project changed the way you think about AI generated code.
    --- It made me realize the more functionality of AI generated code. I did not know that AI can change functions from one file to another but definitely needs careful observation because it may not move everything and it may suggest to delete code that is needed. For example it suggested to delete a moved function but also wanted to delete an import of another function that was already moved. 