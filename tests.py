from check_pwd import check_pwd


def test_empty_string():
    assert check_pwd("") is False

def test_seven_chars_too_short():
    assert check_pwd("Abcde1!") is False

def test_twenty_one_chars_too_long():
    assert check_pwd("Aa1!" + "a" * 17) is False

def test_no_lowercase():
    assert check_pwd("ABCDEFG1!") is False

def test_no_uppercase():
    assert check_pwd("abcdefg1!") is False

def test_no_digit():
    assert check_pwd("Abcdefg!!") is False

def test_no_symbol():
    assert check_pwd("Abcdefg1") is False

def test_valid_with_at_symbol():
    assert check_pwd("Abcdefg1@") is True

def test_non_english_lowercase_not_counted():
    assert check_pwd("ABCDEF\u00e91!") is False   # é

def test_non_english_uppercase_not_counted():
    assert check_pwd("abcdefg\u00c91!") is False   # É

def test_non_ascii_digit_not_counted():
    assert check_pwd("Abcdefg\u0663!") is False   # Arabic-Indic 3


def main():
    tests = [(n, f) for n, f in globals().items() if n.startswith("test_")]
    for name, fn in tests:
        try:
            fn()
        except AssertionError:
            print(f"FAILED: {name}")


if __name__ == "__main__":
    main()
