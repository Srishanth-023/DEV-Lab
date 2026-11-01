# Question 30: Use Bokeh to produce an interactive visualization with appropriate labels, tooltips, and a legend for a suitable dataset.
# Q30: Bokeh interactive visualization (labels, tooltips, legend)
import numpy as np
import pandas as pd
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure, output_file, show
from bokeh.transform import factor_cmap

# ---- Small iris-type dataset (30 records) ----
iris = pd.DataFrame({
    "sepal_length": [
        5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9,
        7.0, 6.4, 6.9, 5.5, 6.5, 5.7, 6.3, 4.9, 6.6, 5.2,
        6.3, 5.8, 7.1, 6.3, 6.5, 7.6, 4.9, 7.3, 6.7, 7.2,
    ],
    "sepal_width": [
        3.5, 3.0, 3.2, 3.1, 3.6, 3.9, 3.4, 3.4, 2.9, 3.1,
        3.2, 3.2, 3.1, 2.3, 2.8, 2.8, 3.3, 2.4, 2.9, 2.7,
        3.3, 2.7, 3.0, 2.9, 3.0, 3.0, 2.5, 2.9, 2.5, 3.6,
    ],
    "petal_length": [
        1.4, 1.4, 1.3, 1.5, 1.4, 1.7, 1.4, 1.5, 1.4, 1.5,
        4.7, 4.5, 4.9, 4.0, 4.6, 4.5, 4.7, 3.3, 4.6, 3.9,
        6.0, 5.1, 5.9, 5.6, 5.8, 6.6, 4.5, 6.3, 5.8, 6.1,
    ],
    "petal_width": [
        0.2, 0.2, 0.2, 0.2, 0.2, 0.4, 0.3, 0.2, 0.2, 0.1,
        1.4, 1.5, 1.5, 1.3, 1.5, 1.3, 1.6, 1.0, 1.3, 1.4,
        2.5, 1.9, 2.1, 1.8, 2.2, 2.1, 1.7, 1.8, 1.8, 2.5,
    ],
    "species": np.repeat(["setosa", "versicolor", "virginica"], 10),
})

source = ColumnDataSource(iris)
species = sorted(iris["species"].unique())

output_file("q30_bokeh.html")
p = figure(title="Sepal Length vs Petal Length",
           x_axis_label="Sepal length (cm)",
           y_axis_label="Petal length (cm)",
           tools="pan,wheel_zoom,box_zoom,reset")
p.scatter("sepal_length", "petal_length", source=source, size=10,
          color=factor_cmap("species", "Category10_3", species),
          legend_field="species")
p.add_tools(HoverTool(tooltips=[("Species", "@species"),
                                ("Sepal length", "@sepal_length"),
                                ("Petal length", "@petal_length")]))
p.legend.location = "top_left"
p.legend.click_policy = "hide"
show(p)
