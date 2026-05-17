import streamlit as st
import pandas as pd
import plotly.express as px

# ================= PAGE CONFIG =================
st.set_page_config(page_title="Freelancer Expense Dashboard", layout="wide")

# ================= HEADER (AESTHETIC) =================
st.markdown("""
<h1 style='text-align:center;
background: linear-gradient(to right, #74ebd5, #ACB6E5, #fbc2eb);
-webkit-background-clip: text;
color: transparent;
font-size: 55px;'>
💰 Freelancer Financial Analytics Dashboard
</h1>
""", unsafe_allow_html=True)

st.markdown("### 📊 20 Freelancers Smart Expense System")

# ================= LOAD DATA =================
df = pd.read_csv("data/multi_user_expenses.csv")

df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.to_period("M").astype(str)

# ================= FILTER =================
st.sidebar.header("🎯 Filters")
user = st.sidebar.selectbox("Select Freelancer", df["user_id"].unique())

filtered = df[df["user_id"] == user]

# ================= KPIs =================
income = filtered[filtered["amount"] > 0]["amount"].sum()
expense = filtered[filtered["amount"] < 0]["amount"].sum()
savings = income + expense

col1, col2, col3 = st.columns(3)

col1.metric("💰 Income", f"₹{income:,.0f}")
col2.metric("💸 Expense", f"₹{abs(expense):,.0f}")
col3.metric("🧾 Savings", f"₹{savings:,.0f}")

st.markdown("---")

# ================= CATEGORY DATA =================
cat = filtered[filtered["amount"] < 0].groupby("category")["amount"].sum().abs().reset_index()

# ================= AESTHETIC COLORS =================
colors_soft = [
    "#A0C4FF", "#BDB2FF", "#FFC6FF",
    "#FFD6A5", "#FDFFB6", "#CAFFBF"
]

# ================= CATEGORY BAR CHART =================
st.markdown("## 🟣 Spending by Category")

fig1 = px.bar(
    cat,
    x="category",
    y="amount",
    color="category",
    text="amount",
    color_discrete_sequence=colors_soft
)

st.plotly_chart(fig1, use_container_width=True)

# ================= MONTHLY TREND =================
st.markdown("## 🔵 Monthly Spending Trend")

monthly = filtered[filtered["amount"] < 0].groupby("month")["amount"].sum().abs().reset_index()

fig2 = px.line(
    monthly,
    x="month",
    y="amount",
    markers=True,
    line_shape="spline",
    color_discrete_sequence=["#74b9ff"]
)

st.plotly_chart(fig2, use_container_width=True)

# ================= PIE CHART =================
st.markdown("## 🟢 Expense Distribution")

fig3 = px.pie(
    cat,
    names="category",
    values="amount",
    hole=0.45,
    color_discrete_sequence=colors_soft
)

st.plotly_chart(fig3, use_container_width=True)

# ================= SMART SPENDING STATUS =================
st.markdown("## 📊 Spending Status")

total_spend = abs(expense)

if total_spend < 5000:
    status = "🟢 Low Spender"
    msg = "Excellent control over expenses."
elif total_spend < 15000:
    status = "🟡 Normal Spender"
    msg = "Healthy spending pattern."
else:
    status = "🔴 High Spender"
    msg = "Reduce unnecessary expenses."

st.markdown(f"### {status}")
st.info(msg)

# ================= RECOMMENDED VS ACTUAL =================
st.markdown("## 💡 Recommended vs Actual Spending")

recommended_ratios = {
    "Food": 0.30,
    "Travel": 0.15,
    "Shopping": 0.20,
    "Bills": 0.25,
    "Entertainment": 0.10
}

actual = filtered[filtered["amount"] < 0].groupby("category")["amount"].sum().abs()
total = actual.sum()

comparison = []

for cat_name, ratio in recommended_ratios.items():
    rec = total * ratio
    act = actual.get(cat_name, 0)
    comparison.append([cat_name, rec, act])

comp_df = pd.DataFrame(comparison, columns=["Category", "Recommended", "Actual"])

st.dataframe(comp_df)

fig4 = px.bar(
    comp_df,
    x="Category",
    y=["Recommended", "Actual"],
    barmode="group",
    color_discrete_sequence=["#55efc4", "#ff7675"]
)

st.plotly_chart(fig4, use_container_width=True)

# ================= TRANSACTION TABLE =================
st.markdown("## 📄 Transaction History")
st.dataframe(filtered.sort_values("date", ascending=False))