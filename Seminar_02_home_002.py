# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
N = int(input ("-->  "))
def NumNum (N):
    result = 1
    for i in range (1, N+1):
      result = result*i
      print  (result, ',', end = '')     
NumNum (N)

# for i in range (1, N):
#         a.append(a[i-1]*(i))
# while len(a)<N:
#         a.append(a[-1]*a[])