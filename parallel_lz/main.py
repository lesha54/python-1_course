import asyncio
import multiprocessing
from other import WebPageDownloader, DataExchangeManager, AsyncTaskManager

def start_lab_work():

    list_of_websites = [
        "https://google.com",
        "https://python.org",
        "https://github.com",
        "https://wikipedia.org",
        "https://reddit.com",
        "https://yandex.ru",
        "https://apple.com",
        "https://microsoft.com",
        "https://amazon.com",
        "https://habr.com"
    ]

    downloader_instance = WebPageDownloader(list_of_websites)
    sequential_time = downloader_instance.run_sequentially()
    parallel_time = downloader_instance.run_with_threads()
    
    print(f"\n результат задания 1")
    print(f"Время последовательно: {sequential_time:.2f} сек.")
    print(f"Время параллельно: {parallel_time:.2f} сек.")


    print("\nЗадание 2")
    sender_side, receiver_side = multiprocessing.Pipe()

    producer_process = multiprocessing.Process(
        target=DataExchangeManager.generate_numbers, 
        args=(sender_side, 1000)
    )
    consumer_process = multiprocessing.Process(
        target=DataExchangeManager.calculate_squares, 
        args=(receiver_side,)
    )

    producer_process.start()
    consumer_process.start()
    producer_process.join()
    consumer_process.join()

    print("\nЗадание 3")
    async_manager = AsyncTaskManager()
    time_async_parallel = asyncio.run(async_manager.run_all_tasks_parallel())
    time_async_sequential = asyncio.run(async_manager.run_all_tasks_sequential())
    
    print(f"\nрезультат задания 3:")
    print(f"Одновременный запуск занял: {time_async_parallel:.2f} сек.")
    print(f"Последовательный запуск занял: {time_async_sequential:.2f} сек.")

if __name__ == "__main__":
    start_lab_work()
