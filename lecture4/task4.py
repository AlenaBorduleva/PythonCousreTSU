# Ввод данных
n = input("Enter the number n: ")

try:
    int(n)
except ValueError:
    print ("Not an integer")
else:
    if not 1 < int(n):
        print("Incorrect value")
    else:
        a = list(range(2, int(n) + 1))
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