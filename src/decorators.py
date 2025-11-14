from functools import wraps


def print_to_file_or_console(text: str, filename: str = "") -> None:
    """Выводит сообщение text в файл(если в параметре filename передано имя файла) или в консоль"""
    if filename:
        with open(filename, "a") as file:
            file.write(text + "\n")
    else:
        print(text)


def log(filename: str = ""):
    """Декоратор, который логирует начало, результат и конец выполнения функции
    в файл(если указано имя файла) или в консоль"""
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs) -> object:

            if filename:
                file = open(filename, "w")
                file.close()

            print_to_file_or_console(f"start of executing {func.__name__}", filename)

            result = None

            try:
                result = func(*args, **kwargs)
            except Exception as e:
                err_type = str(type(e))
                text = f"{func.__name__} error: {err_type}. Inputs: {args}, {kwargs}"
                print_to_file_or_console(text, filename)
            else:
                text = f"{func.__name__} result = {result}"
                print_to_file_or_console(text, filename)

            print_to_file_or_console(f"finish of executing {func.__name__}", filename)
            return result

        return inner

    return wrapper
