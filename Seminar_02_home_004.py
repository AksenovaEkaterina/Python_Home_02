# Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
N = int(input ("-->  "))
def NumNum (N):
    a = []
    start = -N
    finish = N
    a_a = 1
    for i in range (start, finish+1): 
        a.append (i)
        a_a = a_a*i
    print  (a)
    print  ("произведение элементов = ", a_a)
NumNum (N)