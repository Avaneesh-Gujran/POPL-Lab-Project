import threading
import queue

def data_producer(data_queue):
    # Simulated data source
    data = ["Data 1", "Data 2", "Data 3"]
    for item in data:
        data_queue.put(item)

def data_consumer(data_queue):
    while not data_queue.empty():
        item = data_queue.get()
        # Process the data here
        print("Processing:", item)
        data_queue.task_done()

def main():
    data_queue = queue.Queue()

    # Create producer and consumer threads
    producer_thread = threading.Thread(target=data_producer, args=(data_queue,))
    consumer_threads = [threading.Thread(target=data_consumer, args=(data_queue,)) for _ in range(3)]

    # Start the threads
    producer_thread.start()
    for consumer_thread in consumer_threads:
        consumer_thread.start()

    # Wait for all threads to finish
    producer_thread.join()
    for consumer_thread in consumer_threads:
        consumer_thread.join()

if __name__ == "__main__":
    main()
