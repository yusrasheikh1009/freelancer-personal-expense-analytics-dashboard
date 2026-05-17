# 💰 Freelancer Personal Expense Analytics Dashboard

## 📌 Overview
The Freelancer Expense Analytics Dashboard is a data-driven financial intelligence system designed to help analyze, track, and visualize spending behavior of 20 simulated freelancers.

It transforms raw transaction data into meaningful insights using Python, Pandas, and Streamlit, similar to fintech platforms like Google Pay, CRED, and modern banking dashboards.

This project demonstrates how data science can be applied to financial analytics, budgeting, and decision-making systems.

---

## 🚀 Key Features

📊 Interactive expense analytics dashboard  
👤 Multi-user freelancer simulation (20 users)  
📅 Month-wise financial analysis  
🍩 Category-wise spending distribution  
💰 Budget tracking system  
⚠️ Overspending detection alerts  
📈 Monthly spending trend analysis  
🎨 Aesthetic interactive visualizations  
📂 Transaction data viewer  
🧠 Smart financial insights engine  

---

## 🔄 System Workflow

Data Generation → Data Cleaning → Feature Engineering → Filtering Engine → Budget Calculation → Analytics Engine → Visualization → Insights Dashboard

### Steps:
- Generate synthetic freelancer transaction data  
- Clean and structure dataset  
- Add derived features (month, user segmentation)  
- Apply filters (user, category, month)  
- Compute KPIs and spending metrics  
- Perform budget vs spending analysis  
- Generate interactive visualizations  
- Display final dashboard using Streamlit  

---

## 🧠 Tech Stack

Python, Pandas, NumPy, Plotly, Streamlit, Git & GitHub

---

## 📊 Analytics & Intelligence Features

- Total Spending Analysis  
- Income vs Expense Calculation  
- Savings Estimation  
- Category-wise Expense Breakdown  
- Monthly Spending Trends  
- Budget Utilization Tracking  
- Overspending Detection System  
- User-wise Spending Behavior  
- Top Spending Category Identification  
- Dynamic Filtering System  
- Real-time Dashboard Updates  

---
Skills Demonstrated:
Data Analysis
Financial Analytics
Python Programming
Dashboard Development
Data Visualization
Business Intelligence

## 📈 Outputs

✔ Category-wise spending distribution  
✔ Monthly expense trends  
✔ Budget utilization tracking  
✔ Spending status classification (Low / Normal / High)  
✔ Recommended vs Actual spending comparison  
✔ Interactive dashboard visualizations  

---

## 🖥️ Run Project

```bash
python -m streamlit run src/app_streamlit.py

Then open:
http://localhost:8501

## 📸 Screenshots

### 🏠 Dashboard Overview
c:\Users\hp\Pictures\Screenshots\Screenshot 2026-05-17 122842.png
---

### 📈 Monthly Spending Trends
c:\Users\hp\Pictures\Screenshots\Screenshot 2026-05-17 122857.png
---
### 📈 Spender Type
c:\Users\hp\Pictures\Screenshots\Screenshot 2026-05-17 122916.png

### 🟢 Budget vs Actual Spending
c:\Users\hp\Pictures\Screenshots\Screenshot 2026-05-17 122928.png

---
### 📄 Transaction Data View
c:\Users\hp\Pictures\Screenshots\Screenshot 2026-05-17 122946.png

⚠️ Important Notes
Install dependencies:

pip install -r requirements.txt

Run dataset generator first:

python src/generate_users.py

Run only using Streamlit:

streamlit run src/app_streamlit.py

Project Structure
Freelancer-Expense-Analytics-Dashboard/
│
├── data/
│   └── multi_user_expenses.csv
│
├── src/
│   ├── generate_users.py
│   └── app_streamlit.py
│
├── outputs/
├── images/
├── requirements.txt
└── README.md

Conclusion

This project demonstrates how data science and visualization can be used to build intelligent financial dashboards similar to real-world fintech applications.
It helps understand:
Spending behavior analysis
Budget tracking systems
Data visualization techniques
Business intelligence thinking

🚀 Future Improvements
AI-based expense prediction system
Smart budgeting recommendations
Login-based multi-user authentication system
PDF report generation
Cloud deployment (Streamlit Cloud / AWS)

👨‍💻 Author
Yusra Sheikh Ashfaq