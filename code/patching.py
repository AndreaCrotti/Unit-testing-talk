from mock import patch

@patch('library.function', new=lambda: print("hello"))
def test_run_func():
    pass
