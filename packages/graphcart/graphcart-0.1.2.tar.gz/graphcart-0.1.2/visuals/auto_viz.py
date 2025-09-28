# graphcart/auto_viz.py
import pandas as pd
from .core import visualize

def auto_visualize(df: pd.DataFrame, max_plots=5):
    """
    Automatically generate suitable visualizations based on column types.
    """
    plots = []
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns

    # Numeric distributions
    for col in numeric_cols[:max_plots]:
        plots.append(visualize(df, "hist", x=col))

    # Categorical counts
    for col in categorical_cols[:max_plots]:
        plots.append(visualize(df, "bar", x=col))

    # Correlation heatmap
    if len(numeric_cols) > 1:
        plots.append(visualize(df, "heatmap"))

    return plots
