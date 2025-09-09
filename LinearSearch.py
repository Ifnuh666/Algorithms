# Линейный поиск

array = [1, 2, 8, 5, 4, 78, 3]
count = 0

def leneSearching(array, item):
    global count
    for i in range(len(array)):
        count += 1
        if array[i] == item:
            return i
    return None

print(leneSearching(array, 3))
print(f"Количество итераций: {count}")