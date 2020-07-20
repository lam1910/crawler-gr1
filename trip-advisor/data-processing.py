import pandas as pd

final_data = pd.read_json('trip-data.json', encoding='unicode')

# back to csv for import to db
final_data.to_csv('trip-data.csv', header=False)