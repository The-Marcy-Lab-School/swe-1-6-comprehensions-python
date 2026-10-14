from debug import load_setting, log_each_name, tallest_user

TEST_SUITE_NAME = "Debug Tests"


def printed(capsys):
    lines = []
    for line in capsys.readouterr().out.splitlines():
        if line.strip():
            lines.append(line)
    return lines


def test_log_each_name(capsys):
    """log_each_name - prints each name"""
    log_each_name(["Ada", "Zo", "Bob"])
    assert printed(capsys) == ["Ada", "Zo", "Bob"]


def test_tallest_user():
    """tallest_user - returns the user with the greatest height"""
    users = [
        {"name": "Ada", "height": 22},
        {"name": "Zo", "height": 40},
        {"name": "Bob", "height": 28},
    ]
    assert tallest_user(users) == {"name": "Zo", "height": 40}


def test_load_setting_finds_a_key():
    """load_setting - returns the value when the key is there"""
    assert load_setting({"theme": "dark"}, "theme") == "dark"
    assert load_setting({"theme": "dark"}, "missing") is None


def test_load_setting_does_not_swallow_everything():
    """load_setting - only catches a missing key, not every possible error"""
    import inspect

    source = inspect.getsource(load_setting)
    assert "except:" not in source.replace("except :", "except:"), (
        "A bare except: hides every error, including the ones you want to see."
    )
