# Import libraries
import matplotlib.pyplot as plt
import pandas as pd

# Load data via a single CSV
data = pd.read_csv('HouseCosts_NAWI_FMR.csv')

# Check if the required columns exist in the dataset
required_columns = ['Year', 'Average House Price', 'Average Wage Index', 'Average 30-year FMR']
for column in required_columns:
    if column not in data.columns:
        raise ValueError(f"Column '{column}' not found in the CSV file.")

# Values will be the years (1972-2021), the average housing price (in dollars), the average wage index (in dollars), and the 30-year fixed mortgage rate (in percentage)
years = data['Year']
house = data['Average House Price']
awi = data['Average Wage Index']
interest = data['Average 30-year FMR']

# Calculate the relative increases for all three data types
house_relative_increase = ((house.iloc[-1] - house.iloc[0]) / house.iloc[0]) * 100
awi_relative_increase = ((awi.iloc[-1] - awi.iloc[0]) / awi.iloc[0]) * 100
interest_relative_increase = ((interest.iloc[-1] - interest.iloc[0]) / interest.iloc[0]) * 100

# Print the relative increases in percentage
print(f"Average Price of Homes in the US increased by {house_relative_increase:.2f}% from {years.iloc[0]} to {years.iloc[-1]}.")
print(f"Average Wage Index of US citizens increased by {awi_relative_increase:.2f}% from {years.iloc[0]} to {years.iloc[-1]}.")
print(f"Average 30-year fixed mortgage rate of US homes have changed by {interest_relative_increase:.2f}% from {years.iloc[0]} to {years.iloc[-1]}.")

# Create subplots within a single figure
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

# First subplot: Average House Price and Average Wage Index
ax1.plot(years, house, marker='o', linestyle='-', color='red', label='Average House Price')
ax1.plot(years, awi, marker='x', linestyle='-', color='blue', label='Average Wage Index')
ax1.set_xlabel('Year')
ax1.set_ylabel('Value in U.S Dollars')
ax1.legend()
ax1.set_title('Average Cost of a Home in the USA vs. Average Working Wage in the USA since 1972 to 2021')
ax1.grid(True)

# Second subplot: Average 30-year Mortgage Interest Rates
ax2.plot(years, interest, marker='o', linestyle='-', color='green')
ax2.set_xlabel('Year')
ax2.set_ylabel('Rate')
ax2.set_title('Average 30-year Mortgage Interest Rates in the USA since 1972 to 2021')
ax2.grid(True)

# Adjust spacing between subplots
plt.tight_layout()

# Show the combined figure with two subplots
plt.show()