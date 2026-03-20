print('Введите значения первого элемента, множитель прогрессии и номер последнего элемеента')
string =input().split()
b = int(string[0])
q = int(string[1])
n = int(string[2])

def sumGP(b,q,n): 
    sum = (b *(1- q**n) / (1-q))
    return sum

a = print(int(sumGP(b,q,n)))