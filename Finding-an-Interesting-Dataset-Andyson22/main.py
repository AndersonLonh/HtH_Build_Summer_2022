import pandas

pandas.options.display.max_columns = None
pandas.options.display.max_rows = None

basketball_draft_data = pandas.read_csv("basketball_draft.csv")

print(basketball_draft_data)