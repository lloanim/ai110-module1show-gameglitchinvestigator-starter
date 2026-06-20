def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str, low: int, high: int):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."
    
    #Adds the restriction of the different difficulties
    if value < low or value > high:
        return False, None, f"Guess must be between {low} and {high}!"

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

#    try:
#        if guess > secret:
#            return "Too High", "📉 Go LOWER!"
#        else:
#            return "Too Low", "📈 Go HIGHER!"
#    except TypeError:
#        #FIXME: Possible error here. Why type cast guess to string again
#        g = str(guess)
#        if g == secret:
#            return "Win", "🎉 Correct!"
#        if g > secret:
#            return "Too High", "📈 Go HIGHER!"
#        return "Too Low", "📉 Go LOWER!"

#FIX w/ AI: Was that it is not necessary to have the try/except
#           due to it being a saftey net for code thats no longer applied
#           specifically when the guess was typecasted to a string rather than staying as an int
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * attempt_number
        if points < 10:
            points = 10
        return current_score + points


    #FIXME: Too High of an output adds 5 every even attempt and subtracts 5 on odd
    #       If the guess is too high increase 5? In what case should the player gain points
    #if outcome == "Too High":
    #    if attempt_number % 2 == 0:
    #        return current_score + 5
    #    return current_score - 5

    #FIXME: Should not decrease if current_score is 0
    #if outcome == "Too Low":
    #    return current_score - 5


    #FIX w/ AI: A wrong guess is a wrong guess: "Too High" and "Too Low" are treated
    #           the same. Apply a small penalty, but never let the score go negative.
    if outcome == "Too High" or outcome == "Too Low":
        return max(0, current_score - 5)

    return current_score
