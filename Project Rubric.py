# note source as https://www.kaggle.com/gpreda/covid-world-vaccination-progress
import numpy
import pandas as pd

# import the required file
df = pd.read_csv(r'C:/country_vaccinations.csv', index_col="country")

# looking at 3 countries in particular
first = df.loc[["Australia", "United Kingdom", "United States"]]

list = numpy.array(['iso_code', 'total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated', 'daily_vaccinations_raw', 'daily_vaccinations','total_vaccinations_per_hundred', 'people_fully_vaccinated_per_hundred', 'daily_vaccinations_per_million', 'vaccines', 'source_name', 'source_website'])

# dropping the unnecessary columns
second = first.drop(list, axis=1)

# replacing missing values with 0
cleaned_data = second.fillna(0)

vaccine_data = cleaned_data

vaccine_data.index = [x for x in range(1, len(vaccine_data.values) + 1)]
vaccine_data.index.name = 'id'

print(vaccine_data)

# importing the closing prices from yahoo (https://finance.yahoo.com/quote/%5EFTSE%3FP%3DFTSE/history/, https://finance.yahoo.com/quote/%5EGSPC/history?p=%5EGSPC, https://finance.yahoo.com/quote/%5EAXJO/history?p=%5EAXJO)
yahoo_data = pd.read_csv(r'C:/Users/nrodg/OneDrive/Documents/YahooHistoricalData.csv', index_col="date")

# updating the dataframe index
yahoo_data.index = [x for x in range(1, len(yahoo_data.values) + 1)]
yahoo_data.index.name = 'id'

print(yahoo_data)

#Merging the vaccine data with the share index closing price from Yahoo
final_table = pd.merge(vaccine_data, yahoo_data, on="id")

print(final_table)

#Importing matplotlib in order to create graphs

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

#Creating an Australian-specific graph in order to better understand the vaccine/index development over the time period
#To do this, I imported an australia-specific version of the CSV already imported

data_australia = pd.read_csv(r'C:/Users/nrodg/OneDrive/Documents/australiatable.csv', index_col="id")

print(data_australia)

x = data_australia["date"]
y1 = data_australia["people_vaccinated_per_hundred"]
y2 = data_australia["closing_price"]

plt.plot(x,y1)
plt2=plt.twinx()
plt2.plot(x,y2)
plt.show()

#Creating an UK-specific graph as above

data_UK = pd.read_csv(r'C:/Users/nrodg/OneDrive/Documents/unitedkingdomtable.csv', index_col="id")

print(data_UK)

a = data_UK["date"]
b1 = data_UK["people_vaccinated_per_hundred"]
b2 = data_UK["closing_price"]

plt.plot(a,b1)
plt2=plt.twinx()
plt2.plot(a,b2)
plt.show()

#Creating an US-specific graph as above

data_US = pd.read_csv(r'C:/Users/nrodg/OneDrive/Documents/unitedstatestable.csv', index_col="id")

print(data_US)

c = data_US["date"]
d1 = data_US["people_vaccinated_per_hundred"]
d2 = data_US["closing_price"]

plt.plot(c,d1)
plt2=plt.twinx()
plt2.plot(c,d2)
plt.show()