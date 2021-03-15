# Dictionarys in Python {key: value}

tagebuch = {'montag': 'Doofer Tag', 'dienstag': 'war schon besser'}
print(tagebuch)

tagebuch = {'montag': ['schule doof', 'alles doof'], 0: 'War schon besser'} # Als Werte sind Listen Tupel oder Strings oder Zahlen möglich
print(tagebuch)

tagebuch = {'montag': ['schule doof', 'alles doof'],
            'dienstag': ['war schon besser', 'ich bin cool']} # Als Werte sind Listen Tupel oder Strings oder Zahlen möglich
print(tagebuch)

# ----------------------------Dictionary im Dictionarys
tagebuch_2 = {'montag': {'morgens': 'doof', 'mittags': 'dööfer', 'abends': 'am dööfsten'},
            'dienstag': {'morgens': '', 'mittags': '', 'abends': ''}
            }

print(   tagebuch_2['montag']['morgens']    ) # Angabe Key1-> montag Key2-> morgens: darin steht doof