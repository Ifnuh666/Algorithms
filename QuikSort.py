from math import *

array =  [0, 5, 2, 1, 15, -5, 3, 7, 9, 8, 12, 16, -1, -20, 17, -100]
count = 0

def QuikSort(array):
    if len(array) <= 1:
        return array
    pivotIndex = floor(len(array) // 2) # Получаем опорный элемент массива
    pivot = array[pivotIndex] # Запоминаем опорный элемент
    less = [] # Создаем массив, в который будем записывать элементы меньше опорного
    greater = [] # Создаем массив, в который будем записывать элементы больше опорного
    for i in range(len(array)): # Проходимся циклом по всему массиву
        global count
        count += 1
        if i == pivotIndex: # Если элемент итерации равен опорному элементу, то пропускаем его
            continue
        if array[i] < pivot: # Если элемент итерации меньше опорного - добавляем его в массив с меньшими элементами
            less.append(array[i])
        else:
            greater.append(array[i]) # Если элемент итерации больше опорного - добавляем его в массив с большими элементами
    return QuikSort(less) + [pivot] + QuikSort(greater)

print(QuikSort(array))
print(f"Количество итераций: {count}")