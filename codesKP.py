# Пример кода для Блочной(корзинной) сортировки.
def bucket_sort(arr):
    """
    Блочная (корзинная) сортировка для чисел в диапазоне [0, 1)
    """
    if len(arr) == 0:
        return arr
    
    # 1. Создаем пустые корзины
    n = len(arr)
    buckets = [[] for _ in range(n)]
    
    # 2. Распределяем элементы по корзинам
    for num in arr:
        # Определяем индекс корзины
        bucket_index = int(num * n)
        buckets[bucket_index].append(num)
    
    # 3. Сортируем каждую корзину
    for bucket in buckets:
        bucket.sort()  # можно использовать любую сортировку
    
    # 4. Объединяем отсортированные корзины
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)
    
    return sorted_arr

# Универсальная версия для любых чисел
def bucket_sort_general(arr, bucket_size=10):
    """
    Блочная сортировка для произвольных чисел
    """
    if len(arr) == 0:
        return arr
    
    # Находим минимальное и максимальное значения
    min_val = min(arr)
    max_val = max(arr)
    
    # Определяем количество корзин
    bucket_count = (max_val - min_val) // bucket_size + 1
    buckets = [[] for _ in range(int(bucket_count))]
    
    # Распределяем элементы по корзинам
    for num in arr:
        bucket_index = int((num - min_val) // bucket_size)
        buckets[bucket_index].append(num)
    
    # Сортируем каждую корзину и объединяем
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))
    
    return sorted_arr

# Пример использования
if __name__ == "__main__":
    # Тест для чисел в диапазоне [0, 1)
    test_arr1 = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
    print("Исходный массив 1:", test_arr1)
    sorted_arr1 = bucket_sort(test_arr1)
    print("Отсортированный массив 1:", sorted_arr1)
    
    # Тест для произвольных чисел
    test_arr2 = [42, 32, 33, 52, 37, 47, 51, 29, 68, 15]
    print("\nИсходный массив 2:", test_arr2)
    sorted_arr2 = bucket_sort_general(test_arr2, bucket_size=10)
    print("Отсортированный массив 2:", sorted_arr2)

# Результат работы кода Блочной(корзинной) сортировки.
Исходный массив 1: [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
Отсортированный массив 1: [0.32, 0.33, 0.37, 0.42, 0.47, 0.51, 0.52]

Исходный массив 2: [42, 32, 33, 52, 37, 47, 51, 29, 68, 15]
Отсортированный массив 2: [15, 29, 32, 33, 37, 42, 47, 51, 52, 68]



