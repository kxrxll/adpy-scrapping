from datetime import datetime


def logger(func):
    def new_func(*args):
        result = func(*args)
        function_name = func.__name__
        arguments_of_function = [args]
        using_time = datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
        with open('log.txt', 'a') as log_file:
            log_file.write(f'Name: {function_name}\n')
            log_file.write(f'Result: {result}\n')
            log_file.write(f'Date: {using_time}\n')
            for item in arguments_of_function:
                log_file.write(f'Argument: {item}\n')
            log_file.write('\n')
        return result
    return new_func

