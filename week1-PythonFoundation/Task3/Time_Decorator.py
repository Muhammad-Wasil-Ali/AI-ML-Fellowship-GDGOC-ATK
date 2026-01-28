import time

def execution_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Execution time: {end - start:.4f} seconds")
    return wrapper
@execution_time
def slow_function():
    time.sleep(2)
    print("Function finished")

slow_function()
