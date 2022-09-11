# преобразовывает десятичное число в двоичное.

N=int(input('Введите десятичное число: '))

dif=N
num=[]
# num_new=0
num_new=[]
while dif!=0:
    num.append(dif-((dif//2)*2))
    dif=dif//2
print(num)

for i in range((len(num)-1), -1, -1):
    # num_new=num[i]
    num_new.append(num[i])
    # print(num_new)
print(num_new)


   
