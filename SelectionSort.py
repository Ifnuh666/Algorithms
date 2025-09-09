array =  [0, 5, 2, 1, 15, -5, 3, 7, 9, 8, 12, 16]
count = 0

def selectionSort(array):
    global count
    for i in range(len(array)): # Проходим по всей длине массива
        indexMin = i # Предполагаем, что первый элемент массива минимальный
        for j in range(i + 1, len(array)): # Дальше начинаем с 1-го элемента (т.е. с 5) и идем до конца
            if array[j] < array[indexMin]: # Проверяем, что j-й элемент (т.е. 5) меньше нашего первого элемента (т.е. 0; 5 < 0)
                indexMin = j # Если это так, то заменяем первый элемент на j-й
        # Если нашли элемент меньше текущего (например, в нашшем массиве -5 < 0)
        if indexMin != i:   
            count += 1
            # Совершаем обмен
            tmp = array[i] # 0
            array[i] = array[indexMin] # 0 = -5 мы записываем -5
            array[indexMin] = tmp # -5 = 0 т.е. -5 встала на индекс 0 (на первое место)
    return array

print(selectionSort(array))
print(f"Количество итераций: {count}")