import pytest
import requests
import serial
ser = serial.Serial("COM4", 9600)

def get_test_string(test_num):
    BASE_URL = "http://127.0.0.1:8000"
    ENDPOINT = "/test" + str(test_num)
    response = requests.get(BASE_URL + ENDPOINT)
    test_string = response.json()["test_string"]
    return test_string

def get_string_in(test_string):
    string_in = ""
    for i in range(len(test_string)):
        key = ser.read()
        string_in += key.decode('utf-8')
    print("Typed word: " + string_in)
    return string_in
    
@pytest.mark.parametrize("test_num", range(5))
def test_word0(test_num): 
    test_string = get_test_string(test_num)
    print("Enter the following string of characters:\"" + test_string + "\"")
    assert get_string_in(test_string) == test_string
# run pytest -vs test_full_system.py