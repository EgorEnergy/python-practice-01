class Variant1:
    def run(self):
        while True:
            try:
                a = float(input("Введите первое число: "))
            except ValueError:
                print("Ошибка!")
                continue

            inputUserData = input("Введите операцию (+, -, *, /, //, %, ^): ").strip()

            try:
                b = float(input("Введите второе число: "))
            except ValueError:
                print("Ошибка!")
                continue

            if inputUserData == "+":
                print(f"Результат: {a + b}")

            elif inputUserData == "-":
                print(f"Результат: {a - b}")

            elif inputUserData == "*":
                print(f"Результат: {a * b}")

            elif inputUserData == "/":
                if b == 0:
                    print("деление на ноль невозможно!")
                else:
                    print(f"Результат: {a / b}")

            elif inputUserData == "//":
                if b == 0:
                    print("деление на ноль невозможно!")
                else:
                    print(f"Результат: {a // b}")

            elif inputUserData == "%":
                if b == 0:
                    print("деление на ноль невозможно!")
                else:
                    print(f"Результат: {a % b}")

            elif inputUserData == "^":
                # Пользователь вводит ^, а Python использует **
                print(f"Результат: {a ** b}")

            else:
                print("неизвестная операция!")

            againData = input("\nПосчитать ещё (да/нет): ").strip().lower()
            if againData != "да":
                break


class Variant2:
    def run(self):
        while True:
            print("\nВыберите конвертер:")
            print("1 - Градус Цельсия -> Градус Фаренгейта")
            print("2 - Километры -> Мили")
            print("3 - Килограммы -> Фунты")
            print("4 - Метры -> Футы")
            print("0 - Назад")

            choiceUserVar2 = input("выбор: ").strip()

            if choiceUserVar2 == "0":
                break

            if choiceUserVar2 not in ("1", "2", "3", "4"): # Проверка корректного номера
                print("неизвестный номер преобразования")
                continue

            try:
                value = float(input("Введите значение: "))
            except ValueError:
                print("нужно ввести число!")
                continue

            if choiceUserVar2 == "1": # Выполняем конвертацию
                result = value * 9 / 5 + 32
                print(f"{value} C = {result:.2f} F")

            elif choiceUserVar2 == "2":
                result = value * 0.621371
                print(f"{value} км = {result:.2f} миль")

            elif choiceUserVar2 == "3":
                result = value * 2.20462
                print(f"{value} кг = {result:.2f} фунтов")

            elif choiceUserVar2 == "4":
                result = value * 3.28084
                print(f"{value} м = {result:.2f} футов")

class Variant3: # With GitHub use
    def run(self):
        while True:
            try:
                num = int(input("\nВведите целое число (0 для выхода): "))
            except ValueError:
                print("нужно ввести целое число!")
                continue

            if num == 0:
                break

            print(f"Ваше число: {num}")

            if num > 0:
                print("+: да")
            else:
                print("+: нет (отрицательное)")

            if num % 2 == 0:
                print("Четное: да")
            else:
                print("Четное: нет")

            if num % 3 == 0:
                print("Делится на 3: да")
            else:
                print("Делится на 3: нет")

            if num % 5 == 0:
                print("Делится на 5: да")
            else:
                print("Делится на 5: нет")

            n = abs(num) # Простое ли число
            if n < 2:
                print("Простое: нет")
            else:
                flag = True  # пока считаем простым
                # Проверяем делители от 2 до корня из n
                for d in range(2, int(n ** 0.5) + 1):
                    if n % d == 0:
                        flag = False
                        break
                if flag:
                    print("Простое: да")
                else:
                    print("Простое: нет")

            digitsData = len(str(abs(num))) # Количество цифр
            print(f"Количество цифр {digitsData}")

            # Проверка на полный квадрат
            #  Полный квадрат — это число, которое получается при умножении целого числа на само себя (например, 49 = 7*7)
            if num >= 0:  # Отрицательные числа не могут быть полными квадратами
                # Извлекаем корень (возводим в степень 0.5) и отбрасываем дробную часть через int()
                root = int(num ** 0.5)
                # Если корень умноженный сам на себя дает исходное число — значит это полный квадрат
                if root * root == num:
                    print("Полный квадрат: да")
                else:
                    print("Полный квадрат: нет")
            else:
                print("Полный квадрат: нет (число отрицательное)")

            again = input("Проверить ещё одно число? (да/нет): ").strip().lower()
            if again != "да":
                print("Работа программы завершена.")
                break  # Выходим из цикла


class Variant4:
    def run(self):
        print("\nКАЛЬКУЛЯТОР СТОИМОСТИ ПОКУПКИ ")

        listData = [] # список для хранения позиций

        while True: # добавления товаров
            name = input("\nНазвание товара: ").strip()
            if name == "":
                print("название не может быть пустым")
                continue

            try:
                price = float(input("Цена товара: "))
                if price <= 0:
                    print("цена должна быть больше 0")
                    continue
            except ValueError:
                print("нужно ввести число!")
                continue

            try:
                quantity = int(input("Количество: "))
                if quantity <= 0:
                    print("количество должно быть больше 0.")
                    continue
            except ValueError:
                print("нужно ввести целое число!")
                continue

            position_total = price * quantity # Стоимость позиции

            listData.append({ # Сохраняем в корзину
                "name": name,
                "price": price,
                "quantity": quantity,
                "total": position_total
            })

            more = input("Добавить ещё товар (да/нет): ").strip().lower()
            if more != "да":
                break

        total_sum = 0 # Считаем общую сумму
        for item in listData:
            total_sum += item["total"]

        # Определяем скидку
        if total_sum >= 15000:
            discount_percent = 15
        elif total_sum >= 10000:
            discount_percent = 10
        elif total_sum >= 5000:
            discount_percent = 5
        else:
            discount_percent = 0

        # Скидка в рублях и итог
        discountRub = total_sum * discount_percent / 100
        finalPrice = total_sum - discountRub

        # Вывод чека
        print("\nЧЕК")
        for item in listData:
            print(item['name'], item['price'], "x", item['quantity'], "=", item['total'])
        print("Исходная стоимость:", total_sum)
        print("Скидка:", discount_percent, "%")
        print("Скидка в рублях:", discountRub)
        print("Итоговая цена:", finalPrice)



class Main:
    def run(self):
        while True:
            print("1 - Вариант 1. Консольный калькулятор")
            print("2 - Вариант 2. Конвертер единиц")
            print("3 - Вариант 3. Проверка числа")
            print("4 - Вариант 4. Стоимость покупки")
            print("0 - Выход")

            choiceMain = input("Выбери вариант: ").strip()

            if choiceMain == "0":
                print("Выход из программы.")
                break

            elif choiceMain == "1":
                Variant1().run()

            elif choiceMain == "2":
                Variant2().run()

            elif choiceMain == "3":
                Variant3().run()

            elif choiceMain == "4":
                Variant4().run()

            else:
                print("Нет такого варианта")


Main().run()