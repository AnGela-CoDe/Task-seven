a=input('Вы хотите перевести плотность или объём? ').lower()
b=float(input('Введите число для переведа в СИ '))

if a =='объём':
     def my(x, y = 1000000):
         return x /y
     print(my(b),' м**3')
if a =='плотность':
     def pl(x,y=0.000001,z=1000):
          return x/z/y
     print(pl(b),' кг/м**3')
