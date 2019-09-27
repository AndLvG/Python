def line(urav, koord):
    x = float(koord[:koord.find(';')])
    y = float(koord[koord.find(';') + 1:])
    k, b = urav.split('x')
    k, b = int(k), (int(b))
    y_urav = k * x + b
    print(y_urav == y)


line("5x-10", "5;-9")
