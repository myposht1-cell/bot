age = int(input('Сколько вам лет?: '))
if age <= 17:
    print('Вход запрещен')
if age < 0 or age >= 100:
    print('Некоректный возраст')


elif age >= 18:
    print('Можете входить')
elif age >= 25:
    print('Вип зал')

