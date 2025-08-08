import time

def Calctime(function]):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function](*args, **kwargs)
        end = time.time()
        execution_time = end - start
        print(f"Execution time: {execution_time:.2f} seconds.")
        return result
    return wrapper

@Calctime
# CREATE YOUR FUNCTION HERE
