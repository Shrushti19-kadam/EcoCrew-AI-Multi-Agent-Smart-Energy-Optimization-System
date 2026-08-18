from crewai import Task

from agents.usage_agent import usage_agent


usage_task = Task(
    description=(
        "Analyze the following appliance energy consumption data:\n\n"
        "{energy_data}\n\n"
        "Identify the appliance consuming the most monthly energy. "
        "Use these verified calculations from Python:\n"
        "Total monthly energy: {total_energy} kWh\n"
        "Total monthly cost: ₹{total_cost}\n\n"
        "Explain the major energy consumption patterns and mention "
        "which appliances should be prioritized for energy saving."
    ),
    expected_output=(
        "A clear analysis containing:\n"
        "1. The highest energy-consuming appliance.\n"
        "2. Its monthly energy consumption.\n"
        "3. The major energy consumption patterns.\n"
        "4. Practical energy-saving recommendations."
    ),
    agent=usage_agent
)