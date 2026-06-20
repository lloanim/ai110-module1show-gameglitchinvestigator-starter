# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

Part 1:
I highlighted code with a FIXME where I had written questioning why the range change based on difficulty was not working. There I asked it "how can I restrict guess range inclusive. also how do i know if the secret generated will be in range."

Part 2:
I then asked it to help add pytests to verify that this works. But I had also checked by playing the game as shown in README.md. 

**What did the agent do?**

Part 1:
It explained to me that secret is guaranteed to be in range based on randint being inclusive. Then it pointed out that parse_guess did not restrict it so suggested to add "low: int, high: int" and add the code where the value or guess is checked to be in range. If not then it will output that the guess is not in range. Lastly, it said to change in app.py where parse_guess function is called with the new inputs of "low, high". 

Part 2:
Claude had generated 7 more tests when I asked it to verify that parse_guess works with the changes made. The first test is inclusive bounds, a test below range, a test above range, a test non-numerical, an empty guess, and a float guess still works. But these are tests that deal with easy mode where range is from 1 to 20. 

**What did you have to verify or fix manually?**

I had to make sure this worked as well in all levels of difficulty and stoped the bash command from testing because it does not work with what it gives. Rather I use the command python -m pytest to verify the tests work. 

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Verify changes to restrict range of guess based on difficulty | "can you add pytests for this change?" | 7 tests: test_parse_guess_accepts_value_in_range(), test_parse_guess_accepts_inclusive_bounds(), test_parse_guess_rejects_below_range(), test_parse_guess_rejects_above_range(), test_parse_guess_rejects_non_number(), test_parse_guess_rejects_empty_and_none(), test_parse_guess_float_string_truncates_then_range_checks()| Yes | Passed testing and verified through the game itself |


| Negative numbers | "does the below range test, test for negative numbers as well" | To add another test that proves negative numbers are not accepted | Yes | Passed testing and verified through the game itself |


---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
