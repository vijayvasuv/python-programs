import pytest
from authenticate import validate_email, generate_code

def test_validate_email():
    with pytest.raises(ValueError):
        assert validate_email("")
        assert validate_email("abcd")
    assert validate_email("vijayvasuv@gmail.com") == "vijayvasuv@gmail.com"

def test_generate_code():
    assert (len(generate_code())) == 6




