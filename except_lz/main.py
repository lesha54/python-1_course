import pandas as pd
import os

class CheckCSV:
    def __init__(self, filepath):
        self.filepath = filepath
        self.expected_columns = [
            "Участники гражданского оборота",
            "Тип операции", "Сумма операции", 
            "Вид расчета",
            "Место оплаты",
            "Терминал оплаты",
            "Дата оплаты", 
            "Время оплаты",
            "Результат операции",
            "Cash-back",
            "Сумма cash-back"
        ]

    def check(self):
        try:
            if not os.path.exists(self.filepath):
                print(f"Возникла следующая ошибка: [Errno 2] No such file or directory: '{self.filepath}'")
                return
            if os.path.getsize(self.filepath) == 0:
                print("Возникла следующая ошибка: Датафрейм пуст")
                return
            df = pd.read_csv(self.filepath)
            if list(df.columns) != self.expected_columns:
                print("Возникла следующая ошибка: Структура датафрейма НЕ соответствует ожидаемой.")
                print(f"Ожидаемые колонки: {self.expected_columns}")
                print(f"Фактические в файле: {list(df.columns)}")
                return 
            if df['Сумма операции'].dtype != 'float64' and df['Сумма операции'].dtype != 'int64':
                print(f"- В столбце 'Сумма операции' тип данных не соответствует ожидаемому.")
                print(f"Ожидается: число, Фактически: {df['Сумма операции'].dtype}")

            print("Чтение датафрейма завершено успешно")
            return df

        except Exception as error:
            print(f"Возникла неизвестная ошибка: {error}")
            return None

if __name__ == "__main__":
    checker = CheckCSV("var6.csv")
    df = checker.check()
