def task(numbers: list) -> int:
    gen_exp = (number**2 for number in numbers)  # записать выражение-генератор для возведения чисел в квадрат
    return sum(gen_exp)


if __name__ == "__main__":
    list_numbers = [i for i in range(1, 11)]  # list(range(1, 11))
    print(task(list_numbers))
