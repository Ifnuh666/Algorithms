array =  [0, 5, 2, 1, 15, -5, 3, 7, 9, 8, 12, 16, -1, -20, 17]
count = 0

def BubbleSort(array):
    global count
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j + 1] < array[j]: # Сравниваем последующий элемент и текущий, например, 5 и 2. 5 < 2, значит меняем их местами
                tmp = array[j] # 5[1]
                array[j] = array[j + 1] # 5[1] = 2[2]. Записываем 2
                array[j + 1] = tmp # 2[1] = 5[2] т.е. 5 встала на индекс 2
            count += 1
    return array

print(BubbleSort(array))
print(f"Количество итераций: {count}")