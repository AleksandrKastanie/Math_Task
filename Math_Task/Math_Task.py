#Практическая работа по математике------------------------------
from random import *
from math import *
from keyboard import * 
print("Добро пожаловать на тест по матиматике, Выберите сложность от 1 до 3".center(60,"*"))
Hard=0
while Hard not in [1,2,3]:
    try: 
        Hard=int(input("Сложность: "))
    except ValueError:
        print("Только 1, 2, 3!")
    else:
        print("Просят же, 1, 2 или 3!")
if Hard==1:
   min=2
   max=10
   tehed=["+","-"]
elif Hard==2:
   min=2
   max=20
   tehed=["+","-","*"]
else:
    min=-20
    max=30
    tehed=["+","-","*","//"]

p=0#правильный ответ 
kokku=0
while True:
    v=input("Продолжаем? esc - выйти, space - продолжаем")
    if v=="stop":
        break
    else:
        kokku+=1
        a=randint(min, max)
        b=randint(min, max)
        Hard=choice(tehed)# работает только с модулем Random и выбирает из списка значение 
        if Hard=="//" :
            while b==0:
                try:
                    b=randint(min,max)
                except:
                    ValueError
        print(f"{a}{Hard}{b}=", end=" ")
        õige=eval(str(a)+Hard+str(b))
        vastus=" "
        while type (vastus) !=int:
            try:
                vastus=int(input("="))
            except ValueError:
                print("Vale vastus: Sisestage täisearv")
        if vastus==int(õige):
             print("Правильный ответ")
             p+=1
        else:
             print("Не правильный ответ")
print("kokku ülesandeid oli: ", kokku)
print("Õige vastused: ",p)
K=(p/kokku)*100
if K<60:
    print("Hinne 2, GG")
elif 60<=K<75:
    print("Hinne 3")
elif 75<=K<90:
    print("Hinne 4")
elif K>90:
    print("Hinne 5")