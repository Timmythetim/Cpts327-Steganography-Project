import matplotlib.pyplot as plt
import matplotlib.image as img
import tifffile as tf

x = 0
y = 0
z = 0
m = 0

array = tf.imread("testencoded.tiff")

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
    counter += 1
    if counter == 8:
        message += " "
        counter = 0
print(message)