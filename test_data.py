import pandas as pd

data = pd.read_csv("data/energy_data.csv")

print(data)

data["monthly_energy_kwh"] = (
    data["power_watts"] *
    data["hours_per_day"] *
    30
) / 1000

print("\nEnergy Consumption:")
print(data)

electricity_rate = 8

data["monthly_cost"] = (
    data["monthly_energy_kwh"] * electricity_rate
)

print("\nMonthly Cost:")
print(data)
highest_consumer = data.loc[
    data["monthly_energy_kwh"].idxmax()
]

print("\nHighest Energy Consumer:")
print(highest_consumer)

total_energy = data["monthly_energy_kwh"].sum()
total_cost = data["monthly_cost"].sum()

print("\nTotal Monthly Energy:", total_energy, "kWh")
print("Total Monthly Cost: ₹", total_cost)