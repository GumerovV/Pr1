import math

def main(x, esp):
 q=x
 sum=temp=0
 i=zn=1
 while abs(q-temp)>=esp:
    temp=q
    sum+=q
    i+=2
    zn*=-1
    try:
        q=zn*math.pow(x,i)/math.factorial(i)
    except OverflowError:
        print("Error: Возникло переполнение!")
        return 0
    q=zn*math.pow(x,i)/math.factorial(i)

 print("Сумма ряда с заданной точностью равна: ",sum)

def interface():
 check=True
 while(check):
  try:
      check= int(input("Для нахождения суммы ряда с заданной точностью нажмите (1), для завершения программы нажмите (0)"))
  except ValueError:
      print("Error: Введены некорректные данные!")
      check = False
  if check>1 or check<0:
      check = False
      print("Error: Введены некорректные данные!")
  if check==True:
      inp= True
      while inp:
          try:
            x = float(input("Введите значаение переменной x: "))
            esp = float(input("Введите заданную точность: "))
          except ValueError:
            print("Error: Введены некорректные данные!")
            inp= False
            break
          if esp<0:
              print("Заданныая точность должна быть положительной!")
              continue
          if inp: break
      if inp: main(x, esp)
  if check and inp:
   try:
        flag=int(input("Если хотите изменить точность нажмите (1) или (0), чтобы продолжить"))
   except ValueError:
        print("Error: Введены некорректные данные!")
        break
   if flag > 1 or flag < 0:
       print("Error: Введены некорректные данные!")
       break
   while flag:
      esp = float(input("Введите заданную точность: "))
      if esp < 0:
          print("Заданныая точность должна быть положительной!")
          continue
      main(x, esp)
      flag=int(input("Если хотите изменить точность нажмите (1) или (0), чтобы продолжить"))

interface()


