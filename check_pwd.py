LOWER = "abcdefghijklmnopqrstuvwxyz"
UPPER = LOWER.upper()
DIGITS = "0123456789"
SYMBOLS = "~`!@#$%^&*()_+-="


def check_pwd(pwd):
    if not 8 <= len(pwd) <= 20:
        return False
    if not any(c in LOWER for c in pwd):
        return False
    if not any(c in UPPER for c in pwd):
        return False
    if not any(c in DIGITS for c in pwd):
        return False
    if not any(c in SYMBOLS for c in pwd):
        return False
    return True
