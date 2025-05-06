from flask import Flask, render_template
import pandas as pd
import os
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

def read_sample_data():
    """Read the sample data exported from Hadoop"""
    data_path = '/hadoop-data/sample_data.csv'
    if os.path.exists(data_path):
        # Assuming the data is exported as CSV with comma separator
        try:
            df = pd.read_csv(data_path, header=None, 
                             names=['emp_no', 'birth_date', 'first_name', 'last_name', 'gender', 'hire_date'])
            return df
        except Exception as e:
            return f"Error reading data: {str(e)}"
    else:
        return "Sample data file not found. Data may not have been converted yet."

def generate_charts(df):
    """Generate charts from the data"""
    charts = []
    
    # Only generate charts if we have valid data
    if isinstance(df, pd.DataFrame) and not df.empty:
        # Gender distribution chart
        plt.figure(figsize=(8, 6))
        gender_counts = df['gender'].value_counts()
        gender_counts.plot(kind='pie', autopct='%1.1f%%')
        plt.title('Employee Gender Distribution')
        plt.tight_layout()
        
        # Save to a BytesIO object
        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        gender_chart = base64.b64encode(buf.read()).decode('utf-8')
        charts.append(('Gender Distribution', gender_chart))
        plt.close()
        
        # Hire date histogram
        plt.figure(figsize=(10, 6))
        df['hire_date'] = pd.to_datetime(df['hire_date'])
        df['hire_year'] = df['hire_date'].dt.year
        hire_year_counts = df['hire_year'].value_counts().sort_index()
        
        if not hire_year_counts.empty:  # Check if hire_year_counts is not empty
            hire_year_counts.plot(kind='bar')
            plt.title('Employee Hire Years')
            plt.xlabel('Year')
            plt.ylabel('Number of Employees')
            plt.tight_layout()
            
            # Save to a BytesIO object
            buf = BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            hire_chart = base64.b64encode(buf.read()).decode('utf-8')
            charts.append(('Employee Hire Years', hire_chart))
        plt.close()
    
    return charts

@app.route('/')
def index():
    # Read sample data
    data = read_sample_data()
    
    # Process data for display
    if isinstance(data, pd.DataFrame):
        # Generate charts
        charts = generate_charts(data)
        
        # Convert DataFrame to HTML table
        data_html = data.to_html(classes='table table-striped', index=False)
        
        # Render template with data
        return render_template('index.html', 
                              data_html=data_html,
                              data_available=True,
                              charts=charts,
                              conversion_successful=True)
    else:
        # Render template with error message
        return render_template('index.html',
                              error_message=data,
                              data_available=False,
                              conversion_successful=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
