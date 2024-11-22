# Encryption
def encryption(plaintext, key):
    result = ""

    for i in range(len(plaintext)):
        char = plaintext[i]

        if char == " ":
            result += result
        elif char.isupper():
            value = ord(char) - 65
            result += chr(((value * key) % 26) + 65)
        else:
            value = ord(char) - 97
            result += chr(((value * key) % 26) + 97)
    return result

input = open("input.txt", "r+")
output = open("output.txt", "w")

plaintext = input.read();
key = 7
result = encryption(plaintext, key)
input.truncate(0)
output.write(result)

input.close()
output.close()
