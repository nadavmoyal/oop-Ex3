from unittest import TestCase
from unittest import TestCase
from GraphAlgo import GraphAlgo
from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
from Node import Node


class TestGraphAlgo(TestCase):
    def setUp(self):
        self.ga0: GraphAlgoInterface = GraphAlgo()
        self.ga1: GraphAlgoInterface = GraphAlgo()
        self.ga2: GraphAlgoInterface = GraphAlgo()
        self.ga3: GraphAlgoInterface = GraphAlgo()
        self.ga4: GraphAlgoInterface = GraphAlgo()
        self.ga5: GraphAlgoInterface = GraphAlgo()
        self.ga0.load_from_json('../data/A0.json')
        self.ga1.load_from_json('../data/A1.json')
        self.ga2.load_from_json('../data/A2.json')
        self.ga3.load_from_json('../data/A3.json')
        self.ga4.load_from_json('../data/A4.json')
        self.ga5.load_from_json('../data/A5.json')

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
        self.temp=self.ga0.get_graph()

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
        _graphAlgo = GraphAlgo()
        _graph = DiGraph()
        _graph.add_node(0, (2, 3))
        _graph.add_node(1, (3, 3))
        _graph.add_node(2, (5, 3))
        _graph.add_node(3, (5, 2))
        _graph.add_node(4, (2, 9))
        _graph.add_edge(0, 1, 10)
        _graph.add_edge(1, 2, 10)
        _graph.add_edge(2, 0, 1)
        _graph.add_edge(2, 1, 1)
        _graph.add_edge(1, 3, 2)
        _graph.add_edge(3, 2, 7)
        _graph.add_edge(3, 0, 4)
        _graph.add_edge(4, 0, 3)
        _graphAlgo.__init__(_graph)
        self.assertEqual((2, 8), (_graphAlgo.TSP(list[0,1])))

    def test_center_point(self):
        _graphAlgo = GraphAlgo()
        _graph = DiGraph()
        _graph.add_node(0, (2, 3))
        _graph.add_node(1, (3, 3))
        _graph.add_node(2, (5, 3))
        _graph.add_node(3, (5, 2))
        _graph.add_node(4, (2, 9))
        _graph.add_edge(0, 1, 10)
        _graph.add_edge(1, 2, 10)
        _graph.add_edge(2, 0, 1)
        _graph.add_edge(2, 1, 1)
        _graph.add_edge(1, 3, 2)
        _graph.add_edge(3, 2, 7)
        _graph.add_edge(2, 4, 8)
        _graph.add_edge(3, 0, 4)
        _graph.add_edge(4, 0, 3)
        _graphAlgo.__init__(_graph)
        self.assertEqual((2,8),(_graphAlgo.centerPoint()))
        self.assertEqual((7, 6.806805834715163),self.ga0.centerPoint())
        self.assertEqual((8, 9.925289024973141),self.ga1.centerPoint())
        self.assertEqual((0, 7.819910602212574),self.ga2.centerPoint())
        self.assertEqual((2, 8.182236568942237),self.ga3.centerPoint())
        self.assertEqual((6, 8.071366078651435),self.ga4.centerPoint())
        self.assertEqual((40, 9.291743173960954),self.ga5.centerPoint())


    def test_dijkstra(self):
        self.fail()
