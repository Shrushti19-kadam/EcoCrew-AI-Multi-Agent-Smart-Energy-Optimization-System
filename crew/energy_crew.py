from crewai import Crew, Process

from agents.usage_agent import usage_agent
from tasks.energy_tasks import usage_task


energy_crew = Crew(
    agents=[usage_agent],
    tasks=[usage_task],
    process=Process.sequential,
    verbose=True
)