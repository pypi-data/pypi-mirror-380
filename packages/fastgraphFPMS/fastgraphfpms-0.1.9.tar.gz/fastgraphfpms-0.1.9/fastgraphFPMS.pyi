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