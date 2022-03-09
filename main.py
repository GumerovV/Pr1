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
 return sum

def CHECK():
    check = True
    while check:
        try:
            x = float(input())
            check = False
            if x > 1 or x < 0:
                print("Error: Введены некорректные данные!")
                check = True
        except ValueError:
            print("Error: Введены некорректные данные!")
    return x

def interface():
 check=True
 while(check):
  print("Для нахождения суммы ряда с заданной точностью нажмите (1), для завершения программы нажмите (0)")
  check= CHECK()
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
          if inp: break
      print("Сумма ряда с заданной точностью равна: ", main(x, esp))
  if check and inp:
   print("Если хотите изменить точность нажмите (1) или (0), чтобы продолжить")
   flag = CHECK()
   while flag:
      try:
          esp = float(input("Введите заданную точность: "))
          if esp<0:
             print("Error: Заданная точность должна быть положительной!")
             continue
      except ValueError:
          print("Error: Введены некорректные данные!")
          continue
      print("Сумма ряда с заданной точностью равна: ", main(x, esp))
      print("Если хотите изменить точность нажмите (1) или (0), чтобы продолжить")
      flag = CHECK()

interface()