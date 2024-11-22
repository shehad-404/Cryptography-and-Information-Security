# Decryption
def MultiplicativeInverse(a, n):
    r1 = n
    r2 = a
    s1 = 1
    s2 = 0
    t1 = 0
    t2 = 1
    while r2 > 0:
        q = int(r1 / r2)
        r = r1 - q * r2
        r1 = r2
        r2 = r

        s = s1 - q * s2
        s1 = s2
        s2 = s

        t = t1 - q * t2
        t1 = t2
        t2 = t

    t = t1

    if r1 == 1:
        return t + n
    else:
        return " "


def encryption(plaintext, key1, key2):
    result = ""

    for i in range(len(plaintext)):
        char = plaintext[i]

        if char == "":
            result += result
        elif char.isupper():
            value = ((ord(char) - 65) - key2)
            result += chr(((value * key1) % 26) + 65)
        else:
            value = ((ord(char) - 97) - key2)
            result += chr(((value * key1) % 26) + 97)

    return result


input = open("output.txt", "r+")
output = open("input.txt", "w")

plaintext = input.read();
key1 = 7
key2 = 2
value = MultiplicativeInverse(key1, 26)

if value != " ":
    result = encryption(plaintext, value, key2)

    output.write(result)
    input.truncate(0)
else:
    print("Decryption is not possible by this key")

input.close()
output.close()
