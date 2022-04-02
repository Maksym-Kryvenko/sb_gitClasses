import pandas as pd
import requests

url = "https://itunes.apple.com/search"
params = {'media': 'music', 'term': 'einaudi', 'limit': 150}
response = requests.post(url, data=params)
response_json = response.json()

df = pd.DataFrame(response_json['results'])
df.to_excel('C:\\Users\\maks1\\Desktop\\SB classes\\Intro to DS\\Ludovico Einaudi.xlsx', sheet_name='track', index_label='id')
df.to_csv('C:\\Users\\maks1\\Desktop\\SB classes\\Intro to DS\\Ludovico Einaudi.csv', sep='|', index=False)
