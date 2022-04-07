#Задание 1
a = 1
b = 10
print("Вы ввели следующие переменные - ", a,b)
chislo1 = int(input("Введите первое число "))
stroka1 = input("Введите первую строку ")
chislo2 = int(input("Введите второе число "))
stroka2 = input("Введите вторую строку ")
print(f'Вы ввели следующие значения - {chislo1}, {stroka1}, {chislo2}, {stroka2}')

#Задание 2
vremja = int(input("Введите количество секунд"))
chasi = vremja//3600
minuti = (vremja - chasi*3600)//60
sekundi = vremja - (chasi*3600 + minuti*60)
print(f'Введенное время {chasi}, {minuti}, {sekundi}')

#Задание 3
n = int(input("Введите число n - "))
symma = (n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n)))
print(symma)

#Задание 4
i = int(input("Введите целое положительное число - "))
r = -1
while i > 10:
    d = i % 10
    i //= 10
    if d > r:
        r = d
print(r)

#Задание 5
viruchka = int(input("Введите значение выручки фирмы - "))
izderzki = int(input("Введите значение издержек фирмы - "))
if viruchka > izderzki:
    print("Прибыль, выручка больше издержек")
else:
    print("Убыток, издержки больше выручки")

# Задание 6
viruchka = int(input("Введите значение выручки фирмы, тыс. руб. - "))
izderzki = int(input("Введите значение издержек фирмы, тыс. руб. - "))
pribil = viruchka - izderzki
if viruchka > izderzki:
    print(f"Прибыль, выручка больше издержек. Рентабельность выручки составила в процентах - {(pribil/viruchka) * 100}")
    rabochie = int(input("Введите количество работников фирмы - "))
    print(f"Прибыль в расчете на одного сотрудника составляет, тыс. руб. - {pribil/rabochie}")
elif viruchka == izderzki:
    print("Делайте планирование, прибыли нет!")
else:
    print("Убыток, издержки больше выручки")


# Задание 7
a = int(input("Введите сколько километров Вы пробежали - "))
b = int(input("Введите километраж, пробежать который Вы бы хотели - "))
days = 1
while a < b:
    a = a + 0.1*a
    days = days + 1
print(f"Dы достигнете желаемого на день", days)