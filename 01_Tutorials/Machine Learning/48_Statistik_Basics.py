import numpy as np

samples = np.array([1, 1, 1, 2, 2, 2, 2, 3, 3, 3,
                    4, 4, 4, 4, 4, 5, 5, 6, 6, 6]) # Gewürfelte Aufgen bei 20x Würfeln

print(samples.shape)

mean = np.mean(samples) # Sum(Samples)/Len(samples)
var = np.var(samples) # sum([x-mean])**2 for x in samples]/len(samples)

print(mean)
print(var)

import matplotlib.pyplot as plt
_, counts = np.unique(samples, return_counts=True)

print(counts)
plt.bar(range(1,len(counts)+1), counts, color="blue")
plt.show()