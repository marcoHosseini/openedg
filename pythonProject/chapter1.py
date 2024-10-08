import os.path


def kreis(radius):
    if radius <= 0:
        print("bitte positive zahlen und kein Null")
    else:
        umfang = radius * 3.14 * 2
        durchmeser = radius * 2
        flaeche = 3.14 * radius ** 2
        print(umfang, durchmeser, flaeche)


def calc(a, b):
    if a <= 0 and b <= 0:
        print("bitte keine negative Zahlen")
    else:
        summ = a + b
        sub = a - b
        mult = a * b
        div = a / b
        qub = a ** 2 + b ** 2
        tet = a ** 3 + a ** 3
        print(summ, " ", sub, " ", mult, " ", div, " ", qub, " ", tet)


def bookCalc(blockages, gb):
    boockbayte = 30 * 80 * blockages
    number = 1024 ** 3 * gb / boockbayte
    print("number of boock is: ", number)


