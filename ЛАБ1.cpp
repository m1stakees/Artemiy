// Массив на C++
#include <iostream>
#include <vector>
using namespace std;

int main() {
    const int SIZE = 7;
    vector<int> numbers(SIZE);
    
    cout << "Введите " << SIZE << " чисел: ";
    for(int i = 0; i < SIZE; ++i) {
        cin >> numbers[i];
    }
    
    // Вывод для проверки
    cout << "Введенные числа: ";
    for(int num : numbers) {
        cout << num << " ";
    }
    cout << endl;
    
    return 0;
}

// Стек на C++
#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main() {
    stack<string> wordStack;
    
    // Добавление элементов
    wordStack.push("apple");
    wordStack.push("banana");
    wordStack.push("cherry");
    
    cout << "Размер стека: " << wordStack.size() << endl;
    
    // Демонстрация работы стека
    cout << "Элементы в стеке (LIFO): ";
    while(!wordStack.empty()) {
        cout << wordStack.top() << " ";
        wordStack.pop();
    }
    cout << endl;
    
    return 0;
}
