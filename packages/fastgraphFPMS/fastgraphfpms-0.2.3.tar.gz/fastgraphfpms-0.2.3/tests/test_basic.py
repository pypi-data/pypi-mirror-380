# Test basique
import time
from collections import deque
import fastgraphFPMS as fg

def load_adjacency_matrix(filename):
    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    if not lines:
        raise ValueError("Le fichier est vide ou invalide")

    n = int(lines[0])

    matrix = [list(map(int, line.split())) for line in lines[1:]]

    if len(matrix) != n:
        raise ValueError(f"La matrice doit avoir {n} lignes, mais en a {len(matrix)}")
    if any(len(row) != n for row in matrix):
        raise ValueError("La matrice d'adjacence doit être carrée")

    return matrix

def bfs(matrix, start):
    num_nodes = len(matrix)

    # Vérification des bornes
    if start < 0 or start >= num_nodes:
        raise IndexError("start doit être entre 0 et num_nodes - 1")

    INF = float("inf")
    dist = [INF] * num_nodes
    parent = [-1] * num_nodes

    dist[start] = 0
    q = deque([start])

    while q:
        u = q.popleft()

        for v, edge in enumerate(matrix[u]):
            if edge != 0:  
                if dist[v] == INF:
                    dist[v] = dist[u] + 1
                    parent[v] = u
                    q.append(v)

    return dist, parent

# g = fg.Graph()

# g.load_from_file("tests/input_5.txt")

# start = time.time()
# dist, par = g.bfs(48)
# print(f"Temps pris par C++ pour bfs : {time.time() - start} secondes")

# print("Distance : ",dist)
# print("Parents : ",par)

# g.save_to_file("tests/output_5.txt")

# matrix = load_adjacency_matrix("tests/output_5.txt")

# start = time.time()
# dist, par = bfs(matrix, 48)
# print(f"Temps pris par python pour bfs : {time.time() - start} secondes")

# print("Distance : ",dist)
# print("Parents : ",par)


# g2 = fg.Graph()
# g2.load_from_file("tests/input_7.txt")

# g2.print()

# start = time.time()
# NSCC, list_scc = g2.find_scc()
# print(f"Réalisé en {time.time() - start} secondes")
# print(f"Nombre de composantes fortement connexes : {NSCC}")
# for i, elem in enumerate(list_scc):
#     print(f"Composante fortement connexe numéro {i+1} : {elem}")


# g3 = fg.Graph()
# g3.load_from_file("tests/input_8.txt")
# group1, group2 = g3.is_bigraph()

# print(f"Team blue : {group1}")
# print(f"Team Red : {group2}")


# g4 = fg.Graph()
# g4.load_from_file("tests/input_9.txt")
# cost, mst = g4.kruskal()

# print(f"L'arbre optimal coûte : {cost}")
# print(mst)


g5 = fg.Graph()
g5.load_from_file("tests/input_10.txt")
dist, par = g5.dijkstra(0, 7)
print(dist)
print(par)

print('✅ Test réussi!')