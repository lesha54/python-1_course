import pandas as pd

class TerminalSorter:
    def __init__(self, dataframe, column="Терминал оплаты"):
        self.df = dataframe.copy()
        self.column = column
        self._prepare()

    def _prepare(self):
        self.df["_Банк"] = self.df[self.column].str.split("-").str[0]

    def saving_sorted_tables(self):
        for bank_name, sub_df in self.df.groupby("_Банк"):
            safe_name = bank_name.replace(" ", "_")
            filename = f"{safe_name}.csv"
            final_df = sub_df.drop(columns=["_Банк"])
            final_df.to_csv(filename, index=False, encoding="utf-8-sig")
            print(f"Сохранено: {filename}")

    def __neg__(self):
        initial_len = len(self.df)
        cleaned_df = self.df.drop_duplicates()
        removed = initial_len - len(cleaned_df)
        print(f"Количество повторяющихся строк в наборе данных: {removed}")
        self.df = cleaned_df
        self.saving_sorted_tables()
