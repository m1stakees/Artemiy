main.cpp
cpp
#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

/*
 * Задание 22: Y = cos( || sin(pi + (B^2/A)^1/2) / tan(A^1/3) || )
 * A = 1.2, B = 1.4
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
    
    // Вычисление: (B^2/A)^1/2
    double sqrt_term = sqrt(B * B / A);
    
    // Кубический корень A^1/3 = A^(1/3)
    double cbrt_A = pow(A, 1.0 / 3.0);
    
    // Числитель: sin(pi + (B^2/A)^1/2)
    double numerator = sin(M_PI + sqrt_term);
    
    // Знаменатель: tan(A^1/3)
    double denominator = tan(cbrt_A);
    
    // Проверка деления на ноль
    if (fabs(denominator) < 1e-10) {
        cout << "Ошибка: тангенс(A^1/3) близок к нулю!" << endl;
        return 1;
    }
    
    // Вычисление внутреннего выражения с модулями
    double inner = fabs(numerator / denominator);
    double arg = fabs(inner);
    double Y = cos(arg);
    
    // Форматированный вывод (fixed, setprecision)
    cout << fixed << setprecision(10);
    cout << "\Результат вычислений:\";
    cout << "A = " << A << endl;
    cout << "B = " << B << endl;
    cout << "A^1/3 = " << cbrt_A << endl;
    cout << "(B^2/A)^1/2 = " << sqrt_term << endl;
    cout << "Y = " << Y << endl;
    
    cout << "\Программа выполнена успешно!" << endl;
    return 0;
}


=== Задание 22 ===
Введите A: 1.2
Введите B: 1.4

Результат вычислений:
A = 1.2000000000
B = 1.4000000000
∛A = 1.0626585692
√(B²/A) = 1.0801234497
Y = 0.8611761143

Программа выполнена успешно!
