import pytest
import serial
ser = serial.Serial("COM4", 9600)

word = ""

def get_word(word):
    for i in range(6):
        key = ser.read()
        word = word + key.decode('utf-8')
    print("Typed word: " + word)
    return (word)

def test_word(): 
    assert get_word(word) == amazing_passcode

# command: pytest -s test_recieve_key.py



amazing_passcode = "potato"