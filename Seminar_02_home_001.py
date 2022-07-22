# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
num = input ("-->  ")
def del_point(num):
    del_num = num.find(',')
    if del_num != -1:
        num_1 = num[:del_num]+num[(del_num+1):] 
    else: num_1 = num
    return num_1

def count_num (num):
    num_res = int (num)
    result = 0
    for i in range(len(num)):
        a = num_res %10
        result += a 
        num_res = (num_res-a)/10
    return result

print (del_point(num))
print (count_num (del_point(num)))
    
