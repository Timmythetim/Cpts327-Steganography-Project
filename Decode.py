import matplotlib.pyplot as plt
import matplotlib.image as img
import tifffile as tf

x = 0
y = 0
z = 0
m = 0
message = ""
finalmessage = ""
counter = 0

string = input("Please enter local file path of encoded image\n")
size = ""
try:
    array = tf.imread(string)


    while counter < 32:
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
        size += last
        counter += 1
    counter = 0
    print(int(size,2))
    size = int(size,2)
    while counter < size*8 + 8:
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
        message += last
        counter += 1

except:
    print("File not found!")

x = 0
while x+8 < len(message):
    character = message[x:x+8]
    character = int(character,2)
    character = chr(character)
    finalmessage += character
    x += 8

file = open("output", "w")
file.write(finalmessage)
print(finalmessage)