from logic_utils import check_guess, update_score, parse_guess

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


def test_parse_guess_accepts_value_in_range():
    # A valid number inside the range parses successfully
    ok, value, err = parse_guess("10", 1, 20)
    assert ok is True
    assert value == 10
    assert err is None


def test_parse_guess_accepts_inclusive_bounds():
    # Both the low and high bounds are valid guesses (inclusive range)
    ok_low, value_low, err_low = parse_guess("1", 1, 20)
    assert ok_low is True
    assert value_low == 1
    assert err_low is None

    ok_high, value_high, err_high = parse_guess("20", 1, 20)
    assert ok_high is True
    assert value_high == 20
    assert err_high is None


def test_parse_guess_rejects_below_range():
    # A number below the low bound is rejected
    ok, value, err = parse_guess("0", 1, 20)
    assert ok is False
    assert value is None
    assert err is not None


def test_parse_guess_rejects_above_range():
    # A number above the high bound is rejected
    ok, value, err = parse_guess("21", 1, 20)
    assert ok is False
    assert value is None
    assert err is not None


def test_parse_guess_rejects_negative_number():
    # A negative number parses as an int but is below the low bound
    ok, value, err = parse_guess("-5", 1, 20)
    assert ok is False
    assert value is None
    assert err is not None


def test_parse_guess_rejects_non_number():
    # Non-numeric input is rejected before the range check
    ok, value, err = parse_guess("abc", 1, 20)
    assert ok is False
    assert value is None
    assert err == "That is not a number."


def test_parse_guess_rejects_empty_and_none():
    # Empty string and None both prompt for a guess
    for raw in ("", None):
        ok, value, err = parse_guess(raw, 1, 20)
        assert ok is False
        assert value is None
        assert err == "Enter a guess."


def test_parse_guess_float_string_truncates_then_range_checks():
    # "15.9" -> int(float()) -> 15, which is in range
    ok, value, err = parse_guess("15.9", 1, 20)
    assert ok is True
    assert value == 15
