import multiprocessing

def worker_function(number):
    result = number * 2
    print(f"Result: {result}")

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    processes = []

    for num in numbers:
        process = multiprocessing.Process(target=worker_function, args=(num,))
        processes.append(process)
        process.start()

    # for process in processes:
    #     process.join()

    print("All processes have finished.")