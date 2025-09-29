#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "../src/graph.h"

namespace py = pybind11;

PYBIND11_MODULE(fastgraphFPMS, m) {
    m.doc() = R"pbdoc(
    
        FastGraphFPMS - Une librairie de graphes ultra-rapide implémentée en C++
        
        Cette librairie fournit des algorithmes de graphes optimisés pour la performance.
        
        Exemples d'utilisation:
            >>> import fastgraphFPMS as fg
            >>> graph = fg.Graph([[0, 1], [1, 0]])
            >>> graph.bfs(0)
            [0, 1]

    )pbdoc";
    
    py::class_<fastgraphfpms::Graph>(m, "Graph", R"pbdoc(

        Représente un graphe avec une matrice d'adjacence.
        
        Cette classe permet de créer et manipuler des graphes, et d'exécuter
        divers algorithmes graphiques optimisés.
        
        Args:
            matrix: Matrice d'adjacence (liste de listes d'entiers)
            filename: Chemin vers un fichier contenant la matrice

    )pbdoc")
    
    .def(py::init<>(), R"pbdoc(

        Crée un graphe vide.
        
        Example:
            >>> graph = Graph()

    )pbdoc")
    
    .def(py::init<const vector<vector<int>>&>(), 
         py::arg("matrix"),
         R"pbdoc(

        Crée un graphe à partir d'une matrice d'adjacence.
        
        Args:
            matrix: Matrice d'adjacence représentant le graphe
            
        Example:
            >>> matrix = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
            >>> graph = Graph(matrix)

    )pbdoc")
    
    .def(py::init<const string&>(), 
         py::arg("filename"),
         R"pbdoc(

        Crée un graphe à partir d'un fichier.
        
        Args:
            filename: Chemin vers le fichier contenant la matrice
            
        Example:
            >>> graph = Graph("mon_graphe.txt")

    )pbdoc")
    
    // === MÉTHODES DE BASE ===
    .def("get_num_nodes", &fastgraphfpms::Graph::get_num_nodes, R"pbdoc(

        Retourne le nombre de nœuds du graphe.
        
        Returns:
            int: Nombre de nœuds dans le graphe
            
        Example:
            >>> nb_nodes = graph.get_num_nodes()
            >>> print(f"Le graphe a {nb_nodes} nœuds")

    )pbdoc")

    // === FICHIERS ===
    .def("load_from_file", &fastgraphfpms::Graph::load_from_file, 
         py::arg("filename"), R"pbdoc(

        Charge un graphe depuis un fichier.
        
        Args:
            filename: Chemin vers le fichier contenant la matrice
            
        Format du fichier:
            Première ligne: nombre de nœuds
            Lignes suivantes: matrice d'adjacence
            
        Example:
            >>> graph.load_from_file("graphe.txt")

    )pbdoc")
    
    .def("save_to_file", &fastgraphfpms::Graph::save_to_file, 
         py::arg("filename"), R"pbdoc(

        Sauvegarde le graphe dans un fichier.
        
        Args:
            filename: Chemin où sauvegarder le fichier

    )pbdoc")

    .def("print", &fastgraphfpms::Graph::print, R"pbdoc(

        Affiche les structures de données Head, Successeurs et Weights.
        
    )pbdoc")
    
    .def("bfs", &fastgraphfpms::Graph::bfs,
        py::arg("start"), R"pbdoc(

        Effectue une exploration en largeur sur le graphique en partant du noeud start.

        Args:
            start: noeud de démarrage pour l'exploration

        )pbdoc")
        
    .def("dfs", &fastgraphfpms::Graph::dfs,
        py::arg("start"), R"pbdoc(

        Effectue une exploration en profondeur sur le graphique en partant du noeud start.

        Args:
            start: noeud de démarrage pour l'exploration

        )pbdoc")
        
        
    .def("find_cc", &fastgraphfpms::Graph::find_cc, R"pbdoc(

        Renvoie le nombre de composante connexe et une liste comprenant chaque composante connexe.
        
        )pbdoc")

    .def("find_scc", &fastgraphfpms::Graph::find_scc, R"pbdoc(

        Renvoie le nombre de composante fortement connexe et une liste comprenant chaque composante fortement connexe.
        
        )pbdoc")
        
    .def("is_bigraph", &fastgraphfpms::Graph::is_bigraph, R"pbdoc(

        Renvoie, si le graph est bipartie, deux listes contenant les noeuds séparés en deux groupes.

        )pbdoc");
    
    // Version
    #ifdef VERSION_INFO
    m.attr("__version__") = VERSION_INFO;
    #else
    m.attr("__version__") = "0.1.0";
    #endif
}