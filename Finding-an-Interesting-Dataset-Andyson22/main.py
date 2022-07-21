import pandas

pandas.options.display.max_columns = None
pandas.options.display.max_rows = None

covid_2020_data = pandas.read_csv("covid19_countrywise_Data.csv")

print(covid_2020_data)