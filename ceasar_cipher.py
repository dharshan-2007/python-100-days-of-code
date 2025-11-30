# Ceasar Cipher

"""value of a is 97
value of z is 122
"""


def encode(str1, shift):
    res = ""
    for i in str1:
        val = ord(i)
        if (i >= "a") and (i <= "z"):
            if val + shift > 122:
                rem = (val + shift) - 122
                val = 97 + (
                    rem - 1
                )  # if we want to shift z to one char 97 is the value of a so we are subtracting 1 to make sure we get the expected output
            else:
                val += shift
        res = res + chr(val)
    print("\n\t------Encoded Message------\n")
    print(res)


def decode(str1, shift):
    res = ""
    for i in str1:
        val = ord(i)
        if (i >= "a") and (i <= "z"):
            if val - shift < 97:
                rem = 97 - (val - shift)
                val = 122 - (
                    rem - 1
                )  # if we want to shift a to one char 122 is the value of z so we are subtracting 1 to make sure we get the expected output
            else:
                val = val - shift
        res = res + chr(val)
    print("\n\t-------Decoded Message---------\n")
    print(res)


# main
print("Welcome to Ceasar Cipher..\n")
mode = int(input("1. Encode\n2. Decode\nEnter your option(1 or 2): "))
ip = input("Enter your message: ").lower()
shift = int(input("Enter number of shifts you want: "))
if mode == 1:
    encode(ip, shift)
elif mode == 2:
    decode(ip, shift)
else:
    print("Wrong Input")
