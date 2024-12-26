import pytest
from password import generate_password

def test_generate_password():
    assert len(generate_password("6")) == 6
    assert len(generate_password("100")) == 100
    with pytest.raises(ValueError):
        assert generate_password("sdfdsf")
        assert generate_password("")

