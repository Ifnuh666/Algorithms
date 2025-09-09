graph = {} # Создается пустой граф

# Прописываем из каких вершин к каким мы можем попасть
graph['a'] = ['b', 'c']
graph['b'] = ['f']
graph['c'] = ['d', 'e']
graph['d'] = ['f']
graph['e'] = ['f']
graph['f'] = ['g']

def breadthSearch(graph, start, end): # В параметры функции передаем начальную точку и конечную
    queue = [] # создаем пустой массив
    visited = set() # Создаем пустое множество
    queue.append(start) # Добавляем в нашу очередь стартовую вершину
    visited.add(start)
    while len(queue) > 0: # Цикл будет идти до тех пор, пока в нашей очереди есть хотя бы один элемент
        current = queue.pop(0) # Достаем из очереди текущую вершину
        if current not in graph: # Проверяем, если по этой вершине в графе ничего нет, то делаем пустой массив, тем самым даем понять, что дальше ничего нет
            graph[current] = []
        if end in graph[current]: # Если в графе по текущей вершине есть конечная точка, то завершаем поиск и возвращаем True
            return True
        else: # Если предыдущее условие не сработало, то добавляем новые вершины
            for neighbor in graph[current]:  
                if neighbor not in visited:  
                    queue.append(neighbor)
                    visited.add(neighbor)  
    return False

print(breadthSearch(graph, 'a', 'g'))