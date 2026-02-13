import mysql.connector
import pandas as pd
import plotly.express as px

config = {
    'user': 'root',         
    'password': '123456',
    'host': 'localhost',        
    'database': 'Student'       
}

try:
    conn = mysql.connector.connect(**config)
    print("Successfully connected to the database!")

    query = """
    SELECT 
        sm.Name, 
        sm.Course, 
        s.SubjectCode1, 
        s.SubjectCode2, 
        s.SubjectCode3, 
        s.SubjectCode4, 
        s.SubjectCode5
    FROM StudentMaster sm
    INNER JOIN Subject s ON sm.RegNo = s.RegNo;
    """

    df = pd.read_sql(query, conn)
    
    if df.empty:
        print("No data found.")
    else:
        # 5. RESHAPE DATA (Crucial for Bar Charts)
        # We transform the 5 columns (SubjectCode1...5) into two: 'Subject_Slot' and 'Code'
        df_melted = df.melt(
            id_vars=['Name', 'Course'], 
            value_vars=['SubjectCode1', 'SubjectCode2', 'SubjectCode3', 'SubjectCode4', 'SubjectCode5'],
            var_name='Subject_Slot', 
            value_name='Code'
        )

        # 6. CREATE THE PLOTLY BAR CHART
        fig = px.bar(
            df_melted, 
            x="Name",           # Students on the X-axis
            y="Code",           # Subject Code value on the Y-axis
            color="Subject_Slot", # Different color for each subject slot
            barmode="group",    # Puts bars side-by-side (use 'stack' for stacked)
            title="Subject Codes per Student",
            labels={"Code": "Subject ID", "Subject_Slot": "Subject No."},
            hover_data=['Course'] # Shows the course when you hover over a bar
        )

        # Optional: Force Y-axis to show integers (since subject codes are IDs)
        fig.update_layout(yaxis_type='linear')
        
        fig.show()

except mysql.connector.Error as err:
    print(f"Database Error: {err}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("\nDatabase connection closed.")