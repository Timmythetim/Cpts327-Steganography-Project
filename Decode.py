import matplotlib.pyplot as plt
import matplotlib.image as img
import tifffile as tf

x = 0
y = 0
z = 0
m = 0
character = ""
finalmessage = ""

string = input("Please enter local file path of encoded image\n")

try:
    array = tf.imread(string)

    delimeter = "1111111111111111"

    message = ""
    counter = 0
    print(array[0])
    while delimeter != "0000000000000000":
        binary = format((array[x][y][z]), '08b')
        last = binary[-1]
        # print(last)
        # input("Press Enter to continue...")
        z += 1
        if z == 3:
            y += 1
            z = 0
        if y == len(array[0]):
            x += 1
            y = 0
        delimeter = delimeter[1:]
        delimeter += last
        message += last
        # counter += 1
        # if counter == 8:
        #     message += " "
        #     counter = 0
except:
    print("File not found!")
x = 0
while x+8 < len(message):
    character = message[x:x+8]
    character = int(character,2)
    character = chr(character)
    finalmessage += character
    x += 8


print(finalmessage)