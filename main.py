number_of_lines = int(input("Введите количество строк: ")) # запрос на ввод количества строк
if number_of_lines <= 0: # проверка на количество строк
    print("Количество строк не может быть отрицательным и равным нулю.") # вывод

lines_list = [input(f"Введите строку {i + 1}: ") for i in range(number_of_lines)] # создание списка строк с помощью генератора списка

unique_words = set() # множество

for line in lines_list: # перебираем строки в списке
    words = line.split() # разделяем строку по пробелам
    words_lower = [word.lower() for word in words] # приводим каждое слово к нижнему регистру
    unique_words.update(words_lower) # обновляем множество

print(f"Количество различных слов: {len(unique_words)}") # выводим
