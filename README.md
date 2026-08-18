
# ⚡ EcoCrew AI — Multi-Agent Smart Energy Optimization System

<div align="center">

---

## 🚀 Overview

**EcoCrew AI** is an AI-powered smart energy optimization system that analyzes appliance-level electricity consumption and converts raw energy data into meaningful insights and practical recommendations.

Users can upload their appliance energy-consumption CSV file, after which the system:

- ⚡ Calculates monthly energy consumption
- 💰 Estimates monthly electricity cost
- 🔥 Identifies the highest energy-consuming appliance
- 📊 Visualizes appliance-wise energy usage
- 💡 Estimates potential savings
- 🤖 Uses CrewAI + Groq to generate AI-powered energy analysis
- 🌱 Provides practical energy-saving recommendations

---

## 🎯 Problem Statement

A traditional electricity bill tells users **how much electricity they consumed**, but it does not clearly explain:

- Which appliance consumes the most energy?
- Which appliances contribute most to the monthly bill?
- Where should users focus their energy-saving efforts?
- What practical actions can reduce consumption?

**EcoCrew AI solves this problem by combining deterministic data analysis with AI-powered interpretation.**

---

## ✨ Key Features

| Feature                   | Description                                       |
| ------------------------- | ------------------------------------------------- |
| 📂 CSV Upload             | Upload your own appliance energy dataset          |
| ✅ Data Validation        | Validates required CSV columns and numeric values |
| ⚡ Energy Calculation     | Calculates monthly energy consumption in kWh      |
| 💰 Cost Estimation        | Calculates estimated monthly electricity cost     |
| 🔥 Top Consumer Detection | Finds the appliance consuming the most energy     |
| 📊 Interactive Dashboard  | Displays KPIs, charts and appliance details       |
| 🤖 AI Energy Analysis     | Uses CrewAI and Groq for intelligent analysis     |
| 💡 Recommendations        | Generates practical energy-saving suggestions     |
| 🌱 Optimization Insights  | Helps prioritize high-impact appliances           |

---

## 🧠 System Architecture

```text
                    ┌──────────────────────┐
                    │      USER            │
                    │                      │
                    │   Upload CSV File    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   DATA VALIDATION    │
                    │                      │
                    │ • Required Columns   │
                    │ • Numeric Validation │
                    │ • Data Cleaning      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ ENERGY CALCULATION   │
                    │                      │
                    │ • Monthly kWh        │
                    │ • Monthly Cost       │
                    │ • Highest Consumer   │
                    └──────────┬───────────┘
                               │
                 ┌─────────────┴─────────────┐
                 │                           │
                 ▼                           ▼
       ┌──────────────────┐        ┌──────────────────┐
       │    STREAMLIT     │        │     CREWAI       │
       │    DASHBOARD     │        │    WORKFLOW      │
       │                  │        │                  │
       │ • Metrics        │        │ Energy Analyst   │
       │ • Charts         │        │ Agent            │
       │ • Data Table     │        └────────┬─────────┘
       └──────────────────┘                 │
                                            ▼
                                  ┌──────────────────┐
                                  │     GROQ LLM     │
                                  │                  │
                                  │ AI Reasoning &   │
                                  │ Recommendations  │
                                  └────────┬─────────┘
                                           │
                                           ▼
                                  ┌──────────────────┐
                                  │  FINAL AI REPORT │
                                  │                  │
                                  │ • Patterns       │
                                  │ • Insights       │
                                  │ • Recommendations│
                                  └──────────────────┘
```


🤖 CrewAI Architecture

The current implementation uses a modular CrewAI workflow.

                 ┌──────────────────────────┐
                 │      Energy Crew         │
                 │   Sequential Process     │
                 └────────────┬─────────────┘
                              │
                              ▼
                 ┌──────────────────────────┐
                 │ Energy Consumption       │
                 │ Analyst Agent            │
                 │                          │
                 │ Role: Energy Analyst     │
                 └────────────┬─────────────┘
                              │
                              ▼
                 ┌──────────────────────────┐
                 │        Groq LLM          │
                 │   gpt-oss-20b            │
                 └────────────┬─────────────┘
                              │
                              ▼
                 ┌──────────────────────────┐
                 │ AI Energy Analysis       │
                 │ + Recommendations        │
                 └──────────────────────────┘

Current implementation: the CrewAI workflow currently contains one specialized Energy Consumption Analyst agent. The architecture is designed to be extended with additional specialized agents in future versions.

🔄 End-to-End Workflow
CSV Upload
    ↓
Validate Required Columns
    ↓
Clean Numeric Data
    ↓
Calculate Monthly Energy
    ↓
Calculate Monthly Cost
    ↓
Identify Highest Consumer
    ↓
Display Dashboard
    ↓
User Clicks "Analyze Energy Usage"
    ↓
CrewAI Agent Receives Processed Data
    ↓
Groq LLM Analysis
    ↓
Energy Consumption Patterns
    ↓
Energy-Saving Recommendations
    ↓
Final AI Report
📐 Energy Calculation

Monthly energy consumption is calculated using:

Monthly Energy (kWh)
====================

Power (Watts) × Hours/Day × 30
--------------------------------

              1000
Example
AC Power = 1500 W
Usage = 5 hours/day

Monthly Energy
= (1500 × 5 × 30) / 1000

= 225 kWh/month
💰 Electricity Cost Calculation

The current application uses an electricity rate of ₹8/kWh.

Monthly Cost
============

Monthly Energy × Electricity Rate

Example:

225 kWh × ₹8
==============

₹1,800/month
💡 Potential Savings

The dashboard currently estimates potential savings as 15% of the calculated monthly electricity bill.

Potential Savings
=================

Monthly Bill × 15%

This is an estimated optimization opportunity, not a guaranteed saving. Actual savings depend on appliance efficiency, usage behavior and electricity tariff structure.

📊 Example Dataset
appliance,power_watts,hours_per_day
AC,1500,5
Fan,75,10
TV,120,4
Refrigerator,200,24
Washing Machine,500,1
Light,10,6
Example Results
Appliance	Power	Hours/Day	Monthly Energy
🔥 AC	1500 W	5	225.0 kWh
🧊 Refrigerator	200 W	24	144.0 kWh
🌀 Fan	75 W	10	22.5 kWh
🧺 Washing Machine	500 W	1	15.0 kWh
📺 TV	120 W	4	14.4 kWh
💡 Light	10 W	6	1.8 kWh
📈 Dashboard

The application provides a dark-themed Streamlit dashboard containing:

Energy Overview
⚡ Total Monthly Energy
💰 Estimated Monthly Bill
🔥 Highest Consumer
💡 Potential Savings
Analytics
Monthly energy by appliance
Monthly cost by appliance
Appliance-level data table
Highest energy-consuming appliance
AI Analysis
Energy consumption analysis
Consumption patterns
Priority appliances
Energy-saving recommendations
🖼️ Project Screenshots

Create a folder:

screenshots/

Add screenshots such as:

screenshots/
├── dashboard.png
├── analytics.png
└── ai-analysis.png

Then add:

![EcoCrew AI Dashboard](screenshots/dashboard.png)

![Energy Analytics](screenshots/analytics.png)

![AI Energy Analysis](screenshots/ai-analysis.png)
🛠️ Technology Stack
Category	Technology
Programming	Python
Dashboard	Streamlit
Data Processing	Pandas
AI Agent Framework	CrewAI
LLM Provider	Groq
LLM	groq/openai/gpt-oss-20b
Version Control	Git
Repository	GitHub
Development	VS Code
📁 Project Structure
EcoCrew-AI/
│
├── agents/
│   └── usage_agent.py
│
├── crew/
│   └── energy_crew.py
│
├── tasks/
│   └── energy_tasks.py
│
├── data/
│   └── energy_data.csv
│
├── app.py
├── run_crew.py
├── calculations.py
├── test_data.py
├── .gitignore
└── README.md
File Responsibilities
File	Purpose
app.py	Main Streamlit application
usage_agent.py	Defines the CrewAI energy analyst agent
energy_tasks.py	Defines the energy analysis task
energy_crew.py	Creates the CrewAI sequential workflow
run_crew.py	Runs the CrewAI workflow independently
calculations.py	Supporting calculation logic
test_data.py	Data testing utility
🔐 Environment Setup

Create a .env file:

GROQ_API_KEY=your_groq_api_key
⚠️ Security

Never upload your API key to GitHub.

Do not commit:

.env

Never hard-code:

GROQ_API_KEY = "your-secret-key"

Use environment variables instead.

⚙️ Installation

1. Clone Repository
   git clone https://github.com/Shrushti19-kadam/EcoCrew-AI-Multi-Agent-Smart-Energy-Optimization-System.git
2. Navigate to Project
   cd EcoCrew-AI-Multi-Agent-Smart-Energy-Optimization-System
3. Create Virtual Environment
   python -m venv .venv
4. Activate Environment

Windows PowerShell:

.venv\Scripts\Activate.ps1
5. Install Dependencies
pip install -r requirements.txt
▶️ Run Application

Start the Streamlit dashboard:

streamlit run app.py

Then open the local URL displayed in the terminal.

🤖 Run CrewAI Separately

To execute the CrewAI workflow using the example dataset:

python run_crew.py
📋 CSV Requirements

Your CSV must contain:

appliance
power_watts
hours_per_day

Example:

appliance,power_watts,hours_per_day
AC,1500,5
Fan,75,10
TV,120,4
🧪 Data Validation

The application checks:

Required columns
Numeric power values
Numeric usage values
Empty or invalid records
CSV readability

Invalid or incomplete data is handled before the energy analysis begins.

🚧 Current Limitations

The current version does not yet include:

❌ Real-time smart meter integration
❌ IoT appliance control
❌ Historical database
❌ Energy forecasting
❌ Dynamic electricity tariffs
❌ User authentication
❌ Multiple specialized agents running together
❌ Automated appliance control

These are planned future improvements.

🔮 Future Roadmap
Phase 1 — Current Version
 Manual CSV upload
 CSV validation
 Energy calculation
 Electricity cost estimation
 Highest consumer detection
 Interactive dashboard
 CrewAI integration
 Groq LLM integration
 AI recommendations
Phase 2 — Multi-Agent Intelligence
 Energy Pattern Analyst Agent
 Optimization Strategy Agent
 Savings Advisor Agent
 Personalized energy plans
 Appliance-specific recommendations
Phase 3 — Predictive Analytics
 Historical usage database
 Monthly consumption forecasting
 Electricity bill prediction
 Seasonal energy prediction
 Consumption anomaly detection
Phase 4 — Smart Home Integration
 Smart meter integration
 IoT sensors
 Smart plugs
 Real-time monitoring
 Automated energy optimization
🧠 Why CrewAI?

Traditional data analysis is excellent for accurate numerical calculations.

LLMs are useful for interpreting data and generating human-readable recommendations.

EcoCrew AI combines both:

Verified Python Calculations
          +
Structured Energy Data
          +
CrewAI Agent
          +
Groq LLM
          ↓
AI-Powered Energy Insights

This keeps numerical calculations deterministic while using AI for interpretation and recommendations.

📚 Learning Outcomes

This project demonstrates practical experience with:

Python
Pandas
Streamlit
CrewAI
AI Agents
LLM integration
Groq API
Prompt engineering
CSV data processing
Data validation
Dashboard development
Environment variables
Git & GitHub
Modular AI application architecture
🎥 Demo

Add your screen-recorded demo here:

[▶️ Watch EcoCrew AI Demo](YOUR_VIDEO_LINK)

Recommended demo flow:

Upload CSV
    ↓
Dashboard Metrics
    ↓
Energy Chart
    ↓
Highest Consumer
    ↓
AI Analysis
    ↓
Recommendations
🌱 Project Impact

EcoCrew AI aims to make household electricity consumption easier to understand.

Raw Energy Data
       ↓
Data Analysis
       ↓
Consumption Insights
       ↓
AI Recommendations
       ↓
Energy Optimization
       ↓
Potential Cost Savings

The goal is simple:

Understand where energy is being consumed and identify where optimization can have the greatest impact.

👩‍💻 Author
Srushti Kadam

AI & Data Science Student | Aspiring AI/ML Engineer

Interested in:

Artificial Intelligence
Machine Learning
Generative AI
LLM Applications
AI Agents
Data Science
⭐ Support

If you find this project useful:

⭐ Star the repository
🍴 Fork the project
💡 Share feedback

📜 License

This project is developed for educational and portfolio purposes.
