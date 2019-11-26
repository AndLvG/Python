with open('input.bmp', 'rb') as in_bmp_file:
    body = list(bytes(in_bmp_file.read()))
    body_negativ = []

    for i, elem in enumerate(body):
        if i < 54:
            body_negativ.append(elem)
        else:
            body_negativ.append(255 - elem)

with open('res.bmp', 'wb') as out_bmp_file:
    out_bmp_file.write(bytes(body_negativ))
