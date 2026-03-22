# for i in range(6):
#     print(i)
count = 0
word = 'hello world!'
for i in word:
    if i == ('o'):
       # print('yes')
       count += 1

print('count:', count)





IsHasCar = True

while IsHasCar:
    if input('Enter data: ') == 'stop':
        IsHasCar = False


for i in range(1, 11):
    if i == 5:
        break

    if i % 2 == 0:
        continue

    print(i)

