# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

N=int(input('Введите кол-во элементов в списке: '))

def Input_List(num):
    arr=[]
    for i in range(num):
        arr.append(float(input(f'введите {i+1} элемент: ')))
    return arr
arr=Input_List(N)
print(arr)
max_num=0
min_num=99
for i in range(N):
    if (arr[i]*100-arr[i]//1*100)<min_num:
        min_num=(arr[i]*100-arr[i]//1*100)
    if (arr[i]*100-arr[i]//1*100)>max_num:
        max_num=(arr[i]*100-arr[i]//1*100)
print((max_num-min_num)/100)