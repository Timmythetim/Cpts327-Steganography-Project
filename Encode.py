import matplotlib.pyplot as plt
import matplotlib.image as img
import tifffile as tf
import magic
from bitstring import BitArray
from cryptography.fernet import Fernet
# image = img.imread("keys.png")
stringpic = input("Please enter local file path of image to encode\n")
string = input("Please enter local file path of file to embed, any file type is acceptable\n")
length = 0
# try:
if "text" in magic.from_file(string,mime=True):
    file = open(string, "r")
    keyfile = open("secretkey.txt", "r")
    array = tf.imread(stringpic)

    plaintext = file.read()
    key = keyfile.read()
    key = bytes(key,"utf-8")
    fernet = Fernet(key)
    plaintext = fernet.encrypt(plaintext.encode())
    plaintext = plaintext.decode("utf-8")
    print(plaintext)
    length = len(plaintext)
    message = '{:032b}'.format(length)
    print(message)
    for x in plaintext:
        message += format((ord(x)), '08b')
    print(message)
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
else:
    file = open(string, "br")

    array = tf.imread(stringpic)

    plaintext = file.read()
    length = len(plaintext)
    numbers = []
    print(plaintext[1])
    for x in plaintext:
        numbers.append(x)
    print(numbers[:16])

    message = '{:032b}'.format(length)
    for x in range(0,len(numbers)):
        temp = '{:08b}'.format(numbers[x])
        message += temp
    x = 0
    y = 0
    z = 0
    m = 0
    x = 0
    while m < len(message):
        if x == len(array):
            print("Encoded File is too large to put into this image! Choose a bigger image or smaller file!")
            break
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
    if x != len(array):
        tf.imwrite("testencoded.tiff",array)
# # except:
# #     print("An error has occurred, check your file names!")