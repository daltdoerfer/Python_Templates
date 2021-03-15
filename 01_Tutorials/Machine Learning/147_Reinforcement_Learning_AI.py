# Notwendige Packages: GYM, PYGAME
# https://gym.openai.com/docs/
# Sollte Warnung bei der Installation von gym auftreten folgenden Befehl
# ausführen: pip install gym --use-feature=2020-resolver

# Begriffe: AI
# Episode: Eine Episode ist ein Kompletter Spieldurchlauf.
#          Vom Start bis zum Sieg/Niederlage
# The observation_space: defines the structure of the observations your
#                        environment will be returning. Learning agents
#                        usually need to know this before they start running,
#                        in order to set up the policy function. Some
#                        general-purpose learning agents can handle a wide range
#                        of observation types: Discrete, Box, or pixels
#                        (which is usually a Box(0, 255, [height, width, 3]) for RGB pixels).
#

# Sonstige Begriffe:
# Percentile -> https://numpy.org/doc/stable/reference/generated/numpy.percentile.html
#

import gym
import numpy as np

from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical

class Agent:
    def __init__(self, env):  # Übergabe der Environment an den Agenten
        self.env = env  # Konstruktor
                        # Speichern wieviele Features unser Netzwerk haben wird.
                        # Basier drauf, wie viele Eigenschaften ein State (also eine Observation) haben kann
                        # Beispiel: Fifa bei 30 Fps
                        #           Ort des Spielers S_X, S_Y, S_Z
                        #           Ort des Balles   B_X, B_Y, B_Z
                        #           Vermutlich dann 6 Features pro Frame

        self.num_actions = self.env.action_space.n  # Anzahl der berechneten Aktionen ermitteln
        self.num_observations = self.env.observation_space.shape[0]  # Aus Environment die Anzahl der Features ermitteln -> natürlich nur bei Gym internen Games
        self.model = self.build_model()  # Modell abspeichern

    # Build-Step 1
    def build_model(self):  # Implementierung des Neuronalen Netzwerkes (als Klassifikationsproblem)

        model = Sequential()
        model.add(Dense(units=100, input_dim=self.num_observations))  # Input Layer(Anzahl input_dim Neuronen) to first Hidden Layer (Anzahl "units" Neuronen). WICHTIG: Erster Hidden Layer braucht immer Verbindung zu Input Layer -> input_dim.
        #print(f"Observations: {self.num_observations}")
        model.add(Activation("relu"))
        model.add(Dense(units=self.num_actions))  # Output Layer mit so vielen Neuronen wie Actions vorhanden sind
        model.add(Activation("softmax"))   # Softmax-Layer wird verwendet wenn Klassifikationsproblem vorliegt mit mehr als 2 Klassen (Ausgabe von Wahrscheinlichkeitswerten für jede mögliche Klasse -> Die höchste gewinnt)
        model.summary() # Input Layer: 100 Neuronen mit 4 Observation-Inputs -> Gewichtsmatrix: 100*4 = 400 ; Außerdem 100 bias Neuronen extra -> 400+100 = 500

        model.compile(loss="categorical_crossentropy", # Optimizer (sgd stochastic Gradient Descent) arbeitet mit loss-Funktion.
                      optimizer="Adam",
                      metrics=["accuracy"])
        return model

    # Build-Step 3
    def get_action(self, state):  # Basierend auf unserem Netzwerk schauen, was die Wahrscheinlichkeit für jede Aktion ist
        state = state.reshape(1, -1)  # Wir haben aktuell Dim [2,] brauchen aber Dim [1,2]
        action_prob = self.model(state).numpy()[0]  # Berechnung der Prediction auf Basis des States
                                                    # -> Ausgangssignal des NN -> Tensorflow Tensor macht Umrechnung in numpy Array notwendig
                                                    # -> Numpy Array z.B.[0.7, 0.3 ] -> 70% Wahrscheinlichkeit Aktion 1 auszuführen z.B.: links gehen
        action = np.random.choice(self.num_actions, p=action_prob)
        return action

    # Build-Step 2
    def get_samples(self, num_episodes):  # Eine Episode ist ein Kompletter Spieldurchlauf: Vom Start bis zum Sieg/Niederlage
        rewards = [0.0 for _ in range(num_episodes)]  # Listcomprehension Listemit nullwerten. Inhalt: Speichert den Totalen Reward zur jeweiligen Aktion/State
        episodes = [[] for _ in range(num_episodes)]  # Listcomprehension -> leere Liste      Inhalt: Speichert die Aktion und den aktuellen State als Erweiterung in Liste

        for episode in range(num_episodes):  # Eine Episode ist ein Kompletter Spieldurchlauf:
                                             # Vom Start bis zum Sieg/Niederlage
            state = self.env.reset()  # Reset des Spiels auf Anfangszustand
            total_reward = 0.0  # Reward pro Episode initialisieren

            while True:  # Schleife Solange aktiv bis break-Befehl kommt
                action = self.get_action(state)
                new_state, reward, done, _ = self.env.step(action)
                                                                   #Beinhaltet Aktionsausführung:
                                                                   # daraus resultiert neuer State (z.b. im nächsten Frame))
                                                                   # daraus resultiert reward oder kein Reward
                total_reward += reward
                episodes[episode].append((state, action))  # Speichert die Aktion und den aktuellen State als Erweiterung in Liste
                state = new_state

                if done:
                    rewards[episode] = total_reward # Schreibt den aktuellen reward in Liste
                    break
        return rewards, episodes

    # Build-Step 6
    def filter_episodes(self, rewards, episodes, percentile):
        reward_bound = np.percentile(rewards, percentile) # das q-te percentile. z.B. die oberen 30% möchten wir haben -> die unteren 70 Prozent werden rausgefiltert
                                                          # -> Ergebnis wäre der reward den wir bräuchten um die besten 30% zu erreichen
        x_train, y_train = [], []  # erzeugt leere listen
        for reward, episode in zip(rewards, episodes):
            if reward >= reward_bound:  # Trainingsset zusammenstellen wenn Belohnung größer/gleich unsere Zielbound ist
                observations = [step[0] for step in episode]  # step[0] -> was in Tupel an Stelle 0 steht (hier wäre das der State)
                actions = [step[1] for step in episode]  # step[1] -> was in Tupel an Stelle 1 steht (hier wäre das der State)

                x_train.extend(observations)
                y_train.extend(actions)

        x_train = np.array(x_train)
        y_train = to_categorical(y_train, num_classes=self.num_actions)
        return x_train, y_train, reward_bound

    # Build-Step 4
    def train(self, percentile, num_iterations, num_episodes): # Training ausführen
        for _ in range(num_iterations):
            rewards, episodes = self.get_samples(num_episodes) # Generierung von Spielzügen
            x_train, y_train, reward_bound = self.filter_episodes(rewards, episodes, percentile) # Filter_episodes filtert beste Episoden heraus, die wir in der get_samples gespielt haben.
                                                                                                 # z.B: 20 Spieldurchläufe, davon waren 8 gut und 12 Schlecht

            self.model.fit(x=x_train, y=y_train, verbose=0)                                      #-> die 8 Besten Tupel (Action+State) werden dann gespeichert um des Netzwerk zu trainieren
            reward_mean = np.mean(rewards) # Liste aus rewards
            print(f"Reward mean: {reward_mean}, Reward bound: {reward_bound}") # In jeder Iteration ausgeben wie gut wir gerade sind
            if reward_mean > 450: # Spiel wird gewonnen wenn wir 450 Punkte erreicht haben
                break

    # Build-Step 5
    def play(self, num_episodes, render=True):
        for episode in range(num_episodes):  # Eine Episode ist ein Kompletter Spieldurchlauf: Vom Start bis zum Sieg/Niederlage

            state = self.env.reset()  # Reset des Spiels auf Anfangszustand
            total_reward = 0.0  # Reward pro Episode initialisieren

            while True:  # Schleife Solange aktiv bis break-Befehl kommt
                if render:
                    self.env.render() # Spiel grafisch darstellen wenn render = TRUE

                action = self.get_action(state)
                state, reward, done, _ = self.env.step(action)
                # Beinhaltet Aktionsausführung:
                # daraus resultiert neuer State (z.b. im nächsten Frame))
                # daraus resultiert reward oder kein Reward
                total_reward += reward

                if done:
                    print(f"Total reward: {total_reward} in episode: {episode + 1}")
                    break

#################################################################
# Main Funktion in Python (wie in void in C oder Java)
#################################################################
if __name__ == "__main__":

    env = gym.make("CartPole-v1")  # Man erstellt eine Instanz von dem  jeweiligen Spiel
    agent = Agent(env)  # Objekt vom Angenten mit der entsprechenden Environment erstellen

    # Agent Trainieren
    agent.train(
                percentile=70.0,  # Bei jeder Iteration wollen wir nach 70% Percentile filtern
                num_iterations=15,  # in Jeder Iteration spielen wir 100x das Spiel durch
                num_episodes=100
                )

    print("Training abgeschlossen. Bitte irgendeinen Wert in Konsole eingeben")
    input() # Nach dem Training Bestätigen, das Spiel losgeht
    agent.play(num_episodes=10)  # Spielen Lassen
