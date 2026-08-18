

# ⚡ EcoCrew AI — Multi-Agent Smart Energy Optimization System

An AI-powered smart energy optimization system that analyzes appliance electricity consumption and provides actionable energy-saving recommendations using **CrewAI, Groq, Python, Pandas, and Streamlit**.

---

## 📌 Project Overview

EcoCrew AI helps users understand their household electricity consumption by allowing them to upload an appliance energy consumption CSV file.

The system analyzes the uploaded data and provides:

- ⚡ Total monthly energy consumption
- 💰 Estimated monthly electricity bill
- 🔥 Highest energy-consuming appliance
- 📊 Appliance-wise energy analysis
- 💡 Potential energy savings
- 🤖 AI-powered energy consumption analysis
- 🌱 Energy-saving recommendations

---

## ✨ Features

### 📂 CSV Upload

Users can manually upload their appliance energy consumption CSV file.

Required columns:

```text
appliance
power_watts
hours_per_day
```

⚡ Energy Calculation

Monthly energy consumption is calculated using:

Monthly Energy (kWh)
====================

Power (Watts) × Hours per Day × 30
------------------------------------

              1000
💰 Electricity Cost Estimation

The system estimates the monthly electricity cost based on the configured electricity rate.

Monthly Cost = Monthly Energy × Electricity Rate
🔥 Highest Energy Consumer

The system automatically identifies the appliance consuming the most electricity.

📊 Energy Dashboard

The Streamlit dashboard displays:

Total Monthly Energy
Estimated Monthly Bill
Highest Energy Consumer
Potential Savings
Energy Consumption Chart
Appliance Details
🤖 AI Energy Analysis

CrewAI processes the energy consumption data and generates an AI-based analysis containing:

Highest energy-consuming appliance
Major consumption patterns
Energy-saving recommendations
Overall optimization strategy
🧠 AI Workflow
User
 │
 ▼
Upload CSV
 │
 ▼
Data Validation
 │
 ▼
Energy Calculation
 │
 ▼
Streamlit Dashboard
 │
 ▼
CrewAI Agent
 │
 ▼
Groq LLM
 │
 ▼
AI Energy Analysis
 │
 ▼
Energy-Saving Recommendations
🛠️ Tech Stack
Programming Language
Python
AI & LLM
CrewAI
Groq
Data Processing
Pandas
Frontend / Dashboard
Streamlit
Custom CSS
Development Tools
VS Code
Git
GitHub
Python Virtual Environment
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
📊 Example Dataset
appliance,power_watts,hours_per_day
AC,1500,5
Fan,75,10
TV,120,4
Refrigerator,200,24
Washing Machine,500,1
Light,10,6

Example result:

Appliance	Monthly Energy
AC	225.0 kWh
Refrigerator	144.0 kWh
Fan	22.5 kWh
Washing Machine	15.0 kWh
TV	14.4 kWh
Light	1.8 kWh
⚙️ Installation

1. Clone the Repository
   git clone https://github.com/Shrushti19-kadam/EcoCrew-AI-Multi-Agent-Smart-Energy-Optimization-System.git
2. Open the Project
   cd EcoCrew-AI-Multi-Agent-Smart-Energy-Optimization-System
3. Create Virtual Environment
   python -m venv .venv
4. Activate Virtual Environment

Windows PowerShell:

.venv\Scripts\Activate.ps1
5. Install Dependencies
pip install -r requirements.txt
🔐 Environment Setup

Create a .env file in the project folder:

GROQ_API_KEY=your_groq_api_key

Do not upload your .env file or API key to GitHub.

▶️ Run the Application

Start the Streamlit dashboard:

streamlit run app.py

Then open the local URL shown in the terminal.

🤖 Run CrewAI

To run the CrewAI workflow separately:

python run_crew.py
🔄 Application Flow
CSV Upload
    ↓
Validate Data
    ↓
Calculate Monthly Energy
    ↓
Calculate Electricity Cost
    ↓
Find Highest Consumer
    ↓
Display Dashboard
    ↓
CrewAI Analysis
    ↓
Groq LLM
    ↓
AI Recommendations
🔮 Future Enhancements
📈 Energy consumption forecasting
📊 Historical usage tracking
💰 Dynamic electricity tariff calculation
🏠 Smart home / IoT integration
🔌 Smart meter integration
🤖 Multiple specialized CrewAI agents
🎯 Personalized energy-saving plans
📱 Mobile-friendly dashboard
👤 User authentication
🗄️ Database integration
🎯 Project Goal

The goal of EcoCrew AI is to transform raw appliance electricity data into meaningful insights and practical recommendations.

Raw Data
   ↓
Analysis
   ↓
AI Insights
   ↓
Recommendations
   ↓
Energy Optimization
👩‍💻 Author

Srushti Kadam

AI & Data Science Student
Interested in Artificial Intelligence, Machine Learning, Generative AI, and AI Agents.

⭐ Support

If you find this project useful, consider giving the repository a ⭐ star.

📜 License

This project is developed for educational and portfolio purposes.
