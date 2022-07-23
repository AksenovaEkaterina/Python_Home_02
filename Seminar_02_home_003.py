# Задать список из n чисел последовательности (1+1/n)**n и вывести на экран их сумму
# Пример: Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
N = int(input ("-->  "))
def NumNum (N):
    a = []
    sum_a = 0
    for i in range (1, N+1): 
        a.append ((1+1/i)**i)
        sum_a += a[i-1]
    print  (a, ',', end = '')
    print  (' sum = ' , sum_a )        
NumNum (N)
