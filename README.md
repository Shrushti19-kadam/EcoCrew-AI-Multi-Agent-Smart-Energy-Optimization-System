
<div align="center">

---

## 💜 About The Project

**EcoCrew AI** is an AI-powered smart energy optimization system that analyzes appliance-level electricity consumption and converts raw energy data into meaningful insights and practical recommendations.

Users can upload an appliance energy CSV file and analyze:

- ⚡ Monthly energy consumption
- 💰 Estimated electricity cost
- 🔥 Highest energy-consuming appliance
- 📊 Appliance-wise consumption
- 💡 Potential savings
- 🤖 AI-powered energy analysis
- 🌱 Energy-saving recommendations

The project combines **Python-based data analysis** with **CrewAI and Groq LLM** to transform electricity data into understandable energy insights.

---

## 🎯 Problem Statement

Traditional electricity bills show the total electricity consumed, but they do not clearly identify which appliances are responsible for the highest consumption.

EcoCrew AI focuses on answering three important questions:

> 🔍 Which appliance consumes the most energy?

> 📊 What are the major energy consumption patterns?

> 💡 Which appliances should be prioritized for energy saving?

---

## ✨ Key Features

### 📂 Manual CSV Upload

Users can upload their own appliance energy-consumption CSV file directly through the Streamlit dashboard.

### ⚡ Energy Consumption Analysis

The system automatically calculates monthly energy consumption for every appliance.

### 💰 Electricity Cost Estimation

The application calculates the estimated monthly electricity cost based on the configured electricity rate.

### 🔥 Highest Energy Consumer

EcoCrew AI automatically identifies the appliance with the highest monthly energy consumption.

### 📊 Energy Analytics

The dashboard provides appliance-level energy and cost visualization.

### 🤖 AI Energy Analysis

CrewAI analyzes the processed energy data and generates:

- Consumption patterns
- Highest-consuming appliance
- Priority areas
- Energy-saving recommendations

### 🌱 Smart Recommendations

The AI provides practical recommendations to help users reduce unnecessary electricity consumption.

---

## 🧠 How It Works

```text
User
 │
 ▼
Upload Energy CSV
 │
 ▼
Data Validation
 │
 ▼
Energy Calculation
 │
 ▼
Cost Calculation
 │
 ▼
Highest Consumer Detection
 │
 ├──────────────► Streamlit Dashboard
 │
 ▼
CrewAI Energy Analyst
 │
 ▼
Groq LLM
 │
 ▼
AI Energy Analysis
 │
 ▼
Energy-Saving Recommendations
```

🤖 CrewAI Architecture

The current implementation uses a specialized Energy Consumption Analyst agent.

              ┌──────────────────────┐
              │      Energy Crew     │
              │   Sequential Process │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │ Energy Consumption   │
              │    Analyst Agent     │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │       Groq LLM       │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   AI Energy Report   │
              │                      │
              │ • Patterns           │
              │ • Insights           │
              │ • Recommendations    │
              └──────────────────────┘

Current version: one specialized energy analyst agent is implemented. The architecture can be extended with additional agents in future versions.

📐 Energy Calculation

Monthly energy consumption is calculated using:

Monthly Energy (kWh)
====================

Power (Watts) × Hours/Day × 30
--------------------------------

              1000
Example
Power = 1500 W
Usage = 5 hours/day

Monthly Energy
= (1500 × 5 × 30) / 1000

= 225 kWh/month
💰 Electricity Cost

The current application uses an electricity rate of:

₹8 / kWh

Formula:

Monthly Cost
============

Monthly Energy × Electricity Rate

Example:

225 × ₹8
==========

₹1,800/month
📊 Example Dataset
appliance,power_watts,hours_per_day
AC,1500,5
Fan,75,10
TV,120,4
Refrigerator,200,24
Washing Machine,500,1
Light,10,6
Example Analysis
Appliance	Power	Hours/Day	Monthly Energy
🔥 AC	1500 W	5	225.0 kWh
🧊 Refrigerator	200 W	24	144.0 kWh
🌀 Fan	75 W	10	22.5 kWh
🧺 Washing Machine	500 W	1	15.0 kWh
📺 TV	120 W	4	14.4 kWh
💡 Light	10 W	6	1.8 kWh

Highest Energy Consumer: AC

Total Monthly Energy: 422.7 kWh

Estimated Monthly Bill: ₹3,381.60

🛠️ Technology Stack
Technology	Purpose
🐍 Python	Core application development
🎨 Streamlit	Interactive web dashboard
🐼 Pandas	Data processing and analysis
🤖 CrewAI	AI agent orchestration
⚡ Groq	LLM inference
🔧 Git	Version control
🐙 GitHub	Source code management
💻 VS Code	Development environment
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
app.py	Main Streamlit dashboard
usage_agent.py	Energy Consumption Analyst agent
energy_tasks.py	CrewAI energy analysis task
energy_crew.py	CrewAI crew configuration
run_crew.py	Standalone CrewAI execution
calculations.py	Energy calculation utilities
test_data.py	Data testing utility
🔐 Environment Setup

Create a .env file in the project directory:

GROQ_API_KEY=your_groq_api_key
⚠️ Security

Never expose your API key publicly.

Do not upload:

.env

to GitHub.

⚙️ Installation

1. Clone the Repository
   git clone https://github.com/Shrushti19-kadam/EcoCrew-AI-Multi-Agent-Smart-Energy-Optimization-System.git
2. Open Project Directory
   cd EcoCrew-AI-Multi-Agent-Smart-Energy-Optimization-System
3. Create Virtual Environment
   python -m venv .venv
4. Activate Virtual Environment

Windows PowerShell:

.venv\Scripts\Activate.ps1
5. Install Dependencies
pip install -r requirements.txt
▶️ Run the Application

Start the Streamlit dashboard:

streamlit run app.py

The application will open in your browser.

🤖 Run CrewAI Workflow

To run the CrewAI workflow independently:

python run_crew.py
📋 CSV Requirements

The uploaded CSV must contain:

appliance
power_watts
hours_per_day

Example:

appliance,power_watts,hours_per_day
AC,1500,5
Fan,75,10
TV,120,4
🚧 Current Limitations

The current version does not include:

Real-time smart meter integration
IoT appliance monitoring
Historical database
Energy forecasting
Dynamic electricity tariffs
User authentication
Automated appliance control
Multiple specialized agents running together
🔮 Future Scope
🤖 Advanced Multi-Agent System

Future versions can introduce:

Energy Pattern Analyst
Optimization Strategy Agent
Savings Advisor
Personalized Energy Planner
📈 Predictive Analytics
Monthly energy forecasting
Electricity bill prediction
Seasonal consumption prediction
Energy anomaly detection
🏠 Smart Home Integration
Smart meter integration
IoT sensors
Smart plugs
Real-time monitoring
Automated energy optimization
📚 Learning Outcomes

This project demonstrates practical experience with:

Python
Data Analysis
Pandas
Streamlit
CrewAI
AI Agents
Groq API
LLM Integration
Prompt Engineering
CSV Data Processing
Data Validation
Git & GitHub
AI Application Development
👩‍💻 Author

<div align="center">
Srushti Kadam
