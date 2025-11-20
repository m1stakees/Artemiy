def min_coins(coins, S):
    coins.sort(reverse=True)
    count = 0
    
    for coin in coins:
        if S >= coin:
            num = S // coin
            count += num
            S -= num * coin
    
    return count

print("Введите номиналы монет через пробел (например: 1 5 10 25):")
coins_input = input().strip()

try:
    coins = list(map(int, coins_input.split()))
    if not coins:
        print("Ошибка: список номиналов пуст!")
        exit()
    if any(c <= 0 for c in coins):
        print("Ошибка: номиналы должны быть положительными числами!")
        exit()
except ValueError:
    print("Ошибка: введите только целые числа через пробел!")
    exit()

print("Введите сумму для размена:")
try:
    S = int(input())
    if S < 0:
        print("Ошибка: сумма должна быть неотрицательной!")
        exit()
except ValueError:
    print("Ошибка: введите целое число!")
    exit()

result = min_coins(coins, S)
print(f"Минимальное количество монет для размена: {result}")


# Вывод програмного кода при использовании онлайн-компилятора Jdoodle:
# Введите номиналы монет через пробел (например: 1 5 10 25):
# 1 3 6 9
# Введите сумму для размена:
# 4
# Минимальное количество монет для размена: 2
