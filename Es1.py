import numpy as np

#Esercizio 1
list1 = []
for i in range(1,11):
    list1.append(i)
print(list1)

list1 = [x for x in range(1,11)]
print(list1)

list2 = []
for i in range(1,11):
    if i % 2 == 0:
        list2.append(i)
print(list2)

list2 = [x for x in range(1,11) if x % 2 == 0]
print(list2)

list3 = []
for i in list2:
    list3.append(i**2)
print(list3)

list3 = [x**2 for x in list2]
print(list3)


#Esercizio 
list4 = np.array(list1)
print(list4.size)
print(list4.dtype)

def primo(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

list5 = [x for x in range(1,11) if primo(x)]
print(list5)

#Esercizio 3
list6 = [x for x in range(1,11)]
a = np.array(list6)
print(a)

b = a[3:6]
print(b)

c = np.flip(a)
print(c)
print(a/c)

list7 = [x for x in list6[3:6]]
list8 = [x for x in list6[::-1]]

j = 0
for i in list6: 
    print(i/list8[j])
    j += 1


