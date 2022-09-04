a = input("Введите число до запятой: ")
b = input("Введите число после запятой перед периодом: ")
c = input("Введите число в периоде: ")

y = str(b+c)

i = len(c)
u = str(i*"9")

g = len(b)
t = str(g*"0")

x = str(u+t)

# answer = int(a)+((int(y)-int(b))/(int(x))) 
#print(answer)

print(f"Ответ: {a} + {str((int(y)-int(b)))} / {x}")