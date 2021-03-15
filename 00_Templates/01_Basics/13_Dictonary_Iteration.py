# Wie Auf: Keys, Values zugreifen {key: value}

tagebuch = {'montag': 'Doofer Tag', 'dienstag': 'war schon besser'}

tagebuch2 = {'montag': ['schule doof', 'alles doof'],
            'dienstag': ['war schon besser', 'ich bin cool']} # Als Werte sind Listen Tupel oder Strings oder Zahlen möglich

# Nur Keys ausgeben
for k in tagebuch.keys(): # Über die Verwendung von keys wird sofort deutlich dass es sich um ein Dictionary handeln muss
    print(k)

# Keys UND Values ausgeben
for k, v in tagebuch2.items():
    print(k, ' -- ', v)

# Keys UND Values Separat ausgeben
for (k, v) in tagebuch2.items():
    print('key: ', k)
    for val in v:
        print(val)

# Nur Value ausgeben
for v in tagebuch2.values():
    print(v)

