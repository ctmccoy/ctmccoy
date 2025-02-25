
import pandas as pd

file_path = "IN300_Dataset1.csv"
data = pd.read_csv(file_path)

# calculate the frequency and arrange in descending format
source_frequency = data['Source'].value_counts().sort_values(ascending=False)

destination_frequency = data['Destination'].value_counts().sort_values(ascending=False)

protocol_frequency = data['Protocol'].value_counts().sort_values(ascending=False)

# display the results
print("Source IP frequency count in descending format:")
print()
print(source_frequency)
print("\nDestination IP frequency in descending format:")
print()
print(destination_frequency)
print("\nProtocol IP frequency in descending format:")
print()
print(protocol_frequency)

