num1 = 1
num2 = 1
 
n = input("Порядковий номер елементу ряду Фібоначі: ")
n = int(n)
 
i = 0
while i < n - 2:
    sum = num1 + num2
    num1 = num2
    num2 = sum
    i += 1
 
print(num2)