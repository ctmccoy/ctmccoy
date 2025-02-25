import pandas as pd
from tabulate import tabulate

file_path = 'IN300_Dataset1.csv'
data = pd.read_csv(file_path)

# filter to keep rows that dont match the alphabetical protocol string
malicious_traffic = data[~data['Protocol'].str.match('^[A-Za-z]')]

# group and count frequency of each group renamed to Frequency
traffic_counts = malicious_traffic.groupby(['Source', 'Destination', 'Protocol', 'Length', 'Info']).size().reset_index(name='Frequency')

# filter for high frequency traffic
high_freq_traffic = traffic_counts[traffic_counts['Frequency'] > 100]

# print output
print("High-Frequency Malicious Traffic where Frequency > 100:")
print(tabulate(high_freq_traffic, headers='keys', tablefmt='grid'))
