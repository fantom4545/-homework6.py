x=44
print('Hello')
if x>33:
    print('OK')
print('Goodbye')
# примеры
a, b =10, 4
if a > b:
    print('a > b')
if a > b and a > 0:
    print("успех")
if (a > b) and (a > 0 or b < 1000):
    print("успех")
if 4 < b and b > 10:
    print("успех")
# можно сравннивать - числа, строки, списки
if '34' > '123':
    print("успех")
if [1 ,2] > [1 ,2]:
    print("успех")
#нельзя сравнивать - разнные типы
#if '6' > 5:
    #print("успех")
#if [5 , 6] > 5:
    #print("успех")
#но
if '6'!= 5:
    print("успех")