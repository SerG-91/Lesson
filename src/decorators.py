from functools import wraps


def log(filename=None):
    """Декоратор автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки."""
    def dekorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not filename:
                print(f'{func.__name__} started')
                try:
                    func(*args, **kwargs)
                    print(f'{func.__name__} ok')
                    print(f'{func.__name__} finished')
                except Exception as e:
                    print(f'{func.__name__} error: {e}. Inputs: {args}, {kwargs}')
            else:
                try:
                    func(*args, **kwargs)
                    with open(filename, 'w') as file:
                        file.write(f'{func.__name__} ok')
                except Exception as e:
                    with open(filename, 'w') as file:
                        file.write(f'{func.__name__} error: {e}. Inputs: {args}, {kwargs}')
            # return result
        return wrapper
    return dekorator