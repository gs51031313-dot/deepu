import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.ensemble import RandomForestClassifier
import base64

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Student Intelligence Dashboard", layout="wide")

# ---------------- BACKGROUND + UI ----------------
def set_bg():
    with open("rbu1.jpg", "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()

    st.markdown(f"""
    <style>

    /* 🌄 BACKGROUND */
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* 🌫️ LIGHT OVERLAY */
    .stApp::before {{
        content: "";
        position: fixed;
        inset: 0;
        backdrop-filter: blur(8px);
        background: rgba(255, 255, 255, 0.55);
        z-index: -1;
    }}

    /* 🔵 BLUE SIDEBAR (UPDATED) */
    section[data-testid="stSidebar"] {{
        background: linear-gradient(180deg, #1e3a8a, #1e40af, #1d4ed8);
        border-right: 1px solid rgba(0, 200, 255, 0.3);

        box-shadow:
            0 0 20px rgba(0, 140, 255, 0.6),
            inset 0 0 15px rgba(255, 255, 255, 0.08);
    }}

    section[data-testid="stSidebar"] * {{
        color: white !important;
    }}

    section[data-testid="stSidebar"] .stRadio > div {{
        background: rgba(255, 255, 255, 0.08);
        padding: 10px;
        border-radius: 12px;
        transition: 0.3s;
    }}

    section[data-testid="stSidebar"] .stRadio > div:hover {{
        background: rgba(0, 200, 255, 0.25);
        box-shadow: 0 0 12px rgba(0, 180, 255, 0.8);
    }}

    /* 🧊 METRIC CARDS */
    [data-testid="stMetric"] {{
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(10px);
        padding: 20px;
        border-radius: 18px;
        border: 1px solid rgba(0,0,0,0.1);
        color: black;
    }}

    /* ✨ BLUR + GLOW TITLES */
    h1, h2, h3 {{
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(15px);
        padding: 12px 30px;
        border-radius: 18px;
        display: inline-block;

        color: black !important;
        font-weight: bold;
        letter-spacing: 1px;

        box-shadow:
            0 0 10px rgba(0, 150, 255, 0.6),
            0 0 25px rgba(0, 150, 255, 0.4),
            inset 0 0 10px rgba(255, 255, 255, 0.4);

        text-shadow:
            0 0 5px rgba(0, 150, 255, 0.8),
            0 0 10px rgba(0, 150, 255, 0.6);
    }}

    h1:hover, h2:hover, h3:hover {{
        transform: scale(1.03);
        box-shadow:
            0 0 20px rgba(0, 200, 255, 1),
            0 0 40px rgba(0, 200, 255, 0.8);
    }}

    /* 🖤 TEXT */
    p, div, span {{
        color: black !important;
    }}

    /* 📊 TABLE */
    [data-testid="stDataFrame"] {{
        background: rgba(255,255,255,0.9);
        backdrop-filter: blur(8px);
        border-radius: 12px;
        color: black !important;
    }}

    /* 🔘 BUTTON */
    .stButton>button {{
        background: linear-gradient(90deg, #2563eb, #1e40af);
        color: white;
        border-radius: 10px;
        border: none;
    }}

    </style>
    """, unsafe_allow_html=True)

set_bg()

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    return pd.read_csv("student_exam_dataset_2000.csv")

df = load_data()

# ---------------- ML MODEL ----------------
X = df[["Math", "Science", "English"]]
y = (df["Percentage"] >= 40).astype(int)

model = RandomForestClassifier()
model.fit(X, y)
# ---------------- SIDEBAR LOGO ----------------
# ---------------- SIDEBAR LOGO ----------------
def add_sidebar_logo():
    with open("RBU2.png", "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()

    st.sidebar.markdown("""
        <style>
        .logo-container {
            text-align: center;
            padding: 15px 10px 25px 10px;
        }

        .logo-img {
            width: 180px;
            border-radius: 20px;
            transition: 0.3s ease-in-out;
            box-shadow: 0 0 20px rgba(0, 200, 255, 0.6);
        }

        .logo-img:hover {
            transform: scale(1.05);
            box-shadow: 0 0 30px rgba(0, 200, 255, 0.9);
        }

        .logo-title {
            color: #00cfff;
            font-size: 18px;
            font-weight: bold;
            margin-top: 10px;
            letter-spacing: 1px;
        }

        .logo-sub {
            color: #9ca3af;
            font-size: 12px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.sidebar.markdown(f"""
        <div class="logo-container">
            <img src="data:image/png;base64,{encoded}" class="logo-img">
        </div>
    """, unsafe_allow_html=True)

add_sidebar_logo()
# ---------------- SIDEBAR ----------------
st.sidebar.title("🎓 Student System")

page = st.sidebar.radio("MENU", [
    "Dashboard",
    "Analytics",
    "Reports",
    "Prediction"
])

# Filters
st.sidebar.markdown("## 🔍 Filters")

selected_grade = st.sidebar.multiselect(
    "Select Grade",
    df["Grade"].unique(),
    default=df["Grade"].unique()
)

min_perc, max_perc = st.sidebar.slider(
    "Percentage Range",
    0, 100, (0, 100)
)

filtered_df = df[
    (df["Grade"].isin(selected_grade)) &
    (df["Percentage"] >= min_perc) &
    (df["Percentage"] <= max_perc)
].copy()

# ---------------- DASHBOARD ----------------
if page == "Dashboard":

    st.markdown("<h1 style='text-align:center;'>📊 Student Intelligence Dashboard</h1>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Students", len(filtered_df))
    col2.metric("Average %", round(filtered_df["Percentage"].mean(), 2))
    col3.metric("Top Score", round(filtered_df["Percentage"].max(), 2))

    pass_percent = (filtered_df["Percentage"] >= 40).mean() * 100
    col4.metric("Pass %", f"{round(pass_percent,2)}%")

    st.markdown("---")

    st.subheader("📈 Performance Overview")
    fig = px.line(
        filtered_df.groupby("Grade")["Percentage"].mean().reset_index(),
        x="Grade",
        y="Percentage",
        markers=True
    )
    fig.update_layout(template="plotly_white")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("🏆 Top Students")
    st.dataframe(
        filtered_df.sort_values(by="Percentage", ascending=False).head(5)
    )

    st.subheader("📊 Pass vs Fail")
    filtered_df["Result"] = filtered_df["Percentage"].apply(
        lambda x: "Pass" if x >= 40 else "Fail"
    )

    fig2 = px.pie(filtered_df, names="Result")
    fig2.update_layout(template="plotly_white")
    st.plotly_chart(fig2, use_container_width=True)

# ---------------- ANALYTICS ----------------
elif page == "Analytics":

    st.title("📊 Analytics")

    col1, col2 = st.columns(2)

    with col1:
        fig = px.histogram(filtered_df, x="Percentage", nbins=20)
        fig.update_layout(template="plotly_white")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig2 = px.box(filtered_df, y="Percentage")
        fig2.update_layout(template="plotly_white")
        st.plotly_chart(fig2, use_container_width=True)

    st.subheader("📚 Subject-wise Average")

    subjects = ["Math", "Science", "English"]
    avg = [filtered_df[sub].mean() for sub in subjects]

    fig3 = px.bar(x=subjects, y=avg)
    fig3.update_layout(template="plotly_white")
    st.plotly_chart(fig3, use_container_width=True)

# ---------------- REPORTS ----------------
elif page == "Reports":

    st.title("📄 Reports")

    st.download_button(
        label="📥 Download CSV",
        data=filtered_df.to_csv(index=False),
        file_name="student_report.csv",
        mime="text/csv"
    )

# ---------------- PREDICTION ----------------
# ---------------- PREDICTION ----------------
elif page == "Prediction":

    st.title("🤖 Pass/Fail Prediction")

    math = st.number_input("Math Marks", 0, 100)
    science = st.number_input("Science Marks", 0, 100)
    english = st.number_input("English Marks", 0, 100)

    if st.button("Predict Result"):
        result = model.predict([[math, science, english]])

        # -------- CUSTOM STYLING --------
        st.markdown("""
        <style>
        .pass-box {
            background-color: #d4f8e8;
            color: #065f46;
            padding: 20px;
            border-radius: 12px;
            font-size: 20px;
            font-weight: bold;
            text-align: center;
            box-shadow: 0 0 15px rgba(0,255,150,0.4);
            border: 1px solid #34d399;
        }
        .fail-box {
            background-color: #ffe4e6;
            color: #7f1d1d;
            padding: 20px;
            border-radius: 12px;
            font-size: 20px;
            font-weight: bold;
            text-align: center;
            box-shadow: 0 0 15px rgba(255,0,0,0.3);
            border: 1px solid #f87171;
        }
        </style>
        """, unsafe_allow_html=True)

        # -------- RESULT DISPLAY --------
        if result[0] == 1:
            st.markdown(
                '<div class="pass-box">✅ Student will PASS 🎉</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                '<div class="fail-box">❌ Student may FAIL</div>',
                unsafe_allow_html=True
            )

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("📌 Developed by Darshandeep Singh")