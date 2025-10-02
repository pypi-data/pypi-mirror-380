# tufteplotlib  
Minimalist plotting for Python, inspired by Edward Tufte’s principles of data visualization.

`tufteplotlib` is a Python library built on top of [matplotlib](https://matplotlib.org/) for generating minimalist, high–data-density graphs in the style proposed by Edward Tufte in [*The Visual Display of Quantitative Information*](https://www.edwardtufte.com/book/the-visual-display-of-quantitative-information/).

<p align="center">
  <img src="doc/visual_display_of_quantitative_information.jpg" width="250" loading="lazy"/>
</p>

Tufte promotes:

- Maximising the data–ink ratio: remove non-essential lines, marks, and colours.  
- Content-driven spines and axes: spines span only the data domain and range, for rapid inspection.  
- Minimal scaffolding: grid lines, ticks, and labels are light, precise, and unobtrusive.
- Direct labeling: wherever possible, place labels on the data rather than in legends.  

#### 🧭 Navigation:
- [Examples](#-examples)
- [Installation](#-installation)
- [Contributing](#-contributing)
- [License](#-license)
- [Plots:](#-plots)

  | Comparison            | Composition       | Distribution                    | Relationship            |
  |-----------------------|-------------------|---------------------------------|-------------------------|
  | [Bar](#bar)           | [Pareto](#pareto) | [Density](#density)             | [Line](#line)           |
  | [Barcode](#barcode)   |                   | [Galaxy](#galaxy)               | [Rug](#rug)             |
  | [Quartile](#quartile) |                   | [Histogram](#histogram)         | [Scatter](#scatter)     |
  |                       |                   | [Stem and Leaf](#stem-and-leaf) | [Sparkline](#sparkline) |
  |                       |                   |                                 | [Time Series](#time)    |

## 🔎 Examples

Here is a small gallery of common plots using `tufteplotlib` on the left, versus default rendering in `matplotlib` on the right:

<p align="center">
  <img src="doc/bar_chart_comparison.png" width="400" loading="lazy"/>
  <br>
  <img src="doc/barcode_plot_comparison.png" width="300" loading="lazy"/>
  <img src="doc/density_plot_comparison.png" width="300" loading="lazy"/>
  <br>
  <img src="doc/histogram_comparison.png" width="300" loading="lazy"/>
  <img src="doc/quartile_plot_comparison.png" width="300" loading="lazy"/>
  <br>
  <img src="doc/line_plot_comparison.png" width="600" loading="lazy"/>
  <br>
  <img src="doc/time_series_comparison.png" width="600" loading="lazy"/>
</p>

[🔝 Back to Top.](#tufteplotlib)

---

## 💾 Installation

`tufteplotlib` is currently available only from GitHub. You can install it directly using:

```
pip install git+https://github.com/Woolfrey/software_tufte_plot.git
```

Or clone the repo and install locally:

```
git clone https://github.com/Woolfrey/software_tufte_plot.git
cd software_tufte_plot
pip install -e .
```

To confirm the library is installed correctly, run the following:

```
pip show tufteplotlib
```

and you should see something like:

```
Name: tufteplotlib
Version: 1.0.0
Summary: An extension to matplotlib for creating graphs in the style of Edward Tufte.
Home-page: https://github.com/Woolfrey/software_tufte_plot
Author: Jon Woolfrey
Author-email: jonathan.woolfrey@gmail.com
License: GPLv3
Location: /home/woolfrey/.local/lib/python3.10/site-packages
Requires: matplotlib, numpy, pandas
Required-by: 
```

You can even run commands such as `tufte-scatter`, `tufte-time` etc to execute example code.

[🔝 Back to Top.](#tufteplotlib)

## 🤝 Contributing

> [!NOTE]
> I am not a software engineer, so contributions to improving `tufteplotlib` are welcome!

- **Report issues:** If you find a bug, unexpected behavior, or have a feature request, open an [issue](../../issues).  
- **Fork & pull request:** Fork the repository, make your changes, and submit a pull request.  
- **Code style:** Please follow the minimalist Tufte style — keep your changes clean and avoid unnecessary visual clutter.  
- **Documentation:** Examples, explanations, and README improvements are highly appreciated.  
- **Testing:** Ensure that your code changes do not break existing functionality. Add small example plots if relevant.

[🔝 Back to Top.](#tufteplotlib)


## 📜 License

`tufteplotlib` is released under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).  
You are free to use, modify, and distribute this software under the terms of the GPLv3.  
See the included [LICENSE](LICENSE) file for full details.

[🔝 Back to Top.](#tufteplotlib)

## 📊 Plots

### Bar

_Compare quantities across nominal categories._

To see a full example, run `tufte-bar` in the terminal.

<p align="center">
  <img src="doc/bar_chart.png" width="300" loading="lazy"/>
</p>

Minimal example:

```python
import numpy as np
from tufteplotlib import bar_chart

categories = ["Satiety", "Triumvirate", "Gourmand", "Machiavellian", "Boudoir"]
values = np.random.randint(3, 20, size=len(categories))

fig, ax = bar_chart(categories, values)
plt.tight_layout()
plt.show()
```

[🔝 Back to Top.](#tufteplotlib)

### Barcode

_Show the distribution of observations across nominal categories._

Run `tufte-barcode` in the terminal to see an example.

<p align="center">
  <img src="doc/barcode_plot.png" width="300" height="auto" loading="lazy"/>
</p>

> [!TIP]
> If the data are dense, consider using the [quartile](#quartile) plot instead.

Minimal implementation:

```python
fom tufteplotlib import barcode_plot

params = {"Lowenstein": {"mu": 5, "sigma": 3, "n": 50},
          "Zweig": {"mu": 7, "sigma": 1, "n": 50},
          "Sneed": {"mu": 6, "sigma": 2, "n": 50}}

categories = []
values = []

for cat, p in params.items():
    data = np.random.normal(loc=p["mu"], scale=p["sigma"], size=p["n"])
    categories.extend([cat]*p["n"])
    values.extend(data)

fig, ax = barcode_plot(categories, values)

plt.tight_layout()

plt.show()
```

[🔝 Back to Top.](#tufteplotlib)

### Density

_Show the distribution of observations across a 1-dimensional data set._

Run `tufte-density` in the terminal to see an example.

<p align="center">
  <img src="doc/density_plot.png" width="300" height="auto" loading="lazy"/>
</p>

> [!TIP]
> If the data are sparse, consider using a [histogram](#histogram) instead.

Minimal implementation:

```python
import numpy as np
from tufteplotlib import density_plot

data = np.random.normal(loc=0, scale=1, size=500)
fig, ax = density_plot(data)

plt.tight_layout()
plt.show()
```

[🔝 Back to Top.](#tufteplotlib)

### Galaxy

_Illustrate the density of data distributed across 2-dimensional coordinates._

Run `tufte-galaxy` in the terminal to see an example.

<p align="center">
  <img src="doc/galaxy_plot.png" width="300" height="auto" loading="lazy"/>
</p>

Minimal implementation:

```python
import numpy as np
from tufteplotlib import galax_plot

n_points = 10000

x = np.random.uniform(low=-1.0, high=1.0, size=n_points)
y = np.random.uniform(low=-1.0, high=1.0, size=n_points)
z = np.random.uniform(low= 0.0, high=1.0, size=n_points)

# Create plot
ax, im = galaxy_plot(x, y, z)
                       
# Create the colorbar (minimal)
cbar = add_min_max_colorbar(im, ax=ax)

plt.tight_layout()
plt.show()
```

[🔝 Back to Top.](#tufteplotlib)

### Histogram

_Show the distribution of a 1-dimensional data set._

From the terminal use `tufte-histogram` to see an example.

<p align="center">
  <img src="doc/histogram.png" width="300" height="auto" loading="lazy"/>
</p>

> [!TIP]
> If the data are dense, consider using the [density plot](#density) instead.

Minimal implementation:

```python
import numpy as np
from tufteplotlib import histogram_plot

data = np.random.normal(loc=0.0, scale=1.0, size=100)

fig, ax = histogram_plot(data)

plt.tight_layout()
plt.show()
```

[🔝 Back to Top.](#tufteplotlib)

### Line

_Draw a line using a 2-dimensional data set._

Use `tufte-line` in the terminal to see an example.

<p align="center">
  <img src="doc/line_plot.png" width="400" height="auto" loading="lazy"/>
</p>

Minimal implementation:

```
import numpy as np
from tufteplotlib import line_plot

t = np.linspace(0, 10, 200)
y = np.sin(t)
y_noisy = y + np.random.normal(0, 0.1, size=t.shape)

fig, ax = line_plot(t, y_noisy)

plt.tight_layout()
plt.show()
```

[🔝 Back to Top.](#tufteplotlib)

### Pareto

_Show the individual contribution of nominal categories to a total quantity._

Use `tufte-pareto` in the terminal to see an example.

<p align="center">
  <img src="doc/pareto_chart.png" width="300" height="auto" loading="lazy"/>
</p>

> [!TIP]
> The pareto rule is a heuristic that states 20% of causes produce 80% of outcomes. This chart be used to illustrate and discern the 20% of causes.

> [!NOTE]
> The pareto chart is a personal favourite. Tufte never mentioned them in his books. He did, however, criticise the use of _pie charts_ since the mapping between the angle of a slice and its quantity is nonlinear, and hence difficult to discern its true proportions. The pareto chart, in contrast:
> 1. Preserves proportions between categories, and
> 2. Features a cumulative % line plot showing its contribution to the total.

Minimal implementation:

```python
import numpy as np
from tufteplotlib import pareto_chart

categories = ["A", "B", "C", "D", "E"]

np.random.seed()

values = np.random.rand(len(categories)) * 20

fig, ax = pareto_chart(categories, values)

ax[1].set_ylim(-10, 110) # Move the cumulative line plot upward

plt.tight_layout()
plt.show()
```

[🔝 Back to Top.](#tufteplotlib)

### Quartile

_Show the distribution of observations across nominal categories._

Use `tufte-quartile` in the terminal to see an example.

<p align="center">
  <img src="doc/quartile_plot.png" width="300" height="auto" loading="lazy"/>
</p>

> [!TIP]
> If the data are sparse, consider using the [barcode plot](#barcode) instead.

Minimal implementation:

```python
import numpy as np
from tufteplotlib import quartile_plot

params = {"A": {"mu": 5, "sigma": 3, "n": 100},
          "B": {"mu": 6, "sigma": 2, "n": 100},
          "C": {"mu": 7, "sigma": 1, "n": 100}}

categories = []
values = []

for cat, p in params.items():
    data = np.random.normal(loc=p["mu"], scale=p["sigma"], size=p["n"])
    categories.extend([cat]*p["n"])
    values.extend(data)

fig, ax = quartile_plot(categories, values)

plt.tight_layout()
plt.show()
```

[🔝 Back to Top.](#tufteplotlib)

### Rug

_Plot individual observations in a 2-dimensional dataset, with ticks on the axes to show marginal distributions._

Run `tufte-rug` in the terminal to see an example.

<p align="center">
  <img src="doc/rug_plot.png" width="300" height="auto" loading="lazy"/>
</p>

Minimal implementation:

```python
import numpy as np
from tufteplotlib import rug_plot

x = np.random.normal(loc=0, scale=1, size=200)
y = np.random.normal(loc=0, scale=1, size=200)

fig, ax = rug_plot(x, y)

plt.tight_layout()
plt.show()
```

[🔝 Back to Top.](#tufteplotlib)

### Scatter

_Plot individual observations from a 2-dimensional data set._

Use `tufte-scatter` in the terminal to see an example.

<p align="center">
  <img src="doc/scatter_plot.png" width="300" height="auto" loading="lazy">
</p>

Minimal implementation:

```python
import random
from tufteplotlib.datasets import anscombe
from tufteplotlib import scatter_plot

data = anscombe[random.choice(list(anscombe.keys()))]

x, y = data[:, 0], data[:, 1]

fig, ax = scatter_plot(x, y)

plt.tight_layout()
plt.show()
```

[🔝 Back to Top.](#tufteplotlib)

### Sparkline

_Illustrate the change in a quantity across time._

Use `tufte-sparkline` to see an example.

<p align="center">
  <img src="doc/sparkline.png" width="400" height="auto" loading="lazy"/>
</p>

Minimal implementation:

```python
import numpy as np
from tufteplotlib import sparkline

y = np.random.normal(0, 1, 30).cumsum()

fig, ax = sparkline(y)

plt.tight_layout()
plt.show()
```

[🔝 Back to Top.](#tufteplotlib)

### Stem and Leaf

_Plot an horizontal histogram for a 1-dimensional data set where the 1st significant digit(s) are used as the categories._

Use `tufte-stem` in the terminal to see an example.

|  Stem | Leaves |
|------:|:-------|
|     5 | .03 .10 .13 .89 |
|     6 | .39 .45 .63 .95 |
|     7 | .48 .84 |
|     8 | .11 .14 .19 .59 .69 .72 .99 |
|     9 | .04 .08 .28 .38 .49 .90 |
|    10 | .13 .17 .20 .55 .73 .95 |
|    11 | .32 .78 |
|    12 | .35 .36 .58 .70 .96 .99 |
|    13 | .02 .22 .25 .58 .60 .60 .66 .79 .86 |
|    14 | .43 .78 .85 .96 |

> [!TIP]
> You can output the plot with different formatting for `Markdown`, `LaTeX`, or `CSV` ready to use!

Minimal implementation:

```python
import numpy as np
from tufteplotlib import stem_and_leaf_plot

data = np.random.randint(5, 15, size=20) + np.random.rand(20)

print(stem_and_leaf_plot(data, output="plain")) # or "Markdown", "LaTeX", "CSV"
```

### Time

_Plot values over time to visualise change and trends._

In the terminal enter `tufte-time` to see an example.

<p align="center">
  <img src="doc/time_series.png" width="400" height="auto" loading="lazy"/>
</p>

> [!TIP]
> If the data are dense, consider using the [line plot](#line) instead.

Minimal implementation:

```python
import numpy as np
from tufteplotlib import time_series

t = np.linspace(0, 10, 10)
y = 5.0 * np.sin(t) + 1.0 * np.random.randn(10)

fig, ax = time_series(t, y)

plt.tight_layout()
plt.show()
```

[🔝 Back to Top.](#tufteplotlib)
