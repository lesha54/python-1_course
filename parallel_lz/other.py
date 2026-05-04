import time
import requests
import threading
import asyncio
import random


class WebPageDownloader:
    def __init__(self, list_of_urls):
        self.urls = list_of_urls
    def download_single_url(self, url):
        try:
            response = requests.get(url, timeout = 5)
            data_size = len(response.content)
            print(f"Загружено: {url} (размер: {data_size} байт)")
        except Exception as error:
            print(f"Ошибка при загрузке {url}: {error}")

    def run_sequentially(self):
        print("\nСтарт последовательной загрузки")
        start_time = time.time()
        for url in self.urls:
            self.download_single_url(url)
        end_time = time.time()
        return end_time - start_time

    def run_with_threads(self):
        print("\nСтарт загрузки через потоки(параллельно)")
        start_time = time.time()
        list_of_threads = []

        for url in self.urls:
            worker_thread = threading.Thread(target=self.download_single_url, args=(url,))
            list_of_threads.append(worker_thread)
            worker_thread.start()

        for thread in list_of_threads:
            thread.join()
        end_time = time.time()

        return end_time - start_time


class DataExchangeManager:
    @staticmethod
    def generate_numbers(pipe_connection, amount_to_generate):
        print(f"Создаю {amount_to_generate} случайных чисел")
        for _ in range(amount_to_generate):
            number = random.randint(-1_000_000, 1_000_000)
            pipe_connection.send(number)
        
        pipe_connection.send(None)
        pipe_connection.close()

    @staticmethod
    def calculate_squares(pipe_connection):
        print("Начинаю принимать данные")
        while True:
            received_data = pipe_connection.recv()
            if received_data is None:
                break
            square_result = received_data ** 2
            if random.random() < 0.02: 
                print(f"Проверка: Квадрат числа {received_data} равен {square_result}")
        pipe_connection.close()


class AsyncTaskManager:
    async def run_task_with_delay(self, task_name, sleep_duration):
        print(f"Задача '{task_name}' запущена (пауза {sleep_duration} сек.)")
        await asyncio.sleep(sleep_duration)
        print(f"Задача '{task_name}' успешно выполнена")

    async def run_all_tasks_parallel(self):
        print("\nАсинхронный режим: Работаем одновременно")
        start_time = time.time()
        tasks_to_run = [
            self.run_task_with_delay("Первая", 3),
            self.run_task_with_delay("Вторая", 1),
            self.run_task_with_delay("Третья", 2),
            self.run_task_with_delay("Четвертая", 0.5),
            self.run_task_with_delay("Пятая", 1.5)
        ]
        await asyncio.gather(*tasks_to_run)
        return time.time() - start_time

    async def run_all_tasks_sequential(self):
        print("\nАсинхронный режим: Работаем по очереди")
        start_time = time.time()
        delays = [3, 1, 2, 0.5, 1.5]
        names = ["Первая", "Вторая", "Третья", "Четвертая", "Пятая"]
        
        for name, delay in zip(names, delays):
            await self.run_task_with_delay(name, delay)
            
        return time.time() - start_time
