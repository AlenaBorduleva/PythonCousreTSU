# Ввод данных
t = input("Enter the temperature t: ")

#Проверка
try:
    float(t[ : -1])
except ValueError:
    print ("Not a float")
else:
    
    if t[-1] != 'C' and t[-1] != 'F':
        print ("Incorrect units")
    
    elif t[-1] == 'C' and float(t[ : -1]) < -273.16:
        print ("The temperature is below absolute zero in C")
    
    elif t[-1] == 'F' and float(t[ : -1]) < -459.69:
        print ("The temperature is below absolute zero in K")  
               
#Перевод температуры
    else: 
               
        if t[-1] == "C":
            Tf = (9/5) * float(t[ : -1]) + 32
            print (Tf, "F")

        elif t[-1] == "F":
            Tc = (5/9)*(float(t[ : -1]) - 32)
            print (Tc, "C")