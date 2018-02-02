"""Do aplikacji dołącz rozwiązania zadań:

♦ ZADANIE 1. Napisz generator kodów pocztowych, który przyjmuje 2 stringi: "79-900" i "80-155" i zwraca listę kodów pomiędzy nimi.

♦ ZADANIE 2. Podana jest lista zawierająca elementy o wartościach 1-n. Napisz funkcję, która sprawdzi, jakich elementów brakuje:

1-n = [1,2,3,4,5,...,10]
np. n=10
wejście: [2,3,7,4,9], 10
wyjście: [1,5,6,8,10]

♦ ZADANIE 3. Należy wygenerować listę liczb od 2 do 5.5 ze skokiem co 0.5.
Dane wynikowe muszą być typu decimal.

"""

from decimal import Decimal


def zadanie_1(kod1, kod2):
    kod1, kod2 = int(kod1.replace('-', '')), int(kod2.replace('-', ''))
    return["%02d-%03d" % divmod(i, 1000) for i in range(kod1 + 1, kod2)if divmod(i, 1000)[1] is not 0]


def zadanie_2(lista, n):
    return [i+1 for i in range(n) if i+1 not in lista]


def zadanie_3():
    return [Decimal(i * 5 + 20) / 10 for i in range(8)]


print(zadanie_1("79-900", "80-155"))
print(zadanie_2([2,3,7,4,9], 10))
print(zadanie_3())
