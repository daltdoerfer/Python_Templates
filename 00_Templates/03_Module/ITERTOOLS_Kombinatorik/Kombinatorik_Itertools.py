import itertools # https://docs.python.org/3/library/itertools.html

all_features = ['milch', 'salz', 'eier', 'äpfel', 'brot', 'wasser']
num_features_total = len(all_features)
print("Länge der Liste: ",num_features_total)

# Beispiel 1
for num in range(1, num_features_total+1): # 1 bis inclusive 6
    for features in itertools.combinations(all_features, num): # Alle Möglichen Kombinationen erstellen. Num-Wert=2 sagt aus wieviele Möglichkeiten mit 2 unterschiedlichen Features möglich sind
        #df_features = pd.DataFrame(df, columns=features)
     print("Num: ", num, "Features: ", features)

# Beispiel 2
# Ermittlung aller Kombinationen
total_feature_combs = 0
for num in range(1, num_features_total): # Iteration von 1 bis 13
    a = [v for v in itertools.combinations(all_features, num)]
    print(a)
    current_feature_combs = len([v for v in itertools.combinations(all_features, num)]) #https://docs.python.org/3/library/itertools.html ->  Kombinationstool
    total_feature_combs += current_feature_combs
    print("Combs with", num, "combs")