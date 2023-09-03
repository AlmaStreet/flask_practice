import threading

def print_numbers():
    for i in range(1, 6):
        print(f"Number {i}")

def print_letters():
    for letter in 'abcde':
        print(f"Letter {letter}")

def worker_function(number):
    result = number * 2
    print(f"Result: {result}")

if __name__ == "__main__":
    threads = []
    # thread1 = threading.Thread(target=print_numbers)
    # thread2 = threading.Thread(target=print_letters)

    numbers = [1, 2, 3, 4, 5]

    for num in numbers:
        threads.append(threading.Thread(target=worker_function, args=(num,)))

    # threads.append(threading.Thread(target=print_numbers))
    # threads.append(threading.Thread(target=print_letters))

    for thread in threads:
        thread.start()

    # thread1.start()  # Start the first thread
    # thread2.start()  # Start the second thread

    # thread1.join()   # Wait for the first thread to finish
    # thread2.join()   # Wait for the second thread to finish

    print("Both threads have finished.")