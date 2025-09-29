TEST_MODE = False

def set_test_mode(val: bool):
    global TEST_MODE
    TEST_MODE = val

def is_test_mode() -> bool:
    return TEST_MODE