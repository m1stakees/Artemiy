# 1) Пример кода для Блочной(корзинной) сортировки.
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


# 2) Пример кода Блинной сортировки.

def pancake_sort(arr):
    """
    Блинная сортировка - сортировка массива с помощью переворотов
    """
    n = len(arr)
    
    # Постепенно уменьшаем размер неотсортированной части
    for curr_size in range(n, 1, -1):
        # Находим индекс максимального элемента в неотсортированной части
        max_idx = find_max_index(arr, curr_size)
        
        # Если максимальный элемент не на своем месте
        if max_idx != curr_size - 1:
            # Переворачиваем так, чтобы максимальный элемент оказался в начале
            if max_idx != 0:
                print(f"Переворот 1: ставим максимум {arr[max_idx]} в начало")
                flip(arr, max_idx)
            
            # Переворачиваем всю неотсортированную часть, 
            # чтобы максимум оказался на своем месте
            print(f"Переворот 2: ставим максимум {arr[0]} на позицию {curr_size-1}")
            flip(arr, curr_size - 1)
        
        print(f"Текущее состояние массива: {arr}")
    
    return arr

def flip(arr, k):
    """
    Переворачивает первые k элементов массива
    """
    left = 0
    right = k
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

def find_max_index(arr, n):
    """
    Находит индекс максимального элемента в первых n элементах
    """
    max_idx = 0
    for i in range(1, n):
        if arr[i] > arr[max_idx]:
            max_idx = i
    return max_idx

# Демонстрация работы
if __name__ == "__main__":
    print("=== БЛИННАЯ СОРТИРОВКА ===")
    test_array = [3, 1, 4, 2, 5]
    print(f"Исходный массив: {test_array}")
    print("\nПроцесс сортировки:")
    result = pancake_sort(test_array.copy())
    print(f"\nОтсортированный массив: {result}")


# Результат работы кода Блинной сортироки.
Исходный массив: [3, 1, 4, 2, 5]

Процесс сортировки:
Текущее состояние массива: [3, 1, 4, 2, 5]
Переворот 1: ставим максимум 4 в начало
Переворот 2: ставим максимум 4 на позицию 3
Текущее состояние массива: [2, 3, 1, 4, 5]
Переворот 1: ставим максимум 3 в начало
Переворот 2: ставим максимум 3 на позицию 2
Текущее состояние массива: [1, 2, 3, 4, 5]
Текущее состояние массива: [1, 2, 3, 4, 5]

Отсортированный массив: [1, 2, 3, 4, 5]


# 3) Сортировка бусинами 

def bead_sort(arr):
    """
    Сортировка бусинами (гравитационная сортировка)
    Работает только для неотрицательных целых чисел
    """
    if not arr:
        return arr
    
    # Находим максимальное значение в массиве
    max_val = max(arr)
    
    # Создаем "абак" - матрицу бусин
    abacus = [[0] * len(arr) for _ in range(max_val)]
    
    print(f"Создан абак размером {max_val} x {len(arr)}")
    print("Размещаем бусины...")
    
    # Размещаем бусины в абаке
    for i, num in enumerate(arr):
        for j in range(num):
            abacus[j][i] = 1
    
    print("Абак после размещения бусин:")
    print_abacus(abacus)
    
    print("\nПрименяем гравитацию...")
    
    # Применяем "гравитацию" - бусины падают вниз
    for i in range(len(abacus)):
        # Считаем количество бусин в ряду
        bead_count = sum(abacus[i])
        
        # Создаем новый ряд с бусинами слева
        new_row = [1] * bead_count + [0] * (len(arr) - bead_count)
        abacus[i] = new_row
    
    print("Абак после гравитации:")
    print_abacus(abacus)
    
    # Собираем результат - считаем бусины в каждом столбце
    result = []
    for col in range(len(arr)):
        column_sum = sum(abacus[row][col] for row in range(max_val))
        result.append(column_sum)
    
    return result

def print_abacus(abacus):
    """Визуализация абака"""
    for row in reversed(abacus):  # переворачиваем для наглядности
        print(' '.join('●' if cell else '○' for cell in row))

# Демонстрация работы
if __name__ == "__main__":
    print("=== СОРТИРОВКА БУСИНАМИ ===")
    test_array = [3, 1, 4, 2]
    print(f"Исходный массив: {test_array}")
    print("\nПроцесс сортировки:")
    
    result = bead_sort(test_array)
    print(f"\nОтсортированный массив: {result}")

# Результат работы кода сортировки бусинами.

Исходный массив: [3, 1, 4, 2]

Процесс сортировки:
Создан абак размером 4 x 4
Размещаем бусины...
Абак после размещения бусин:
○ ○ ● ○
● ○ ● ○
● ○ ● ●
● ● ● ●

Применяем гравитацию...
Абак после гравитации:
● ○ ○ ○
● ● ○ ○
● ● ● ○
● ● ● ●

Отсортированный массив: [4, 3, 2, 1]

# 4) код для поиска cкачками:

import math

def jump_search(arr, target):
    """
    Поиск прыжками в отсортированном массиве
    """
    n = len(arr)
    
    # Если массив пустой
    if n == 0:
        return -1
    
    # Определяем размер прыжка
    step = int(math.sqrt(n))
    print(f"Размер массива: {n}, размер прыжка: {step}")
    
    # Поиск блока, где может находиться элемент
    prev = 0
    while arr[min(step, n) - 1] < target:
        print(f"Прыжок: проверяем элемент arr[{min(step, n) - 1}] = {arr[min(step, n) - 1]}")
        prev = step
        step += int(math.sqrt(n))
        
        # Если вышли за границы массива
        if prev >= n:
            return -1
    
    print(f"Целевой элемент между индексами {prev} и {min(step, n)}")
    
    # Линейный поиск в найденном блоке
    print("Выполняем линейный поиск в блоке...")
    while arr[prev] < target:
        print(f"Проверяем arr[{prev}] = {arr[prev]}")
        prev += 1
        
        # Если дошли до конца блока или массива
        if prev == min(step, n):
            return -1
    
    # Проверяем, найден ли элемент
    if arr[prev] == target:
        print(f"Найден элемент arr[{prev}] = {arr[prev]}")
        return prev
    else:
        print("Элемент не найден")
        return -1

# Демонстрация работы
if __name__ == "__main__":
    print("=== ПОИСК ПРЫЖКАМИ ===")
    
    # Отсортированный массив для поиска
    sorted_array = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    target = 55
    
    print(f"Отсортированный массив: {sorted_array}")
    print(f"Целевой элемент: {target}")
    print("\nПроцесс поиска:")
    
    result = jump_search(sorted_array, target)
    
    if result != -1:
        print(f"\nЭлемент {target} найден на позиции {result}")
    else:
        print(f"\nЭлемент {target} не найден в массиве")

# Дополнительные примеры
def jump_search_examples():
    print("\n" + "="*50)
    print("ДОПОЛНИТЕЛЬНЫЕ ПРИМЕРЫ:")
    
    test_cases = [
        ([1, 3, 5, 7, 9, 11, 13, 15], 7),
        ([1, 3, 5, 7, 9, 11, 13, 15], 10),
        ([2, 4, 6, 8, 10], 2),
        ([2, 4, 6, 8, 10], 11)
    ]
    
    for arr, target in test_cases:
        print(f"\nМассив: {arr}, поиск: {target}")
        result = jump_search(arr, target)
        print(f"Результат: {'Найден' if result != -1 else 'Не найден'}")

# Запуск дополнительных примеров
jump_search_examples()

Результат работы кода поиска скачками: 

Отсортированный массив: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
Целевой элемент: 55

Процесс поиска:
Размер массива: 16, размер прыжка: 4
Прыжок: проверяем элемент arr[3] = 2
Прыжок: проверяем элемент arr[7] = 13
Целевой элемент между индексами 8 и 12
Выполняем линейный поиск в блоке...
Проверяем arr[8] = 21
Проверяем arr[9] = 34
Найден элемент arr[10] = 55

Элемент 55 найден на позиции 10
