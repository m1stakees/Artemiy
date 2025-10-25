АЛГОРИТМЫ СОРТИРОВКИ
Сортировка обменом (Пузырьковая)
python
def bubble_sort(collection):
    """
    Оптимизированная пузырьковая сортировка
    """
    elements_count = len(collection)
    
    for pass_num in range(elements_count):
        # Флаг для отслеживания перестановок
        had_swaps = False
        
        # Проходим по неотсортированной части
        for position in range(elements_count - pass_num - 1):
            if collection[position] > collection[position + 1]:
                # Обмен элементов
                collection[position], collection[position + 1] = \
                    collection[position + 1], collection[position]
                had_swaps = True
        
        # Если перестановок не было - массив отсортирован
        if not had_swaps:
            break

# Демонстрация
if __name__ == "__main__":
    sample_data = [64, 34, 25, 12, 22, 11, 90]
    print(f"До сортировки: {sample_data}")
    
    bubble_sort(sample_data)
    print(f"После сортировки: {sample_data}")
Сортировка вставками
python
def insertion_sort(collection):
    """
    Эффективная сортировка вставками для небольших массивов
    """
    # Начинаем со второго элемента
    for current_idx in range(1, len(collection)):
        current_value = collection[current_idx]
        compare_idx = current_idx - 1
        
        # Сдвигаем элементы больше текущего
        while compare_idx >= 0 and current_value < collection[compare_idx]:
            collection[compare_idx + 1] = collection[compare_idx]
            compare_idx -= 1
        
        # Вставляем текущее значение на правильную позицию
        collection[compare_idx + 1] = current_value

# Демонстрация
if __name__ == "__main__":
    sample_numbers = [12, 11, 13, 5, 6]
    print(f"Исходный массив: {sample_numbers}")
    
    insertion_sort(sample_numbers)
    print(f"Результат: {sample_numbers}")
Сортировка Шелла
python
def shell_sort(collection):
    """
    Улучшенная сортировка Шелла с последовательностью шагов
    """
    total_elements = len(collection)
    gap = total_elements // 2
    
    # Последовательное уменьшение шага
    while gap > 0:
        # Сортировка вставками с заданным шагом
        for i in range(gap, total_elements):
            temp = collection[i]
            j = i
            
            # Сдвиг элементов с учетом шага
            while j >= gap and collection[j - gap] > temp:
                collection[j] = collection[j - gap]
                j -= gap
            
            collection[j] = temp
        
        # Уменьшаем шаг
        gap //= 2

# Демонстрация
if __name__ == "__main__":
    test_data = [12, 34, 54, 2, 3]
    print(f"Входные данные: {test_data}")
    
    shell_sort(test_data)
    print(f"Отсортированный массив: {test_data}")
Быстрая сортировка
python
def quick_sort(collection):
    """
    Чистая реализация быстрой сортировки
    """
    # Базовый случай
    if len(collection) <= 1:
        return collection
    
    # Выбор опорного элемента
    pivot = collection[len(collection) // 2]
    
    # Разделение на три части
    smaller = [x for x in collection if x < pivot]
    equal = [x for x in collection if x == pivot]
    larger = [x for x in collection if x > pivot]
    
    # Рекурсивная сортировка и объединение
    return quick_sort(smaller) + equal + quick_sort(larger)

# Демонстрация
if __name__ == "__main__":
    unsorted_data = [3, 6, 8, 10, 1, 2, 1]
    print(f"Несортированный: {unsorted_data}")
    
    sorted_data = quick_sort(unsorted_data)
    print(f"Отсортированный: {sorted_data}")
АЛГОРИТМЫ ПОИСКА
Линейный поиск
python
def linear_search(collection, target_value):
    """
    Простой линейный поиск с подробным выводом
    """
    for idx, element in enumerate(collection):
        if element == target_value:
            return idx  # Элемент найден
    
    return -1  # Элемент не найден

# Демонстрация
if __name__ == "__main__":
    data_list = [4, 2, 7, 1, 9, 3]
    search_target = 7
    
    found_index = linear_search(data_list, search_target)
    
    if found_index != -1:
        print(f"Элемент {search_target} обнаружен на позиции {found_index}")
    else:
        print(f"Элемент {search_target} отсутствует в массиве")
Поиск по Фибоначчи
python
def fibonacci_search(collection, target_value):
    """
    Эффективный поиск по Фибоначчи для отсортированных массивов
    """
    def generate_fibonacci(limit):
        """Генерирует числа Фибоначчи до заданного предела"""
        fib_sequence = [0, 1]
        while fib_sequence[-1] < limit:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence
    
    size = len(collection)
    if size == 0:
        return -1
    
    # Получаем последовательность Фибоначчи
    fib_numbers = generate_fibonacci(size)
    
    # Инициализация переменных
    fib_idx = len(fib_numbers) - 1
    offset = 0
    
    while fib_idx > 0:
        # Вычисляем проверяемый индекс
        check_idx = min(offset + fib_numbers[fib_idx - 1], size - 1)
        
        if collection[check_idx] < target_value:
            # Сужаем поиск справа
            offset = check_idx
            fib_idx -= 1
        elif collection[check_idx] > target_value:
            # Сужаем поиск слева
            fib_idx -= 2
        else:
            # Элемент найден
            return check_idx
    
    # Проверка последнего элемента
    if fib_numbers[0] and collection[offset] == target_value:
        return offset
    
    return -1

# Демонстрация
if __name__ == "__main__":
    sorted_array = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
    target_element = 90
    
    result_index = fibonacci_search(sorted_array, target_element)
    
    if result_index != -1:
        print(f"Элемент {target_element} расположен на позиции {result_index}")
    else:
        print(f"Элемент {target_element} не обнаружен")
