from math import *
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
count = 0

def binarySearch(array, item):
    global count
    start = 0 # позиция 1 элемента
    end = len(array) - 1 # позиция последнего элемента 
    middle = None
    found  = False # переменная флаг для отображения нашли мы элемент или нет
    position = -1  # если мы не найдем элемент, то вернется -1

    while (found == False and start <= end):
        count += 1
        middle = floor(start + end) // 2
        if (array[middle] == item):
            found = True
            position = middle
            return position
        if (item < array[middle]):
            end = middle - 1
        else:
            start = middle + 1
    return position


# Бинарный поиск рекруссивынм способом

def recursiveBinarySearch(array, item, start, end): # Позиции начального и конечного элемента передаем в параметре функции
    global count
    middle = floor(start + end) // 2 # получаем значение среднего элемента
    count += 1
    if item == array[middle]: # Проводим проверку, если наш искомый элемент равен среднему элементу, то возвращаем позицию этого элемента
        return middle
    if item < array[middle]: # Если искомый элемент еньше элемента, который лежит по этому индексу, то мы возвращаем результат выполнения функции
        return recursiveBinarySearch(array, item, start, middle - 1) # Т.е. тут мы будем идти сначала массива, стартовый элемент будет равен 0
    else:
        return recursiveBinarySearch(array, item, middle + 1, end) # Тут делаем тоже самое, только смещаемся с центрального элемента на один шаг вперед и конечная позция будет end


print(recursiveBinarySearch(array, 2, 0, len(array))) # Происходит вызов функции - здесь наша стартвоая позиция равна 0, а конечная длине массива
print(f"Количество итераций: {count}")