import numpy as np

hidden = np.random.rand(49, 41)
out = np.random.rand(41, 26)
error = np.random.rand(21)


def zapis_do_pliku(hidden, output, error):
    file = open("src/wagi/hidden.txt", "w")
    for i in range(len(hidden)):
        for j in range(len(hidden[0,])):
            file.write(str(hidden[i, j]) + " ")
        if i != (len(hidden) - 1):
            file.write("\n")
    file.close()

    file = open("src/wagi/out.txt", "w")
    for i in range(len(out)):
        for j in range(len(out[0,])):
            file.write(str(out[i, j]) + " ")
        if i != (len(out) - 1):
            file.write("\n")
    file.close()

    file = open("src/wagi/error.txt", "w")
    file.write(str(error.sum()))
    file.close()
    return 0


zapis_do_pliku(hidden, out, error)
