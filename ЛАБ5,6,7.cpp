#include <iostream>
#include <algorithm>

// Оптимизированная функция сортировки выбором
void selectionSort(int data[], int size) {
    for (int current = 0; current < size - 1; ++current) {
        int minPosition = current;
        
        // Поиск минимального элемента в неотсортированной части
        for (int next = current + 1; next < size; ++next) {
            if (data[next] < data[minPosition]) {
                minPosition = next;
            }
        }
        
        // Обмен элементов, если нашли меньший
        if (minPosition != current) {
            std::swap(data[current], data[minPosition]);
        }
    }
}

// Универсальная функция вывода массива
void displayArray(const int data[], int size) {
    for (int i = 0; i < size; ++i) {
        std::cout << data[i] << " ";
    }
    std::cout << "\n";
}

int main() {
    int numbers[] = {64, 25, 12, 22, 11};
    int count = sizeof(numbers) / sizeof(numbers[0]);
    
    std::cout << "Исходный массив:\n";
    displayArray(numbers, count);
    
    selectionSort(numbers, count);
    
    std::cout << "Отсортированный массив:\n";
    displayArray(numbers, count);
    
    return 0;
}
