main.cpp (консольный ввод)
cpp
#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

/*
 * Задание 22: Y = cos( || sin(π + √(B²/A)) / tan(∛A) || )
 * A = 1.2, B = 1.4
 * Тема: Ввод-вывод данных в C++
 */

int main() {
    double A, B;
    
    // Форматированный ввод с консоли (оператор >>)
    cout << "=== Задание 22 ===\n";
    cout << "Введите A: ";
    cin >> A;
    cout << "Введите B: ";
    cin >> B;
    
    // Проверка корректности ввода
    if (cin.fail()) {
        cout << "Ошибка ввода данных!" << endl;
        return 1;
    }
    
    // Вычисление: √(B²/A)
    double sqrt_term = sqrt(B * B / A);
    
    // Кубический корень ∛A = A^(1/3)
    double cbrt_A = pow(A, 1.0 / 3.0);
    
    // Числитель: sin(π + √(B²/A))
    double numerator = sin(M_PI + sqrt_term);
    
    // Знаменатель: tan(∛A)
    double denominator = tan(cbrt_A);
    
    // Проверка деления на ноль
    if (fabs(denominator) < 1e-10) {
        cout << "Ошибка: тангенс(∛A) близок к нулю!" << endl;
        return 1;
    }
    
    // Вычисление внутреннего выражения с модулями
    double inner = fabs(numerator / denominator);
    double arg = fabs(inner);
    double Y = cos(arg);
    
    // Форматированный вывод (fixed, setprecision)
    cout << fixed << setprecision(10);
    cout << "\nРезультат вычислений:\n";
    cout << "A = " << A << endl;
    cout << "B = " << B << endl;
    cout << "∛A = " << cbrt_A << endl;
    cout << "√(B²/A) = " << sqrt_term << endl;
    cout << "Y = " << Y << endl;
    
    cout << "\nПрограмма выполнена успешно!" << endl;
    return 0;
}
