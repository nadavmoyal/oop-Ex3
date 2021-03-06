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
        self.ga0.load_from_json('A0.json')
        self.ga1.load_from_json('A1.json')
        self.ga2.load_from_json('A2.json')
        self.ga3.load_from_json('A3.json')
        self.ga4.load_from_json('A4.json')
        self.ga5.load_from_json('A5.json')


    def test_get_load_save_graph(self):
        _graphAlgo = GraphAlgo()
        _graph = DiGraph()
        _graph.add_node(0, (2, 3))
        _graph.add_node(1, (3, 3))
        _graph.add_node(2, (5, 3))
        _graph.add_node(3, (2, 5))
        _graph.add_edge(0, 1, 1)
        _graph.add_edge(1, 2, 1)
        _graph.add_edge(2, 3, 1)

        _graphAlgo.__init__(_graph)
        GraphToGet=_graphAlgo.get_graph()
        self.assertEqual(4,GraphToGet.v_size())
        self.assertEqual(3,GraphToGet.e_size())


        self.GraphToLoad: GraphAlgoInterface = GraphAlgo()
        self.GraphToLoad.load_from_json('A0.json')
        self.assertEqual(32,self.GraphToLoad.__sizeof__())
        self.GraphToLoad.save_to_json('SavedGraphTest.json')


    def test_shortest_path(self):
        _graphAlgo = GraphAlgo()
        _graph = DiGraph()
        _graph.add_node(0, (2, 3))
        _graph.add_node(1, (3, 3))
        _graph.add_node(2, (5, 3))
        _graph.add_node(3, (5, 3))
        _graph.add_node(4, (5, 3))
        _graph.add_node(5, (5, 3))
        _graph.add_node(6, (5, 3))
        _graph.add_edge(0, 1, 1)
        _graph.add_edge(1, 2, 1)
        _graph.add_edge(2, 3, 1)
        _graph.add_edge(3, 4, 1)
        _graph.add_edge(4, 5, 1)
        _graph.add_edge(5, 6, 1)
        _graph.add_edge(0, 6, 20)
        _graphAlgo.__init__(_graph)
        self.assertEqual(_graphAlgo.shortest_path(0,6), (6, [0, 1, 2,3,4,5,6]))
        self.assertEqual(_graphAlgo.shortest_path(1,0), (float('inf'), []))
        self.assertEqual(_graphAlgo.shortest_path(0,0), (0, []))


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



    def test_tsp(self):
        _graphAlgo = GraphAlgo()
        _graph = DiGraph()
        _graph.add_node(0, (2, 3))
        _graph.add_node(1, (3, 3))
        _graph.add_node(2, (5, 3))
        _graph.add_node(3, (5, 2))
        _graph.add_node(4, (2, 9))
        _graph.add_edge(0, 1, 1)
        _graph.add_edge(1, 2, 1)
        _graph.add_edge(3, 2, 10)

        _graphAlgo.__init__(_graph)
        self.assertEqual(([0,1,2],2), (_graphAlgo.TSP([0])))


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


