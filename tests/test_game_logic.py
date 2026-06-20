from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_hint_direction_matches_guess():
    # check_guess returns (outcome, message); the message tells the user
    # which direction to guess next.
    # Guess above the secret -> tell them to go LOWER
    outcome_high, message_high = check_guess(60, 50)
    assert outcome_high == "Too High"
    assert "LOWER" in message_high.upper()

    # Guess below the secret -> tell them to go HIGHER
    outcome_low, message_low = check_guess(40, 50)
    assert outcome_low == "Too Low"
    assert "HIGHER" in message_low.upper()


def test_update_score_win_awards_points():
    # A win on the first attempt awards 100 - 10*1 = 90 points
    assert update_score(0, "Win", 1) == 90


def test_update_score_win_has_minimum_floor():
    # Points never drop below 10, even on late winning attempts
    assert update_score(0, "Win", 20) == 10


def test_update_score_wrong_guess_applies_penalty():
    # A wrong guess (high or low) subtracts 5 points
    assert update_score(50, "Too High", 1) == 45
    assert update_score(50, "Too Low", 1) == 45


def test_update_score_never_goes_negative():
    # The penalty must not push the score below 0
    assert update_score(0, "Too High", 1) == 0
    assert update_score(3, "Too Low", 1) == 0
