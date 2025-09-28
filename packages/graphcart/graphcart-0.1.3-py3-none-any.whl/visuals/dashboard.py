import streamlit as st
import pandas as pd
from .auto_viz import auto_visualize
from .core import visualize

def run_dashboard():
    """
    Launch the GraphCart Streamlit dashboard.
    Users can upload a CSV and generate auto or custom plots.
    """
    st.title("GraphCart Interactive Dashboard")

    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("Preview of dataset:", df.head())

        
        if st.checkbox("Generate Auto Visuals"):
            st.subheader("Auto Plots")
            plots = auto_visualize(df)
            for fig in plots:
                st.plotly_chart(fig, use_container_width=True)

        
        st.subheader("Custom Plot")
        plot_type = st.selectbox("Select Plot Type", 
                                 ["scatter", "bar", "hist", "box", "violin", "swarm", "scatter3d", "heatmap"])

        numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
        categorical_cols = df.select_dtypes(include=['object', 'category', 'bool']).columns.tolist()

        x_col, y_col, z_col, hue_col = None, None, None, None

        if plot_type in ["scatter", "violin", "swarm", "box"]:
            x_col = st.selectbox("X-axis", df.columns)
            y_col = st.selectbox("Y-axis", df.columns)
            hue_col = st.selectbox("Hue (optional)", [None] + list(df.columns))
        elif plot_type == "hist":
            x_col = st.selectbox("Column", numeric_cols)
        elif plot_type == "scatter3d":
            x_col = st.selectbox("X-axis", numeric_cols)
            y_col = st.selectbox("Y-axis", numeric_cols)
            z_col = st.selectbox("Z-axis", numeric_cols)
        elif plot_type == "bar":
            x_col = st.selectbox("X-axis", df.columns)
            y_col = st.selectbox("Y-axis", numeric_cols)

        if st.button("Generate Plot"):
            if plot_type == "hist":
                fig = visualize(df, plot_type=plot_type, column=x_col)
            elif plot_type in ["scatter", "violin", "swarm", "box"]:
                fig = visualize(df, plot_type=plot_type, x=x_col, y=y_col, hue=hue_col)
            elif plot_type == "scatter3d":
                fig = visualize(df, plot_type=plot_type, x=x_col, y=y_col, z=z_col)
            elif plot_type == "bar":
                fig = visualize(df, plot_type=plot_type, x=x_col, y=y_col)
            elif plot_type == "heatmap":
                fig = visualize(df, plot_type=plot_type)
            st.plotly_chart(fig, use_container_width=True)
