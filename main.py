from time import sleep
def code(number):
    password = ''
    for n in range(1, number):
        for m in range(n + 1, number):
            if number % (n + m) == 0:
                password += str(n) + str(m)
    return password

print('Какой номер указан на камне в первом поле? (3 до 20): ')
print("Пароль: ", code(int(input())))
sleep(2)
print("Поздравляю, Вы разгадали шифр!")