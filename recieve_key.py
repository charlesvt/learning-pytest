import serial
ser = serial.Serial("COM4", 9600)

amazing_passcode = "potato"

def get_word():
    word = ""
    for i in range(6):
        key = ser.read()
        word += key.decode('utf-8')
    print("Typed word: " + word)
    return (word)