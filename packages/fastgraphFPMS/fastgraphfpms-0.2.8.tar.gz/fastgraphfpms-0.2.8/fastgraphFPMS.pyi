"""
Type stubs for fastgraphFPMS - Pour l'autocomplétion IDE
"""

from typing import List, Tuple, Union

class Graph:
    """
    Représente un graphe avec une matrice d'adjacence.
    
    Cette classe permet de créer et manipuler des graphes, et d'exécuter
    divers algorithmes graphiques optimisés.
    """
    
    def __init__(self, matrix: List[List[int]] = None) -> None:
        """
        Crée un graphe à partir d'une matrice d'adjacence.
        
        Args:
            matrix: Matrice d'adjacence représentant le graphe
            directed: True pour un graphe dirigé, False pour non dirigé
        """
        ...
    
    def __init__(self, filename: str) -> None:
        """
        Crée un graphe à partir d'un fichier.
        
        Args:
            filename: Chemin vers le fichier contenant la matrice
            directed: True pour un graphe dirigé, False pour non dirigé
        """
        ...
    
    def get_num_nodes(self) -> int:
        """Retourne le nombre de nœuds du graphe."""
        ...
    
    def get_is_directed(self) -> bool:
        """Indique si le graphe est dirigé."""
        ...
    
    def load_from_file(self, filename: str) -> None:
        """Charge un graphe depuis un fichier."""
        ...
    
    def save_to_file(self, filename: str) -> None:
        """Sauvegarde le graphe dans un fichier."""
        ...

    def print(self) -> None:
        """Affiche les structures de données."""
        ...

    def bfs(self, start: int) -> Tuple[List[int], List[int]]:
        """Exploration en largeur sur le graph.
            Args:
                Start: int
            Return:
                Distance: List[int]
                Parents: List[int]"""
        ...

    def dfs(self, start: int) -> Tuple[List[int], List[int]]:
        """Exploration en profondeur sur le graph.
            Args:
                Start: int
            Return:
                Distance: List[int]
                Parents: List[int]"""
        ...
    
    def find_cc(self) -> Tuple[int, List[List[int]]]:
        """Retourne le nombre de composante connexe et les composantes connexes.
            Args:
                /
            Return:
                Nombre de composante connexe: int
                Liste des composantes connexes: List[List[int]]"""
        ...
    
    def find_scc(self) -> Tuple[int, List[List[int]]]:
        """Retourne le nombre de composante fortement connexe et les composantes fortement connexes.
            Args:
                /
            Return:
                Nombre de composante fortement connexe: int
                Liste des composantes fortement connexes: List[List[int]]"""
        ...
    def is_bigraph(self) -> Tuple[List[int], List[int]]:
        """Retourne, si le graphe est bipartie, deux listes contenant les noeuds séparés en deux groupes.
            Args:
                /
            Return:
                Group 1: List[int]
                Group 2: List[int]
            """
        ...
    
    def prim(self) -> Tuple[int,List[Tuple[int,int,int]]]:
        """Retourne le coût de l'arbre optimale.
            Args:
                /
            Return:
                Cost: int
                Mst: List[Tuple[int, int, int]]
        """
        ...

    def kruskal(self) -> Tuple[int,List[Tuple[int,int,int]]]:
        """Retourne le coût de l'arbre optimale.
            Args:
                /
            Return:
                Cost: int
                Mst: List[Tuple[int, int, int]]
        """
        ...

    def dijkstra(self, s: int, t: int = -1) -> Union[Tuple[List[int], List[int]], Tuple[int, List[int]]]:
        """
        Retourne les distances depuis le noeud start ainsi que les parents de chaque noeud via Dijkstra.
            Args:
                s: int
                t: int = -1
            Return:
                if t == -1:
                    Dist: List[int]
                    Parent: List[int]
                else:
                    Dist: int
                    Parent: List[int]
        """
        ...

    def sedgewick_vitter(self, s:int, t: int = -1) -> Union[Tuple[List[int], List[int]], Tuple[int, List[int]]]:
        """
        Retourne les distances depuis le noeud start ainsi que les parents de chaque noeud via Sedgewick et Vitter.
            Args:
                s: int
                t: int = -1
            Return:
                if t == -1:
                    Dist: List[int]
                    Parent: List[int]
                else:
                    Dist: int
                    Parent: List[int]
        """
        ...

    def dijkstra_bucket(self, s:int, t: int = -1) -> Union[Tuple[List[int], List[int]], Tuple[int, List[int]]]:
        """
        Retourne les distances depuis le noeud start ainsi que les parents de chaque noeud via Dijkstra à bucket.
            Args:
                s: int
                t: int = -1
            Return:
                if t == -1:
                    Dist: List[int]
                    Parent: List[int]
                else:
                    Dist: int
                    Parent: List[int]
        """
        ...

    def bellman_ford(self, s:int, t:int = -1) -> Union[Tuple[List[int], List[int]], Tuple[int, List[int]]]:
        """
        Retourne les distances depuis le noeud start ainsi que les parents de chaque noeud via Bellman.
            Args:
                s: int
                t: int = -1
            Return:
                if t == -1:
                    Dist: List[int]
                    Parent: List[int]
                else:
                    Dist: int
                    Parent: List[int]
        """
        ...

    def has_negative_cycle(self) -> bool:
        """
        Retourne une variable booléenne si le graphe possède un cycle négatif.
            Args:
                /
            Return:
                Ans: bool
        """
        ...

    def floyd_warshall(self) -> Tuple[List[List[int]], List[List[int]]]:
        """
        Calcule les plus courts chemins entre toutes les paires de nœuds.
        
        Returns:
            Tuple contenant:
            - distances: matrice des distances entre toutes les paires de nœuds
            - next: matrice pour reconstruire les chemins
            
        Example:
            >>> dist, next = graph.floyd_warshall()
            >>> distance_0_5 = dist[0][5]
        """
        ...

    def get_shortest_paths_matrix(self) -> List[List[int]]:
        """
        Retourne la matrice des plus courtes distances entre toutes les paires.
        
        Returns:
            Matrice carrée où l'élément [i][j] représente la distance de i à j
            
        Example:
            >>> dist_matrix = graph.get_shortest_paths_matrix()
            >>> print(f"Distance de 0 à 5: {dist_matrix[0][5]}")
        """
        ...

    def has_negative_cycle_floyd(self) -> bool:
        """
        Détecte les cycles négatifs avec l'algorithme de Floyd-Warshall.
        
        Returns:
            True si un cycle négatif est présent, False sinon
            
        Example:
            >>> if graph.has_negative_cycle_floyd():
            ...     print("Cycle négatif détecté!")
        """
        ...

    def find_eulerian_path(self) -> List[int]:
        """
        Trouve un chemin eulérien (passe par chaque arête exactement une fois).
        
        Returns:
            Liste des nœuds dans l'ordre du chemin, ou liste vide si impossible
        """
        ...

    def find_eulerian_circuit(self) -> List[int]:
        """
        Trouve un circuit eulérien (cycle qui passe par chaque arête exactement une fois).
        
        Returns:
            Liste des nœuds dans l'ordre du circuit, ou liste vide si impossible
        """
        ...

    def has_eulerian_path(self) -> bool:
        """
        Vérifie l'existence d'un chemin eulérien.
        
        Returns:
            True si un chemin eulérien existe
        """
        ...

    def has_eulerian_circuit(self) -> bool:
        """
        Vérifie l'existence d'un circuit eulérien.
        
        Returns:
            True si un circuit eulérien existe
        """
        ...

    def find_hamiltonian_path(self) -> List[int]:
        """
        Trouve un chemin hamiltonien (passe par chaque sommet exactement une fois).
        
        Warning: Algorithme exponentiel - pour petits graphes seulement.
        
        Returns:
            Liste des nœuds dans l'ordre du chemin, ou liste vide si impossible
        """
        ...

    def find_hamiltonian_circuit(self) -> List[int]:
        """
        Trouve un cycle hamiltonien (passe par chaque sommet exactement une fois).
        
        Warning: Algorithme exponentiel - pour petits graphes seulement.
        
        Returns:
            Liste des nœuds dans l'ordre du cycle, ou liste vide si impossible
        """
        ...

    def has_hamiltonian_path(self) -> bool:
        """
        Vérifie les conditions nécessaires pour un chemin hamiltonien.
        
        Returns:
            True si les conditions nécessaires sont satisfaites
        """
        ...

    def has_hamiltonian_circuit(self) -> bool:
        """
        Vérifie les conditions nécessaires pour un cycle hamiltonien.
        
        Returns:
            True si les conditions nécessaires sont satisfaites
        """
        ...