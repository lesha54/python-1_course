from po import CountSunDayHistogram
import pandas as pd

try:
    dataframe = pd.read_csv("steam_players.csv")
    histogram = CountSunDayHistogram(dataframe)
    histogram.show_histogram()
except Exception as error:
    print(f"что-то пошло не так: {error}")
