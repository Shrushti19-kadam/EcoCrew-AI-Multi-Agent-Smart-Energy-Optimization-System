import os

from crewai import Agent, LLM


llm = LLM(
    model="groq/openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.2,
    drop_params=True
)


usage_agent = Agent(
    role="Energy Consumption Analyst",
    goal="Analyze appliance energy consumption and identify major consumption patterns.",
    backstory=(
        "You are an expert energy analyst. "
        "You analyze electricity usage data and identify "
        "which appliances consume the most energy."
    ),
    llm=llm,
    verbose=True
)