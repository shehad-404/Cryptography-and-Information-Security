# decryption of Caesar cipher
def decryption(ciphertext, key):
    result = ""
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char == ' ':
            result += char
        elif char.isupper():
            result += chr(((((ord(char) - key) - 65) % 26) + 65)+32)
        else:
            result += chr((((ord(char) - key) - 97) % 26) + 97)
    return result

input = open("output.txt", "r+");
output = open("input.txt", "w");
ciphertext = input.read();
key = 3;
result = decryption(ciphertext, key)
output.write(result)
input.truncate(0)

input.close()
output.close()
