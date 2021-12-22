from unittest import TestCase
from unittest import TestCase
from GraphAlgo import GraphAlgo
from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
from Node import Node


class TestGraphAlgo(TestCase):
    def DefaultGraphAlgo(self):
        _graphAlgo = GraphAlgo()
        _graph = DiGraph()
        _graph.add_node(0,2,3)
        _graph.add_node(1,3,3)
        _graph.add_node(2,8,5)
        _graph.add_node(3,5,2)
        _graph.add_node(4,6,4)
        _graph.add_edge(0,1,2)
        _graph.add_edge(0,2,4)
        _graph.add_edge(2,4,5)
        _graph.add_edge(1,3,3)
        _graph.add_edge(3,0,4)
        _graph.add_edge(3,1,6)
        _graph.add_edge(4,2,2)



    def test_get_graph(self):
        _graphAlgo = GraphAlgo()
        _graph = DiGraph()
        _graph.add_node(0,2,3)
        _graph.add_node(1,3,3)
        _graph.add_node(2,8,5)
        _graph.add_node(3,5,2)
        _graph.add_node(4,6,4)
        _graph.add_edge(0,1,2)
        _graph.add_edge(0,2,4)
        _graph.add_edge(2,4,5)
        _graph.add_edge(1,3,3)
        _graph.add_edge(3,0,4)
        _graph.add_edge(3,1,6)
        _graph.add_edge(4,2,2)

        self.fail()

    def test_load_from_json(self):
        self.fail()

    def test_save_to_json(self):
        self.fail()

    def test_shortest_path(self):
        self.fail()

    def test_plot_graph(self):
        _graphAlgo = GraphAlgo()
        _graph = DiGraph()
        _graph.add_node(0, (2, 3))
        _graph.add_node(1, (3, 3))
        _graph.add_node(2, (8, 5))
        _graph.add_node(3, (5, 2))
        _graph.add_node(4, (6, 4))
        _graph.add_edge(0, 1, 2)
        _graph.add_edge(0, 2, 4)
        _graph.add_edge(2, 4, 5)
        _graph.add_edge(1, 3, 3)
        _graph.add_edge(3, 0, 4)
        _graph.add_edge(3, 1, 6)
        _graph.add_edge(4, 2, 2)
        _graphAlgo.__init__(_graph)
        dic = _graphAlgo.get_graph().get_all_v()
        for x in dic:
            n1 = _graphAlgo.get_graph().get_all_v().get(x).get_pos()
            print(n1)


    def test_tsp(self):
        self.fail()

    def test_center_point(self):
        _graphAlgo = GraphAlgo()
        _graph = DiGraph()
        _graph.add_node(0, (2, 3))
        _graph.add_node(1, (3, 3))
        _graph.add_node(2, (8, 5))
        _graph.add_edge(0, 1, 10)
        _graph.add_edge(1, 2, 10)
        _graph.add_edge(2, 0, 1)
        _graph.add_edge(2, 1, 1)
        _graphAlgo.__init__(_graph)
        self.assertEqual((2,1),(_graphAlgo.centerPoint()))

    def test_dijkstra(self):
        self.fail()
