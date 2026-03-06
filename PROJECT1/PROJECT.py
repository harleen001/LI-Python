import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Project", page_icon=":bar_chart:",layout="wide")
cola,colb=st.columns([3,7])
with colb:
   st.title(':red[PETROLEUM PRODUCTS]')

#PDF OPTION
st.markdown("## 🖨 Export as PDF")
show_all = st.checkbox("Show All Sections for PDF Export", value=False)

tab1,tab2,tab3=st.tabs(['WORLD ANALYSIS','INDIA ANALYSIS','PREDICTION'])
def tab1_content():
    
    df = pd.read_csv("PP COUNTRY-WISE.csv")
    df.columns = df.columns.str.strip()
  


    st.header(":blue[Country-Wise Production]")

# Sidebar for user inputs
    st.sidebar.header("Controls")
    

# Select top N countries
    top_n = st.sidebar.slider("Select top N countries", min_value=5, max_value=30, value=10, step=1)
    


# Filter top N countries
    top_countries = df.nlargest(top_n, "Production(thousand barrels/day)")

# Choropleth Map
    fig = px.choropleth(
    top_countries,
    locations="Country",
    locationmode="country names",
    color="Production(thousand barrels/day)",
    hover_name="Country",
    color_continuous_scale='YlOrRd',
    title=f"Top {top_n} Countries by Petroleum Products Production (thousand barrels/day)"
    
)   
    st.markdown("---")

    fig.update_layout(geo=dict(showframe=False, showcoastlines=True))

# Show the map
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("---")

    df=pd.read_csv(r'C:\Users\hp\Desktop\PROJECT\PP COUNTRY-WISE.csv')

    fig=px.bar(top_countries,x='Country',y='Production(thousand barrels/day)',height=500,
           template='gridon',color='Country')
    st.plotly_chart(fig,use_container_width=True)
    st.markdown("---")

###############################################################################################################################
########################################################################################################
#########################################################################################################
def tab2_content():
    
    col1,col2=st.columns([5,5])
    with col1:
    # Load data
       df = pd.read_csv("Statewise_Sales Consumption.csv")
       df.columns = df.columns.str.strip()
       st.header(':blue[State-Wise Consumption]')
       st.markdown('----')

# Dropdown to select state
       states = df['STATE/UT'].unique()
       selected_state = st.selectbox("Select a State/UT",sorted( states))
# Filter for selected state
       filtered_df = df[df['STATE/UT'] == selected_state]

# Reshape to long format
       melted_df = filtered_df.melt(id_vars='STATE/UT', var_name='Fiscal Year', value_name='Value')

# Sort Fiscal Year
       melted_df['Fiscal Year'] = pd.Categorical(
       melted_df['Fiscal Year'],
       categories=sorted(melted_df['Fiscal Year'].unique()),
       ordered=True
)

# Create figure using plotly.graph_objects for better control
       fig = go.Figure()

# Bar trace
       fig.add_trace(go.Bar(
     x=melted_df['Fiscal Year'],
      y=melted_df['Value'],
    text=melted_df['Value'],
    textposition='outside',
    name='Value',
    marker_color='skyblue'
))

# Line trace
       fig.add_trace(go.Scatter(
    x=melted_df['Fiscal Year'],
    y=melted_df['Value'],
    mode='lines+markers',
    name='Trend Line',
    line=dict(color='orange')
))

# Update layout
       fig.update_layout(
    title=f"{selected_state} - Yearly Consumption Trend",
    xaxis_title='Fiscal Year',
    yaxis_title='Value(1000 Metric Tonnes)',
    hovermode='x unified',
    bargap=0.2
)

# Show in Streamlit
       st.plotly_chart(fig, use_container_width=True)
       
####################################################################################
    with col2:
    # Load Excel
      df = pd.read_excel("product wise consump.xlsx")
      df.columns = df.columns.str.strip()
      st.header(':blue[Product-Wise Consumption]')
      st.markdown('----')
# Extract product column & months
      product_col = df.columns[0]
      months = df.columns[1:]
      df[product_col] = df[product_col].astype(str).str.strip()

# Dropdown for product
      products = df[product_col].dropna().unique()
      selected_product = st.selectbox("Select a Product", products)

# Filter data
      row = df[df[product_col] == selected_product]

      if not row.empty:
        y_values = row.iloc[0, 1:].values
        x_months = months

    # Create plot
        fig = go.Figure()

    # Glowing shadow-style line (thicker & faded underlayer)
        fig.add_trace(go.Scatter(
        x=x_months,
        y=y_values,
        mode='lines',
        line=dict(width=8, color='rgba(255,0,0,0.2)'),  # red shadow
        showlegend=False,
        hoverinfo='skip'  # hide hover for glow
    ))

    # Main line on top
        fig.add_trace(go.Scatter(
        x=x_months,
        y=y_values,
        mode='lines+markers',
        name='Value',
        line=dict(width=3, color='crimson'),
        marker=dict(size=8, color='crimson'),
        hovertemplate='Month: %{x}<br>Value: %{y:,.0f}<extra></extra>'
    ))

    # Layout styling
        fig.update_layout(
        title=f"{selected_product} - Monthly Consumption Trend(2023-24)",
        xaxis_title="Month",
        yaxis_title="Value(1000 Metric Tonnes)",
        hovermode="x unified",
        template='simple_white',
        height=500
    )

        st.plotly_chart(fig, use_container_width=True)

      else:
        st.warning("No data found for the selected product.")
    st.markdown("---")

#######################################################
# --- Load & Clean Data ---
    df = pd.read_csv("Petroleum_Sector_Contribution.csv")
    df = df[['Year', 'Excise_duty ', 'Sales_Tax ']]
    df.columns = ['Year', 'Excise_duty', 'Sales_Tax']
    df['Year'] = df['Year'].astype(str)

# --- Custom Color Palette ---
    excise_colors = [
    '#264653', '#2a9d8f', '#e9c46a', '#f4a261', '#e76f51',
    '#6a4c93', '#457b9d', '#1d3557', '#ff6b6b', '#ffa600'
]
    sales_colors = [
    '#003f5c', '#58508d', '#bc5090', '#ff6361', '#ffa600',
    '#00b894', '#fdcb6e', '#d63031', '#6c5ce7', '#0984e3'
]

# --- Donut Chart 1: Excise Duty by Year ---
    fig1 = go.Figure(data=[go.Pie(
    labels=df['Year'],
    values=df['Excise_duty'],
    hole=0.45,
    textinfo='label+percent',
    marker=dict(colors=excise_colors),
    hovertemplate='Year: %{label}<br>Excise Duty: ₹%{value} Cr'
)])
    fig1.update_layout(title="🛢️ Excise Duty Contribution by Year")

# --- Donut Chart 2: Sales Tax by Year --- 
    fig2 = go.Figure(data=[go.Pie(
    labels=df['Year'],
    values=df['Sales_Tax'],
    hole=0.45,
    textinfo='label+percent',
    marker=dict(colors=sales_colors),
    hovertemplate='Year: %{label}<br>Sales Tax: ₹%{value} Cr'
)])
    fig2.update_layout(title="⛽ Sales Tax Contribution by Year")

# --- Layout ---
    st.header(":blue[Petroleum Sector Contribution in GDP]")


    col3, col4 = st.columns(2)
    with col3:
       st.plotly_chart(fig1, use_container_width=True)
    with col4:
       st.plotly_chart(fig2, use_container_width=True)

    st.markdown("---")
#######################################################
    import_df = pd.read_excel("import.xlsx")
    export_df = pd.read_csv("export.csv")

# Clean column names
    import_df.columns = import_df.columns.str.strip()
    export_df.columns = export_df.columns.str.strip()

# Rename for convenience
    import_df.rename(columns={"PRODUCT": "Product"}, inplace=True)
    export_df.rename(columns={"PRODUCT": "Product"}, inplace=True)

# Define month order (April to March)
    month_order = ["APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER",
               "OCTOBER", "NOVEMBER", "DECEMBER", "JANUARY", "FEBRUARY", "MARCH"]

# Get valid month columns
    month_cols = [col for col in import_df.columns if col in month_order]

# Track active tab
    if "active_tab" not in st.session_state:
       st.session_state.active_tab = "Import"
    
    st.header(":blue[Import/Export of Petroleum Products in 2023-24]")

# Create UI tabs
    tabA, tabB = st.tabs(["📥 Import of Petroleum Products", "📤 Export of Petroleum Products"])

# ========== IMPORT TAB ==========
    with tabA:
        st.session_state.active_tab = "Import of Petroleum Products"
        

        selected_product = st.selectbox("Select a Product (Import)", import_df["Product"].unique())

        filtered = import_df[import_df["Product"] == selected_product]
        if not filtered.empty:
           data = filtered[month_cols].T
           data.columns = [selected_product]
           data.index.name = "Month"
           data.reset_index(inplace=True)
           data["Month"] = pd.Categorical(data["Month"], categories=month_order, ordered=True)
           data.sort_values("Month", inplace=True)

           fig = px.line(
            data,
            x="Month",
            y=selected_product,
            markers=True,
            line_shape='spline',
            title=f"Monthly Import Trend: {selected_product}",
            template='plotly_white',
            labels={selected_product: "Quantity (000 MT)"}
        )
           fig.update_traces(
            line=dict(width=3),
            marker=dict(size=8, color='black', line=dict(width=1, color='white')),
            hovertemplate='<b>%{x}</b><br>Quantity: %{y:,} (000 MT)<extra></extra>'
        )
           fig.update_layout(
            title_font_size=20,
            title_x=0.5,
            xaxis_title="Month",
            yaxis_title="Quantity (in '000 Metric Tonnes)",
            xaxis=dict(showgrid=True, tickangle=45),
            yaxis=dict(showgrid=True, zeroline=False),
            plot_bgcolor='rgba(0,0,0,0)',
            hovermode="x unified"
        )
           st.plotly_chart(fig, use_container_width=True)
        
# ========== EXPORT TAB ==========
    with tabB:
       st.session_state.active_tab = "Export of Petroleum Products"
      

       selected_product = st.selectbox("Select a Product (Export)", export_df["Product"].unique())

       filtered = export_df[export_df["Product"] == selected_product]
       if not filtered.empty:
           data = filtered[month_cols].T
           data.columns = [selected_product]
           data.index.name = "Month"
           data.reset_index(inplace=True)
           data["Month"] = pd.Categorical(data["Month"], categories=month_order, ordered=True)
           data.sort_values("Month", inplace=True)

           fig = px.line(
            data,
            x="Month",
            y=selected_product,
            markers=True,
            line_shape='spline',
            title=f"Monthly Export Trend: {selected_product}",
            
            template='plotly_white',
            labels={selected_product: "Quantity (000 MT)"}
        )
           fig.update_traces(
            line=dict(width=3),
            marker=dict(size=8, color='black', line=dict(width=1, color='white')),
            hovertemplate='<b>%{x}</b><br>Quantity: %{y:,} (000 MT)<extra></extra>'
        )
           fig.update_layout(
            title_font_size=20,
            title_x=0.5,
            xaxis_title="Month",
            yaxis_title="Quantity (in '000 Metric Tonnes)",
            xaxis=dict(showgrid=True, tickangle=45),
            yaxis=dict(showgrid=True, zeroline=False),
            plot_bgcolor='rgba(0,0,0,0)',
            hovermode="x unified"
        )
           st.plotly_chart(fig, use_container_width=True)
    




    st.markdown("---")
############################################################################################################
#######################################################################################################
##########################################################################################################
def tab3_content():
    
    df = pd.read_csv("ML.csv")
    X = df[["year"]]
    y = df["consumption"]

    # Train the model
    import pickle
    with open("trained_model.pkl","rb")as f:
       model=pickle.load(f)



# Sidebar: Year selection
   # st.selectbox("📅 Select the year",list(range(2015,2031)))
    st.header(" :blue[Prediction:Petroleum Products Consumption  in India]")
    st.markdown('----')
    
    selected_year = st.selectbox("Select year to predict:", list(range(2020, 2035)))

# Prediction
    predicted_value = model.predict([[selected_year]])[0]

# Full prediction range
    future_years = np.arange(df["year"].min(), 2035).reshape(-1, 1)
    future_preds = model.predict(future_years)

# Streamlit display
   
    st.write(f"### 📌 Selected Year: **{selected_year}**")
    st.markdown("---")
    st.write(f"### 📈 Predicted Consumption: **{predicted_value:,.1f} (1000 metric tonnes)**")
    st.markdown("---")

# Plotly graph
    fig = go.Figure()

# Actual data with '+' markers
    fig.add_trace(go.Scatter(
    x=df["year"],
    y=y,
    mode='markers+text',
    name='Actual Data',
    marker=dict(symbol='cross', size=10, color='blue'),
    text=[f"{val:,.1f}" for val in y],
    textposition="top center",
    hovertemplate="Year: %{x}<br>Consumption: %{y:,.1f}<extra></extra>"
))

# Regression line
    fig.add_trace(go.Scatter(
    x=future_years.flatten(),
    y=future_preds,
    mode='lines',
    name='Regression Line',
    line=dict(color='red'),
    hovertemplate="Year: %{x}<br>Predicted: %{y:,.1f}<extra></extra>"
))

# Prediction point
    fig.add_trace(go.Scatter(
    x=[selected_year],
    y=[predicted_value],
    mode='markers',
    name='Prediction Point',
    marker=dict(size=12, color='green', symbol='circle'),
    hovertemplate=f"Selected Year: {selected_year}<br>Prediction: {predicted_value:,.1f}<extra></extra>"
))

# Layout
    fig.update_layout(
    title=" Prediction of Petroleum Products Consumption ",
    xaxis_title="Year",
    yaxis_title="Consumption (1000 Metric Tonnes)",
    legend_title="Legend",
    template="plotly_white"
)

# Show plot
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("---")

# --- Show all sections or use tabs ---
if show_all:
    st.markdown("""
    <script>
        window.addEventListener('load', function() {
            window.print();
        });
    </script>
    """, unsafe_allow_html=True)

    tab1_content()
    tab2_content()
    tab3_content()
    
else:
    tab1, tab2, tab3 = st.tabs(["WORLD ANALYSIS","INDIA ANALYSIS","PREDICTION"])
    with tab1: tab1_content()
    with tab2: tab2_content()
    with tab3: tab3_content()
  
