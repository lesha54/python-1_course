import pandas as pd
from other import TerminalSorter

def run_task():
    try:
        source_df = pd.read_csv("var6.csv")
        terminal_manager = TerminalSorter(source_df)
        -terminal_manager

    except FileNotFoundError:
        print("Файл не найден")
    except Exception as error:
        print(f"Что-то пошло не так {error}")

if __name__ == "__main__":
    run_task()
