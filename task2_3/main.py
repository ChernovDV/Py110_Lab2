def pow_gen(base: int):
    x = 0
    while True:
        yield  base ** x    # записать функцию-генератор
        x += 1


if __name__ == "__main__":
    pow_numbers = pow_gen(10)

    for _ in range(5):
        print(next(pow_numbers))
