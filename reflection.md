# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
    When I first ran the game it told me that my guess of 40 should be higher. My next input was 50 telling me to guess higher when it should have been lower. The next input I put was 80 again telling me to guess higher. When I inputed 100 it told me to guess higher again. On my last attempt I guessed 135 and thats when it told me to go guess lower and revealed that the number was 38. Giving me a score of -5. 

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
    The hints kept telling me to guess higher when at my second attempt should have said for me to guess lower. 
    The score is negative after not being able to guess the number
    Does not allow for you to actually start the game over


**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input         | Expected Behavior   |      Actual Behavior     | Console Output / Error |
|---------------|---------------------|--------------------------|------------------------|
|  guess of 40  |     "Go LOWER" hint    "Go HIGHER" hint shown           none
|  guess of 50  |     "Go LOWER" hint    "Go HIGHER" hint shown           none
|  last guess   |                                                       preventOverflow
    of 135      |     "Go LOWER" hint    "Go LOWER" hint shown       modifier is required


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

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
