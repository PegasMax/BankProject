import pytest

from src.decorators import log


@pytest.mark.parametrize(
    "a_example,b_example, expected_log",
    [
        (
            3,
            5,
            """start of executing adding_function
adding_function result = 8
finish of executing adding_function\n""",
        ),
        (
            3,
            "string",
            """start of executing adding_function
adding_function error: <class 'TypeError'>. Inputs: (3, 'string'), {}
finish of executing adding_function\n""",
        ),
    ],
)
def test_log_to_file(a_example, b_example, expected_log):
    @log("logger.txt")
    def adding_function(a, b):
        return a + b

    adding_function(a_example, b_example)
    file = open("logger.txt", "r")
    logged = file.read()
    file.close()
    assert logged == expected_log


@pytest.mark.parametrize(
    "a_example,b_example, expected_log",
    [
        (
            3,
            5,
            """start of executing adding_function
adding_function result = 8
finish of executing adding_function\n""",
        ),
        (
            3,
            "string",
            """start of executing adding_function
adding_function error: <class 'TypeError'>. Inputs: (3, 'string'), {}
finish of executing adding_function\n""",
        ),
    ],
)
def test_log_to_console(capsys, a_example, b_example, expected_log):
    @log()
    def adding_function(a, b):
        return a + b

    adding_function(a_example, b_example)
    captured = capsys.readouterr()
    assert captured.out == expected_log
