def select_non_overlapping_tasks(tasks):
    """
    Жадный алгоритм выбора максимального количества непересекающихся задач
    """
    # Сортируем задачи по времени окончания
    sorted_tasks = sorted(tasks, key=lambda x: x[1])
    
    selected = []
    last_end = 0  # Время окончания последней выбранной задачи
    
    for start, end in sorted_tasks:
        # Выбираем задачу, если она не пересекается с предыдущей
        if start >= last_end:
            selected.append((start, end))
            last_end = end
    
    return selected, len(selected)

def main():
    try:
        # Ввод количества задач
        n = int(input("Введите количество задач: "))
        if n <= 0:
            print("Количество задач должно быть положительным числом")
            return
            
        tasks = []
        
        # Ввод данных для каждой задачи
        for i in range(n):
            while True:
                try:
                    start = int(input(f"Задача {i+1}: Введите время начала: "))
                    end = int(input(f"Задача {i+1}: Введите время окончания: "))
                    
                    if start >= end:
                        print("Время начала должно быть меньше времени окончания. Повторите ввод.")
                        continue
                        
                    tasks.append((start, end))
                    break
                    
                except ValueError:
                    print("Ошибка: введите целые числа")
        
        # Выполнение алгоритма
        selected_tasks, count = select_non_overlapping_tasks(tasks)
        
        # Вывод результатов
        print("\nВыбранные задачи:")
        for task in selected_tasks:
            print(f"Начало: {task[0]}, Конец: {task[1]}")
        print(f"Общее количество выбранных задач: {count}")
        
    except ValueError:
        print("Ошибка ввода данных")

if __name__ == "__main__":
    main()
