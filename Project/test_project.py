import pytest
from project import get_input, api_call, save_result

def test_get_input():
    assert get_input("Breaking Bad") == "Breaking Bad"
    assert get_input("sdfsdg$5^") == "sdfsdg$5^"
    with pytest.raises(TypeError):
        assert get_input("")

def test_api_call():
    result = {}
    result = api_call("Breaking")
    assert isinstance(result, dict)
    with pytest.raises(KeyError):
        assert api_call("sdfsdg$^")

def test_save_result():
    assert save_result("yes") == "Data saved in myfile.txt. Binge-watch!"
    assert save_result("no") == "Thanks, binge-watch!"
    with pytest.raises(TypeError):
        assert save_result("")
        assert save_result("sdfsdf")

