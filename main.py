kolichestvo_strok=int(input("Введите количество строк: ")) #запрос на ввод
if kolichestvo_strok <=0: # если условие правдиво
    print("Количество строк не может быть отрицательным и равным нулю.") # выводим это
    
list = [] # список создаем пустой
for i in range(kolichestvo_strok): #цикл который выполняется kolichestvo_strok раз
    stroki = input(f"Введите строку {i + 1}: ") # вводим строку
    list.append(stroki) #добавляем ее в список

unucalnie_stroki = set() # создаем пустое множество

for stroki in list: #перебераем строки в списке
    w = stroki.split() #делим по пробелам и присваеиваем w
    ww = [word.lower() for word in w]  # приводим к нижнему регистру
    unucalnie_stroki.update(ww) # обновляем наше множество

print(f"Количество различных слов: {len(unucalnie_stroki)}") # и выводим количество(len) различных(set) слов
