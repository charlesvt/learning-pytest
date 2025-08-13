import pytest
import requests
import serial
ser = serial.Serial("COM4", 9600)

def get_test_string():
    BASE_URL = "http://127.0.0.1:8000"
    ENDPOINT = "/test4"
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
    
def test_word(): 
    test_string = get_test_string()
    print("Enter the following string of characters:\"" + test_string + "\"")
    assert get_string_in(test_string) == test_string