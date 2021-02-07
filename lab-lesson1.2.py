print ("Общество в начале XXI века")
def qualifier(a):
    if 0<=a<7:
        print("Детский сад")
    elif 7<=a<=18:
        print("Вам в школу")
    elif 19<=a<25:
        print("Вам в профессиональное учебное заведение")
    elif 25<=a<60:
        print("Вам на работу")
    elif 60<=a<=120:
        print("Вам предоставляется выбор")
    elif a<0 or a>120:
        print("Ошибка! Это программа для людей!")
 
print('Общество в начале XXI века')
 
user_old= int(input('Сколько вам лет? => '))
qualifier(user_old)