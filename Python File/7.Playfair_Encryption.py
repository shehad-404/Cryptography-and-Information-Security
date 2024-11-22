#Encrypt
import numpy
# Initialize the matrix
matrix = numpy.array([
    ['p', 'l', 'a', 'y', 'f'],
    ['i', 'r', 'e', 'x', 'm'],
    ['b', 'c', 'd', 'g', 'h'],
    ['k', 'n', 'o', 'q', 's'],
    ['t', 'u', 'v', 'w', 'z']
])

result = numpy.transpose(matrix)

plaintext = "hidethegoldinthetreestump"
plaintext = plaintext.replace("j", "i")
plaintextpair = []
ciphertextpair = []

i = 0
while i < len(plaintext):
    a = plaintext[i]
    b = ''

    if (i + 1) == len(plaintext):
        b = 'x'
    else:
        b = plaintext[i + 1]
    if a != b:
        plaintextpair.append(a + b)
        i += 2
    else:
        plaintextpair.append(a + 'x')
        i += 1

for pair in plaintextpair:
    applied_rule = True

    if applied_rule:
        for row in range(5):
            if pair[0] in matrix[row] and pair[1] in matrix[row]:
                for i in range(5):
                    if matrix[row][i] == pair[0]:
                        j0 = i

                for i in range(5):
                    if matrix[row][i] == pair[1]:
                        j1 = i

                applied_rule = False
                ciphertextpair.append((matrix[row][(j0 + 1) % 5]) + (matrix[row][(j1 + 1) % 5]))


    if applied_rule:
        for row in range(5):
            if pair[0] in result[row] and pair[1] in result[row]:
                for i in range(5):
                    if matrix[i][row] == pair[0]:
                        j0 = i

                    for i in range(5):
                        if matrix[i][row] == pair[1]:
                            j1 = i

                    applied_rule = False
                ciphertextpair.append((matrix[(j0 + 1) % 5][row]) + (matrix[(j1 + 1) % 5][row]))


    if applied_rule:
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == pair[0]:
                    x0 = row
                    y0 = col
            for row1 in range(5):
                for col1 in range(5):
                    if matrix[row1][col1] == pair[1]:
                        x1 = row1
                        y1 = col1
        ciphertextpair.append((matrix[x0][y1]) + (matrix[x1][y0]))

print(plaintextpair)
print(ciphertextpair)
