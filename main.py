while True:
    try:
        a = int(input("Введите количество строк: "))
        if a < 1:
            print("Количество строк должно быть положительным и не должно равняться нулю.")
            continue
        break
    except ValueError:
        print("Введите целое число.")

kk = []
for i in range(a):
    s = input(f"Введите строку {i + 1}: ")
    kk.append(s)

u = set()

for s in kk:
    w = s.split()
    u.update(w)

print("Количество различных слов: ", len(u))
