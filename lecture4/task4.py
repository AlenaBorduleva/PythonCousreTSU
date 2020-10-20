# Ввод данных
n = input("Enter the number n: ")
# осуществляем проверку
try:
    int(n)
except ValueError:
    print ("Not an integer")
else:
    if  int(n) < 2:
        print("Incorrect value")
    else:
        a = list(range(2, int(n) + 1)) #создаём список, n+1 для того, чтобы захватить значение n
        for el in a:
            if el != 0:
                for index in range (0, len(a)):
                    if (a[index] != el) and (a[index] % el == 0):
                        a[index] = 0
        a = set(a)
        a.remove(0)
        print (a)

        f = open('sample.txt', 'w')
        for el in a:
            f.write(str(el) + '\n')

        f.close()