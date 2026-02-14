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
        df_melted = df.melt(
            id_vars=['Name', 'Course'], 
            value_vars=['SubjectCode1', 'SubjectCode2', 'SubjectCode3', 'SubjectCode4', 'SubjectCode5'],
            var_name='Subject_Slot', 
            value_name='Code'
        )
        fig = px.bar(
            df_melted, 
            x="Name",      
            y="Code",          
            color="Subject_Slot",
            barmode="group",   
            title="Subject Codes per Student",
            labels={"Code": "Subject ID", "Subject_Slot": "Subject No."},
            hover_data=['Course']
        )
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