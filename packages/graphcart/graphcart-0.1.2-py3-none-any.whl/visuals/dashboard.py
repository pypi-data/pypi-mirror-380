# graphcart/dashboard.py
import streamlit as st
import pandas as pd
from .core import visualize
from .auto_viz import auto_visualize

def launch_dashboard():
    st.set_page_config(page_title="GraphCart Dashboard", layout="wide")
    st.title("📊 GraphCart Dynamic Dashboard")

    # File uploader
    file = st.file_uploader("Upload CSV or Excel", type=["csv", "xlsx"])
    if file:
        df = pd.read_csv(file) if file.name.endswith(".csv") else pd.read_excel(file)
        st.subheader("🔍 Dataset Preview")
        st.write(df.head())

        # Auto visuals
        if st.checkbox("Generate Auto Visuals"):
            plots = auto_visualize(df)
            for p in plots:
                st.pyplot(p)

        # Custom visualization
        st.subheader("🎨 Create Custom Plot")
        plot_type = st.selectbox("Choose plot type", ["scatter", "bar", "heatmap", "box", "violin", "swarm", "scatter3d"])
        x = st.selectbox("X-axis", df.columns, index=0)
        y = st.selectbox("Y-axis", df.columns, index=1 if len(df.columns) > 1 else 0)

        hue = None
        if plot_type in ["scatter", "violin", "swarm", "box"]:
            hue = st.selectbox("Color (optional)", [None] + list(df.columns))

        fig = visualize(df, plot_type, x=x, y=y, hue=hue)
        st.pyplot(fig)
