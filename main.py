import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="Concrete Data Analysis", layout="wide")

# Add title
st.title("Concrete Data Analysis Dashboard")

# Read the data
@st.cache_data
def load_data():
    df = pd.read_csv('Concrete_Data_Yeh.csv')
    return df

# Load the data
df = load_data()

# Display first 5 rows
st.subheader("First 5 Rows of Dataset")
st.dataframe(df.head())

# Column selection and analysis
st.subheader("Column Analysis")

# Select column for analysis
selected_column = st.selectbox(
    "Select a column to analyze:",
    options=df.columns,
    help="Choose a column to generate boxplot visualization"
)

# Create boxplot using plotly
fig = px.box(
    df,
    y=selected_column,
    title=f"Boxplot of {selected_column}",
    height=500
)

# Update layout
fig.update_layout(
    showlegend=False,
    plot_bgcolor='white',
    boxgap=0.2,
    yaxis_title=selected_column
)

# Display plot
st.plotly_chart(fig, use_container_width=True)

# Show basic statistics
st.subheader(f"Basic Statistics for {selected_column}")
stats = df[selected_column].describe()
st.dataframe(stats)
