import numpy as np

y_true = np.array([0,1,0,1])
y_pred = np.array([1,1,1,1])

print(f"Einträge y_True {y_true.shape[0]}")

logic = y_true == y_pred
print(logic)

i=0
for entry in y_true:
    i=i+1
    print(i)

logic2 = [1 for y_t, y_p in zip(y_true, y_pred) if y_t ==  y_p]
print(logic2)

accuracy = np.sum(y_true == y_pred)