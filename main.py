a = float(input('Введите первое число: ')) #ввод числа
b = float(input('Введите второе число: ')) #ввод числа
 
rez = "числа равны " if a == b else (f"найменьшее: {a}" if a < b else f"найменьшее {b}") #тернарное выражение 

print(rez) # вывод
