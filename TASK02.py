# находит произведение пар чисел списка. Парой считаем первый
# и последний элемент, второй и предпоследний и т.д.

# import TASK01

N=int(input('Введите кол-во элементов списка: '))
# list_num=TASK01.Input_List(N)
# print(list_num)

def Input_List(num):
    arr=[]
    for i in range(num):
        arr.append(int(input(f'введите {i+1} элемент: ')))
    return arr
arr=Input_List(N)
com_arr=[]
i=0
while i<(len(arr)/2):
    com_arr.append(arr[i]*arr[N-1-i])
    i+=1
print(com_arr)