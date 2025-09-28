from .core import visualize
import pandas as pd

def auto_visualize(df: pd.DataFrame):
    """
    Automatically generate plots for a DataFrame.
    Returns a list of plotly figures.
    """
    plots = []
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object', 'category', 'bool']).columns.tolist()
    
    
    for col in numeric_cols:
        fig = visualize(df, plot_type="hist", column=col)
        plots.append(fig)
    
    
    for i in range(len(numeric_cols)):
        for j in range(i+1, len(numeric_cols)):
            fig = visualize(df, plot_type="scatter",
                            x=numeric_cols[i],
                            y=numeric_cols[j])
            plots.append(fig)
    
    
    for col in categorical_cols:
        fig = visualize(df, plot_type="bar", x=col)
        plots.append(fig)
    
    
    if len(numeric_cols) >= 2:
        fig = visualize(df, plot_type="heatmap")
        plots.append(fig)
    
    return plots
