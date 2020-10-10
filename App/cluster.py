import numpy as np
import pandas as pd
import warnings
import os
# import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


from itertools import product


from matplotlib.colors import ListedColormap


from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV

from bokeh.io import output_file, show, output_notebook, push_notebook
from bokeh.plotting import figure, reset_output
from bokeh.models import ColumnDataSource, HoverTool, CategoricalColorMapper, CDSView, GroupFilter, FactorRange, Slope
from bokeh.layouts import row,column, gridplot
from bokeh.models.widgets import Tabs, Panel
from bokeh.io import curdoc
from bokeh.core.properties import value

from sklearn.metrics import silhouette_score
curdoc().theme = 'light_minimal'

# output_notebook()
#ignore warnings
warnings.filterwarnings('ignore')

def cluster(file_name, seperated, dim1, dim2,y_name):
    # Open the data
    df = pd.read_csv(file_name,sep=seperated)
    # Define features X
    X = np.asarray(df.iloc[:,:-1]) 
    # Define target y
    Y = np.asarray(df[y_name])
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, stratify=Y)
    x_orig = df.drop(y_name, axis=1).values 
    return plot_cluster(x_orig, dim1, dim2,y_train, df)


def plot_cluster(x, dim_1, dim_2,y_train, df):
    n_clusters=None
    best_silh_score, best_kmeans = -np.inf, None
    best_n_cluster = None
    if n_clusters is None:
        for n_clusters in [2, 3, 4, 5,6,7,8]:
            kmeans = KMeans(n_clusters=n_clusters)
            dim_slice = [dim_1, dim_2]

            kmeans.fit(x[:, dim_slice], y_train)
            y_predict = kmeans.predict(x[:, dim_slice])
            
            sil_score = silhouette_score(x[:, dim_slice], y_predict)
            
            print(f"wine quality score for {n_clusters} clusters is {sil_score}")
            
            if sil_score > best_silh_score:
                best_silh_score = sil_score
                best_kmeans = kmeans
                best_n_cluster = n_clusters
    
    n_clusters = best_n_cluster
    kmeans = best_kmeans
    y_predict = kmeans.predict(x[:, dim_slice])
    
    clusters = kmeans.cluster_centers_
    colors = ["red", "blue", "yellow", "green", "black", "grey"]
    
    cluster_results_df = pd.DataFrame({"x_comp_0": x[:, dim_1], "x_comp_1": x[:, dim_2], "color": [colors[i] for i in y_predict]})
    cluster_results_source = ColumnDataSource(data=cluster_results_df)
    
    cluster_center_df = pd.DataFrame({"x_comp_0": clusters[:, 0], "x_comp_1": clusters[:, 1],
                                  "color": colors[:n_clusters],
                                  "label": [f"Cluster {i}" for i in range(len(clusters))]})
    cluster_source = ColumnDataSource(data=cluster_center_df)
    
    print(f"Plot of {list(df)[dim_1]} vs {list(df)[dim_2]}")
    
    plot = figure()

    plot.circle(x="x_comp_0", y="x_comp_1", source=cluster_results_source, color="color")
    plot.diamond(x="x_comp_0", y="x_comp_1", source=cluster_source, color="color", legend="label", size=20)
    # from bokeh.io import export_png
    show(plot)
    # export_png(plot, filename="static/plot.png")
    return plot
    

    
