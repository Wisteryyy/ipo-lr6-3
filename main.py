while True: # бесконечный цикл, который прерывается только после break
    try: #пытаемся
        a = int(input("Введите количество строк: ")) # ввести чисо
        if a < 1: # и если оно меньше единицы
            print("Количество строк должно быть положительным и не должно равняться нулю.") # то выводит соответствующее сообщение
            continue # но попытка не пытка проб=буем еще раз
        break # прерываемся если все получилось
    except ValueError: # обработка ошибки
        print("Введите целое число.") # ну ваще бред написал

kk = [] # список создаем пустой
for i in range(a): #цикл который выполняется a раз
    s = input(f"Введите строку {i + 1}: ") # вводим строку
    kk.append(s) #добавляем ее в список

u = set() # создаем пустое множество

for s in kk: #перебераем строки в списке
    w = s.split() #делим по пробелам и присваеиваем w
    u.update(w) # обновляем наше множество

print("Количество различных слов: ", len(u)) # и выводим количество(len) различных(set) слов
