import pandas as pd

from crew.energy_crew import energy_crew

data = pd.read_csv("data/energy_data.csv")

energy_data = data.to_string(index=False)

data["monthly_energy_kwh"] = (
    data["power_watts"] * data["hours_per_day"] * 30
) / 1000

electricity_rate = 8
data["monthly_cost"] = data["monthly_energy_kwh"] * electricity_rate

total_energy = data["monthly_energy_kwh"].sum()
total_cost = data["monthly_cost"].sum()

result = energy_crew.kickoff(
    inputs={
        "energy_data": energy_data,
        "total_energy": total_energy,
        "total_cost": total_cost
    }
)

print("\n===== FINAL AGENT RESULT =====")
print(result)