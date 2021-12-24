from unittest import TestCase

from GraphInterface import GraphInterface
from DiGraph import DiGraph

class TestDiGraph(TestCase):
    def test_v_size(self):
        g = DiGraph()  # creates an empty directed graph
        for n in range(4):
            g.add_node(n)
        self.assertEqual(g.v_size(), 4)  # after add 4 node
        g.remove_node(2)
        self.assertEqual(g.v_size(), 3)  # after del node 2

    def test_e_size(self):
        g = DiGraph()  # creates an empty directed graph
        for n in range(4):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)
        self.assertEqual(g.e_size(), 5)  # after add 5 edgs
        g.remove_edge(1, 3)
        self.assertEqual(g.e_size(), 4)  # after remove_edge(1,3)

    def test_get_mc(self):
        g = DiGraph()  # creates an empty directed graph
        for n in range(4):
            g.add_node(n)
        self.assertEqual(g.get_mc(), 4)  # after add 4 node '_mc' will be 4
        g.remove_node(2) # now '_mc' will be 5
        self.assertEqual(g.get_mc(), 5)

    def test_add_edge(self):
        g = DiGraph()  # creates an empty directed graph
        for n in range(4):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)
        self.assertEqual(g.e_size(), 5)  # after add 5 edges

        edgeWeWnatToSeeInside = {0: {1: 1.1}, 1: {0: 1}, 2: {1: 1.3}, 3: {2: 1.1, 1: 1.9}}
        self.assertDictEqual(g._edgesInside,edgeWeWnatToSeeInside)


        edgeWeWnatToSeeOut = {0: {1: 1}, 1: {0: 1.1, 2: 1.3, 3: 1.9}, 2: {3: 1.1}, 3: {}}
        self.assertDictEqual(g._edgesOut, edgeWeWnatToSeeOut)

        # now we will try with delete edge
        g.remove_edge(1, 3)
        self.assertEqual(g.e_size(), 4)  # after remove_edge(1,3)

        edgeWeWnatToSeeInside = {0: {1: 1.1}, 1: {0: 1}, 2: {1: 1.3}, 3: {2: 1.1}}
        self.assertDictEqual(g._edgesInside,edgeWeWnatToSeeInside)


        edgeWeWnatToSeeOut = {0: {1: 1}, 1: {0: 1.1, 2: 1.3}, 2: {3: 1.1}, 3: {}}
        self.assertDictEqual(g._edgesOut, edgeWeWnatToSeeOut)


    def test_add_node(self):
        g = DiGraph()  # creates an empty directed graph
        g.add_node(0,(0,1,0)) # remember that in pos is (x,y,z)
        g.add_node(1,(1,0,0)) # remember that in pos is (x,y,z)
        self.assertEqual(g.v_size(),2)


    def test_remove_node(self):
        """"        g = DiGraph()  # creates an empty directed graph
        g.add_node(0, (0, 1, 0))  # remember that in pos is (x,y,z)
        g.add_node(1, (1, 0, 0))  # remember that in pos is (x,y,z)
        self.assertEqual(g.v_size(), 2)
        g.remove_node(0)
        self.assertEqual(g.v_size(), 1)
        self.assertEqual(g.get_all_v().get(1), (1, 0, 0)) # we make sure that only node 1 in pos (1,0,0) will stay
"""

        g: GraphInterface = DiGraph()
        for n in range(4):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(0, 2, 1)
        g.add_edge(0, 3, 1.1)
        g.add_edge(1, 0, 4)
        self.assertEqual(4, g.e_size())  # after add 4 edge
        g.remove_node(0)
        self.assertEqual(0, g.e_size())  # all edge connect to node 0 so all need to remove



    def test_remove_edge(self):
        g = DiGraph()  # creates an empty directed graph
        for n in range(4):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)
        self.assertEqual(g.e_size(), 5)  # after add 5 edges
        self.assertEqual(g.get_mc(), 9)  # 4 nodes + 5 edges created
        g.remove_edge(2,3)
        self.assertEqual(g.e_size(), 4)  # after del edge (2,3)
        self.assertEqual(g.get_mc(), 10)  # mc will grow also when del

    # def test_get_all_v(self):
    #     g = DiGraph()  # creates an empty directed graph
    #     g.add_node(0, (0, 1, 0))  # remember that in pos is (x,y,z)
    #     g.add_node(1, (1, 0, 0))  # remember that in pos is (x,y,z)
    #     self.assertEqual(g.v_size(), 2)
    #
    #     # nodesWeWantToSeeInOurGraphValues = {id: 0, "pos": (0, 1, 0), "id": 1, "pos": (1, 0, 0)}#{0: (0, 1, 0), 1: (1, 0, 0)}
    #     # self.assertDictEqual(g._nodes,nodesWeWantToSeeInOurGraph)
    #
    #     g.remove_node(0) # we del node 0:(0,1,0)
    #     nodesWeWantToSeeInOurGraph = {1: (1, 0, 0)}
    #     self.assertDictEqual(g._nodes,nodesWeWantToSeeInOurGraph)


    def test_all_in_edges_of_node(self):
        g = DiGraph()  # creates an empty directed graph
        for n in range(4):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)

        self.assertEqual(g.e_size(), 5)  # after add 5 edges

        edgeWeWnatToSeeInside = {0: {1: 1.1}, 1: {0: 1}, 2: {1: 1.3}, 3: {2: 1.1, 1: 1.9}}
        self.assertDictEqual(g._edgesInside,edgeWeWnatToSeeInside)

        # now we will try with delete edge
        g.remove_edge(1, 3)
        self.assertEqual(g.e_size(), 4)  # after remove_edge(1,3)

        edgeWeWnatToSeeInside = {0: {1: 1.1}, 1: {0: 1}, 2: {1: 1.3}, 3: {2: 1.1}}
        self.assertDictEqual(g._edgesInside,edgeWeWnatToSeeInside)


    def test_all_out_edges_of_node(self):
        g = DiGraph()  # creates an empty directed graph
        for n in range(4):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)

        self.assertEqual(g.e_size(), 5)  # after add 5 edges

        edgeWeWnatToSeeOut = {0: {1: 1}, 1: {0: 1.1, 2: 1.3, 3: 1.9}, 2: {3: 1.1}, 3: {}}
        self.assertDictEqual(g._edgesOut, edgeWeWnatToSeeOut)

        # now we will try with delete edge
        g.remove_edge(1, 3)
        self.assertEqual(g.e_size(), 4)  # after remove_edge(1,3)

        edgeWeWnatToSeeOut = {0: {1: 1}, 1: {0: 1.1, 2: 1.3}, 2: {3: 1.1}, 3: {}}
        self.assertDictEqual(g._edgesOut, edgeWeWnatToSeeOut)


