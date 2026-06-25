import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Data Science Portfolio", layout="wide")

# ---------- SIDEBAR NAVIGATION ----------
st.sidebar.title("📊 Projects")
projects = {
    "🏠 Home": "home",
    "1. Safety Stock Forecaster": "stock",
    "2. Marketing Attribution": "attribution",
    "3. CLV Predictor": "clv",
    "4. Churn Prevention": "churn",
    "5. Cloud Cost Anomaly": "cloud",
    "6. Project Estimator": "estimator",
    "7. Credit Underwriting": "credit",
    "8. Rental Yield": "rental",
    "9. Flight Risk": "flight",
    "10. Price Shield": "price"
}
selection = st.sidebar.radio("Choose a project", list(projects.keys()))
project_key = projects[selection]

# ---------- HOME PAGE ----------
def home():
    st.title("🚀 Data Science Portfolio – Direct‑ROI Projects")
    st.markdown("""
    I turn raw data into **financial impact**. Each project below is a live prototype that demonstrates:
    - **Business pain** understood
    - **Machine learning** solution engineered (in Colab)
    - **Interactive dashboard** (this Streamlit app) to showcase the ROI
    - **Deployed** on Streamlit Cloud, code on GitHub

    Use the sidebar to explore any project.
    """)
    st.image("https://via.placeholder.com/800x200?text=Building+Data+Products+that+Save+or+Make+Money", use_column_width=True)

# ---------- PROJECT 1: Safety Stock Forecaster ----------
def project_stock():
    st.header("📦 Dynamic Safety Stock & Inventory Stockout Forecaster")
    st.markdown("""
    **Business Pain:** Over‑stocking ties up cash; under‑stocking loses sales.  
    **Solution:** Prophet/XGBoost forecast 30‑day demand with seasonality & holidays.  
    **ROI Pitch:** *"Predict demand swings 30 days ahead and recommend exact safety stock – reduce dead stock cash and prevent stockouts."*
    """)

    # Dummy data: daily sales
    dates = pd.date_range(start='2023-01-01', periods=90, freq='D')
    sales = 100 + 20 * np.sin(np.linspace(0, 4*np.pi, 90)) + np.random.normal(0, 5, 90)
    df = pd.DataFrame({'Date': dates, 'Sales': sales})

    fig = px.line(df, x='Date', y='Sales', title='Actual Daily Sales (Last 90 Days)')
    st.plotly_chart(fig, use_container_width=True)

    # Forecast (dummy)
    forecast = [sales[-1] + i*0.5 + np.random.normal(0,2) for i in range(30)]
    forecast_dates = pd.date_range(start=dates[-1] + pd.Timedelta(days=1), periods=30)
    df_forecast = pd.DataFrame({'Date': forecast_dates, 'Forecast': forecast})

    fig2 = px.line(df_forecast, x='Date', y='Forecast', title='30‑Day Demand Forecast')
    st.plotly_chart(fig2, use_container_width=True)

    safety_stock = int(np.percentile(forecast, 95))  # 95th percentile
    st.metric("📦 Recommended Safety Stock Units", safety_stock, delta="to prevent stockouts")

# ---------- PROJECT 2: Marketing Attribution ----------
def project_attribution():
    st.header("📢 Algorithmic Multi‑Channel Marketing Attribution Engine")
    st.markdown("""
    **Business Pain:** Marketing spend is wasted – which channel actually drives conversions?  
    **Solution:** Markov‑chain or regression‑based attribution vs. flawed last‑click.  
    **ROI Pitch:** *"Reallocate ad budget from low‑performers to high‑performers – boost ROAS without increasing total spend."*
    """)

    channels = ['Facebook', 'Google', 'TikTok', 'Email']
    last_click = [40, 35, 15, 10]
    algorithmic = [30, 45, 20, 5]  # dummy

    df = pd.DataFrame({
        'Channel': channels,
        'Last‑Click Attribution (%)': last_click,
        'Algorithmic Attribution (%)': algorithmic
    })

    fig = px.bar(df, x='Channel', y=['Last‑Click Attribution (%)', 'Algorithmic Attribution (%)'],
                 barmode='group', title='Attribution Comparison')
    st.plotly_chart(fig, use_container_width=True)

    # Budget simulation slider
    budget = st.slider("💰 Total Monthly Ad Budget ($)", 1000, 10000, 5000)
    # Assume algorithmic suggests shifting 20% from low to high
    new_alloc = [budget * 0.3, budget * 0.45, budget * 0.2, budget * 0.05]
    current_alloc = [budget * 0.4, budget * 0.35, budget * 0.15, budget * 0.1]
    df2 = pd.DataFrame({'Channel': channels, 'Current Spend': current_alloc, 'Optimised Spend': new_alloc})
    fig2 = px.bar(df2, x='Channel', y=['Current Spend', 'Optimised Spend'],
                  barmode='group', title='Budget Reallocation Simulation')
    st.plotly_chart(fig2, use_container_width=True)

    st.success(f"📈 Estimated ROAS increase: +{np.random.randint(15, 30)}%")

# ---------- PROJECT 3: CLV Predictor ----------
def project_clv():
    st.header("💎 Customer Lifetime Value (CLV) & Tier‑Shift Predictor")
    st.markdown("""
    **Business Pain:** Acquiring new customers costs 5x more – need to retain VIPs.  
    **Solution:** RFM + regression model to predict 12‑month value.  
    **ROI Pitch:** *"Flag high‑value cohorts early so retention teams prioritise the right accounts."*
    """)

    # Dummy customer segments
    segments = ['Bronze', 'Silver', 'Gold', 'Platinum']
    avg_clv = [200, 500, 1200, 3000]
    retention_rate = [0.6, 0.75, 0.85, 0.95]

    df = pd.DataFrame({'Segment': segments, 'Avg 12‑Month CLV ($)': avg_clv, 'Retention Rate': retention_rate})
    fig = px.bar(df, x='Segment', y='Avg 12‑Month CLV ($)', color='Retention Rate',
                 title='CLV by Customer Tier', color_continuous_scale='Blues')
    st.plotly_chart(fig, use_container_width=True)

    # Discount simulation
    discount = st.slider("💸 Offer Discount (%) to Gold/Platinum", 0, 20, 5)
    new_retention = [r + (discount/100)*0.1 for r in retention_rate]  # simplistic
    df2 = pd.DataFrame({'Segment': segments, 'New Retention': new_retention})
    fig2 = px.bar(df2, x='Segment', y='New Retention', title='Projected Retention after Discount')
    st.plotly_chart(fig2, use_container_width=True)

# ---------- PROJECT 4: Churn Prevention (Placeholder) ----------
def project_churn():
    st.header("🔄 B2B Subscription 'Next‑Best‑Action' Churn Prevention")
    st.markdown("""
    **Business Pain:** SaaS churn costs millions – users cancel after inactivity.  
    **Solution:** LightGBM classifier gives daily churn probability + prescribes action.  
    **ROI Pitch:** *"Prescribe the exact action to save each account before they cancel."*
    """)
    st.info("Demo: Search an account to see churn risk and recommended action.")
    account = st.text_input("Enter account ID (e.g., 'acme_inc')")
    if account:
        risk = np.random.uniform(0, 1)
        st.metric("Churn Probability", f"{risk:.0%}")
        if risk > 0.7:
            st.warning("⚠️ Action Required: Offer free training call – user hasn't used analytics in 14 days.")
        else:
            st.success("✅ Low risk – continue normal engagement.")

# ---------- PROJECT 5: Cloud Cost Anomaly (Placeholder) ----------
def project_cloud():
    st.header("☁️ Serverless Cloud Infrastructure Cost Anomaly Forecaster")
    st.markdown("""
    **Business Pain:** Unexpected cloud bills due to inefficient code or traffic spikes.  
    **Solution:** Isolation Forest detects anomalies + linear trend projects monthly cost.  
    **ROI Pitch:** *"Catch inefficient patterns early to prevent bill spikes."*
    """)
    dates = pd.date_range(start='2023-01-01', periods=60, freq='D')
    costs = 100 + np.cumsum(np.random.normal(0, 2, 60)) + np.random.normal(0, 5, 60)
    df = pd.DataFrame({'Date': dates, 'Daily Cost ($)': costs})
    fig = px.line(df, x='Date', y='Daily Cost ($)', title='Daily Cloud Spend')
    st.plotly_chart(fig, use_container_width=True)
    projected = costs[-1] + np.random.normal(5, 2)
    st.metric("Projected Monthly Cost", f"${projected*30:.0f}", delta=f"${projected*30 - 4500:.0f} vs budget")

# ---------- PROJECT 6: Estimator (Placeholder) ----------
def project_estimator():
    st.header("📐 Dynamic Freelancer/Contractor Milestone Pricing Estimator")
    st.markdown("""
    **Business Pain:** Under‑quoting complex projects kills profits.  
    **Solution:** Gradient‑boosted regression predicts hours with 95% CI.  
    **ROI Pitch:** *"Never under‑quote again – use your own historical bottlenecks to estimate accurately."*
    """)
    pages = st.slider("Number of pages", 1, 50, 10)
    features = st.slider("Custom features", 0, 20, 5)
    api = st.checkbox("API connections?")
    hours = 20 + pages*2 + features*5 + (10 if api else 0)
    st.metric("Estimated Hours", f"{hours} h", delta=f"95% CI: [{int(hours*0.85)}, {int(hours*1.15)}]")

# ---------- PROJECT 7: Credit Underwriting (Placeholder) ----------
def project_credit():
    st.header("🏦 Automated FinTech Alternative Credit Underwriting")
    st.markdown("""
    **Business Pain:** Traditional credit scores exclude many good borrowers.  
    **Solution:** XGBoost with SHAP explanations on alternative data.  
    **ROI Pitch:** *"Expand addressable market by safely approving low‑risk applicants without a credit score."*
    """)
    income = st.number_input("Monthly income ($)", 1000, 20000, 4000)
    rent = st.number_input("Monthly rent ($)", 0, 5000, 1200)
    utility = st.slider("Utility payment consistency (0-100)", 0, 100, 80)
    # dummy model
    score = 0.4*income/10000 + 0.3*utility/100 - 0.2*rent/5000
    approved = score > 0.5
    if approved:
        st.success("✅ Approved (Green)")
    else:
        st.error("❌ Denied (Red)")
    st.bar_chart({"Risk Factors": [income/10000, utility/100, rent/5000]})

# ---------- PROJECT 8: Rental Yield (Placeholder) ----------
def project_rental():
    st.header("🏠 Short‑Term Rental Real Estate Yield Optimisation")
    st.markdown("""
    **Business Pain:** Pricing short‑term rentals optimally across seasons.  
    **Solution:** Regression model predicts occupancy and suggests dynamic pricing.  
    **ROI Pitch:** *"Maximise annual ROI by adjusting nightly rates to local occupancy patterns."*
    """)
    zipcode = st.selectbox("Select region", ['90210', '60614', '10001'])
    if zipcode:
        avg_rate = np.random.randint(100, 300)
        occupancy = np.random.uniform(0.5, 0.9)
        st.metric("Suggested Nightly Rate", f"${avg_rate}")
        st.metric("Projected Occupancy", f"{occupancy:.0%}")
        fig = px.line(x=['Jan','Feb','Mar','Apr','May','Jun'], y=np.random.randint(80,200,6),
                      title='Seasonal Pricing Schedule')
        st.plotly_chart(fig)

# ---------- PROJECT 9: Flight Risk (Placeholder) ----------
def project_flight():
    st.header("👥 Employee Flight‑Risk & Hiring Cost Prevention")
    st.markdown("""
    **Business Pain:** Losing senior talent costs thousands in replacement.  
    **Solution:** Classification model ranks flight‑risk probability by department.  
    **ROI Pitch:** *"Identify at‑risk employees early to retain key personnel before they quit."*
    """)
    dept = st.selectbox("Department", ['Engineering', 'Sales', 'Marketing'])
    risk = np.random.uniform(0, 1)
    st.metric(f"{dept} Flight Risk", f"{risk:.0%}")
    st.info("Estimated replacement cost liability: $XX,XXX")

# ---------- PROJECT 10: Price Shield (Placeholder) ----------
def project_price():
    st.header("📦 B2B Corporate Procurement Raw Material Price Shield")
    st.markdown("""
    **Business Pain:** Commodity price volatility erodes margins.  
    **Solution:** Time‑series forecast 90‑day price trends.  
    **ROI Pitch:** *"Alert procurement to impending price hikes – buy before the market climbs."*
    """)
    dates = pd.date_range(start='2023-01-01', periods=90)
    prices = 100 + np.cumsum(np.random.normal(0, 0.5, 90)) + np.random.normal(0, 2, 90)
    df = pd.DataFrame({'Date': dates, 'Price': prices})
    fig = px.line(df, x='Date', y='Price', title='Commodity Price Trend & Forecast')
    st.plotly_chart(fig)
    if prices[-1] > prices[0]*1.05:
        st.warning("⚠️ Optimal Buying Window: NOW – prices expected to rise further.")
    else:
        st.info("⏳ Wait – prices are stable/dropping.")

# ---------- ROUTER ----------
if project_key == "home":
    home()
elif project_key == "stock":
    project_stock()
elif project_key == "attribution":
    project_attribution()
elif project_key == "clv":
    project_clv()
elif project_key == "churn":
    project_churn()
elif project_key == "cloud":
    project_cloud()
elif project_key == "estimator":
    project_estimator()
elif project_key == "credit":
    project_credit()
elif project_key == "rental":
    project_rental()
elif project_key == "flight":
    project_flight()
elif project_key == "price":
    project_price()