import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer

# Load the data
df = pd.read_csv("terrorism_dataset.csv")

#Quick Analysis
df.head()
df.tail()
df.describe()
df.info()
df.columns()

# Handling missing data
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy = "median")               # replaces with median value
np_num = df.select_dtypes(include = [np.number])           # only processing numeric values
imputer.fit(np_num)
imputer.statistics_                                         # median values -> column wise
x = imputer.transform(np_num)                   # this will replace median values from null values

# This line of code creates a new Date column in your DataFrame by combining three separate columns (iyear, imonth, iday) into a single, proper date format.
df["imonth"] = df["imonth"].replace(0 , 1)
df["iday"] = df["iday"].replace(0 , 1)
df["Date"] = pd.to_datetime(df["iyear"].astype(str) + "-" + df["imonth"].astype(str) + "-" + df["iday"].astype(str) , errors = "coerce")
df = df.drop(columns = ["iyear" , "imonth" , "iday"])  

# Convert 'region_txt' and 'attacktype1_txt' to the category data type
df["region_txt"] = df["region_txt"].astype('category')
df["attacktype1_txt"] = df["attacktype1_txt"].astype('category')

# Define the list of countries you're interested in
target_countries = ["India" , "Afghanistan" , "Iraq"]

# Use .isin() to filter
south_asia = df[df["country_txt"].isin(target_countries)]

# Group by date and country, count attacks, and unstack countries into columns
attack_trends = south_asia.groupby(["Date" , "country_txt"]).size().unstack()
attack_trends
sns.set_style("whitegrid")
plt.figure(figsize = (15 , 7))
attack_trends.plot(kind = "line" , figsize = (15 , 7))
plt.title('Frequency of Terrorist Attacks Over Time(1970-2017)', fontsize=16)
plt.xlabel('Year', fontsize=20)
plt.ylabel('Number of Attacks', fontsize=20)
plt.legend(title='Country' , fontsize = 20)
plt.grid(True)
plt.show()

# Group by country and sum the casualties. Fill NaN with 0 before summing.
casualties = south_asia.groupby("country_txt")[["nkill" , "nwound"]].sum()
casualties["total"] = casualties["nkill"] + casualties["nwound"]   
casualties = casualties.sort_values("total" , ascending = False)                               
casualties[["nkill" , "nwound"]].plot(kind  = "bar" , stacked = True , figsize = (10 , 6) , color=['#d9534f', '#f0ad4e'])
plt.title('Total Casualties by Country (1970-2017)', fontsize=16)
plt.xlabel('Country', fontsize=20)
plt.ylabel('Total Number of Casualties', fontsize=20)
plt.xticks(rotation=0)                                                # Keep country names horizontal
plt.legend(['Fatalities', 'Injuries'] , fontsize = 20)

# Create a figure with 3 subplots, arranged in 1 row and 3 columns
fig , axes = plt.subplots(1 , 3 , figsize = (20 , 8) , sharex = True)           # sharex makes the x-axis scale the same
fig.suptitle('Top 10 Primary Target Types by Country' , fontsize = 24)
countries = ["Iraq" , "Afghanistan" , "India"]                                  # Order them by total attacks for consistency
for i , country in enumerate(countries):
     # Filter for the current country
    country_df = df[df["country_txt"] == country]
    # Check if the filtered DataFrame is empty
    if country_df.empty:
        axes[i].set_title(f"{country}\n(No Data)", fontsize=16)                 # Update title on blank plot
        continue
    top_targets = country_df["targtype1_txt"].value_counts().nlargest(10)      # Get the top 10 target types
    sns.barplot(y = top_targets.index , x = top_targets.values , ax = axes[i] , palette='viridis')
    axes[i].set_title(country , fontsize = 20)
    axes[i].set_xlabel("No. of attacks" , fontsize = 20)
    axes[i].set_ylabel("")
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

print(south_asia['country_txt'].unique())
           