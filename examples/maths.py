def fibonacci_save_result(func):
    saved_result = {}
    def __inner__(n: int):
        if n in saved_result:
            return saved_result[n]
        else:
            result = func(n)
            saved_result[n] = result
            return result
    return __inner__


@fibonacci_save_result
def fibonacci(n: int):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

