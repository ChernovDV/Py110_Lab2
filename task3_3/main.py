def header_footer(fun):  # написать декоратор
    def wrapper():
        print("========")
        fun()
        print("========")
    return wrapper


@header_footer
def my_func():
    print("Hello World")


if __name__ == "__main__":
    my_func()
