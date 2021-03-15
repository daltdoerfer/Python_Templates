# Übersicht über die Datensätz Case Study 1
# Datensatz 1: Cali Housing
# Datensatz 2: MNIST Dataset (64 Pixel Beschrieben eine Zahl)

import numpy as np
np.random.seed(42)
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.datasets import load_digits

# CALI HOUSING REGRESSION (Häuserkosten in Kalifornien)

cal_housing = fetch_california_housing()
x, y = cal_housing.data, cal_housing.target
df = pd.DataFrame(data=x, columns=cal_housing.feature_names)
df["y"] = y

df.head()
"""
MedInc 	HouseAge 	AveRooms 	AveBedrms 	Population 	AveOccup 	Latitude 	Longitude 	y
0 	8.3252 	41.0 	6.984127 	1.023810 	322.0 	2.555556 	37.88 	-122.23 	4.526
1 	8.3014 	21.0 	6.238137 	0.971880 	2401.0 	2.109842 	37.86 	-122.22 	3.585
2 	7.2574 	52.0 	8.288136 	1.073446 	496.0 	2.802260 	37.85 	-122.24 	3.521
3 	5.6431 	52.0 	5.817352 	1.073059 	558.0 	2.547945 	37.85 	-122.25 	3.413
4 	3.8462 	52.0 	6.281853 	1.081081 	565.0 	2.181467 	37.85 	-122.25 	3.422
"""
df.info()
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 20640 entries, 0 to 20639
Data columns (total 9 columns):
#   Column      Non-Null Count  Dtype
---  ------      --------------  -----
0   MedInc      20640 non-null  float64
1   HouseAge    20640 non-null  float64
2   AveRooms    20640 non-null  float64
3   AveBedrms   20640 non-null  float64
4   Population  20640 non-null  float64
5   AveOccup    20640 non-null  float64
6   Latitude    20640 non-null  float64
7   Longitude   20640 non-null  float64
8   y           20640 non-null  float64
dtypes: float64(9)
memory usage: 1.4 MB
"""

df.describe()
"""
MedInc 	HouseAge 	AveRooms 	AveBedrms 	Population 	AveOccup 	Latitude 	Longitude 	y
count 	20640.000000 	20640.000000 	20640.000000 	20640.000000 	20640.000000 	20640.000000 	20640.000000 	20640.000000 	20640.000000
mean 	3.870671 	28.639486 	5.429000 	1.096675 	1425.476744 	3.070655 	35.631861 	-119.569704 	2.068558
std 	1.899822 	12.585558 	2.474173 	0.473911 	1132.462122 	10.386050 	2.135952 	2.003532 	1.153956
min 	0.499900 	1.000000 	0.846154 	0.333333 	3.000000 	0.692308 	32.540000 	-124.350000 	0.149990
25% 	2.563400 	18.000000 	4.440716 	1.006079 	787.000000 	2.429741 	33.930000 	-121.800000 	1.196000
50% 	3.534800 	29.000000 	5.229129 	1.048780 	1166.000000 	2.818116 	34.260000 	-118.490000 	1.797000
75% 	4.743250 	37.000000 	6.052381 	1.099526 	1725.000000 	3.282261 	37.710000 	-118.010000 	2.647250
max 	15.000100 	52.000000 	141.909091 	34.066667 	35682.000000 	1243.333333 	41.950000 	-114.310000 	5.000010
"""

df.plot(kind="scatter", x="Longitude", y="Latitude", alpha=0.4,

        figsize=(10,7), c="y", cmap=plt.get_cmap("jet"), colorbar=True)

plt.show()

# MNIST CLASSIFICATION

mnist = load_digits()
x, y = mnist.data, mnist.target
df = pd.DataFrame(data=x)
df["y"] = y

df.head()
"""
0 	1 	2 	3 	4 	5 	6 	7 	8 	9 	... 	55 	56 	57 	58 	59 	60 	61 	62 	63 	y
0 	0.0 	0.0 	5.0 	13.0 	9.0 	1.0 	0.0 	0.0 	0.0 	0.0 	... 	0.0 	0.0 	0.0 	6.0 	13.0 	10.0 	0.0 	0.0 	0.0 	0
1 	0.0 	0.0 	0.0 	12.0 	13.0 	5.0 	0.0 	0.0 	0.0 	0.0 	... 	0.0 	0.0 	0.0 	0.0 	11.0 	16.0 	10.0 	0.0 	0.0 	1
2 	0.0 	0.0 	0.0 	4.0 	15.0 	12.0 	0.0 	0.0 	0.0 	0.0 	... 	0.0 	0.0 	0.0 	0.0 	3.0 	11.0 	16.0 	9.0 	0.0 	2
3 	0.0 	0.0 	7.0 	15.0 	13.0 	1.0 	0.0 	0.0 	0.0 	8.0 	... 	0.0 	0.0 	0.0 	7.0 	13.0 	13.0 	9.0 	0.0 	0.0 	3
4 	0.0 	0.0 	0.0 	1.0 	11.0 	0.0 	0.0 	0.0 	0.0 	0.0 	... 	0.0 	0.0 	0.0 	0.0 	2.0 	16.0 	4.0 	0.0 	0.0 	4

5 rows × 65 columns
"""
df.info()
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1797 entries, 0 to 1796
Data columns (total 65 columns):
#   Column  Non-Null Count  Dtype
---  ------  --------------  -----
0   0       1797 non-null   float64
1   1       1797 non-null   float64
2   2       1797 non-null   float64
3   3       1797 non-null   float64
4   4       1797 non-null   float64
5   5       1797 non-null   float64
6   6       1797 non-null   float64
7   7       1797 non-null   float64
8   8       1797 non-null   float64
9   9       1797 non-null   float64
10  10      1797 non-null   float64
11  11      1797 non-null   float64
12  12      1797 non-null   float64
13  13      1797 non-null   float64
14  14      1797 non-null   float64
15  15      1797 non-null   float64
16  16      1797 non-null   float64
17  17      1797 non-null   float64
18  18      1797 non-null   float64
19  19      1797 non-null   float64
20  20      1797 non-null   float64
21  21      1797 non-null   float64
22  22      1797 non-null   float64
23  23      1797 non-null   float64
24  24      1797 non-null   float64
25  25      1797 non-null   float64
26  26      1797 non-null   float64
27  27      1797 non-null   float64
28  28      1797 non-null   float64
29  29      1797 non-null   float64
30  30      1797 non-null   float64
31  31      1797 non-null   float64
32  32      1797 non-null   float64
33  33      1797 non-null   float64
34  34      1797 non-null   float64
35  35      1797 non-null   float64
36  36      1797 non-null   float64
37  37      1797 non-null   float64
38  38      1797 non-null   float64
39  39      1797 non-null   float64
40  40      1797 non-null   float64
41  41      1797 non-null   float64
42  42      1797 non-null   float64
43  43      1797 non-null   float64
44  44      1797 non-null   float64
45  45      1797 non-null   float64
46  46      1797 non-null   float64
47  47      1797 non-null   float64
48  48      1797 non-null   float64
49  49      1797 non-null   float64
50  50      1797 non-null   float64
51  51      1797 non-null   float64
52  52      1797 non-null   float64
53  53      1797 non-null   float64
54  54      1797 non-null   float64
55  55      1797 non-null   float64
56  56      1797 non-null   float64
57  57      1797 non-null   float64
58  58      1797 non-null   float64
59  59      1797 non-null   float64
60  60      1797 non-null   float64
61  61      1797 non-null   float64
62  62      1797 non-null   float64
63  63      1797 non-null   float64
64  y       1797 non-null   int32
dtypes: float64(64), int32(1)
memory usage: 905.6 KB
"""

df.describe()
"""
0 	1 	2 	3 	4 	5 	6 	7 	8 	9 	... 	55 	56 	57 	58 	59 	60 	61 	62 	63 	y
count 	1797.0 	1797.000000 	1797.000000 	1797.000000 	1797.000000 	1797.000000 	1797.000000 	1797.000000 	1797.000000 	1797.000000 	... 	1797.000000 	1797.000000 	1797.000000 	1797.000000 	1797.000000 	1797.000000 	1797.000000 	1797.000000 	1797.000000 	1797.000000
mean 	0.0 	0.303840 	5.204786 	11.835838 	11.848080 	5.781859 	1.362270 	0.129661 	0.005565 	1.993879 	... 	0.206455 	0.000556 	0.279354 	5.557596 	12.089037 	11.809126 	6.764051 	2.067891 	0.364496 	4.490818
std 	0.0 	0.907192 	4.754826 	4.248842 	4.287388 	5.666418 	3.325775 	1.037383 	0.094222 	3.196160 	... 	0.984401 	0.023590 	0.934302 	5.103019 	4.374694 	4.933947 	5.900623 	4.090548 	1.860122 	2.865304
min 	0.0 	0.000000 	0.000000 	0.000000 	0.000000 	0.000000 	0.000000 	0.000000 	0.000000 	0.000000 	... 	0.000000 	0.000000 	0.000000 	0.000000 	0.000000 	0.000000 	0.000000 	0.000000 	0.000000 	0.000000
25% 	0.0 	0.000000 	1.000000 	10.000000 	10.000000 	0.000000 	0.000000 	0.000000 	0.000000 	0.000000 	... 	0.000000 	0.000000 	0.000000 	1.000000 	11.000000 	10.000000 	0.000000 	0.000000 	0.000000 	2.000000
50% 	0.0 	0.000000 	4.000000 	13.000000 	13.000000 	4.000000 	0.000000 	0.000000 	0.000000 	0.000000 	... 	0.000000 	0.000000 	0.000000 	4.000000 	13.000000 	14.000000 	6.000000 	0.000000 	0.000000 	4.000000
75% 	0.0 	0.000000 	9.000000 	15.000000 	15.000000 	11.000000 	0.000000 	0.000000 	0.000000 	3.000000 	... 	0.000000 	0.000000 	0.000000 	10.000000 	16.000000 	16.000000 	12.000000 	2.000000 	0.000000 	7.000000
max 	0.0 	8.000000 	16.000000 	16.000000 	16.000000 	16.000000 	16.000000 	15.000000 	2.000000 	16.000000 	... 	13.000000 	1.000000 	9.000000 	16.000000 	16.000000 	16.000000 	16.000000 	16.000000 	16.000000 	9.000000

8 rows × 65 columns
"""