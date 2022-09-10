#  Программа, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

N=int(input('Введите кол-во элементов в списке: '))

def Input_List(num):
    arr=[]
    for i in range(num):
        arr.append(int(input()))
    return arr

arr = Input_List(N)
print(arr)
summ=0
for i in range(0,len(arr),2):
    summ+=arr[i]
print(summ)
