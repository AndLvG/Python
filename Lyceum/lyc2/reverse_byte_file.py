def reverse():
    with open('input.dat', 'rb') as in_file:
        b = in_file.read()
    with open('output.dat', 'wb') as out_file:
        out_file.write(b[::-1])
