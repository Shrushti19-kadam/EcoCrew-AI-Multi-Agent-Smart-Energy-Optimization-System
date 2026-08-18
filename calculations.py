def calculate_energy(power_watts, hours_per_day, days):
    energy = (power_watts * hours_per_day * days) / 1000
    return energy


def calculate_cost(energy_kwh, electricity_rate):
    cost = energy_kwh * electricity_rate
    return cost


energy = calculate_energy(1500, 5, 30)
cost = calculate_cost(energy, 8)

print("Monthly Energy:", energy, "kWh")
print("Monthly Cost: ₹", cost)