import streamlit as st
import pandas as pd
from crew.energy_crew import energy_crew

st.set_page_config(
    page_title="EcoCrew AI",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>

    /* =====================================================
       MAIN BACKGROUND
       ===================================================== */

    .stApp {
        background:
            radial-gradient(
                circle at 10% 0%,
                rgba(56, 189, 248, 0.06),
                transparent 25%
            ),
            radial-gradient(
                circle at 90% 0%,
                rgba(139, 92, 246, 0.06),
                transparent 25%
            ),
            #080D18;

        color: #E5E7EB;
    }


    .block-container {
        max-width: 1450px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }


    /* =====================================================
       SIDEBAR
       ===================================================== */

    section[data-testid="stSidebar"] {
        background-color: #0C1321 !important;
        border-right: 1px solid #202C42;
    }

    section[data-testid="stSidebar"] * {
        color: #D7DEE9;
    }


    section[data-testid="stSidebar"] h1 {
        color: #F8FAFC !important;
    }

    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #E2E8F0 !important;
    }


    /* =====================================================
       UPLOAD BOX - CYAN
       ===================================================== */

    section[data-testid="stFileUploaderDropzone"] {

        background-color: #0B1A2B !important;

        border: 1px solid #1597C8 !important;

        border-radius: 14px !important;

        box-shadow:
            0 0 18px rgba(56, 189, 248, 0.06);
    }


    section[data-testid="stFileUploaderDropzone"]:hover {

        background-color: #0D2237 !important;

        border-color: #38BDF8 !important;
    }


    /* Upload text */

    section[data-testid="stFileUploaderDropzone"] span {

        color: #BAE6FD !important;
    }


    /* Upload button */

    section[data-testid="stFileUploaderDropzone"] button {

        background-color: #132A3A !important;

        color: #7DD3FC !important;

        border: 1px solid #38BDF8 !important;

        border-radius: 8px !important;
    }


    section[data-testid="stFileUploaderDropzone"] button:hover {

        background-color: #173A50 !important;

        color: #E0F2FE !important;

        border-color: #67E8F9 !important;
    }


    /* Uploaded filename */

    [data-testid="stFileUploaderFileName"] {

        color: #E0F2FE !important;
    }


    /* =====================================================
       REQUIRED CSV INFO BOX - PURPLE
       ===================================================== */

    section[data-testid="stSidebar"] div[data-testid="stAlert"] {

        background-color: #17142B !important;

        border: 1px solid #7C5CFC !important;

        border-radius: 14px !important;

        color: #DDD6FE !important;

        box-shadow:
            0 0 18px rgba(139, 92, 246, 0.07);
    }


    section[data-testid="stSidebar"] div[data-testid="stAlert"] p {

        color: #DDD6FE !important;
    }


    /* =====================================================
       MAIN HEADINGS
       ===================================================== */

    h1,
    h2,
    h3,
    h4 {

        color: #F8FAFC !important;

        font-weight: 750 !important;
    }


    p {

        color: #AAB5C5;
    }


    /* =====================================================
       METRIC CARDS
       ===================================================== */

    div[data-testid="stMetric"] {

        background:
            linear-gradient(
                145deg,
                #121D30,
                #0F1727
            );

        border: 1px solid #263650;

        border-radius: 16px;

        padding: 20px;

        box-shadow:
            0 10px 28px rgba(0, 0, 0, 0.28);

        transition: 0.2s ease;
    }


    div[data-testid="stMetric"]:hover {

        border-color: #42577A;

        transform: translateY(-2px);
    }


    div[data-testid="stMetricLabel"] {

        color: #94A3B8 !important;
    }


    div[data-testid="stMetricValue"] {

        color: #F8FAFC !important;

        font-weight: 800 !important;
    }


    /* =====================================================
       AI BUTTON - PURPLE
       ===================================================== */

    .stButton > button {

        width: 100%;

        background:
            linear-gradient(
                135deg,
                #7C3AED,
                #5B21B6
            ) !important;

        color: #FFFFFF !important;

        border: 1px solid #8B5CF6 !important;

        border-radius: 11px !important;

        padding: 12px 20px !important;

        font-weight: 700 !important;

        box-shadow:
            0 8px 22px rgba(124, 58, 237, 0.25);

        transition: 0.2s ease;
    }


    .stButton > button:hover {

        background:
            linear-gradient(
                135deg,
                #8B5CF6,
                #6D28D9
            ) !important;

        border-color: #A78BFA !important;

        transform: translateY(-2px);

        box-shadow:
            0 12px 30px rgba(139, 92, 246, 0.35);
    }


    /* =====================================================
       MAIN INFO BOX - BLUE
       ===================================================== */

    div[data-testid="stAlert"] {

        background-color: #0B1D30 !important;

        border: 1px solid #1677A8 !important;

        border-radius: 14px !important;

        color: #BAE6FD !important;
    }


    div[data-testid="stAlert"] p {

        color: #BAE6FD !important;
    }


    /* =====================================================
       SUCCESS MESSAGE - GREEN
       ===================================================== */

    div[data-testid="stAlert"][data-baseweb="notification"] {

        border-radius: 12px;
    }


    /* =====================================================
       DATAFRAME
       ===================================================== */

    div[data-testid="stDataFrame"] {

        background-color: #101827;

        border: 1px solid #263650;

        border-radius: 14px;

        overflow: hidden;
    }


    /* =====================================================
       DIVIDERS
       ===================================================== */

    hr {

        border-color: #202C42 !important;
    }


    /* =====================================================
       INPUT FOCUS
       ===================================================== */

    input:focus,
    textarea:focus {

        border-color: #8B5CF6 !important;

        box-shadow:
            0 0 0 1px #8B5CF6 !important;
    }


    /* =====================================================
       SCROLLBAR
       ===================================================== */

    ::-webkit-scrollbar {

        width: 8px;
    }


    ::-webkit-scrollbar-track {

        background: #080D18;
    }


    ::-webkit-scrollbar-thumb {

        background: #334155;

        border-radius: 10px;
    }


    ::-webkit-scrollbar-thumb:hover {

        background: #6366F1;
    }

    </style>
    """,
    unsafe_allow_html=True
)
 

with st.sidebar:

    st.title("⚡ EcoCrew AI")

    st.caption(
        "Smart Energy Optimization System"
    )

    st.divider()

    st.subheader("📂 Upload Energy Data")

    st.write(
        "Upload your appliance CSV file"
    )

    uploaded_file = st.file_uploader(
        "Choose CSV file",
        type=["csv"],
        label_visibility="collapsed"
    )


    st.divider()

    st.subheader("📌 Required CSV Columns")

    st.info(
        "Your CSV must contain:\n\n"
        "• appliance\n\n"
        "• power_watts\n\n"
        "• hours_per_day"
    )

    st.caption(
        "Only the uploaded CSV will be analyzed."
    )



st.title("⚡ EcoCrew AI")

st.subheader(
    "Smart Energy Optimization Dashboard"
)

st.write(
    "Analyze appliance energy consumption, "
    "identify major energy consumers, and get "
    "AI-powered energy-saving recommendations."
)



if uploaded_file is None:

    st.divider()

    st.info(
        "📂 Upload your appliance CSV from the sidebar "
        "to start the energy analysis."
    )

    st.stop()



try:

    data = pd.read_csv(uploaded_file)

except Exception as e:

    st.error(
        f"Unable to read CSV file: {e}"
    )

    st.stop()



required_columns = [
    "appliance",
    "power_watts",
    "hours_per_day"
]


missing_columns = [
    column
    for column in required_columns
    if column not in data.columns
]


if missing_columns:

    st.error(
        "Missing required columns: "
        + ", ".join(missing_columns)
    )

    st.stop()




data["power_watts"] = pd.to_numeric(
    data["power_watts"],
    errors="coerce"
)

data["hours_per_day"] = pd.to_numeric(
    data["hours_per_day"],
    errors="coerce"
)


data = data.dropna(
    subset=[
        "appliance",
        "power_watts",
        "hours_per_day"
    ]
)


if data.empty:

    st.error(
        "No valid appliance data found."
    )

    st.stop()




data["monthly_energy_kwh"] = (
    data["power_watts"]
    * data["hours_per_day"]
    * 30
) / 1000


electricity_rate = 8


data["monthly_cost"] = (
    data["monthly_energy_kwh"]
    * electricity_rate
)



total_energy = data[
    "monthly_energy_kwh"
].sum()


total_cost = data[
    "monthly_cost"
].sum()


estimated_savings = (
    total_cost * 0.15
)


highest_consumer = data.loc[
    data["monthly_energy_kwh"].idxmax()
]


if total_energy > 0:

    highest_share = (
        highest_consumer["monthly_energy_kwh"]
        / total_energy
    ) * 100

else:

    highest_share = 0



st.success(
    f"📄 {uploaded_file.name} uploaded successfully"
)

st.caption(
    f"{len(data)} appliances detected"
)




st.divider()

st.header("📈 Energy Overview")


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "⚡ Monthly Energy",
        f"{total_energy:.1f} kWh"
    )


with col2:

    st.metric(
        "💰 Estimated Bill",
        f"₹{total_cost:.2f}"
    )


with col3:

    st.metric(
        "🔥 Top Consumer",
        highest_consumer["appliance"]
    )


with col4:

    st.metric(
        "💡 Potential Savings",
        f"₹{estimated_savings:.0f}"
    )




st.divider()

st.header(
    "🔥 Highest Energy Consumer"
)


st.info(
    f"{highest_consumer['appliance']} is your "
    f"highest energy-consuming appliance with "
    f"{highest_consumer['monthly_energy_kwh']:.1f} "
    f"kWh/month ({highest_share:.1f}% of total usage)."
)



st.divider()

st.header(
    "📊 Energy Analytics"
)


chart1, chart2 = st.columns(2)


with chart1:

    st.subheader(
        "⚡ Monthly Energy by Appliance"
    )

    energy_chart = data.set_index(
        "appliance"
    )["monthly_energy_kwh"]

    st.bar_chart(
        energy_chart,
        height=350
    )


with chart2:

    st.subheader(
        "💰 Monthly Cost by Appliance"
    )

    cost_chart = data.set_index(
        "appliance"
    )["monthly_cost"]

    st.bar_chart(
        cost_chart,
        height=350
    )



st.divider()

st.header(
    "📋 Appliance Details"
)


display_data = data.copy()


display_data[
    "monthly_energy_kwh"
] = display_data[
    "monthly_energy_kwh"
].round(2)


display_data[
    "monthly_cost"
] = display_data[
    "monthly_cost"
].round(2)


st.dataframe(
    display_data,
    use_container_width=True,
    hide_index=True
)




st.divider()

st.header(
    "🤖 AI Energy Analysis"
)


st.write(
    "CrewAI + Groq analyzes your energy data "
    "and generates personalized energy-saving "
    "recommendations."
)


if st.button(
    "🔍 Analyze Energy Usage"
):

    with st.spinner(
        "🤖 AI is analyzing your energy data..."
    ):

        energy_data = data.to_string(
            index=False
        )


        try:

            result = energy_crew.kickoff(
                inputs={
                    "energy_data": energy_data,
                    "total_energy": total_energy,
                    "total_cost": total_cost
                }
            )


            st.markdown(
                result.raw
            )


        except Exception as e:

            st.error(
                f"AI analysis failed: {e}"
            )



st.divider()

st.caption(
    "⚡ EcoCrew AI • Smart Energy Optimization System "
    "• Powered by Streamlit + CrewAI + Groq"
)