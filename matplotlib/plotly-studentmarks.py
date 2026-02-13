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
        print("No data found. Ensure your 'Subject' table has matching RegNo entries.")
    else:
        print("\n--- Fetched Data ---")
        print(df.head())

        plot_df = df.set_index('Name')[['SubjectCode1', 'SubjectCode2', 'SubjectCode3', 'SubjectCode4', 'SubjectCode5']]

        fig = px.imshow(
            plot_df,
            labels=dict(x="Subject Slot", y="Student Name", color="Subject ID"),
            x=['Sub 1', 'Sub 2', 'Sub 3', 'Sub 4', 'Sub 5'],
            color_continuous_scale='Turbo', 
            title="Student Academic Subject Mapping",
            aspect="auto"
        )

        fig.update_traces(text=plot_df.values, texttemplate="%{text}")
        fig.show()

except mysql.connector.Error as err:
    print(f"Database Error: {err}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("\nDatabase connection closed.")