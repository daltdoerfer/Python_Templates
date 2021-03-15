# Das richtige Anlegen von Listen (Vektoren und Matrizen)

# ---------------------------------------------------1-D Listen (Vektoren)-----------------------------------------------
vector = [0, 0, 0, 0, 0] # Schlechtes vorgehen
print(vector)

vector = [0 for _ in range(10)] # Gutes Vorgehen, Vorteil -> Größe durch Parameter in () -> Veränderbar
                               # "_" steht für Variable die nicht in der Workspace erstellt wird. Man könnte jedoch auch z.B. i nehmen
print(vector)

vec_gen = (1 for _ in range(10)) # Achtung hier sind runde Klammern "()"
print(vec_gen) # Geht nicht auszugeben
vector = [val for val in vec_gen] # Schreibt Vektor in Liste
print(vector)

# --------------------------------------------------- Matrizen-----------------------------------------------------------

matrix = [[1, 0],[2, 3],[4, 5]]
print(matrix)
matrix = [[0 for j in range(3)] for i in range (3)] # 3x3 Matrix: [[<Spalten>]<Zeilen>] mit allen Werten == 0
print(matrix)

matrix = [[i * j for j in range(3)] for i in range (3)] # 3x3 Matrix: [[<Spalten>]<Zeilen>]: Z1: i=0,j=0,1,2    Z2: i=1 j=0,1,2     Z3: i=2 j=0,1,2
print(matrix)