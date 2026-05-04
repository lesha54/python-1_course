import pandas as pd
import matplotlib.pyplot as plt
from logger import log_call

class CountSunDayHistogram:
    def __init__(self, dataframe):
        self.df = dataframe.copy()

    @log_call()
    def show_histogram(self):
        country_counts = self.df['country'].value_counts().reset_index()
        country_counts.columns = ['country', 'players']
        target_countries = ["Russian Federation", "Brazil", "United States", "Kazakhstan"]
        df_plot = country_counts[country_counts["country"].isin(target_countries)]
        plt.figure(figsize=(10, 6))
        plt.barh(df_plot["country"], df_plot["players"], color="red")
        plt.title("Количество игроков по странам")
        plt.tight_layout()
        plt.show()

