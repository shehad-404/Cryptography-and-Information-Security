# Encrpytion
def encryption(plaintext, key1, key2):
    result = ""

    for i in range(len(plaintext)):
        char = plaintext[i]

        if char == "":
            result += result
        elif char.isupper():
            value = ord(char) - 65
            result += chr((((value * key1) + key2) % 26) + 65)
        else:
            value = ord(char) - 97
            result += chr((((value * key1) + key2) % 26) + 97)

    return result

input = open("input.txt", "r+")
output = open("output.txt", "w")

plaintext = input.read();
key1 = 7
key2 = 2

result = encryption(plaintext, key1, key2)
output.write(result)
input.truncate(0)

input.close()
output.close()
