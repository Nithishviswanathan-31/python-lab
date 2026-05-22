## Exp 08 — Python libraries

Programs demonstrating essential Python scientific and data libraries.

| File | Description |
|------|-------------|
| 08a_pandas_demo.py | DataFrame creation, reading CSV, filtering rows, groupby operations |
| 08b_numpy_demo.py | Array creation, arithmetic, matrix operations, statistical functions |
| 08c_matplotlib_demo.py | Line chart, bar chart, pie chart, histogram using Matplotlib |
| 08d_scipy_demo.py | Statistical functions, linear algebra, and signal processing basics |

## Concepts used
- **Pandas** : DataFrame, Series, read_csv(), head(), describe(), groupby(), loc[], iloc[]
- **NumPy**  : ndarray, reshape(), zeros(), ones(), dot(), mean(), std(), linspace()
- **Matplotlib**: plt.plot(), plt.bar(), plt.pie(), plt.hist(), plt.show(), labels, titles
- **SciPy**  : scipy.stats (mean, mode, t-test), scipy.linalg (matrix solve)

## Installation
```bash
pip install pandas numpy matplotlib scipy
```

## Sample output

**08b — NumPy**
```
Array  : [1 2 3 4 5]
Mean   : 3.0
Std Dev: 1.41
Matrix multiply result:
[[19 22]
 [43 50]]
```

**08c — Matplotlib**
Generates and displays:
- Line plot of y = x²
- Bar chart of student marks
- Pie chart of subject distribution