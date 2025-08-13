import pytest
from recieve_key import amazing_passcode, get_word

def test_word(): 
    assert get_word() == amazing_passcode

# command: pytest -s test_recieve_key.py