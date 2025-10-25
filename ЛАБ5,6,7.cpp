АЛГОРИТМЫ СОРТИРОВКИ
Сортировка выбором (Selection Sort)
cpp
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
Сортировка слиянием (Merge Sort)
cpp
#include <iostream>
#include <vector>

class MergeSorter {
public:
    static void sort(std::vector<int>& data) {
        if (data.size() > 1) {
            mergeSort(data, 0, data.size() - 1);
        }
    }

private:
    static void mergeSort(std::vector<int>& data, int start, int end) {
        if (start >= end) return;
        
        int middle = start + (end - start) / 2;
        mergeSort(data, start, middle);
        mergeSort(data, middle + 1, end);
        merge(data, start, middle, end);
    }

    static void merge(std::vector<int>& data, int start, int middle, int end) {
        std::vector<int> left(data.begin() + start, data.begin() + middle + 1);
        std::vector<int> right(data.begin() + middle + 1, data.begin() + end + 1);
        
        int i = 0, j = 0, k = start;
        
        while (i < left.size() && j < right.size()) {
            data[k++] = (left[i] <= right[j]) ? left[i++] : right[j++];
        }
        
        // Добавляем оставшиеся элементы
        while (i < left.size()) data[k++] = left[i++];
        while (j < right.size()) data[k++] = right[j++];
    }
};

int main() {
    std::vector<int> numbers = {38, 27, 43, 3, 9, 82, 10};
    
    std::cout << "Исходный массив: ";
    for (int num : numbers) std::cout << num << " ";
    std::cout << "\n";
    
    MergeSorter::sort(numbers);
    
    std::cout << "Отсортированный массив: ";
    for (int num : numbers) std::cout << num << " ";
    std::cout << "\n";
    
    return 0;
}
Пирамидальная сортировка (Heap Sort)
cpp
#include <iostream>
#include <vector>

class HeapSorter {
public:
    static void sort(std::vector<int>& data) {
        int size = data.size();
        
        // Построение max-кучи
        for (int i = size / 2 - 1; i >= 0; --i) {
            heapify(data, size, i);
        }
        
        // Последовательное извлечение элементов
        for (int i = size - 1; i > 0; --i) {
            std::swap(data[0], data[i]);
            heapify(data, i, 0);
        }
    }

private:
    static void heapify(std::vector<int>& data, int heapSize, int root) {
        int largest = root;
        int left = 2 * root + 1;
        int right = 2 * root + 2;
        
        if (left < heapSize && data[left] > data[largest]) {
            largest = left;
        }
        
        if (right < heapSize && data[right] > data[largest]) {
            largest = right;
        }
        
        if (largest != root) {
            std::swap(data[root], data[largest]);
            heapify(data, heapSize, largest);
        }
    }
};

int main() {
    std::vector<int> numbers = {12, 11, 13, 5, 6, 7};
    
    std::cout << "Исходный массив: ";
    for (int num : numbers) std::cout << num << " ";
    std::cout << "\n";
    
    HeapSorter::sort(numbers);
    
    std::cout << "Отсортированный массив: ";
    for (int num : numbers) std::cout << num << " ";
    std::cout << "\n";
    
    return 0;
}
АЛГОРИТМЫ ПОИСКА
Бинарный поиск
cpp
#include <iostream>
#include <vector>

class BinarySearch {
public:
    static int find(const std::vector<int>& data, int target) {
        int left = 0;
        int right = data.size() - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            if (data[mid] == target) {
                return mid;
            } else if (data[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return -1; // Элемент не найден
    }
};

int main() {
    std::vector<int> numbers = {2, 3, 4, 10, 40};
    int target = 10;
    
    int position = BinarySearch::find(numbers, target);
    
    if (position != -1) {
        std::cout << "Элемент " << target << " найден на позиции: " << position << "\n";
    } else {
        std::cout << "Элемент " << target << " не найден.\n";
    }
    
    return 0;
}
Интерполирующий поиск
cpp
#include <iostream>
#include <vector>

class InterpolationSearch {
public:
    static int find(const std::vector<int>& data, int target) {
        int low = 0;
        int high = data.size() - 1;
        
        while (low <= high && target >= data[low] && target <= data[high]) {
            // Расчет позиции с интерполяцией
            int pos = low + ((double)(high - low) / (data[high] - data[low])) * (target - data[low]);
            
            if (data[pos] == target) {
                return pos;
            } else if (data[pos] < target) {
                low = pos + 1;
            } else {
                high = pos - 1;
            }
        }
        
        return -1; // Элемент не найден
    }
};

int main() {
    std::vector<int> numbers = {10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47};
    int target = 18;
    
    int position = InterpolationSearch::find(numbers, target);
    
    if (position != -1) {
        std::cout << "Элемент " << target << " найден на позиции: " << position << "\n";
    } else {
        std::cout << "Элемент " << target << " не найден.\n";
    }
    
    return 0;
}
