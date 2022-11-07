import matplotlib.pyplot as plt
import matplotlib.image as img
import tifffile as tf
import numpy

# image = img.imread("keys.png")

array = tf.imread("test.tiff")
file = open("Message.txt", "r")
message = file.read()
message += "0000000000000000"
x = 0
y = 0
z = 0
m = 0
print(type(array[x][y][z]))
for x in range(0,10):
    print(array[0][x])
print("\n")
x = 0
while m < len(message):
    if message[m] != " ":
        binary = format((array[x][y][z]), '08b')   
        last = binary[-1]
        if last != message[m]:
            binary = binary[:-1]
            binary += message[m]
            number = "0b" + binary
            number = int(binary,2)
            array[x][y][z] = number
        z += 1
        if z == 3:
            y += 1
            z = 0
        if y == len(array[0]):
            x += 1
            y = 0
            z = 0
    m += 1
tf.imwrite("testencoded.tiff",array)