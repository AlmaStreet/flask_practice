# def log_function_call(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__} with arguments {args} and keyword arguments {kwargs}")
#         result = func(*args, **kwargs)
#         print(f"{func.__name__} returned {result}")
#         return result
#     return wrapper

# @log_function_call
# def add(a, b):
#     return a + b

# @log_function_call
# def minus(a, b, c, d, e=10):
#     return a + b - c - d - e

# result = add(3, 5)  # Output will show function call and return value

# result = log_function_call(add(3, 5))  # Output will show function call and return value

# result = minus(20, 10, 1, 2, 15)


ls = []


def custom_decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print(f"adding to list: {args} and {kwargs['num']}")

    return wrapper


@custom_decorator
def append_list(num):
    ls.append(num)


append_list(num=1)
append_list(num=2)
append_list(num=3)

print(ls)
