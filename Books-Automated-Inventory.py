import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time
import os

class EnterpriseInventoryBot:
    def __init__(self):
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        # Performance: Disable images and popups
        prefs = {
            "profile.managed_default_content_settings.images": 2,
            "profile.default_content_setting_values.notifications": 2
        }
        options.add_experimental_option("prefs", prefs)
        
        self.driver = webdriver.Edge(options=options)
        self.data = []

    def scrape_books(self, category_limit=5):
        """Scrapes multiple categories and handles pagination for inventory collection."""
        try:
            self.driver.get("https://books.toscrape.com/")
            print("🌐 Connection established. Mapping categories...")
            
            # Identify sidebar categories
            category_elements = self.driver.find_elements(By.CSS_SELECTOR, ".side_categories ul li ul li a")
            categories = [(c.text, c.get_attribute("href")) for c in category_elements[:category_limit]]

            for name, url in categories:
                print(f"📂 Scraping Category: {name}")
                self.driver.get(url)
                
                while True:
                    books = self.driver.find_elements(By.CLASS_NAME, "product_pod")
                    for book in books:
                        try:
                            title = book.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a").get_attribute("title")
                            price = float(book.find_element(By.CLASS_NAME, "price_color").text.replace('£', ''))
                            
                            # Extract Star Rating from Class
                            rating_raw = book.find_element(By.CLASS_NAME, "star-rating").get_attribute("class").split()[-1]
                            rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
                            rating = rating_map.get(rating_raw, 0)
                            
                            self.data.append({
                                "Category": name,
                                "Title": title,
                                "Price_GBP": price,
                                "Rating": rating,
                                "Value_Score": round(rating / price, 3) if price > 0 else 0,
                                "Inventory_Date": time.strftime("%Y-%m-%d")
                            })
                        except Exception:
                            continue

                    # Handle Pagination
                    try:
                        next_btn = self.driver.find_element(By.CSS_SELECTOR, "li.next a")
                        next_btn.click()
                    except:
                        break 
            
            df = pd.DataFrame(self.data)
            df.to_csv("inventory_data.csv", index=False)
            print(f"\n✅ DATA PIPELINE SUCCESS: {len(df)} items saved to 'inventory_data.csv'")
            
        finally:
            self.driver.quit()

    def create_dashboard_file(self):
        """Generates the Ultra-UI professional dashboard script."""
        dashboard_code = """
import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="InvenTrace Pro", layout="wide", page_icon="📦")

# 2. Ultra-UI Custom CSS
st.markdown(\"\"\"
    <style>
    .main { background-color: #0e1117; }
    [data-testid="stMetricValue"] { font-size: 32px; color: #00d4ff; font-weight: bold; }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; border-bottom: 1px solid #30363d; }
    .stTabs [data-baseweb="tab"] { 
        height: 50px; background-color: transparent; 
        color: #8b949e; font-size: 16px;
    }
    .stTabs [aria-selected="true"] { color: #00d4ff !important; border-bottom: 2px solid #00d4ff !important; }
    div[data-testid="stExpander"] { background-color: #161b22; border: 1px solid #30363d; border-radius: 8px; }
    </style>
\"\"\", unsafe_allow_html=True)

st.title("📦 InvenTrace Pro | Master Management Console")
st.markdown("---")

try:
    df = pd.read_csv("inventory_data.csv")
    
    # --- Sidebar Controls ---
    with st.sidebar:
        st.header("Global Configuration")
        selected_cats = st.multiselect("Active Categories", options=df['Category'].unique(), default=df['Category'].unique())
        price_range = st.slider("Budget Filter (£)", 0.0, float(df['Price_GBP'].max()), (0.0, float(df['Price_GBP'].max())))
        st.divider()
        st.caption("System Status: Online | Version 2.0.26")

    # Filtering Logic
    f_df = df[(df['Category'].isin(selected_cats)) & (df['Price_GBP'].between(price_range[0], price_range[1]))]

    # --- KPI Ribbon ---
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    kpi1.metric("Current SKUs", len(f_df))
    kpi2.metric("Avg Unit Price", f"£{f_df['Price_GBP'].mean():.2f}")
    kpi3.metric("Stock Valuation", f"£{f_df['Price_GBP'].sum():.0f}")
    kpi4.metric("Avg Rating", f"{f_df['Rating'].mean():.1f} ⭐")

    # --- Feature Tabs ---
    tab1, tab2, tab3 = st.tabs(["📊 Performance Insights", "💎 Strategic ROI", "🗄️ Master Ledger"])

    with tab1:
        c_left, c_right = st.columns(2)
        with c_left:
            # Interactive Sunburst for Category Composition
            fig_sun = px.sunburst(f_df, path=['Category', 'Rating'], values='Price_GBP', 
                                 template="plotly_dark", color_continuous_scale='RdBu')
            st.plotly_chart(fig_sun, width='stretch')
        with c_right:
            # Price Density Histogram
            fig_hist = px.histogram(f_df, x="Price_GBP", color="Category", 
                                   marginal="box", template="plotly_dark")
            st.plotly_chart(fig_hist, width='stretch')

    with tab2:
        st.subheader("High-Value Inventory (Best Rating-to-Price Ratio)")
        # Displaying top Value Score items
        roi_df = f_df.sort_values("Value_Score", ascending=False).head(12)
        st.dataframe(roi_df[['Title', 'Category', 'Price_GBP', 'Rating', 'Value_Score']], 
                     width='stretch', hide_index=True)

    with tab3:
        st.subheader("Inventory Record Search")
        st.dataframe(f_df, width='stretch')

except Exception as e:
    st.warning("Awaiting Data Feed...")
    st.info("Run the Selenium Master Script to populate the Inventory Ledger.")
"""
        with open("dashboard_app.py", "w", encoding="utf-8") as f:
            f.write(dashboard_code)
        print("📁 ULTRA-UI DASHBOARD CREATED: 'dashboard_app.py'")

if __name__ == "__main__":
    bot = EnterpriseInventoryBot()
    #5 categories scraped
    bot.scrape_books(category_limit=5)
    bot.create_dashboard_file()
    print("\n🚀 PIPELINE COMPLETE. Run: streamlit run dashboard_app.py")